"""Pass/fail over verification.md files. Pure functions over parsed dicts; the verifier's own verdict is
displayed next to the computed one and never trusted.

verification.md starts with a yaml block (```yaml ... ```) of `key: value` lines; a small parser reads it,
so the project stays stdlib-only.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass

KEYS = (
    "units_total", "units_found", "rare_total", "rare_found", "upstream_total", "upstream_found",
    "fabricated", "numbers_total", "numbers_exact", "profile_hash", "verifier_verdict",
)
_INT_KEYS = KEYS[:9]
UNITS_MIN = 0.90
RARE_MIN = 0.80
INCOMPLETE = "미실행/불완전"
_FENCE = re.compile(r"^\s*```(?:yaml|yml)?\s*$")
_LINE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*?)\s*$")


def parse_front_matter(text: str) -> dict:
    """Reads `key: value` lines from the first fenced yaml block (or from a leading `---` block)."""
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if _FENCE.match(l) or l.strip() == "---"), None)
    if start is None:
        return {}
    out: dict = {}
    for line in lines[start + 1:]:
        if _FENCE.match(line) or line.strip() == "---":
            break
        m = _LINE.match(line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip("\"'")
        if key in _INT_KEYS:
            try:
                out[key] = int(value)
            except ValueError:
                continue
        else:
            out[key] = value
    return out


@dataclass(frozen=True)
class Result:
    verdict: str  # "pass" | "fail" | INCOMPLETE
    checks: dict  # name -> bool (empty when incomplete)
    reason: str  # why it failed, "" when it passed
    reported: str | None  # verifier_verdict as written
    mismatch: bool  # reported verdict differs from the computed one

    @property
    def passed(self) -> bool:
        return self.verdict == "pass"


def evaluate(d: dict) -> Result:
    reported = d.get("verifier_verdict")
    if any(k not in d for k in KEYS):
        return Result(INCOMPLETE, {}, "키 누락", reported, reported is not None and reported != "fail")
    units_ok = d["units_total"] > 0 and d["units_found"] / d["units_total"] >= UNITS_MIN
    rare_ok = d["rare_total"] == 0 or d["rare_found"] / d["rare_total"] >= RARE_MIN
    upstream_ok = d["upstream_found"] == d["upstream_total"]
    fabricated_ok = d["fabricated"] == 0
    checks = {"units": units_ok, "rare": rare_ok, "upstream": upstream_ok, "fabricated": fabricated_ok}
    reasons = []
    if not units_ok:
        reasons.append("단위 없음" if d["units_total"] == 0 else "단위 미달")
    if not rare_ok:
        reasons.append("희귀 미달")
    if not upstream_ok:
        reasons.append("상류 미달")
    if not fabricated_ok:
        reasons.append("날조")
    verdict = "pass" if all(checks.values()) else "fail"
    return Result(verdict, checks, ", ".join(reasons), reported, reported != verdict)


@dataclass(frozen=True)
class Row:
    run_id: str
    data: dict
    result: Result
    path: str | None


def latest_verification(run_dir: str) -> str | None:
    """`repro/<n>/verification.md` with the largest n, or None."""
    repro = os.path.join(run_dir, "repro")
    if not os.path.isdir(repro):
        return None
    numbered = [(int(n), n) for n in os.listdir(repro) if n.isdigit()]
    for _, n in sorted(numbered, reverse=True):
        path = os.path.join(repro, n, "verification.md")
        if os.path.isfile(path):
            return path
    return None


def summarize(runs_dir: str) -> tuple[list[Row], bool]:
    rows = []
    for name in sorted(os.listdir(runs_dir)):
        run_dir = os.path.join(runs_dir, name)
        if not os.path.isfile(os.path.join(run_dir, "meta.json")):
            continue
        path = latest_verification(run_dir)
        data = {}
        if path:
            with open(path, encoding="utf-8") as f:
                data = parse_front_matter(f.read())
        rows.append(Row(name, data, evaluate(data), path))
    return rows, bool(rows) and all(r.result.passed for r in rows)


def _ratio(d: dict, found: str, total: str) -> str:
    return f"{d[found]}/{d[total]}" if found in d and total in d else "-"


def render(rows: list[Row], all_pass: bool) -> str:
    header = ("run", "units", "rare", "upstream", "fabricated", "numbers", "profile_hash", "verdict")
    table = [header]
    for r in rows:
        d, res = r.data, r.result
        verdict = res.verdict if res.verdict == INCOMPLETE else res.verdict + (f" ({res.reason})" if res.reason else "")
        shown = f"{verdict} | verifier: {res.reported or '-'}" + (" 불일치" if res.mismatch else "")
        table.append((
            r.run_id, _ratio(d, "units_found", "units_total"), _ratio(d, "rare_found", "rare_total"),
            _ratio(d, "upstream_found", "upstream_total"), str(d.get("fabricated", "-")),
            _ratio(d, "numbers_exact", "numbers_total"), str(d.get("profile_hash", "-")), shown,
        ))
    widths = [max(len(row[i]) for row in table) for i in range(len(header))]
    lines = ["  ".join(cell.ljust(widths[i]) for i, cell in enumerate(row)).rstrip() for row in table]
    n_pass = sum(1 for r in rows if r.result.passed)
    lines.append(f"전체: {'합격' if all_pass else '불합격'} ({n_pass}/{len(rows)} 합격)")
    return "\n".join(lines) + "\n"
