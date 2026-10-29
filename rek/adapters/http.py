"""Plain urllib HTTP. Mobile user agent because Naver's mobile pages are server-rendered."""
from __future__ import annotations

import urllib.error
import urllib.request

MOBILE_UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 "
    "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
)


def get(url: str, referer: str | None = None, timeout: float = 30.0) -> bytes:
    headers = {"User-Agent": MOBILE_UA}
    if referer:
        headers["Referer"] = referer
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


class UrllibImageStore:
    """Tries the sized URL, then the bare URL. A missing image returns 0 bytes; it never stops a run."""

    def save(self, url: str, path: str) -> int:
        candidates = [url, url.split("?", 1)[0]]
        for candidate in candidates:
            try:
                data = get(candidate, referer="https://m.blog.naver.com/")
            except urllib.error.HTTPError:
                continue
            with open(path, "wb") as f:
                f.write(data)
            return len(data)
        return 0
