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
- `profile-hash <dir>`: the first 12 characters of the sha256 of `SKILL.md` and `research-method.md` joined together. Exits with 2 if a file is missing.
- `source-sites <runs_dir>`: a markdown table. Columns `도메인 | 글 수 | 출처 수 | 희귀 | 바탕 | 발행처 | 예시 URL`.
- `verify-summary <runs_dir> [--criteria author|own]`: a table and `overall: pass|fail (n/m pass)`. Exits with 0 if all pass, otherwise 1.

## File contracts

- `verification.md` must start with a ```yaml block holding the 11 keys in that order. If a `무효: …` line (the invalid line) follows, the attempt is invalid.
- The three top lines of `units.md`, `main_topic:`, `trigger:`, and `date:`, pass unchanged to the reproduction worker. They must not contain a title, an outlet, or a URL.
- The `excluded_domains:` line in the `units.md` header lists the author's domains and accounts; only the verifier reads it, and the orchestrator never passes it to the reproduction worker.
- `status.md` line format: `<ISO time> | <worker> | <stage> | <one line>`.

## Plugin

Skill `/rek:rek`. Agents `rek:rek` (orchestrator), `rek:rek-source-tracer`, `rek:rek-method-analyst`, `rek:rek-researcher`, `rek:rek-verifier`. A worker receives the brief path and the run (or profile) folder and writes only to that folder.
