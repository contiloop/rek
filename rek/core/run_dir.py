"""Writes one run directory per target: the fixed layout every agent in the loop reads."""
from __future__ import annotations

import json
import os

from rek.core.models import Post
from rek.ports.post_source import ImageStore


def write_run(post: Post, raw: str, out_dir: str, images: ImageStore | None) -> dict:
    os.makedirs(os.path.join(out_dir, "images"), exist_ok=True)
    with open(os.path.join(out_dir, "post.md"), "w", encoding="utf-8") as f:
        f.write(post.to_markdown())
    with open(os.path.join(out_dir, "raw.html"), "w", encoding="utf-8") as f:
        f.write(raw)
    saved = []
    for img in post.images:
        path = os.path.join(out_dir, "images", f"img_{img.index:02d}.png")
        if images is not None:
            size = images.save(img.url, path)
        else:
            size = os.path.getsize(path) if os.path.exists(path) else 0  # --no-images keeps what is there
        saved.append({"index": img.index, "url": img.url, "uploaded_on": img.uploaded_on, "uploaded_at": img.uploaded_at, "caption": img.caption, "bytes": size})
    meta = {
        "source_url": post.source_url,
        "post_id": post.post_id,
        "title": post.title,
        "author": post.author,
        "published_at": post.published_at,
        "block_counts": {k: sum(1 for b in post.blocks if b.kind == k) for k in ("text", "image", "quote", "link", "rule")},
        "outbound_links": post.outbound_links,
        "images": saved,
    }
    with open(os.path.join(out_dir, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    return meta
