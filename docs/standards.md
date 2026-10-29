# Rules to follow

This file lists only what breaks tests, makes test results untrustworthy, or stops the next person from reproducing the work when violated.

## Code

- Python uses only the standard library. To add a dependency, list it in `pyproject.toml` and record the reason in `docs/tracking/decisions/`.
- `rek/core/` knows nothing about the network or site names; its file access is confined to `run_dir.py`, `profile_hash.py` and `verify_summary.summarize`, and everything else in it is pure functions over strings and dicts. Site access is done by `rek/adapters/` implementing the protocols in `rek/ports/`. Only `cli.py` joins the two. If core imports adapters, that is a violation.
- Calculations with a single correct answer (format statistics, reproduction aggregation, pass verdicts, hashes, the domain ledger) are done by code. A brief that makes workers count by hand and report is a violation. Workers run the command and paste its output.
- Write tests before new features (`tests/`). Use real saved pages as fixed data (`tests/fixtures/`). Do not add tests that use the network.
- The `≥` in threshold comparisons includes equality. Text after `## 작성 노트` (the writing-notes heading) is not counted in format statistics.

## Briefs and agents

- No brief or code may contain the name or rules of a specific author. Author-specific content goes only inside `profiles/<author>/`. To check, `grep -ril "<author name>" skills agents rek` must return nothing.
- Every worker agent uses `model: opus` and `effort: max`. The orchestrator does not analyze.
- Script paths inside briefs take the form `${CLAUDE_PLUGIN_ROOT}/skills/rek/references/<file>` and `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek …`. Paths relative to the working folder, or absolute paths, break in other folders.
- Write the Chrome lock, status logging, and label definitions only in `skills/rek/references/evidence.md`. Other briefs refer to it.
- `verification.md` **starts** with 11 yaml keys (`units_total, units_found, rare_total, rare_found, upstream_total, upstream_found,
  fabricated, numbers_total, numbers_exact, profile_hash, verifier_verdict`). The canonical example block is `tests/fixtures/verification_example.md`, and briefs copy it.
- Do not put labels or evidence marks in the body of a reproduced post.

## Data and git

- Do not put `runs/**/images/` and `runs/**/raw.html` into git. Put the other run files and the profiles in.
- Reproductions accumulate by number in `repro/<n>/` and are never overwritten. Do not change `units.md` after a reproduction.
- End each commit message with the line `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`.

## Verification gate

Before merging: `uv run pytest -q` passes in full and `claude plugin validate .` passes. If you changed the plugin structure, run `claude --plugin-dir <this folder> -p "..."` from another folder and confirm that the `rek:rek` skill and the `rek:rek-*` agents are visible.
