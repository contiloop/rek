"""A research folder for a new topic (the product use of the loop, no original post to compare with).

`research/<YYYYMMDD>-<slug>/topic.md` holds the five start lines the topic researcher receives; `check.md`
(written by the topic checker) starts with a yaml block holding `fabricated`, `late_sources`, `checker_verdict`.
The pass line is the project's own criteria minus the unit match that needs an original: a chain with
backward, main and forward units, enough sources, no fabricated fact, no source dated after `date:`.
"""
from __future__ import annotations

import datetime as dt
import os
import re
from dataclasses import dataclass

from rek.core.repro_stats import as_dict as _stats_dict, compute as _stats
from rek.core.verify_summary import INCOMPLETE, OWN_PRIMARY_MIN, OWN_SOURCES_MIN, parse_front_matter

CHECK_KEYS = ("fabricated", "late_sources", "checker_verdict")
TOPIC_KEYS = ("main_topic", "trigger", "date", "language", "profile")
_SLUG = re.compile(r"[^\w]+", re.UNICODE)


def slug(topic: str, limit: int = 40) -> str:
    return _SLUG.sub("-", topic.strip()).strip("-").lower()[:limit].rstrip("-") or "topic"


def folder_name(topic: str, now: dt.datetime) -> str:
    return f"{now:%Y%m%d}-{slug(topic)}"


def topic_lines(main_topic: str, trigger: str, date: str, language: str, profile: str) -> str:
    values = {"main_topic": main_topic.strip(), "trigger": trigger.strip() or "none", "date": date.strip(),
              "language": language.strip(), "profile": profile.strip()}
    return "".join(f"{k}: {values[k]}\n" for k in TOPIC_KEYS)


def default_date(now: dt.datetime) -> str:
    """`YYYY-MM-DD HH:MM KST`, the same form the trace writes in units.md."""
    kst = now.astimezone(dt.timezone(dt.timedelta(hours=9)))
    return f"{kst:%Y-%m-%d %H:%M} KST"


def parse_check(text: str) -> dict:
    return parse_front_matter(text, int_keys=CHECK_KEYS[:2])


@dataclass(frozen=True)
class Verdict:
    verdict: str  # "pass" | "fail" | INCOMPLETE
    checks: dict
    reason: str
    reported: str | None

    @property
    def passed(self) -> bool:
        return self.verdict == "pass"


def evaluate(stats: dict | None, check: dict | None) -> Verdict:
    if stats is None:
        return Verdict(INCOMPLETE, {}, "no research.md", None)
    if check is None or any(k not in check for k in CHECK_KEYS):
        return Verdict(INCOMPLETE, {}, "no check.md or missing keys", (check or {}).get("checker_verdict"))
    dirs = stats.get("units_by_direction", {})
    checks = {
        "chain": all(dirs.get(k, 0) >= 1 for k in ("뒤쪽", "본 주제", "앞쪽")),
        "sources": stats.get("sources", 0) >= OWN_SOURCES_MIN and stats.get("primary", 0) >= OWN_PRIMARY_MIN,
        "fabricated": check["fabricated"] == 0,
        "late_sources": check["late_sources"] == 0,
    }
    names = {"chain": "chain incomplete", "sources": "too few sources", "fabricated": "fabricated", "late_sources": "source after date"}
    reasons = [names[k] for k, ok in checks.items() if not ok]
    detail = (f"chain {dirs.get('뒤쪽', 0)}/{dirs.get('본 주제', 0)}/{dirs.get('앞쪽', 0)}, sources {stats.get('sources', 0)} "
              f"({stats.get('primary', 0)} primary), fabricated {check['fabricated']}, late sources {check['late_sources']}")
    verdict = "pass" if all(checks.values()) else "fail"
    return Verdict(verdict, checks, (", ".join(reasons) + "; " if reasons else "") + detail, check["checker_verdict"])


def summarize(research_dir: str) -> Verdict:
    research = os.path.join(research_dir, "research.md")
    stats = None
    if os.path.isfile(research):
        log = os.path.join(research_dir, "log.md")
        with open(research, encoding="utf-8") as f:
            r_text = f.read()
        l_text = open(log, encoding="utf-8").read() if os.path.isfile(log) else ""
        stats = _stats_dict(_stats(r_text, l_text))
    check = None
    check_path = os.path.join(research_dir, "check.md")
    if os.path.isfile(check_path):
        with open(check_path, encoding="utf-8") as f:
            check = parse_check(f.read())
    return evaluate(stats, check)


def render(research_dir: str, v: Verdict) -> str:
    line = v.verdict if v.verdict == INCOMPLETE else f"{v.verdict} ({v.reason})"
    mismatch = " 불일치" if v.reported and v.verdict != INCOMPLETE and v.reported != v.verdict else ""
    return f"{research_dir}: {line} | checker: {v.reported or '-'}{mismatch}\n"
