"""Site (registered-domain) ledger computed from the sources.md files of one or more runs.

Each `## Sxx — <publisher> … (<date>) [label]` entry is followed by a `URL:` line (one or more URLs,
free text allowed) and a `표시:` line (희귀 / 바탕 marks). The ledger groups the URLs' registered
domains, so a researcher can go back to the sites an author's sources came from.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from urllib.parse import urlparse

_ENTRY = re.compile(r"^## (S\d{2,3}) — (.*?)(?:, |$)")
_URL = re.compile(r"https?://[^\s)\]>\"']+")
_SECOND_LEVEL = {"co.kr", "go.kr", "or.kr", "ne.kr", "re.kr", "ac.kr", "co.jp", "or.jp", "ne.jp", "go.jp", "ac.jp",
                 "com.au", "co.uk", "org.uk", "gov.uk", "com.cn", "com.tw", "com.br", "com.vn", "co.in", "com.sg"}


def registered_domain(url: str) -> str | None:
    host = (urlparse(url).hostname or "").lower()
    if not host or "." not in host:
        return None
    parts = host.split(".")
    if len(parts) >= 3 and ".".join(parts[-2:]) in _SECOND_LEVEL:
        return ".".join(parts[-3:])
    return ".".join(parts[-2:])


@dataclass
class Site:
    domain: str
    runs: set = field(default_factory=set)
    sources: int = 0
    rare: int = 0
    upstream: int = 0
    publishers: set = field(default_factory=set)
    example_urls: list = field(default_factory=list)


def parse_sources(markdown: str, run_id: str, sites: dict[str, Site]) -> None:
    current: dict | None = None
    for line in markdown.splitlines():
        m = _ENTRY.match(line)
        if m:
            current = {"id": m.group(1), "publisher": m.group(2).strip(), "domains": set(), "mark": ""}
            continue
        if current is None:
            continue
        if line.startswith("URL:"):
            for u in _URL.findall(line):
                d = registered_domain(u)
                if d:
                    current["domains"].add((d, u))
        elif line.startswith("표시:"):
            current["mark"] = line
            for d, u in current["domains"]:
                site = sites.setdefault(d, Site(domain=d))
                site.runs.add(run_id)
                site.sources += 1
                site.publishers.add(current["publisher"])
                if "희귀" in line.split(" (")[0]:
                    site.rare += 1
                if "바탕" in line.split(" (")[0] and "저자 글" not in line.split(" (")[0]:
                    site.upstream += 1
                if len(site.example_urls) < 2:
                    site.example_urls.append(u)
            current = None


def render(sites: dict[str, Site]) -> str:
    rows = sorted(sites.values(), key=lambda s: (-len(s.runs), -s.rare, -s.sources, s.domain))
    out = ["| 도메인 | 글 수 | 출처 수 | 희귀 | 바탕 | 발행처 | 예시 URL |", "|---|---|---|---|---|---|---|"]
    for s in rows:
        pubs = ", ".join(sorted(s.publishers))[:60]
        out.append(f"| {s.domain} | {len(s.runs)} | {s.sources} | {s.rare} | {s.upstream} | {pubs} | {s.example_urls[0] if s.example_urls else ''} |")
    return "\n".join(out) + "\n"
