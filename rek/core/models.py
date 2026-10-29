"""Domain objects. No I/O, no HTML, no network."""
from __future__ import annotations

import datetime as dt
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Image:
    index: int  # 1-based order of appearance
    url: str  # full-size URL
    uploaded_on: str | None  # YYYY-MM-DD decoded from the host's URL, if the host encodes it
    caption: str | None
    uploaded_at: str | None = None  # ISO timestamp with offset, when the host encodes the exact time


@dataclass(frozen=True)
class PostSummary:
    """One row of a blog's post list: enough to decide whether a post is worth fetching."""

    post_id: str
    title: str
    date: dt.date


@dataclass(frozen=True)
class Block:
    """One unit of the post body in reading order."""

    kind: str  # "text" | "image" | "quote" | "link" | "rule"
    text: str = ""  # text content, or image placeholder
    image: Image | None = None
    url: str | None = None  # for kind == "link"


@dataclass(frozen=True)
class Post:
    source_url: str
    post_id: str
    title: str
    author: str | None
    published_at: str | None  # ISO-ish as given by the source
    blocks: tuple[Block, ...] = field(default_factory=tuple)

    @property
    def images(self) -> list[Image]:
        return [b.image for b in self.blocks if b.image is not None]

    @property
    def outbound_links(self) -> list[str]:
        return [b.url for b in self.blocks if b.kind == "link" and b.url]

    def to_markdown(self) -> str:
        lines = [f"# {self.title}", ""]
        meta = [f"- source: {self.source_url}", f"- post_id: {self.post_id}"]
        if self.author:
            meta.append(f"- author: {self.author}")
        if self.published_at:
            meta.append(f"- published_at: {self.published_at}")
        lines += meta + [""]
        for b in self.blocks:
            if b.kind == "text":
                lines.append(b.text)
                lines.append("")
            elif b.kind == "image" and b.image:
                cap = f" — {b.image.caption}" if b.image.caption else ""
                up = f" (uploaded {b.image.uploaded_at or b.image.uploaded_on})" if b.image.uploaded_on else ""
                lines.append(f"![img_{b.image.index:02d}{up}{cap}](images/img_{b.image.index:02d}.png)")
                lines.append("")
            elif b.kind == "quote":
                lines.append("> " + b.text.replace("\n", "\n> "))
                lines.append("")
            elif b.kind == "link":
                lines.append(f"[link] {b.url}")
                lines.append("")
            elif b.kind == "rule":
                lines.append("---")
                lines.append("")
        return "\n".join(lines).rstrip() + "\n"
