# Brief: rek-method-analyst

Goal: From several traced posts by one author, extract the **research procedure**, and write it so that an agent that has never seen the author's posts can run the same kind of investigation on a new topic. Record the form of the post (style and structure) only as the container for the results (secondary). First read `evidence.md` (labels, status records, definitions of development unit, rare source, and base source).

Input: all of that author's `runs/<id>/` (`post.md`, `meta.json`, `images/`, `claims.md`, `sources.md` (including the `표시:` (mark) lines and the `## 평범한 검색` (ordinary search) section), `research-path.md`, `units.md`, `prior/`). Read all of it before you write. Keep author-specific content only inside `profiles/<author>/`. Write status records to `profiles/<author>/status.md`.

Measure form statistics with `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek stats <post.md ...>`. Do not count by eye. (The command does not count anything after `## 작성 노트` (writing notes).)

## Output 1: profiles/<author>/research-method.md (core)

Put three lines at the top: `author:` (the name),  separated by commas; this becomes the reproduction worker's read-forbidden list), `built_from:` (the list of run ids). Then the rule ledger. Each rule has an id, one sentence an agent can follow, evidence (post id + the unit number `Dxx` of that post or the source number `Sxx` + a quote of 40 words or fewer), exceptions, and `[observed]` (2 or more posts) or `[inferred]` (1 post). There are seven layers. For a layer with no evidence, write "no evidence" and leave it empty.

1. **계기 (trigger) (T)**: What kind of event, appearing in which medium, becomes a post within how many hours? For a post with no event (a series or a seasonal subject), what is the trigger? Evidence: the Trigger and Timeline sections of `research-path.md` and the image upload times in `meta.json`.
2. **뒤쪽 (back) expansion (B)**: How does the author go down from the main topic into history, origin, and background? Which questions does the author ask (for example, "why did this land become this country's?")? Which kinds of sources does the author go to (wiki or Namuwiki, history books, the author's prior posts)? How many steps down? Evidence: the units placed before the trigger in `units.md` and their sources.
3. **앞쪽 (front) expansion (F)**: How does the author go up from the main topic to money, politics, supply chains, and the Korean angle? Which questions and which kinds of sources (filings, government data, statistics, election data)? Evidence: the units after the trigger.
4. **Where rare sources come from (R)**: The kinds of sources with `표시: 희귀` (mark: rare) (trade journals, statistics pages, ship and company databases, original social posts, report PDFs, foreign-language media) and the path that reached them (which article named them, which search terms worked). So that the reproduction worker finds the same kinds, write a **search-term template** (mark the topic slot with brackets).
5. **Base sources (U)**: The kinds of sources with `표시: 바탕` (mark: base) and how the author uses them (one document as the skeleton with only the numbers updated from recent articles, or several documents chained). When the author's prior post is the base, write only "prior-post slot" and state that the reproduction must find a different base source (wiki, report) for that slot (the reproduction worker cannot see the author's posts).
6. **What the author adds (A)**: Calculations (ratios, conversions, truncation), comparisons (contrast with Korean figures), analogies, the one-line conclusion. What kinds of sentences are not in the sources. Evidence: "What the author added" in `research-path.md`.
7. **What the author does not do (N)**: Things a generic agent would have done but this author does not (for example: no source links, no summary opening, no direct quotes from English primary sources). These rules decide reproduction quality, so extract them by contrasting with an imagined generic draft.

## Output 2: profiles/<author>/writing-structure.md (secondary, optional)

The macro structure (the opening, the placement of background → present → trigger → conclusion, the closing one-liner), the kinds of style and the conditions that decide them, and the rules for sentences, numbers, and images. For each rule, give the evidence post id and the `rek stats` figures. Resolve the rules so that none conflict. In particular, decide each of the following as a single choice and write it down: image spacing versus total image count and position, spacing between numbers and units, the length range of the closing one-liner (one value), the relation between the rule for keeping base sentences and the frame sentences, and where new material goes in the base post. Write `optional: true` at the top.

## Output 3: profiles/<author>/SKILL.md (execution procedure)

Frontmatter: `name: <author>-research`, `description:` (one sentence). The body is an order of steps that an agent that has never seen the author's posts can follow after receiving only the **starting info (main topic, one-sentence trigger, date)**:
1. Research checklist: Expand the T, B, F, R, and U rules into questions, search-term templates, kinds of sources, and stop conditions. Include a line saying not to read material dated after the date or the author's domains. For a "prior-post slot", find a different base source.
2. Build the development units: Connect what you found as back chain → main topic → front chain, and attach sources to each unit (research.md).
3. Put it in the frame: Follow writing-structure.md, and state that it is optional.
4. Self-check: End with the N rules and "no fact that is not in research.md".
Keep it to 300 lines or fewer. For examples, use only bracketed templates. Do not copy sentences, numbers, or names from the author's posts.

Language: Write all three files in English. Keep quotes in their original language. When you finish, report the three file paths, the number of rules (per layer), and the three strongest N rules.
