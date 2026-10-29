"""Ports: what the core needs from the outside world."""
from __future__ import annotations

from typing import Protocol

from rek.core.models import Post


class PostSource(Protocol):
    """Turns a URL into a Post. One adapter per site."""

    def supports(self, url: str) -> bool: ...

    def fetch(self, url: str) -> tuple[Post, str]:
        """Return the parsed post and the raw document it was parsed from."""
        ...


class ImageStore(Protocol):
    def save(self, url: str, path: str) -> int:
        """Download url into path, return byte size."""
        ...
