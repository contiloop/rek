# Structure

REK has two layers. The lower layer is a Python command (`rek`). It does only the work that has a single correct answer: fetching, format statistics, and aggregation.
The upper layer is Claude Code agents (1 orchestrator, 4 workers). They do the work that needs judgment: source tracing, method extraction, reproduction, and scoring.
The two layers connect only through files in the working folder (`runs/`, `profiles/`). Workers do not talk to each other directly.

## Flow (one post)

1. The orchestrator runs `rek fetch <url>` → `runs/<post_id>/post.md`, `meta.json` (including image upload times), `images/`, `raw.html`.
2. `rek prior runs/<post_id>` → copies two kinds of posts into `prior/<id>/`: posts within ±2 days of the image upload date that actually contain the same image file, and recent posts whose titles share a word with the target.
3. The source-tracing worker (`rek-source-tracer`) reads the run folder and writes `claims.md`, `sources.md` (each source carries a `희귀` (rare) or `바탕` (foundation) mark), `research-path.md`, and `units.md` (the development units and four lines of starting information). One worker per post, in parallel.
4. The method-extraction worker (`rek-method-analyst`) reads all runs of that author and writes `profiles/<author>/research-method.md`, `writing-structure.md`, and `SKILL.md`. Once per author.
5. The orchestrator creates `repro/<n>/`, writes `profile_hash.txt` with `rek profile-hash`, then starts the reproduction worker (`rek-researcher`), passing only the four lines at the top of `units.md` → `research.md`, `post.md`, `log.md`. One worker per post, in parallel.
6. The verification worker (`rek-verifier`) compares `units.md` and `sources.md` with `repro/<n>/` and writes `verification.md` (11 yaml keys at the very top).
7. `rek verify-summary runs/` reads the `verification.md` with the highest number and prints the table and the pass/fail result. Only code makes the verdict.

## Components and dependency direction

| Component | Role | Depends on |
|---|---|---|
| `rek/core/` | Models (Post, Block, Image), format statistics, prior-post selection, aggregation, hashing, site ledger. Pure functions. | None |
| `rek/ports/` | Contracts that the outside world must fill: fetch one post, list posts, store images | core |
| `rek/adapters/` | Naver Blog implementation (mobile page parsing, post list API), urllib HTTP | ports, core |
| `rek/cli.py` | Wires the 7 commands to the adapters | All of the above |
| `skills/rek/SKILL.md` | Orchestrator procedure. Briefs are in `references/` | Worker agents, `rek` commands |
| `agents/*.md` | Orchestrator `rek` and 4 workers (all model opus, effort max) | Briefs |
| `runs/`, `profiles/` | Data. They are created in the working folder where you run the tool, not in the plugin | — |

Dependencies point only downward. `core` knows nothing about the network or site names, and touches files only in `run_dir.py`, `profile_hash.py` and `verify_summary.summarize`. To support a new site, add one more `PostSource` and `PostList` implementation under `adapters/`.

## What crosses the boundary

- Plugin → working folder: only `runs/` and `profiles/` files. The plugin folder never receives data.
- Worker → web: search, fetch, and (if available) the user's logged-in Chrome. Read-only.
- The reproduction worker receives only the four lines of starting information, the profile folder, and the folder to write to. It does not receive the original post, the tracing files, or the author's blog.
