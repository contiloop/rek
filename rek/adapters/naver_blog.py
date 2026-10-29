"""Naver blog adapter: parses the mobile SmartEditor ONE page into a Post.

Why the mobile page: blog.naver.com wraps the post in an iframe; m.blog.naver.com serves
the rendered body directly. Why regex, not an HTML parser: the body is a flat sequence of
`se-component` divs and nothing else is needed; a parser dependency would be the only one.
"""
from __future__ import annotations

import base64
import html
import re
from urllib.parse import urlparse

from rek.adapters import http
from rek.core.models import Block, Image, Post

_POST_URL = re.compile(r"^https?://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d+)")
_POST_URL_QUERY = re.compile(r"blogId=([A-Za-z0-9_\-]+).*?logNo=(\d+)")
_COMPONENT = re.compile(r'<div class="se-component se-(\w+)[^"]*"[^>]*>(.*?)(?=<div class="se-component se-|$)', re.S)
_TAG = re.compile(r"<[^>]+>")
_PARAGRAPH = re.compile(r'<p class="se-text-paragraph[^"]*"[^>]*>(.*?)</p>', re.S)
_IMG = re.compile(r'<img[^>]+class="[^"]*se-image-resource[^"]*"[^>]*>', re.S)
_SRC = re.compile(r'(?:data-lazy-src|src)="([^"]+)"')
_CAPTION = re.compile(r'<p class="se-caption[^"]*"[^>]*>(.*?)</p>|<div class="se-caption[^"]*"[^>]*>(.*?)</div>', re.S)
_SOURCE = re.compile(r'<a[^>]+class="[^"]*se-image-source[^"]*"[^>]*>(.*?)</a>|<span[^>]+class="[^"]*se-image-source[^"]*"[^>]*>(.*?)</span>', re.S)
_OGLINK = re.compile(r'<a[^>]+class="[^"]*se-oglink[^"]*"[^>]+href="([^"]+)"', re.S)
_TITLE = re.compile(r"<title>(.*?)</title>", re.S)
_DATE = re.compile(r'class="blog_date"[^>]*>.*?<span class="txt">(.*?)</span>\s*</p>', re.S)
_AUTHOR = re.compile(r'class="blog_author"[^>]*>.*?<strong[^>]*>(.*?)</strong>', re.S)
_UPLOAD_DATE = re.compile(r"pstatic\.net/([A-Za-z0-9]+)/")


def parse_post_url(url: str) -> tuple[str, str]:
    m = _POST_URL.match(url) or _POST_URL_QUERY.search(url)
    if not m:
        raise ValueError(f"not a naver blog post url: {url}")
    return m.group(1), m.group(2)


def _clean(fragment: str) -> str:
    text = _TAG.sub("", fragment)
    text = html.unescape(text).replace("​", "")
    return re.sub(r"[ \t]+", " ", text).strip()


def decode_upload_date(image_url: str) -> str | None:
    """Naver image paths start with base64('YYYYMMDD_n'). Returns YYYY-MM-DD or None."""
    m = _UPLOAD_DATE.search(image_url)
    if not m:
        return None
    token = m.group(1)
    try:
        raw = base64.b64decode(token + "=" * (-len(token) % 4)).decode("ascii")
    except Exception:
        return None
    if len(raw) < 8 or not raw[:8].isdigit():
        return None
    return f"{raw[:4]}-{raw[4:6]}-{raw[6:8]}"


def full_size(image_url: str) -> str:
    base = re.sub(r"\?type=.*$", "", image_url)
    return base + "?type=w966"


def parse(document: str, source_url: str) -> Post:
    blog_id, post_id = parse_post_url(source_url)
    title_m = _TITLE.search(document)
    title = html.unescape(title_m.group(1)).strip() if title_m else post_id
    title = re.sub(r"\s*:\s*네이버 블로그\s*$", "", title)
    date_m = _DATE.search(document)
    author_m = _AUTHOR.search(document)
    main = document.split('class="se-main-container"', 1)
    body = main[1] if len(main) == 2 else document

    blocks: list[Block] = []
    img_index = 0
    for comp in _COMPONENT.finditer(body):
        kind, inner = comp.group(1), comp.group(2)
        if kind == "text":
            paras = [_clean(p) for p in _PARAGRAPH.findall(inner)]
            paras = [p for p in paras if p]
            if paras:
                blocks.append(Block(kind="text", text="\n".join(paras)))
        elif kind == "image":
            for tag in _IMG.findall(inner):
                src = _SRC.search(tag)
                if not src:
                    continue
                img_index += 1
                url = html.unescape(src.group(1))
                cap_m = _CAPTION.search(inner)
                src_m = _SOURCE.search(inner)
                caption = None
                if cap_m:
                    caption = _clean(cap_m.group(1) or cap_m.group(2) or "")
                if src_m:
                    attribution = _clean(src_m.group(1) or src_m.group(2) or "")
                    caption = f"{caption} | {attribution}" if caption else attribution
                blocks.append(
                    Block(
                        kind="image",
                        image=Image(
                            index=img_index,
                            url=full_size(url),
                            uploaded_on=decode_upload_date(url),
                            caption=caption or None,
                        ),
                    )
                )
        elif kind == "quotation":
            text = _clean(inner)
            if text:
                blocks.append(Block(kind="quote", text=text))
        elif kind == "oglink":
            m = _OGLINK.search(inner)
            if m:
                blocks.append(Block(kind="link", url=html.unescape(m.group(1)), text=_clean(inner)))
        elif kind == "horizontalLine":
            blocks.append(Block(kind="rule"))
        # stickers, maps, videos: skipped on purpose; they carry no claim or source.

    return Post(
        source_url=source_url,
        post_id=post_id,
        title=title,
        author=_clean(author_m.group(1)) if author_m else None,
        published_at=_clean(date_m.group(1)).lstrip('・ ') if date_m else None,
        blocks=tuple(blocks),
    )


class NaverBlogSource:
    def supports(self, url: str) -> bool:
        return urlparse(url).netloc.endswith("blog.naver.com")

    def fetch(self, url: str) -> tuple[Post, str]:
        blog_id, post_id = parse_post_url(url)
        mobile = f"https://m.blog.naver.com/{blog_id}/{post_id}"
        document = http.get(mobile).decode("utf-8", errors="replace")
        if "errorType=noPost" in document:
            raise LookupError(f"no post at {mobile} (check the post id)")
        return parse(document, url), document
