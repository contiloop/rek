# Domain rules

## Terms

- **Post (run)**: one traced post. `runs/<post_id>/`. Fetching the same URL again overwrites it.
- **Prior post (prior)**: an earlier post by the same author from which the target post reused sentences or images. Source tracing uses it. Reproduction cannot see it.
- **Claim**: an atomic unit of the body text (number, date, name, quote, event, cause and effect, opinion, reuse of the author's own post).
- **Source**: the document a claim came from. It has a publication time, a URL, a primary or secondary type, a label (observed/inferred/unknown), and a mark (`희귀` (rare) or `바탕` (foundation)).
- **Development unit (unit)**: one link in the chain the post passes through. The boundary is the point where the post moves from one topic to the next. A post usually has 8 to 20 units.
- **Rare source** (`희귀`): a source whose domain is not in the set of registered domains (at most 20) taken from the top 10 results of two runs of the web search tool on the main topic (`본 주제`), one in Korean and one in English. Only observed sources count.
- **Foundation source** (`바탕`): a source that supports 3 or more consecutive development units, or supplies at least a quarter of all claims. A prior post by the author is marked `바탕(저자 글)` (foundation, author's post) and is left out of the required set.
- **Starting information**: the `main_topic:` line at the top of `units.md` (one phrase, not the title), the `trigger:` line (one sentence about what prompted the post, with no outlet or URL, or `none` if there is none), and the `date:` line (the original's publication time). This is everything the reproduction worker receives.
- **Reproduction (repro)**: the research and post produced by a worker that received only the starting information and the profile. They accumulate by number in `repro/<n>/`.

## Label rules

- Every concluding sentence carries one of three labels: `[observed]` (the source was opened and checked directly), `[inferred]` (likely, but the source could not be opened or only partly matches), or `[unknown]` (searched and not found, or not searched). Do not write observed based only on a search result summary.
- A document published after the post cannot be its source. The tracing worker points out such a document and looks for an earlier one.
- When a secondary article names a primary source, record both. Treat the one whose wording matches the post as the source the author read.

## Development unit rules

- Fix `units.md` before starting reproduction, and do not change it after seeing the reproduction result. It is the denominator of the score.
- Units that came from a prior post by the author stay in the denominator. The reproduction cannot see the author's posts, so it must reach that link through other sources.
- A unit whose source is `-` cannot be "found". If such a unit exists, strengthen the source tracing and attach an external source. (In all three posts, units that had relied only on prior posts by the author did get original sources such as 나무위키 (Namuwiki), op-eds, and company histories.)

## Reproduction rules

- The reproduction worker is told nothing about the author. It may not read any other file in that post's run folder or any profile file beyond the three it is given. The verifier marks the attempt invalid if the log shows a page on the author's domains (the `excluded_domains:` line in the `units.md` header, plus mirrors, caches and reposts) or a page that quotes the original was read down to the body.
- The **content** of pages dated after `date:` may not be used. Opening such a page to check its date and then closing it is allowed. Record it as `[접촉]` (contact).
- Every number, name, date, and event in the reproduced post must reach a source in `research.md`. The same holds for the descriptions of image placeholders.
- Do not put labels or evidence marks in the post body. The mapping from sentences to sources lives only in `research.md`.
- Use Chrome normally only after a fetch has failed, read-only, and by one worker at a time (folder lock `runs/.chrome.lock`: wait up to 10 minutes, polling every 30 seconds; delete a lock older than 30 minutes; read one page and release the lock at once).

## Scoring rules

- Unit "found": the reproduction has a unit with the same substance, and its supporting source reaches the same primary source (the same document from the same publisher, or a secondary article that names it). Order does not matter. One reproduction unit matches only one original unit.
- Rare or foundation "found": the reproduction's source list contains the same primary source (or a named secondary one).
- Fabrication: a fact in the reproduced post that appears in none of the sources in `research.md`. A calculation result with its formula written out is not fabrication.
- Invalid (`무효:`, the invalid line): the worker read an author domain or a page quoting the original, down to the body text; the source list contains a page published after `date:`; or the worker read the body of a page dated after `date:` and a fact found only on that page entered the result. Fill in the yaml keys even when the attempt is invalid.
- Two sets of pass thresholds. **Reference-author criteria** (`--criteria author`): units at least 90%, rare at least 80%, all foundation sources except the author's posts, fabrication 0. **Our criteria** (`--criteria own`): a valid attempt, fabrication 0, at least one unit each in the backward (`뒤쪽`), main-topic, and forward (`앞쪽`) directions, and at least 20 sources (at least 5 primary). The current pass condition is our criteria. The reference-author criteria are reported only.
- For each failure, record the responsible stage. No original source, or only a guess → source tracing. The method has no search framework → method extraction. The framework exists but was not run, was found but not used, or the result is fabrication → reproduction. The fix goes in that stage, not in the output.

## New-topic research rules

- A research folder receives five lines (`main_topic`, `trigger`, `date`, `language`, `profile`) and the profile folder. There is no original and no exclusion list; the content of pages after `date:` is still off limits.
- Pass (`rek research-summary`): at least one unit in each of `뒤쪽`, `본 주제`, `앞쪽`; at least 20 sources with at least 5 primary; `fabricated` 0; `late_sources` 0. The checker's opinion is shown next to it and never decides.
- Fabrication and late-source failures go back to the researcher on the same folder; chain and source failures are profile gaps and go back to `/rek:rek` (method extraction).

## When a new post arrives

Reproduce and score a new post first with the current profile (hold-out). Then trace it and feed it into profile re-extraction. The profile is rebuilt every time from all runs of that author. The profile used for scoring is recorded as `profile_hash` (the first 12 characters of the sha256 of SKILL.md + research-method.md). When testing a post with a profile built from that same post, use the variant `profiles/<author>/holdout/<post_id>/`, which has the traces of that post removed.
