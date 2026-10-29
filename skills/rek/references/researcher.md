# Brief: rek-researcher (reproduction: the test subject of the pass test)

Goal: Without having seen the author's post, use only the starting info and that author's research procedure (`profiles/<author>/SKILL.md`) to investigate the same topic, find the development units, and put them into a post. How closely the development and sources you find overlap with the original is the procedure's score. First read `evidence.md` (labels, Chrome rules, status records, definitions of development unit, rare source, and base source).

## What you receive (only this)

- Four starting-info lines: `main_topic:` (one phrase for the main topic), `trigger:` (one sentence for the trigger event, `none` if there is none), `date:` (the original's publication time = your "today"), `language:` (the language to write `post.md` in). You do not receive the title, sources, URLs, or development units.
- `profiles/<author>/SKILL.md` (execution procedure), `research-method.md` (rule ledger), `writing-structure.md` (optional).
- The folder to write in: `runs/<id>/repro/<n>/`. The orchestrator writes `profile_hash.txt` there in advance. Do not touch it.

## Forbidden reads (if you break one, this attempt is invalid)

- The content of any page published after `date:`. Opening a page to check its date and then closing it is allowed. Record it in `log.md` as `[접촉]` (contact). If you did read the body, do not use any fact you saw there (the verification worker checks that every fact in the post reaches a source dated before the date). For a page with no date, judge by date clues in the body. If you cannot judge, do not use it.
- Any other file under `runs/<id>/` (`post.md`, `claims.md`, `sources.md`, `research-path.md`, `units.md`, `images/`, `prior/`, `meta.json`) and any file in the profile folder other than `SKILL.md`, `research-method.md` and `writing-structure.md`.
- If you opened a forbidden item, record it in `log.md` as `[접촉]` immediately, and do not use a single character of what you saw there.

## Allowed

Web search and fetch. For pages that need a login, follow the Chrome rules in evidence.md (lock, read only). Any public material (wikis, articles, reports, statistics, databases, original social posts). If you can open a primary source directly, open it.

## Procedure

1. Write a start line in `status.md` (`runs/<id>/status.md`). Open `log.md` and record every later search term, opened URL, Chrome use, and forbidden contact in time order. Each line must start with one of these four markers: `[검색] <time> <query>` (search), `[열람] <time> <URL> <publication date>` (read), `[크롬] <time> <URL>` (Chrome), `[접촉] <time> <URL> <reason>` (contact). The aggregation command counts by these markers.
2. Carry out the research checklist in `SKILL.md` **in order**. Go through the 뒤쪽 (back) expansion (history, origin) and the 앞쪽 (front) expansion (money, politics, Korean angle) each to its stop condition. Actually run the rare-source search-term templates. For a "prior-post slot", find a different base source (wiki, report, article) instead of the author's post.
3. Write `research.md`. At the top, a unit table. Each row is `| R01 | <name> | <뒤쪽|본 주제|앞쪽|계기> | <one-line summary> | <source ids> |`. (Those four words are 뒤쪽 = back, 본 주제 = main topic, 앞쪽 = front, 계기 = trigger.) Below the table, give each unit a section (`### R01 <name>`) with its supporting sources (URL, publication date, quote of 40 words or fewer, label). At the end, add `## 못 찾은 것` (not found: the links you tried to find and could not, with the search terms you tried) and a `## 출처 목록` (source list) table. Each row is `| S01 | <URL> | <publication date> | <1차|2차> | <how you reached it> |`. The 1차/2차 (primary/secondary) cell must start with one of those two words.
4. Write `post.md`: a post that carries the development units, following `writing-structure.md` (the default frame if it is optional). Write images as the placeholder `![image: <what it should show>]`. **Do not put labels or evidence marks (`[observed…]`, `Rxx`, `Sxx`) in the body of the post.** Write it as the post the reader will read. The mapping between sentences and sources lives only in `research.md`. **Every number, name, date, and event in `post.md` must reach some source in `research.md`.** Do not write a fact that has no source. For a calculation, write the formula in `research.md`.
5. Run `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek repro-stats <repro folder>` and paste its output as is into `## Summary` at the end of `log.md` (do not count by hand). Write a done line in `status.md`.

## Output

`runs/<id>/repro/<n>/research.md`, `post.md`, `log.md`. Write nothing besides these three files. Write `research.md` and `log.md` in English, with quotes in their original language. Write `post.md` in the language given by the `language:` line. When you finish, report the three file paths and the `rek repro-stats` output.
