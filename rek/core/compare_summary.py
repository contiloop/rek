"""One line per run from a comparator's comparison.md. Pure functions over the file's text.

comparison.md starts with a yaml block of 11 keys; the values are the comparison worker's judgments, so this
module copies them and computes no verdict. Validity is decided by the `무효:` line after the block; when the
`invalid` key disagrees with that line, the line gets ` 불일치`.
"""
from __future__ import annotations

from rek.core.verify_summary import INCOMPLETE, is_invalid, parse_front_matter

KEYS = (
    "units_total", "units_covered", "facts_total", "facts_matched", "facts_conflicting", "fabricated",
    "depth_original", "depth_repro", "extra_units", "invalid", "profile_hash",
)
_INT_KEYS = KEYS[:10]
FILE = "comparison.md"


def parse(text: str) -> dict:
    return parse_front_matter(text, int_keys=_INT_KEYS)


def line(run_id: str, text: str) -> str:
    d = parse(text)
    if any(k not in d for k in KEYS):
        return f"{run_id} | {INCOMPLETE}"
    invalid = is_invalid(text)
    validity = ("invalid" if invalid else "valid") + (" 불일치" if d["invalid"] != (1 if invalid else 0) else "")
    return (f"{run_id} | units {d['units_covered']}/{d['units_total']} | facts {d['facts_matched']}/{d['facts_total']} "
            f"(conflict {d['facts_conflicting']}) | fabricated {d['fabricated']} | depth {d['depth_original']}→{d['depth_repro']} "
            f"| extra {d['extra_units']} | {validity} | {d['profile_hash']}")


def render(runs: list[tuple[str, str]]) -> str:
    """runs: (run_id, comparison.md text) in display order."""
    return "".join(line(run_id, text) + "\n" for run_id, text in runs)
