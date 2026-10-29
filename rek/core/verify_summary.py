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
OWN_SOURCES_MIN = 20
OWN_PRIMARY_MIN = 5
_INVALID = re.compile(r"^\s*무효\s*[:：]")
_FENCE = re.compile(r"^\s*```(?:yaml|yml)?\s*$")
_LINE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*?)\s*$")


def is_invalid(text: str) -> bool:
    """True when the verifier wrote a `무효:` line after the yaml block."""
    return any(_INVALID.match(l) for l in text.splitlines())


def evaluate_own(d: dict, invalid: bool, stats: dict | None) -> "Result":
    """The project's own pass line: a valid attempt, no fabricated fact, a chain with backward, main and
    forward units, and enough sources (OWN_SOURCES_MIN, OWN_PRIMARY_MIN of them primary). The author
    thresholds (units/rare/upstream) are reported but not required."""
    reported = d.get("verifier_verdict")
    if any(k not in d for k in KEYS):
        return Result(INCOMPLETE, {}, "missing keys", reported, False)
    if stats is None:
        return Result(INCOMPLETE, {}, "no research.md", reported, False)
    dirs = (stats or {}).get("units_by_direction", {})
    chain_ok = all(dirs.get(k, 0) >= 1 for k in ("뒤쪽", "본 주제", "앞쪽"))
    sources_ok = (stats or {}).get("sources", 0) >= OWN_SOURCES_MIN and (stats or {}).get("primary", 0) >= OWN_PRIMARY_MIN
    checks = {"valid": not invalid, "fabricated": d["fabricated"] == 0, "chain": chain_ok, "sources": sources_ok}
    reasons = [name for name, ok in (("invalid", not invalid), ("fabricated", d["fabricated"] == 0), ("chain incomplete", chain_ok), ("too few sources", sources_ok)) if not ok]
    detail = f"chain {dirs.get('뒤쪽', 0)}/{dirs.get('본 주제', 0)}/{dirs.get('앞쪽', 0)}, sources {(stats or {}).get('sources', 0)} ({(stats or {}).get('primary', 0)} primary)"
    verdict = "pass" if all(checks.values()) else "fail"
    return Result(verdict, checks, (", ".join(reasons) + "; " if reasons else "") + detail, reported, False)


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


def summarize(runs_dir: str, criteria: str = "author") -> tuple[list[Row], bool]:
    """criteria: "author" = the reference author's thresholds; "own" = evaluate_own."""
    from rek.core.repro_stats import as_dict as _stats_dict, compute as _stats

    rows = []
    for name in sorted(os.listdir(runs_dir)):
        run_dir = os.path.join(runs_dir, name)
        if not os.path.isfile(os.path.join(run_dir, "meta.json")):
            continue
        path = latest_verification(run_dir)
        data, invalid, stats = {}, False, None
        if path:
            with open(path, encoding="utf-8") as f:
                text = f.read()
            data, invalid = parse_front_matter(text), is_invalid(text)
            repro_dir = os.path.dirname(path)
            research = os.path.join(repro_dir, "research.md")
            if os.path.isfile(research):
                log = os.path.join(repro_dir, "log.md")
                with open(research, encoding="utf-8") as f:
                    r_text = f.read()
                l_text = open(log, encoding="utf-8").read() if os.path.isfile(log) else ""
                stats = _stats_dict(_stats(r_text, l_text))
        result = evaluate_own(data, invalid, stats) if criteria == "own" else evaluate(data)
        rows.append(Row(name, data, result, path))
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
    lines.append(f"overall: {'pass' if all_pass else 'fail'} ({n_pass}/{len(rows)} pass)")
    return "\n".join(lines) + "\n"
