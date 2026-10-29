"""Naver blog adapter: parses the mobile SmartEditor ONE page into a Post.

Why the mobile page: blog.naver.com wraps the post in an iframe; m.blog.naver.com serves
the rendered body directly. Why regex, not an HTML parser: the body is a flat sequence of
`se-component` divs and nothing else is needed; a parser dependency would be the only one.
"""
from __future__ import annotations

import base64
import datetime as dt
import html
import json
import re
from urllib.parse import unquote_plus, urlparse

from rek.adapters import http
from rek.core.models import Block, Image, Post, PostSummary

_POST_URL = re.compile(r"^https?://(?:m\.)?blog\.naver\.com/([A-Za-z0-9_\-]+)/(\d+)")
_POST_URL_QUERY = re.compile(r"blogId=([A-Za-z0-9_\-]+).*?logNo=(\d+)")
_COMPONENT = re.compile(r'<div class="se-component se-(\w+)[^"]*"[^>]*>(.*?)(?=<div class="se-component se-|$)', re.S)
_TAG = re.compile(r"<[^>]+>")
_PARAGRAPH = re.compile(r'<p class="se-text-paragraph[^"]*"[^>]*>(.*?)</p>', re.S)
_IMG = re.compile(r'<img[^>]+class="[^"]*se-image-resource[^"]*"[^>]*>', re.S)
_SRC = re.compile(r'(?:data-lazy-src|src)="([^"]+)"')
_CAPTION = re.compile(r'class="[^"]*\bse-caption\b[^"]*"[^>]*>(.*?)</div>', re.S)
_SOURCE = re.compile(r'<a[^>]+class="[^"]*se-image-source[^"]*"[^>]*>(.*?)</a>|<span[^>]+class="[^"]*se-image-source[^"]*"[^>]*>(.*?)</span>', re.S)
_OGLINK = re.compile(r'<a[^>]+class="[^"]*se-oglink[^"]*"[^>]+href="([^"]+)"', re.S)
_TITLE = re.compile(r"<title>(.*?)</title>", re.S)
_DATE = re.compile(r'class="blog_date"[^>]*>.*?<span class="txt">(.*?)</span>\s*</p>', re.S)
_AUTHOR = re.compile(r'class="blog_author"[^>]*>.*?<strong[^>]*>(.*?)</strong>', re.S)
_UPLOAD_DATE = re.compile(r"pstatic\.net/([A-Za-z0-9]+)/([A-Za-z0-9]+)\.")
_KST = dt.timezone(dt.timedelta(hours=9))


def parse_post_url(url: str) -> tuple[str, str]:
    m = _POST_URL.match(url) or _POST_URL_QUERY.search(url)
    if not m:
        raise ValueError(f"not a naver blog post url: {url}")
    return m.group(1), m.group(2)


def _clean(fragment: str) -> str:
    text = _TAG.sub("", fragment)
    text = html.unescape(text).replace("​", "")
    return re.sub(r"[ \t]+", " ", text).strip()


def _b64(token: str) -> str | None:
    try:
        return base64.b64decode(token + "=" * (-len(token) % 4)).decode("ascii")
    except Exception:
        return None


def decode_upload_date(image_url: str) -> str | None:
    """Naver image paths start with base64('YYYYMMDD_n'). Returns YYYY-MM-DD or None."""
    m = _UPLOAD_DATE.search(image_url)
    raw = _b64(m.group(1)) if m else None
    if not raw or len(raw) < 8 or not raw[:8].isdigit():
        return None
    return f"{raw[:4]}-{raw[4:6]}-{raw[6:8]}"


def decode_upload_time(image_url: str) -> str | None:
    """The second path segment is base64 of the upload epoch in milliseconds. Returns ISO time in KST."""
    m = _UPLOAD_DATE.search(image_url)
    raw = _b64(m.group(2)) if m else None
    if not raw or not raw.isdigit():
        return None
    return dt.datetime.fromtimestamp(int(raw) / 1000, _KST).replace(microsecond=0).isoformat()


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
                    caption = _clean(cap_m.group(1))
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
                            uploaded_at=decode_upload_time(url),
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

    def blog_of(self, url: str) -> str:
        return parse_post_url(url)[0]

    def post_url(self, blog_id: str, post_id: str) -> str:
        return f"https://blog.naver.com/{blog_id}/{post_id}"

    def fetch(self, url: str) -> tuple[Post, str]:
        blog_id, post_id = parse_post_url(url)
        mobile = f"https://m.blog.naver.com/{blog_id}/{post_id}"
        document = http.get(mobile).decode("utf-8", errors="replace")
        if "errorType=noPost" in document:
            raise LookupError(f"no post at {mobile} (check the post id)")
        return parse(document, url), document


# --- post list -----------------------------------------------------------------------------

_LIST_URL = "https://blog.naver.com/PostTitleListAsync.naver?blogId={blog}&currentPage={page}&countPerPage=30&categoryNo=0&parentCategoryNo="
_ABS_DATE = re.compile(r"^(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})\.?$")
_REL_DATE = re.compile(r"^(\d+)\s*(초|분|시간|일)\s*전$")


def _list_date(text: str, today: dt.date) -> dt.date | None:
    """addDate is "2026. 10. 24." for older posts and "12시간 전" / "방금 전" / "3일 전" for recent ones."""
    text = text.strip()
    m = _ABS_DATE.match(text)
    if m:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = _REL_DATE.match(text)
    if m:
        return today - dt.timedelta(days=int(m.group(1))) if m.group(2) == "일" else today
    if text.endswith("전"):  # "방금 전" and any other relative wording: today
        return today
    return None


def parse_post_list(body: str, today: dt.date) -> list[PostSummary]:
    """One page of PostTitleListAsync.naver. The body escapes single quotes as \\' which JSON does not allow."""
    data = json.loads(body.replace("\\'", "'"))
    posts = []
    for item in data.get("postList") or []:
        date = _list_date(str(item.get("addDate", "")), today)
        if date is None:
            continue
        title = html.unescape(unquote_plus(str(item.get("title", "")))).strip()
        posts.append(PostSummary(post_id=str(item["logNo"]), title=title, date=date))
    return posts


class NaverPostList:
    """Pages the blog's post list newest-first; pages are cached for the life of the object (one run)."""

    def __init__(self, fetch_page=None):
        self._fetch_page = fetch_page or self._http_page
        self._pages: dict[tuple[str, int], list[PostSummary]] = {}

    @staticmethod
    def _http_page(blog_id: str, page: int) -> str:
        url = _LIST_URL.format(blog=blog_id, page=page)
        return http.get(url, referer=f"https://blog.naver.com/{blog_id}", user_agent=http.DESKTOP_UA).decode("utf-8", errors="replace")

    def page(self, blog_id: str, page: int) -> list[PostSummary]:
        key = (blog_id, page)
        if key not in self._pages:
            self._pages[key] = parse_post_list(self._fetch_page(blog_id, page), today=dt.datetime.now(_KST).date())
        return self._pages[key]

    def list_posts(self, blog_id: str, until: dt.date | None) -> list[PostSummary]:
        out: list[PostSummary] = []
        seen: set[str] = set()
        page = 1
        while True:
            rows = [r for r in self.page(blog_id, page) if r.post_id not in seen]
            if not rows:  # empty page, or a page that only repeats what came before: the end
                break
            out.extend(rows)
            seen.update(r.post_id for r in rows)
            if until is not None and any(r.date < until for r in rows):
                break
            page += 1
        return out
