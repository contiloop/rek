# External contracts

## Command line

Every command has the form `rek <subcommand> …`. On failure it exits with code 1 (2 for an input error) and writes a one-line reason to standard error.

- `fetch <url>`: a Naver Blog post address (desktop, mobile, and `PostView.naver?blogId=…&logNo=…` all work). Output goes to `runs/<post_id>/`. For a post that does not exist, it exits with code 1 and "no post at …". For a site with no adapter, it exits with 2.
- `prior <run_dir>`: adds a `prior_search` key to `meta.json` (existing keys are kept). Each candidate has `post_id, title, date, routes,
  status(fetched|present|rejected|failed)`.
- `stats <post.md>…`: JSON. Keys `sentences, numbered_items, max_item_number, numbering_gaps, mean_sentence_chars,
  noun_ending_share, da_ending_share, sentences_with_number_share, images, has_one_liner, one_liner_chars, first_line`.
- `repro-stats <repro_dir>`: JSON. Keys `units, units_by_direction, sources, primary, secondary, searches, pages, chrome,
  contacts`. A unit is an `R<nn> | …` line (the leading `|` is optional). A source is an `S<nn>` line or a list line that starts with a URL in the `## 출처 목록` (source list) section. Records are counted by the line prefixes `[검색] [열람] [크롬] [접촉]` (search, page read, Chrome use, contact).
- `profile-hash <dir>`: the first 12 characters of the sha256 of `SKILL.md`, `research-method.md` and `instances.md` joined together in that order. Exits with 2 and `missing profile file: <path>` if one is missing.
- `source-sites <runs_dir>`: a markdown table. Columns `도메인 | 글 수 | 출처 수 | 희귀 | 바탕 | 발행처 | 예시 URL`.
- `verify-summary <runs_dir> [--criteria author|own]`: a table and `overall: pass|fail (n/m pass)`. Exits with 0 if all pass, otherwise 1.
- `compare-summary <runs_dir>`: one line per run from the `repro/<n>/comparison.md` with the largest n: `<run_id> | <verdict> | depth back o→r, forward o→r | units x/y | facts x/y (conflict c) | fabricated f | extra e | <valid|invalid> | <hash>`. The values are copied from the comparator; only the verdict is computed. `<verdict>` is `pass` when the attempt is valid, `fabricated` is 0, `depth_back_repro ≥ depth_back_original` and `depth_forward_repro ≥ depth_forward_original`; otherwise `fail (<names>)`, the failed conditions comma-separated in the order `valid, fabricated, depth_back, depth_forward` (e.g. `fail (fabricated, depth_back)`). `valid|invalid` follows the `무효:` line; when the `invalid` key disagrees, ` 불일치` follows the `valid|invalid` word. A file with the 11 keys of the earlier contract (`depth_original`, `depth_repro` in place of the four depth keys) gives `<run_id> | old format, no verdict | units x/y | facts x/y (conflict c) | fabricated f | depth o→r | extra e | <valid|invalid> | <hash>`; any other missing key gives `<run_id> | 미실행/불완전`; a run without `comparison.md` is skipped. Exits with 0 when every run with a 13-key `comparison.md` passes, otherwise 1; old-format and incomplete runs do not affect the exit code.
- `research-init <topic> --profile <dir> [--trigger S] [--date 'YYYY-MM-DD HH:MM KST'] [--language L] [--out DIR]`: creates `research/<YYYYMMDD>-<slug>/` with `topic.md` (lines `main_topic:`, `trigger:`, `date:`, `language:`, `profile:` in that order; `trigger: none` when absent; `date` defaults to now in KST; `profile` is the absolute folder) and `profile_hash.txt`. Prints the folder. Exits with 2 if the profile lacks `SKILL.md` or the folder already has a `topic.md`, and with 2 and `missing profile file: <path>` if the profile lacks `research-method.md` or `instances.md` (the three files of `profile-hash`).
- `research-summary <research_dir>`: one line `<dir>: pass|fail (<reasons>; chain b/m/f, sources n (p primary), fabricated x, late sources y) | checker: <opinion>`; `미실행/불완전` when `research.md` or `check.md` is missing. Exits with 0 on pass, otherwise 1.

## File contracts

- `verification.md` must start with a ```yaml block holding the 11 keys in that order. If a `무효: …` line (the invalid line) follows, the attempt is invalid.
- `comparison.md` must start with a ```yaml block holding the 13 keys `units_total, units_covered, facts_total, facts_matched, facts_conflicting, fabricated, depth_back_original, depth_back_repro, depth_forward_original, depth_forward_repro, extra_units, invalid, profile_hash` in that order, with no comments (canonical copy `tests/fixtures/comparison_example.md`). If a `무효: …` line follows the block, the attempt is invalid.
- The three top lines of `units.md`, `main_topic:`, `trigger:`, and `date:`, pass unchanged to the reproduction worker. They must not contain a title, an outlet, or a URL.
- The `excluded_domains:` line in the `units.md` header lists the author's domains and accounts; only the verifier and the comparator read it, and the orchestrator never passes it to the reproduction worker.
- The `units.md` of a test-only run (reproduce and compare, no trace) has only the four header lines `main_topic:`, `excluded_domains:`, `trigger:`, `date:` and no unit table.
- `status.md` line format: `<ISO time> | <worker> | <stage> | <one line>`.
- `check.md` (new-topic research) must start with a ```yaml block holding `fabricated`, `late_sources`, `checker_verdict` in that order.
- `research.md` and `log.md` of a research folder follow the same markers as a `repro/<n>/` folder (`R<nn> |`, `## 출처 목록`, `S<nn>`, `[검색] [열람] [크롬] [접촉]`).
- In `research.md` (a research folder and a `repro/<n>/` folder alike), each image placeholder `![image: <description>]` of `post.md` has a line `image: <description> ← S<nn>[, S<nn>…]` under its unit, with the description text identical to the placeholder's. A placeholder without such a line, or whose ids do not state the description, is a fabrication.

## Plugin

Skills `/rek:rek` (learn a profile from an author's posts) and `/rek:research` (research a new topic with a profile). Agents `rek:rek` (orchestrator), `rek:rek-source-tracer`, `rek:rek-method-analyst`, `rek:rek-researcher`, `rek:rek-verifier`, `rek:rek-comparator`, `rek:rek-topic-researcher`, `rek:rek-topic-checker`. A worker receives the brief path and the run (or profile) folder and writes only to that folder.
