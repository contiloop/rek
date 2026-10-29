# REK — Reverse Engineering Knowledge

Given the URL of a published post, REK traces every claim to its sources, reconstructs how the
author researched the piece, distills that into a research procedure another agent can run, and
tests the procedure: a fresh agent gets only the main topic, one trigger sentence and the date,
researches on its own, and its result is scored against the original's chain of development units
and hard-to-find sources. The goal is a research loop that finds the backward links (history,
origins) and the forward links (money, politics, the local angle) of a topic with every fact traced
to a source; the reference author's posts are the material the procedure was learned from and the
yardstick it is compared with.

The investigation loop is adapted from [morluto/rea](https://github.com/morluto/rea) (reverse
engineering of binaries): route the target → summary-first inventory → evidence ledger whose every
line is `observed`, `inferred` or `unknown` → residual unknowns → reconstruction verified against a
finite list. See `skills/rek/SKILL.md` for the correspondence table.

## What was taken from each reference

| reference | taken | depth | not taken |
|---|---|---|---|
| morluto/rea | investigation loop: route → inventory → evidence with observed/inferred/unknown → residual unknowns → reconstruction verified against a finite claim list; parallel workers with distinct scopes returning sources, conclusions, gaps | principle, rebuilt for text | its MCP tools, binary formats, Evidence IDs and hashing |
| a spec-first agent harness the user already uses | one orchestrator, workers only for independent checks, an independent reviewer that should find nothing, failures routed to the stage that owns them, the user approves before the costly run | principle | its document formats and dialogue stages |
| OneSpiral/ghost-writer and similar style cloners | a style profile is many named dimensions, each with evidence | principle | their dimension list (ours is derived from the posts) |
| ProjectJang guidelines | hexagonal layout, tests before each slice, real data for verification, fix upstream not output, delete leftovers | copy | — |

## Layout

```
rek/                 Python, standard library only (hexagonal: core/ pure logic, ports/, adapters/)
  adapters/naver_blog.py   Naver mobile page → Post; post-list API; decodes image upload times from image URLs
  cli.py                   fetch · prior · stats · repro-stats · profile-hash · source-sites · verify-summary · research-init · research-summary
tests/               pytest, fixture = one real Naver page
.claude-plugin/      plugin manifest (the repository root is the plugin)
skills/research/     the product entry: research a new topic with a profile and write the post
skills/rek/          the learning loop; references/ holds one brief per worker (both skills)
agents/              rek (orchestrator) + six worker agents (opus, effort max); scripts are reached via ${CLAUDE_PLUGIN_ROOT}
research/<date>-<slug>/  topic.md, research.md, post.md, log.md, check.md of one new-topic research
runs/<post_id>/      post.md, meta.json, images/, prior/<id>/ (author's earlier posts), claims.md, sources.md,
                     research-path.md, units.md (development units + start info), status.md,
                     repro/<n>/ (research.md, post.md, log.md, profile_hash.txt, verification.md)
profiles/<author>/   research-method.md (rule ledger with evidence), writing-structure.md (optional), SKILL.md
```

## Install (the repository is both the plugin and its marketplace)

```bash
claude plugin validate <path-to-this-repo>          # manifest + layout check
claude plugin marketplace add <path-to-this-repo>   # once
claude plugin install rek@rek                              # user scope: every session, every project
```

For development without installing, load it for one session: `claude --plugin-dir <path-to-this-repo>`
(after edits run `/reload-plugins`). Installed copies are refreshed with `claude plugin update rek@rek`.

Plugin components are namespaced: the skills are `/rek:research` (the product use) and `/rek:rek` (learning a
profile), the orchestrator agent is `rek:rek`, and the workers are `rek:rek-source-tracer`, `rek:rek-method-analyst`,
`rek:rek-researcher`, `rek:rek-verifier`, `rek:rek-topic-researcher`, `rek:rek-topic-checker`.

## Research a new topic (the product use)

```
/rek:research 알래스카 LNG 프로젝트. 계기: 미국 정부가 한국에 참여를 요청했다
```

The orchestrator creates `research/<date>-<slug>/`, one worker researches the topic with the learned procedure
(`profiles/reference-a/SKILL.md`) and writes the post, a second worker checks that every fact in the post reaches a
source, and `rek research-summary` prints the pass line: a chain in all three directions, at least 20 sources with 5
primary, no fabricated fact, no source dated after the date. `/rek:rek <post url>` is the learning side: it traces an
author's posts and (re)builds the profile the research side uses.

## Data

`runs/` (the traced posts, their sources and the reproduction attempts) stays out of the public repository: it
holds full copies of a third party's posts. Running the loop recreates it in your working folder. The profile
under `profiles/reference-a/` keeps only short quotations as evidence.

## Run

```bash
uv sync                      # inside the repository, for development
uv run pytest
uv run rek fetch https://blog.naver.com/<blog>/<post_id>   # one post → runs/<post_id>/
uv run rek prior runs/<post_id>                              # the author's earlier posts it reuses
uv run rek stats runs/<post_id>/post.md                      # form statistics
uv run rek verify-summary runs/                              # pass/fail over every run (exit 0 = all pass)
```

Pass line, computed by `rek verify-summary` from each run's latest `repro/<n>/verification.md`: development units
re-found ≥ 90 %, rare sources re-found ≥ 80 %, every upstream base source (author's own posts excluded) re-found,
fabricated facts = 0. The reproduction agent sees only the main topic, one trigger sentence and the date, and may
not read the author's blog or anything published after that date.

From any project folder, in Claude Code: `/rek:rek <url> [<url> ...]`, or spawn the `rek:rek` agent and hand it
the URLs. Results are written to `runs/<post_id>/` and `profiles/<author>/` under the current working folder.
Scripts run as `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek …`, so the Python side needs `uv` only.

Only the deterministic steps are code (fetching, counting, hashing, pass/fail). Everything that
needs judgment runs in Opus workers with their briefs; the briefs are the specification.
