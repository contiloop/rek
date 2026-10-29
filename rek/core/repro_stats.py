"""Counts for a reproduction folder, computed from markers the researcher brief fixes.

research.md: a units table whose rows start with `| R<nn> |` and carry a direction cell
(뒤쪽 / 본 주제 / 앞쪽 / 계기); a `## 출처 목록` section whose table rows start with `| S<nn> |`
and carry a 1차/2차 cell. log.md: lines starting with `[검색]`, `[열람]`, `[크롬]`, `[접촉]`.
Counting by markers keeps the worker from re-reading its own files to tally by hand.
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass

_UNIT = re.compile(r"^\|?\s*(R\d{2,3})\s*\|(.*)$")
_SOURCE = re.compile(r"^(?:\|\s*|-\s*|\*\s*)?(S\d{2,3})\b\s*[|—–:-]?(.*)$")
_SOURCE_URL = re.compile(r"^(?:\|\s*|-\s*|\*\s*)(https?://\S+)(.*)$")  # unnumbered list: one URL per line
_DIRECTIONS = ("뒤쪽", "본 주제", "앞쪽", "계기")
_LOG = re.compile(r"^\[(검색|열람|크롬|접촉)\]")


@dataclass(frozen=True)
class ReproStats:
    units: int
    units_by_direction: dict
    sources: int
    primary: int
    secondary: int
    searches: int
    pages: int
    chrome: int
    contacts: int


def _cells(rest: str) -> list[str]:
    return [c.strip() for c in rest.strip().strip("|").split("|")]


def compute(research_md: str, log_md: str) -> ReproStats:
    units: dict[str, str] = {}
    sources: dict[str, str] = {}
    in_sources = False
    for line in research_md.splitlines():
        if line.startswith("## "):
            in_sources = line.strip().startswith("## 출처 목록")
        m = _UNIT.match(line)
        if m and m.group(1) not in units:
            cells = _cells(m.group(2))
            direction = next((d for d in _DIRECTIONS if any(c.startswith(d) for c in cells)), "기타")
            units[m.group(1)] = direction
            continue
        m = _SOURCE.match(line) or (_SOURCE_URL.match(line) if in_sources else None)
        if m and in_sources and m.group(1) not in sources:
            cells = _cells(m.group(2))
            text = " ".join(cells)
            kind = "1차" if re.search(r"(?<![\w가-힣])1차", text) else ("2차" if re.search(r"(?<![\w가-힣])2차", text) else "미상")
            sources[m.group(1)] = kind
    by_dir = {d: sum(1 for v in units.values() if v == d) for d in _DIRECTIONS + ("기타",)}
    counts = {"검색": 0, "열람": 0, "크롬": 0, "접촉": 0}
    for line in log_md.splitlines():
        m = _LOG.match(line.strip())
        if m:
            counts[m.group(1)] += 1
    return ReproStats(
        units=len(units),
        units_by_direction={k: v for k, v in by_dir.items() if v},
        sources=len(sources),
        primary=sum(1 for v in sources.values() if v == "1차"),
        secondary=sum(1 for v in sources.values() if v == "2차"),
        searches=counts["검색"],
        pages=counts["열람"],
        chrome=counts["크롬"],
        contacts=counts["접촉"],
    )


def as_dict(stats: ReproStats) -> dict:
    return asdict(stats)
