"""`rek fetch`, `rek stats`, `rek prior`, `rek verify-summary`, `rek profile-hash`. Wiring only: adapters in, core logic called."""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys

from rek.adapters.http import UrllibImageStore
from rek.adapters.naver_blog import NaverBlogSource, NaverPostList
from rek.core import prior, verify_summary
from rek.core.profile_hash import profile_hash
from rek.core.run_dir import write_run
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
    post, raw = source.fetch(args.url)
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
    images = None if args.no_images else UrllibImageStore()
    for entry, candidate in zip(record["candidates"], plan.candidates):
        out = os.path.join(args.run_dir, "prior", candidate.post_id)
        if os.path.isfile(os.path.join(out, "meta.json")):
            entry["status"] = "present"
            continue
        url = source.post_url(blog_id, candidate.post_id)
        try:
            post, raw = source.fetch(url)
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
    counts = {s: sum(1 for c in record["candidates"] if c["status"] == s) for s in ("fetched", "present", "failed")}
    print(f"{args.run_dir}: list={len(posts)} date_route={len(record['date_route']['found'])} title_route={len(record['title_route']['found'])} words={words} {counts}")
    return 0 if counts["failed"] == 0 else 1


def cmd_verify_summary(args) -> int:
    rows, all_pass = verify_summary.summarize(args.runs_dir)
    print(verify_summary.render(rows, all_pass), end="")
    return 0 if all_pass else 1


def cmd_profile_hash(args) -> int:
    try:
        print(profile_hash(args.profile_dir))
    except FileNotFoundError as e:
        print(f"missing profile file: {e.filename}", file=sys.stderr)
        return 2
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="rek")
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch", help="fetch a post into a run directory")
    f.add_argument("url")
    f.add_argument("--out", help="run directory (default runs/<post_id>)")
    f.add_argument("--no-images", action="store_true")
    f.set_defaults(func=cmd_fetch)
    st = sub.add_parser("stats", help="form statistics of one or more post markdown files")
    st.add_argument("paths", nargs="+")
    st.set_defaults(func=cmd_stats)
    pr = sub.add_parser("prior", help="fetch the author's earlier posts (by image upload dates and title words) into <run_dir>/prior/")
    pr.add_argument("run_dir")
    pr.add_argument("--no-images", action="store_true")
    pr.set_defaults(func=cmd_prior)
    vs = sub.add_parser("verify-summary", help="table of the latest verification.md of every run; exit 1 unless all pass")
    vs.add_argument("runs_dir")
    vs.set_defaults(func=cmd_verify_summary)
    ph = sub.add_parser("profile-hash", help="sha256[:12] of SKILL.md + research-method.md in a profile folder")
    ph.add_argument("profile_dir")
    ph.set_defaults(func=cmd_profile_hash)
    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
