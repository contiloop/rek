"""Ports: what the core needs from the outside world."""
from __future__ import annotations

import datetime as dt
from typing import Protocol

from rek.core.models import Post, PostSummary


class PostSource(Protocol):
    """Turns a URL into a Post. One adapter per site."""

    def supports(self, url: str) -> bool: ...

    def fetch(self, url: str) -> tuple[Post, str]:
        """Return the parsed post and the raw document it was parsed from."""
        ...

    def blog_of(self, url: str) -> str:
        """The blog (author account) id a post URL belongs to."""
        ...

    def post_url(self, blog_id: str, post_id: str) -> str: ...


class PostList(Protocol):
    """A blog's post list, newest first."""

    def list_posts(self, blog_id: str, until: dt.date | None) -> list[PostSummary]:
        """Page forward until a post dated before `until` has been seen; `until=None` reads the whole list."""
        ...


class ImageStore(Protocol):
    def save(self, url: str, path: str) -> int:
        """Download url into path, return byte size."""
        ...
