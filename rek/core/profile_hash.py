"""Identifies the exact profile a verification or a comparison was made against."""
from __future__ import annotations

import hashlib
import os

FILES = ("SKILL.md", "research-method.md", "instances.md")


def profile_hash(profile_dir: str) -> str:
    """First 12 hex chars of sha256 over SKILL.md, research-method.md, instances.md, bytes concatenated in
    that order. Raises FileNotFoundError when any of them is missing."""
    h = hashlib.sha256()
    for name in FILES:
        with open(os.path.join(profile_dir, name), "rb") as f:
            h.update(f.read())
    return h.hexdigest()[:12]
