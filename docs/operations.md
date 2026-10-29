# Running

## Setup (once)

```bash
# 필요: uv (Python 3.12 이상을 uv가 받는다), git, Claude Code
cd /Users/inertia/Desktop/REK
uv sync                                   # .venv와 pytest
uv run pytest -q                          # 44개 통과해야 한다
claude plugin validate .                  # 플러그인 구조 검사
claude plugin marketplace add /Users/inertia/Desktop/REK   # 저장소가 마켓플레이스다
claude plugin install rek@rek             # 모든 세션에서 /rek:rek 와 rek:rek-* 에이전트가 보인다
```

To use the plugin in one session without installing it, run `claude --plugin-dir /Users/inertia/Desktop/REK`. After editing files, run `/reload-plugins`. For an installed copy, run `claude plugin update rek@rek`.

## Commands

| Command | What it does |
|---|---|
| `uv run rek fetch <url> [--out DIR] [--no-images]` | Fetch one post into `runs/<글 id>/`. Naver Blog only. |
| `uv run rek prior runs/<id> [--no-images]` | Fetch the author's prior posts into `prior/<id>/`. Results and rejection reasons go in `meta.json.prior_search`. |
| `uv run rek stats <post.md> ...` | Sentence count, numbered items, ending ratios, image count, one-line comment length. |
| `uv run rek repro-stats runs/<id>/repro/<n>` | Unit count (by direction), source count (primary/secondary), record mark count of a reproduction. |
| `uv run rek profile-hash profiles/<저자>` | Profile version identifier (first 12 characters of the sha256). |
| `uv run rek source-sites runs/` | A table of the sources of all traces, grouped by registered domain. |
| `uv run rek verify-summary runs/ [--criteria author\|own]` | Pass table. Exit code 0 = all pass. |

Inside the plugin, workers use the form `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek …`.

## Running the loop

From any folder, in Claude Code, run `/rek:rek <url> [<url> ...]`, or start the `rek:rek` agent and pass it the URLs. The procedure is the six steps in `skills/rek/SKILL.md`. One worker run at Opus 5.5 max effort costs about 300,000 to 800,000 tokens and takes 30 to 70 minutes (per post: 1 source tracing, 1 reproduction, 1 verification; per author: 1 method extraction). If you run it inside this repository, `runs/` and `profiles/` carry over as they are.

## Data folders

```
runs/<글 id>/   post.md  meta.json  images/(git 제외)  raw.html(git 제외)  prior/<id>/  status.md
                claims.md  sources.md  research-path.md  units.md
                repro/<n>/  profile_hash.txt  research.md  post.md  log.md  verification.md
profiles/<저자>/  research-method.md  writing-structure.md  SKILL.md  status.md  source-sites.raw.md
                  holdout/<글 id>/  (그 글의 흔적을 걷어낸 프로필 변형)
```
