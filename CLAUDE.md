# REK — Reverse Engineering Knowledge

A single-user local tool, packaged as a Claude Code plugin. Given the URL of a published post, it traces every claim to
its sources, reconstructs how the author researched the piece, distills that into a research procedure another agent can
run, and tests the procedure by giving a fresh agent only the topic, one trigger sentence and the date. Python does only
the deterministic part (fetch, counts, pass/fail); every judgment runs in an Opus worker with a written brief. One reference
author (a Korean economics blogger, profile `reference-a`) has been traced so far; the loop itself knows no author.

## Project structure

```
REK/
├── CLAUDE.md / AGENTS.md           → this entry point (identical)
├── .claude-plugin/                 → plugin.json, marketplace.json (the repository is its own marketplace)
├── skills/rek/
│   ├── SKILL.md                    → orchestrator procedure: the six stages
│   ├── AGENTS.md                   → scope and invariants of the agent loop (briefs, markers, isolation)
│   └── references/                 → one brief per worker + evidence.md (labels, Chrome lock, status lines, definitions)
├── agents/                         → rek (orchestrator) and four workers, all `model: opus`, `effort: max`
├── rek/
│   ├── AGENTS.md                   → scope and invariants of the Python package
│   ├── core/                       → pure models, statistics, prior-post selection, pass/fail, hashes, site ledger
│   ├── ports/                      → PostSource, PostList, ImageStore protocols
│   ├── adapters/                   → Naver blog (mobile page parser, post-list API), urllib HTTP
│   └── cli.py                      → `rek fetch | prior | stats | repro-stats | profile-hash | source-sites | verify-summary`
├── tests/                          → pytest; fixtures are real saved pages
├── runs/<post_id>/                 → data: post, trace files, units, repro/<n>/ attempts and their verification
├── profiles/<author>/              → data: research-method, writing-structure, SKILL, holdout/<post_id>/ variants
└── docs/
    ├── architecture.md             → the two layers and how a post flows through the six stages
    ├── business-rules.md           → definitions, label rules, unit rules, reproduction rules, scoring rules
    ├── security.md                 → web content is data, Chrome is read-only, reproduction isolation
    ├── standards.md                → the rules whose violation breaks tests or the experiment
    ├── engineering-notes.md        → Naver quirks, worker traps, scoring traps, tool quirks
    ├── operations.md               → setup, commands, running the loop, data folders
    ├── contracts.md                → CLI output keys, file contracts, plugin component names
    └── tracking/                   → status.md, decisions/, findings.md
```

## Hard gates

- Every worker statement carries `[observed]`, `[inferred]` or `[unknown]` as `skills/rek/references/evidence.md` defines; a
  source that was not opened and matched is never `[observed]`.
- The reproduction worker is told nothing about the author; it never reads the original post, files of its run folder, or the content of
  pages published after `date:`; every fact in its post must trace to a source in its `research.md`.
- `units.md` is fixed before a reproduction starts and never edited afterwards; it is the denominator of every score.
- Pass/fail is computed by `rek verify-summary`, never read from a worker's opinion; any deterministic count is code.
- No author-specific name or rule outside `profiles/<author>/`; workers are `model: opus`, `effort: max`.

## Before you work

- Read `docs/standards.md` and `docs/engineering-notes.md`, then the `AGENTS.md` of the part you touch.
- Before changing a brief in `skills/rek/references/`: read `evidence.md` (shared definitions) and the file-format
  contracts in `docs/contracts.md`; the counters in `rek/core/` parse the markers the briefs prescribe.
- Before changing scoring: read the scoring rules in `docs/business-rules.md` and decision 0001; thresholds live in
  `rek/core/verify_summary.py` and must match the spec'd numbers.
- Before touching the Naver adapter: read the Naver section of `docs/engineering-notes.md` and run `uv run pytest -q`.
- Before launching workers: check `runs/<post_id>/status.md` for a worker already working on that run (one run, one
  worker at a time).

## When something goes wrong

Report to the user immediately when: a reproduction worker touched the author's blog or the original post; a score was
computed from a `units.md` edited after reproduction; a worker wrote outside its folder or ran git; a count or verdict in a
report came from a model instead of `rek` commands. Everything else goes into `docs/tracking/findings.md` with why it cannot
be solved now.
