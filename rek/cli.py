"""`rek fetch`, `rek stats`, `rek prior`, `rek verify-summary`, `rek profile-hash`, `rek research-init`, `rek research-summary`. Wiring only: adapters in, core logic called."""
from __future__ import annotations

import argparse
import urllib.error
import datetime as dt
import json
import os
import sys

from rek.adapters.http import UrllibImageStore
from rek.adapters.naver_blog import NaverBlogSource, NaverPostList
from rek.core import prior, research, verify_summary
from rek.core.profile_hash import profile_hash
from rek.core.run_dir import write_run
from rek.core.repro_stats import as_dict as repro_as_dict, compute as repro_compute
from rek.core.source_sites import parse_sources, render as render_sites
from rek.core.stats import as_dict, compute

SOURCES = [NaverBlogSource()]
POST_LISTS = {NaverBlogSource: NaverPostList}


def _source_for(url: str):
    source = next((s for s in SOURCES if s.supports(url)), None)
    if source is None:
        print(f"no adapter for {url}", file=sys.stderr)
    return source


def cmd_fetch(args) -> int:
    source = _source_for(args.url)
    if source is None:
        return 2
    try:
        post, raw = source.fetch(args.url)
    except (LookupError, urllib.error.URLError) as e:  # no such post, or the site refused
        print(f"fetch failed for {args.url}: {e}", file=sys.stderr)
        return 1
    out = args.out or f"runs/{post.post_id}"
    meta = write_run(post, raw, out, None if args.no_images else UrllibImageStore())
    print(f"{out}: '{meta['title']}' ({meta['published_at']}), blocks={meta['block_counts']}, images={len(meta['images'])}")
    return 0


def cmd_stats(args) -> int:
    rows = {}
    for path in args.paths:
        with open(path, encoding="utf-8") as fh:
            rows[path] = as_dict(compute(fh.read()))
    print(json.dumps(rows, ensure_ascii=False, indent=1))
    return 0


def cmd_prior(args) -> int:
    meta_path = os.path.join(args.run_dir, "meta.json")
    with open(meta_path, encoding="utf-8") as f:
        meta = json.load(f)
    source = _source_for(meta["source_url"])
    if source is None:
        return 2
    blog_id = source.blog_of(meta["source_url"])
    post_list = POST_LISTS[type(source)]()

    # the title route needs the whole list; without title words, only as far back as the date route needs
    words = prior.title_words(meta.get("title", ""))
    until = None if words else prior.earliest_needed(meta)
    posts = post_list.list_posts(blog_id, until) if (words or until) else []
    plan = prior.plan(meta, posts)

    record = plan.as_record()
    record["searched_at"] = dt.datetime.now().astimezone().replace(microsecond=0).isoformat()
    record["list_size"] = len(posts)
    record["list_until"] = until.isoformat() if until else None
    record["date_route"]["confirmed"] = []
    record["date_route"]["rejected"] = []
    paths = prior.reused_image_paths(meta)
    images = None if args.no_images else UrllibImageStore()
    for entry, candidate in zip(record["candidates"], plan.candidates):
        out = os.path.join(args.run_dir, "prior", candidate.post_id)
        present = os.path.isfile(os.path.join(out, "meta.json"))
        url = source.post_url(blog_id, candidate.post_id)
        page = None  # (post, raw) once fetched
        try:
            if "date" in candidate.routes:
                raw_on_disk = os.path.join(out, "raw.html")
                if present and os.path.isfile(raw_on_disk):
                    with open(raw_on_disk, encoding="utf-8") as f:
                        html = f.read()
                else:
                    page = source.fetch(url)
                    html = page[1]
                matched = prior.confirm(html, paths)
                if matched:
                    record["date_route"]["confirmed"].append({"post_id": candidate.post_id, "image_indexes": matched})
                else:
                    record["date_route"]["rejected"].append({"post_id": candidate.post_id, "title": candidate.post.title, "date": candidate.post.date.isoformat(), "reason": "none of the reused image files is on the page"})
                    if "title" not in candidate.routes:
                        entry["status"] = "rejected"
                        print(f"{candidate.post_id} rejected [date] {candidate.post.date} {candidate.post.title}")
                        continue
            if present:
                entry["status"] = "present"
            else:
                post, raw = page or source.fetch(url)
                write_run(post, raw, out, images)
                entry["status"] = "fetched"
        except Exception as e:  # one bad post must not lose the record of the others
            entry["status"] = "failed"
            entry["error"] = f"{type(e).__name__}: {e}"
        print(f"{candidate.post_id} {entry['status']} [{'+'.join(candidate.routes)}] {candidate.post.date} {candidate.post.title}")
    with open(meta_path, encoding="utf-8") as f:
        current = json.load(f)  # re-read: keep every key written by anyone else meanwhile
    current["prior_search"] = record
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(current, f, ensure_ascii=False, indent=1)
    counts = {s: sum(1 for c in record["candidates"] if c["status"] == s) for s in ("fetched", "present", "rejected", "failed")}
    dr, tr = record["date_route"], record["title_route"]
    print(f"{args.run_dir}: list={len(posts)} date_route={len(dr['candidates'])} candidates/{len(dr['confirmed'])} confirmed; title_route={len(tr['found'])} found/{len(tr['kept'])} kept, words={words}; {counts}")
    return 0 if counts["failed"] == 0 else 1


def cmd_verify_summary(args) -> int:
    rows, all_pass = verify_summary.summarize(args.runs_dir, criteria=args.criteria)
    print(verify_summary.render(rows, all_pass), end="")
    return 0 if all_pass else 1


def cmd_repro_stats(args) -> int:
    import json
    import os

    with open(os.path.join(args.repro_dir, "research.md"), encoding="utf-8") as fh:
        research = fh.read()
    log_path = os.path.join(args.repro_dir, "log.md")
    log = open(log_path, encoding="utf-8").read() if os.path.exists(log_path) else ""
    print(json.dumps(repro_as_dict(repro_compute(research, log)), ensure_ascii=False, indent=1))
    return 0


def cmd_source_sites(args) -> int:
    import glob
    import os

    sites: dict = {}
    for run_dir in sorted(glob.glob(os.path.join(args.runs_dir, "*"))):
        path = os.path.join(run_dir, "sources.md")
        if os.path.isfile(path):
            with open(path, encoding="utf-8") as fh:
                parse_sources(fh.read(), os.path.basename(run_dir), sites)
    print(render_sites(sites), end="")
    return 0


def cmd_profile_hash(args) -> int:
    try:
        print(profile_hash(args.profile_dir))
    except FileNotFoundError as e:
        print(f"missing profile file: {e.filename}", file=sys.stderr)
        return 2
    return 0


def cmd_research_init(args) -> int:
    now = dt.datetime.now(dt.timezone.utc)
    if not os.path.isdir(args.profile) or not os.path.isfile(os.path.join(args.profile, "SKILL.md")):
        print(f"no profile at {args.profile}", file=sys.stderr)
        return 2
    out = args.out or os.path.join("research", research.folder_name(args.topic, now.astimezone(dt.timezone(dt.timedelta(hours=9)))))
    if os.path.exists(os.path.join(out, "topic.md")):
        print(f"{out}/topic.md already exists", file=sys.stderr)
        return 2
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "topic.md"), "w", encoding="utf-8") as f:
        f.write(research.topic_lines(args.topic, args.trigger, args.date or research.default_date(now), args.language, os.path.abspath(args.profile)))
    with open(os.path.join(out, "profile_hash.txt"), "w", encoding="utf-8") as f:
        f.write(profile_hash(args.profile) + "\n")
    print(out)
    return 0


def cmd_research_summary(args) -> int:
    v = research.summarize(args.research_dir)
    print(research.render(args.research_dir, v), end="")
    return 0 if v.passed else 1


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="rek")
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch", help="fetch a post into a run directory")
    f.add_argument("url")
    f.add_argument("--out", help="run directory (default runs/<post_id>)")
    f.add_argument("--no-images", action="store_true")
    f.set_defaults(func=cmd_fetch)
    rs = sub.add_parser("repro-stats", help="counts for one repro/<n> folder (units, sources, log markers)")
    rs.add_argument("repro_dir")
    rs.set_defaults(func=cmd_repro_stats)
    st = sub.add_parser("stats", help="form statistics of one or more post markdown files")
    st.add_argument("paths", nargs="+")
    st.set_defaults(func=cmd_stats)
    pr = sub.add_parser("prior", help="fetch the author's earlier posts (by image upload dates and title words) into <run_dir>/prior/")
    pr.add_argument("run_dir")
    pr.add_argument("--no-images", action="store_true")
    pr.set_defaults(func=cmd_prior)
    vs = sub.add_parser("verify-summary", help="table of the latest verification.md of every run; exit 1 unless all pass")
    vs.add_argument("runs_dir")
    vs.add_argument("--criteria", choices=["author", "own"], default="author", help="author = reference-author thresholds (90/80/upstream/0); own = valid, no fabrication, full chain, enough sources")
    vs.set_defaults(func=cmd_verify_summary)
    ss = sub.add_parser("source-sites", help="registered-domain ledger from every runs/<id>/sources.md")
    ss.add_argument("runs_dir")
    ss.set_defaults(func=cmd_source_sites)
    ph = sub.add_parser("profile-hash", help="sha256[:12] of SKILL.md + research-method.md in a profile folder")
    ph.add_argument("profile_dir")
    ph.set_defaults(func=cmd_profile_hash)
    ri = sub.add_parser("research-init", help="create research/<date>-<slug>/ with topic.md (five start lines) and profile_hash.txt")
    ri.add_argument("topic")
    ri.add_argument("--trigger", default="none", help="one sentence for the trigger event; default none")
    ri.add_argument("--date", help="'YYYY-MM-DD HH:MM KST'; default now")
    ri.add_argument("--language", default="Korean")
    ri.add_argument("--profile", required=True, help="profile folder holding SKILL.md and research-method.md")
    ri.add_argument("--out", help="output folder (default research/<YYYYMMDD>-<slug>)")
    ri.set_defaults(func=cmd_research_init)
    rsu = sub.add_parser("research-summary", help="pass line of one research folder (chain, sources, fabricated, late sources); exit 1 unless pass")
    rsu.add_argument("research_dir")
    rsu.set_defaults(func=cmd_research_summary)
    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
