# rek/ — the Python package

## Scope
Fetching posts into run folders, finding the author's earlier posts, form statistics, reproduction counts, the pass/fail
summary, profile hashes and the source-site ledger. Nothing that requires judgment: no claim extraction, no source
matching, no scoring decisions beyond the fixed thresholds.

## Not this package's job
Reading the web for research (workers do that), writing any file under `runs/<id>/` except `post.md`, `meta.json`,
`images/`, `raw.html`, `prior/`, and `meta.json.prior_search`; writing anything under `profiles/`.

## Invariants
- `core/` imports nothing from `adapters/` and knows no URL or site name, and reads or writes files only in `run_dir.py`, `profile_hash.py` and `verify_summary.summarize`; `ports/` holds the protocols; `cli.py` is
  the only place that wires adapters to core.
- Standard library only.
- Thresholds in `core/verify_summary.py`: author criteria units ≥ 0.90, rare ≥ 0.80 (or rare_total 0), upstream_found ==
  upstream_total, fabricated == 0; own criteria valid, fabricated == 0, each of 뒤쪽/본 주제/앞쪽 ≥ 1 unit, sources ≥ 20 with
  ≥ 5 primary. `≥` includes equality. A run without `repro/<n>/verification.md` or with missing keys is "미실행/불완전".
- `core/stats.py` stops counting at a line equal to `## 작성 노트`; the closing one-liner is one unit.
- Markers the counters parse are fixed strings: unit rows `R<nn> |`, the `## 출처 목록` section with `S<nn>` or URL rows,
  log lines starting `[검색] [열람] [크롬] [접촉]`, the `표시:` line with `희귀` / `바탕` / `바탕(저자 글)`, the `무효:` line in
  verification.md. Changing one means changing the briefs, the tests and the existing data together.
- `rek prior` confirms a date-route candidate only when the candidate's page contains one of the reused image files;
  title-route matches are whole title tokens, at most 10 most recent within 730 days; images uploaded less than 24 h before
  publication count as the post's own.

## Patterns
- One `@dataclass(frozen=True)` per domain object in `core/models.py`; functions in `core/*` take and return those or
  plain dicts.
- A site adapter implements `PostSource` (`supports`, `fetch`, `blog_of`, `post_url`) and `PostList` (`list_posts`), and
  is registered in `cli.py`'s `SOURCES`.
- Regex over the mobile page is deliberate: the body is a flat sequence of `se-component` divs and the package has no
  parser dependency.

## Tests
`uv run pytest -q`. Fixtures are real saved pages (`tests/fixtures/naver_224456106651.html`, a post-list JSON page) and the
canonical `verification_example.md` the verifier brief copies. Add a failing test before changing behaviour; cover the
boundary cases named above (equality at thresholds, zero denominators, the notes marker, unnumbered source lists).
