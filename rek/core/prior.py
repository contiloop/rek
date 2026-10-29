"""Which earlier posts of the same author to fetch for a run, and why. Pure: meta.json data + a post list in,
a plan out. The CLI wires the post-list adapter and the fetching.

Two routes, as the spec states them:
- date route: every image the author reused from an earlier post (upload date before this post was written)
  points at the days around that upload; every post dated within ±2 days is a candidate, no title condition.
  A candidate is confirmed only when its page carries one of those image files (`confirm`), so a busy
  posting day does not drag in unrelated posts.
- title route: content words of the title (the generic stop list below removed); a post matches when one of
  its own title tokens equals one of them. Only recent matches are kept, newest first.
"""
from __future__ import annotations

import datetime as dt
import re
from dataclasses import dataclass, field
from urllib.parse import urlparse

from rek.core.models import PostSummary

WINDOW_DAYS = 2
# An image uploaded this close before publication was uploaded while writing this post, not an earlier one.
WRITING_WINDOW_HOURS = 24
# Title route: posts older than this before publication are not fetched, and at most TITLE_KEEP of the rest.
TITLE_MAX_AGE_DAYS = 730
TITLE_KEEP = 10

# Common title words that name no topic. Generic Korean blog vocabulary only; nothing author-specific.
STOP_WORDS = frozenset(
    """한국 이야기 이유 비밀 근황 뜯어보기 알아보자 결과 상황 오늘 최근 프로젝트 대해 대한 feat vs
    내용 정리 주요 현재 이번 지금 문제 의미 방법 생각 관련 이후 이전 정도 경우 때문 그리고 하지만""".split()
)
_STOP = frozenset(w.casefold() for w in STOP_WORDS)
_PARTICLES = ("은", "는", "이", "가", "의", "에", "을", "를", "로", "과", "와")
_WORD = re.compile(r"^[가-힣A-Za-z]{2,}$")
_PUBLISHED = re.compile(r"(\d{4})\.\s*(\d{1,2})\.\s*(\d{1,2})\.?(?:\s*(\d{1,2}):(\d{2}))?")


def parse_published(text: str | None) -> dt.datetime | None:
    """Naver's "2026. 10. 24. 0:10" (time optional) → naive datetime, or None."""
    m = _PUBLISHED.search(text or "")
    if not m:
        return None
    y, mo, d, h, mi = m.groups()
    return dt.datetime(int(y), int(mo), int(d), int(h or 0), int(mi or 0))


def _upload_moment(image: dict) -> dt.datetime | None:
    if image.get("uploaded_at"):
        return dt.datetime.fromisoformat(image["uploaded_at"]).replace(tzinfo=None)
    if image.get("uploaded_on"):
        return dt.datetime.fromisoformat(image["uploaded_on"])
    return None


def reused_images(meta: dict, writing_window_hours: int = WRITING_WINDOW_HOURS) -> list[dict]:
    """Images uploaded before this post was written: their upload dates point at earlier posts."""
    published = parse_published(meta.get("published_at"))
    if published is None:
        return []
    cutoff = published - dt.timedelta(hours=writing_window_hours)
    out = []
    for image in meta.get("images", []):
        moment = _upload_moment(image)
        if moment is not None and moment < cutoff:
            out.append(image)
    return out


def earliest_needed(meta: dict) -> dt.date | None:
    """How far back the post list must reach for the date route."""
    dates = [dt.date.fromisoformat(i["uploaded_on"]) for i in reused_images(meta) if i.get("uploaded_on")]
    return min(dates) - dt.timedelta(days=WINDOW_DAYS) if dates else None


def image_path(url: str) -> str:
    """The image file's path on its host, without the size query: the same file keeps it across posts."""
    return urlparse(url).path.lstrip("/")


def reused_image_paths(meta: dict) -> dict[str, list[int]]:
    out: dict[str, list[int]] = {}
    for image in reused_images(meta):
        if image.get("url"):
            out.setdefault(image_path(image["url"]), []).append(image["index"])
    return out


def confirm(page: str, paths: dict[str, list[int]]) -> list[int]:
    """Indexes of the reused images whose file appears on the candidate's page."""
    return sorted(i for path, indexes in paths.items() if path in page for i in indexes)


def title_tokens(title: str) -> list[str]:
    """Title tokens in order: ≥2 Hangul/Latin letters, trailing particle stripped."""
    out: list[str] = []
    for token in re.split(r"[^가-힣A-Za-z0-9]+", title):
        if not _WORD.match(token):
            continue
        if token.endswith(_PARTICLES) and len(token) > 2:
            token = token[:-1]
        out.append(token)
    return out


def title_words(title: str) -> list[str]:
    """Content words of a title: its tokens minus stop words, each once."""
    out: list[str] = []
    for token in title_tokens(title):
        if token.casefold() not in _STOP and token not in out:
            out.append(token)
    return out


@dataclass(frozen=True)
class Candidate:
    post: PostSummary
    routes: list[str]

    @property
    def post_id(self) -> str:
        return self.post.post_id


@dataclass(frozen=True)
class PriorPlan:
    published_on: dt.date | None
    date_route: dict
    title_route: dict
    candidates: list[Candidate] = field(default_factory=list)

    def as_record(self) -> dict:
        """The `prior_search` block for meta.json (confirmation and fetch status are added by the CLI)."""
        return {
            "published_on": self.published_on.isoformat() if self.published_on else None,
            "writing_window_hours": WRITING_WINDOW_HOURS,
            "date_route": {**self.date_route, "window_days": WINDOW_DAYS},
            "title_route": {**self.title_route, "max_age_days": TITLE_MAX_AGE_DAYS, "keep": TITLE_KEEP},
            "candidates": [
                {"post_id": c.post.post_id, "title": c.post.title, "date": c.post.date.isoformat(), "routes": c.routes}
                for c in self.candidates
            ],
        }


def plan(meta: dict, posts: list[PostSummary]) -> PriorPlan:
    published = parse_published(meta.get("published_at"))
    published_on = published.date() if published else None
    target = str(meta.get("post_id", ""))
    # earlier posts only: the target itself and anything published after it are never priors
    pool = [p for p in posts if p.post_id != target and (published_on is None or p.date <= published_on)]

    windows: list[dict] = []
    by_date: dict[str, list[int]] = {}
    for image in reused_images(meta):
        if image.get("uploaded_on"):
            by_date.setdefault(image["uploaded_on"], []).append(image["index"])
    for uploaded_on, indexes in by_date.items():
        day = dt.date.fromisoformat(uploaded_on)
        lo, hi = day - dt.timedelta(days=WINDOW_DAYS), day + dt.timedelta(days=WINDOW_DAYS)
        matches = [p.post_id for p in pool if lo <= p.date <= hi]
        windows.append({"uploaded_on": uploaded_on, "image_indexes": sorted(indexes), "from": lo.isoformat(), "to": hi.isoformat(), "matches": matches})
    in_window = {m for w in windows for m in w["matches"]}
    date_candidates = [p.post_id for p in pool if p.post_id in in_window]  # list order (newest first), each once

    words = title_words(meta.get("title", ""))
    tokens = {p.post_id: {t.casefold() for t in title_tokens(p.title)} for p in pool}
    by_word = {w: [p.post_id for p in pool if w.casefold() in tokens[p.post_id]] for w in words}
    title_found = [p.post_id for p in pool if any(p.post_id in ids for ids in by_word.values())]
    oldest = published_on - dt.timedelta(days=TITLE_MAX_AGE_DAYS) if published_on else None
    recent = sorted((p for p in pool if p.post_id in title_found and (oldest is None or p.date >= oldest)), key=lambda p: p.date, reverse=True)
    title_kept = [p.post_id for p in recent[:TITLE_KEEP]]

    candidates = []
    for p in pool:
        routes = [name for name, found in (("date", date_candidates), ("title", title_kept)) if p.post_id in found]
        if routes:
            candidates.append(Candidate(post=p, routes=routes))
    return PriorPlan(
        published_on=published_on,
        date_route={"windows": windows, "candidates": date_candidates},
        title_route={"title": meta.get("title", ""), "words": words, "matches": by_word, "found": title_found, "kept": title_kept},
        candidates=candidates,
    )
