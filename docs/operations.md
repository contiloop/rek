# Running

## Setup (once)

```bash
# Requires: uv (it downloads Python 3.12+), git, Claude Code
cd <path-to-this-repo>
uv sync                                   # creates .venv with pytest
uv run pytest -q                          # all tests must pass
claude plugin validate .                  # plugin layout check
claude plugin marketplace add <path-to-this-repo>   # the repository is its own marketplace
claude plugin install rek@rek             # /rek:rek and the rek:rek-* agents appear in every session
```

To use the plugin in one session without installing it, run `claude --plugin-dir <path-to-this-repo>`. After editing files, run `/reload-plugins`. For an installed copy, run `claude plugin update rek@rek`.

## Commands

| Command | What it does |
|---|---|
| `uv run rek fetch <url> [--out DIR] [--no-images]` | Fetch one post into `runs/<post_id>/`. Naver Blog only. |
| `uv run rek prior runs/<id> [--no-images]` | Fetch the author's prior posts into `prior/<id>/`. Results and rejection reasons go in `meta.json.prior_search`. |
| `uv run rek stats <post.md> ...` | Sentence count, numbered items, ending ratios, image count, one-line comment length. |
| `uv run rek repro-stats runs/<id>/repro/<n>` | Unit count (by direction), source count (primary/secondary), record mark count of a reproduction. |
| `uv run rek profile-hash profiles/<author>` | Profile version identifier (first 12 characters of the sha256). |
| `uv run rek source-sites runs/` | A table of the sources of all traces, grouped by registered domain. |
| `uv run rek verify-summary runs/ [--criteria author\|own]` | Pass table. Exit code 0 = all pass. |
| `uv run rek research-init "<topic>" --profile profiles/<author> [--trigger "..."] [--date "..."]` | Create `research/<date>-<slug>/` with the five start lines and the profile hash. |
| `uv run rek research-summary research/<name>` | Pass line of one new-topic research. Exit code 0 = pass. |

Inside the plugin, workers use the form `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek …`.

## Running the loop

From any folder, in Claude Code, run `/rek:rek <url> [<url> ...]`, or start the `rek:rek` agent and pass it the URLs. The procedure is the six steps in `skills/rek/SKILL.md`. One worker run at Opus 5.5 max effort costs about 300,000 to 800,000 tokens and takes 30 to 70 minutes (per post: 1 source tracing, 1 reproduction, 1 verification; per author: 1 method extraction). If you run it inside this repository, `runs/` and `profiles/` carry over as they are.

## Researching a new topic (the product use)

In Claude Code, run `/rek:research <topic>` with the trigger sentence if there is one (for example `/rek:research 알래스카 LNG 프로젝트. 계기: 미국 정부가 한국에 참여를 요청했다`). The procedure is the four steps in `skills/research/SKILL.md`: `rek research-init`, the topic researcher (research and post), the topic checker (`check.md`), `rek research-summary`. Two worker runs per topic, about 40 to 80 minutes. The profile comes from `profiles/<author>/` in the working folder, or from the plugin's own `profiles/` when the working folder has none.

## Data folders

```
runs/<post_id>/   post.md  meta.json  images/(excluded from git)  raw.html(excluded from git)  prior/<id>/  status.md
                claims.md  sources.md  research-path.md  units.md
                repro/<n>/  profile_hash.txt  research.md  post.md  log.md  verification.md
research/<date>-<slug>/  topic.md  profile_hash.txt  research.md  post.md  log.md  check.md  status.md
profiles/<author>/  research-method.md  writing-structure.md  SKILL.md  status.md  source-sites.raw.md
                  holdout/<post_id>/  (profile variant with that post's traces removed)
```
