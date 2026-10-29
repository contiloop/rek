"""Identifies the exact profile a verification was scored against."""
from __future__ import annotations

import hashlib
import os

FILES = ("SKILL.md", "research-method.md")


def profile_hash(profile_dir: str) -> str:
    """First 12 hex chars of sha256 over SKILL.md then research-method.md, bytes concatenated.
    Raises FileNotFoundError when either file is missing."""
    h = hashlib.sha256()
    for name in FILES:
        with open(os.path.join(profile_dir, name), "rb") as f:
            h.update(f.read())
    return h.hexdigest()[:12]
