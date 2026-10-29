# REK — Reverse Engineering Knowledge

Given a published text, REK traces where each claim came from, reconstructs how the author
researched and wrote it, distills that into a writing-method profile, and proves the profile by
regenerating a post and diffing it against the original.

The loop is adapted from [morluto/rea](https://github.com/morluto/rea) (reverse engineering of
binaries): route the target → summary-first inventory → evidence ledger whose every line is
`observed`, `inferred` or `unknown` → verified reconstruction. The orchestration shape (one
orchestrator, independent workers, an independent gate, intent before execution) follows the
dryforge `ready` skill. See `.claude/skills/rek/SKILL.md` for the correspondence table.

## What was taken from each reference

| reference | taken | depth | not taken |
|---|---|---|---|
| morluto/rea | investigation loop: route → inventory → evidence with observed/inferred/unknown → residual unknowns → reconstruction verified against a finite claim list; parallel workers with distinct scopes returning sources, conclusions, gaps | principle, rebuilt for text | its MCP tools, binary formats, Evidence IDs and hashing |
| dryforge `ready` | one orchestrator, workers only for independent checks, an independent gate that must find nothing, findings routed to the stage that owns them, user approves before the costly run | principle | the 3-doc format, the elicitation dialogue stages |
| OneSpiral/ghost-writer and similar style cloners | a style profile is many named dimensions, each with evidence | principle | their dimension list (ours is derived from the posts) |
| ProjectJang guidelines | hexagonal layout, tests before each slice, real data for verification, fix upstream not output, delete leftovers | copy | — |

## Layout

```
rek/                 Python: fetch + normalize only (hexagonal: core/ models, ports/, adapters/)
  adapters/naver_blog.py   Naver mobile page → Post; decodes image upload dates from image URLs
  cli.py                   `rek fetch <url>` → runs/<post_id>/
tests/               pytest, fixture = one real Naver page
.claude/skills/rek/  the agent loop; references/ holds one brief per worker
.claude/agents/      rek-source-tracer, rek-style-analyst, rek-writer, rek-verifier (opus, effort max)
runs/<post_id>/      post.md, meta.json, images/, prior/<id>/ (author's earlier posts the post reuses),
                     claims.md, sources.md, research-path.md, reconstruction.md, verification.md
profiles/<author>/   writing-method.md (rule ledger with evidence), SKILL.md (writer skill)
```

## Run

```bash
uv sync
uv run pytest
uv run rek fetch https://blog.naver.com/<blog>/<post_id>
```

Then, in Claude Code inside this folder: `/rek <url> [<url> ...]`.

Only `rek fetch` is code. Everything after it is judgment, so it runs in Opus workers with their
briefs; the briefs are the specification.
