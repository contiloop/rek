"""`rek fetch <url> [--out runs/<id>] [--no-images]`"""
from __future__ import annotations

import argparse
import sys

from rek.adapters.http import UrllibImageStore
from rek.adapters.naver_blog import NaverBlogSource
from rek.core.run_dir import write_run

SOURCES = [NaverBlogSource()]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="rek")
    sub = p.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch", help="fetch a post into a run directory")
    f.add_argument("url")
    f.add_argument("--out", help="run directory (default runs/<post_id>)")
    f.add_argument("--no-images", action="store_true")
    args = p.parse_args(argv)

    source = next((s for s in SOURCES if s.supports(args.url)), None)
    if source is None:
        print(f"no adapter for {args.url}", file=sys.stderr)
        return 2
    post, raw = source.fetch(args.url)
    out = args.out or f"runs/{post.post_id}"
    meta = write_run(post, raw, out, None if args.no_images else UrllibImageStore())
    print(f"{out}: '{meta['title']}' ({meta['published_at']}), blocks={meta['block_counts']}, images={len(meta['images'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
