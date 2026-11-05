"""One line per run from a comparator's comparison.md, with the pass line. Pure functions over the file's text.

comparison.md starts with a yaml block of 13 keys. The values are the comparison worker's judgments; this module
copies them and computes only the pass line from them: a valid attempt (no `무효:` line after the block), no
fabricated fact, and a backward and a forward depth each at least the original's (`≥` includes equality).
Units covered, facts and extra units are shown but never decide. When the `invalid` key disagrees with the `무효:`
line, the line decides and the validity cell gets ` 불일치`.

A block with the 11 keys of the earlier contract (`depth_original`, `depth_repro` in place of the four depth keys)
is shown as "old format, no verdict"; anything else is incomplete. Neither has a verdict.
"""
from __future__ import annotations

from dataclasses import dataclass

from rek.core.verify_summary import INCOMPLETE, is_invalid, parse_front_matter

DEPTH_KEYS = ("depth_back_original", "depth_back_repro", "depth_forward_original", "depth_forward_repro")
KEYS = (
    "units_total", "units_covered", "facts_total", "facts_matched", "facts_conflicting", "fabricated",
    *DEPTH_KEYS, "extra_units", "invalid", "profile_hash",
)
OLD_KEYS = (
    "units_total", "units_covered", "facts_total", "facts_matched", "facts_conflicting", "fabricated",
    "depth_original", "depth_repro", "extra_units", "invalid", "profile_hash",
)
CONDITIONS = ("valid", "fabricated", "depth_back", "depth_forward")  # the order failed names are printed in
OLD_FORMAT = "old format, no verdict"
FILE = "comparison.md"
_INT_KEYS = tuple(dict.fromkeys(KEYS[:-1] + OLD_KEYS[:-1]))


@dataclass(frozen=True)
class Row:
    line: str
    verdict: str | None  # "pass" | "fail"; None for an old-format or incomplete file


def parse(text: str) -> dict:
    return parse_front_matter(text, int_keys=_INT_KEYS)


def failed_conditions(d: dict, invalid: bool) -> list[str]:
    """Names from CONDITIONS that do not hold, in that order. `d` holds the 13 keys."""
    holds = {
        "valid": not invalid,
        "fabricated": d["fabricated"] == 0,
        "depth_back": d["depth_back_repro"] >= d["depth_back_original"],
        "depth_forward": d["depth_forward_repro"] >= d["depth_forward_original"],
    }
    return [name for name in CONDITIONS if not holds[name]]


def _validity(d: dict, invalid: bool) -> str:
    return ("invalid" if invalid else "valid") + (" 불일치" if d["invalid"] != (1 if invalid else 0) else "")


def _counts(d: dict) -> str:
    return (f"units {d['units_covered']}/{d['units_total']} | facts {d['facts_matched']}/{d['facts_total']} "
            f"(conflict {d['facts_conflicting']}) | fabricated {d['fabricated']}")


def row(run_id: str, text: str) -> Row:
    d = parse(text)
    invalid = is_invalid(text)
    if all(k in d for k in KEYS):
        failed = failed_conditions(d, invalid)
        verdict = f"fail ({', '.join(failed)})" if failed else "pass"
        depth = (f"depth back {d['depth_back_original']}→{d['depth_back_repro']}, "
                 f"forward {d['depth_forward_original']}→{d['depth_forward_repro']}")
        return Row(f"{run_id} | {verdict} | {depth} | {_counts(d)} | extra {d['extra_units']} "
                   f"| {_validity(d, invalid)} | {d['profile_hash']}", "fail" if failed else "pass")
    if all(k in d for k in OLD_KEYS) and not any(k in d for k in DEPTH_KEYS):
        return Row(f"{run_id} | {OLD_FORMAT} | {_counts(d)} | depth {d['depth_original']}→{d['depth_repro']} "
                   f"| extra {d['extra_units']} | {_validity(d, invalid)} | {d['profile_hash']}", None)
    return Row(f"{run_id} | {INCOMPLETE}", None)


def line(run_id: str, text: str) -> str:
    return row(run_id, text).line


def render(runs: list[tuple[str, str]]) -> tuple[str, bool]:
    """runs: (run_id, comparison.md text) in display order. Returns the lines and whether no run failed
    (old-format and incomplete runs do not count)."""
    rows = [row(run_id, text) for run_id, text in runs]
    return "".join(r.line + "\n" for r in rows), all(r.verdict != "fail" for r in rows)
