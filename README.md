# REK — Reverse Engineering Knowledge

Given a published text, REK traces where each claim came from, reconstructs how the author
researched and wrote it, distills that into a writing-method profile, and proves the profile by
regenerating a post and diffing it against the original.

The loop is adapted from [morluto/rea](https://github.com/morluto/rea) (reverse engineering of
binaries): route the target → summary-first inventory → evidence ledger whose every line is
`observed`, `inferred` or `unknown` → verified reconstruction. The orchestration shape (one
orchestrator, independent workers, an independent gate, intent before execution) follows the
dryforge `ready` skill. See `skills/rek/SKILL.md` for the correspondence table.

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
.claude-plugin/      plugin manifest (the repository root is the plugin)
skills/rek/          the agent loop; references/ holds one brief per worker
agents/              worker agents (opus, effort max); scripts are reached via ${CLAUDE_PLUGIN_ROOT}
runs/<post_id>/      post.md, meta.json, images/, prior/<id>/ (author's earlier posts the post reuses),
                     claims.md, sources.md, research-path.md, reconstruction.md, verification.md
profiles/<author>/   writing-method.md (rule ledger with evidence), SKILL.md (writer skill)
```

## Install (the repository is both the plugin and its marketplace)

```bash
claude plugin validate /Users/inertia/Desktop/REK          # manifest + layout check
claude plugin marketplace add /Users/inertia/Desktop/REK   # once
claude plugin install rek@rek                              # user scope: every session, every project
```

For development without installing, load it for one session: `claude --plugin-dir /Users/inertia/Desktop/REK`
(after edits run `/reload-plugins`). Installed copies are refreshed with `claude plugin update rek@rek`.

Plugin components are namespaced: the skill is `/rek:rek`, the orchestrator agent is `rek:rek`, and the
workers are `rek:rek-source-tracer`, `rek:rek-method-analyst`, `rek:rek-researcher`, `rek:rek-verifier`.

## Run

```bash
uv sync                      # inside the repository, for development
uv run pytest
uv run rek fetch https://blog.naver.com/<blog>/<post_id>
```

From any project folder, in Claude Code: `/rek:rek <url> [<url> ...]`, or spawn the `rek:rek` agent and hand it
the URLs. Results are written to `runs/<post_id>/` and `profiles/<author>/` under the current working folder.
Scripts run as `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek …`, so the Python side needs `uv` only.

Only `rek fetch` is code. Everything after it is judgment, so it runs in Opus workers with their
briefs; the briefs are the specification.
