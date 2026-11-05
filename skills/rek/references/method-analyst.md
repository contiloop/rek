# Brief: rek-method-analyst

Goal: From several traced posts by one author, extract the **research procedure**, and write it so that an agent that has never seen the author's posts can run the same kind of investigation on a new topic in any field. The procedure is made of the **moves** the author makes (for example "find who holds the next decision and when that changes hands"), not the **instances** of those moves in the traced posts (for example "looked up the seat count of one legislature"). A rule written from an instance only fits the posts it came from; a reproduction worker given such a rule searches for the old posts' nouns instead of the new topic's. Record the form of the post (style and structure) only as the container for the results (secondary). First read `evidence.md` (labels, status records, definitions of development unit, rare source, and base source).

Input: all of that author's `runs/<id>/` (`post.md`, `meta.json`, `images/`, `claims.md`, `sources.md` (including the `표시:` (mark) lines and the `## 평범한 검색` (ordinary search) section), `research-path.md`, `units.md`, `prior/`). Read all of it before you write. Keep author-specific content only inside `profiles/<author>/`. Write status records to `profiles/<author>/status.md`.

Output: four files in `profiles/<author>/`: `research-method.md`, `instances.md`, `writing-structure.md` (optional), `SKILL.md`. Rebuild all four from scratch; overwrite the old versions. Write nothing else besides `status.md`.

Measure form statistics with `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek stats <post.md ...>`. Do not count by eye. (The command does not count anything after `## 작성 노트` (writing notes).) Build the site table with `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek source-sites runs/`. Count rules with `grep`, as the checklist at the end says. Do not count anything by hand.

## Step 1: Write the move table (instance, move, reason)

Before you write any rule, go through every source in every `sources.md` and every action the author took that `research-path.md` describes (a search, a calculation, a comparison, a choice of what to leave out). For each one, write a block of three lines in the `## Moves` section of `instances.md`:

```
- instance: <post id> <Sxx or Dxx>: <what was read or done, with its real nouns>
  move: <the move the author made, in one sentence without the nouns of that instance>
  reason: <why that move was needed for the post>
```

Several sources that the author reached by the same action in the same post may share one block; list all their ids on the `instance:` line. Every source id of every post appears in at least one block.

How to write the `move:` line: remove every name and every field word of the instance, and say what the author did with it. Example: instance "opened the registry entry of the tanker to see who manages it" → move "open the database record of the main asset to find who owns and who operates it".

## Step 2: Turn moves into rules

Rules are made only from `move:` and `reason:` lines. Instances go down into the rule's evidence lines.

1. Group the moves that do the same thing. Each group is a rule candidate.
2. For every rule candidate, ask once more: "Why did the author do this?" If the answer fits more topics than the candidate does, the answer becomes the rule and the candidate becomes evidence. Example: "looked up the seat count of the legislature" → why? → "to know whether the decision can still change" → rule: "find who holds the next decision and when that changes hands".
3. When two rule candidates from different posts are different instances of the same move, merge them into one rule that names their common ancestor. Example: "found when the fishery collapsed" and "found when the company was founded" → "find the event where the present form of the main subject began".
4. Do not write a rule that depends on the author's own history (the author wrote about this topic before, the post belongs to a series). The agent that uses the profile cannot see the author's posts. What remains of such a pattern is the move behind it, for example "pick one skeleton document".

## Step 3: No nouns in rule sentences

A **rule sentence** is the heading line of a rule in `research-method.md`, any instruction sentence, and every line of `SKILL.md`. A rule sentence contains:

- no proper noun: no person, company, institution, outlet, website, country, region, vessel, or product name;
- no domain noun: no industry, commodity, or resource name (for example fishery, LNG, vessel, rare earth) and no domain unit (for example Mtpa, barrel, tonne);
- no kind of endpoint: a stop condition does not name the kind of event, document or actor where a chain ends (not "a war", "a law", "a person"). State how far to go as a move: what to keep asking, until what kind of answer.

These nouns are allowed only on evidence lines (`- evidence:`, `- why:`, `- try:`) and in `instances.md`.

What is allowed in a rule sentence: generic kinds of sources (wiki, trade paper, wire story, government release, statistics table, company history page, report PDF, database record, original social post), generic actors (government, regulator, company, leader, institution), language names (English, the post's language, the local language of the place), the words "domestic" and "home country" for the author's own country, and bracketed slots.

The same rule applies to the words outside the slots of a query template. Forbidden: `collapse of the [country] [resource] fishery` (the word "fishery" sits outside a slot). Allowed: "find when the [industry or resource] began or collapsed in English research reports and conference papers".

Line format (fixed so the check is possible):

- In `research-method.md`, a rule is exactly one heading line: `### <id>: <the rule in one sentence> <label>`. The id is the layer letter plus a number (`T1`, `B3`, …). The lines below it start with `- evidence:` (post id + unit `Dxx` or source `Sxx` + a quotation), `- why:` (the reason), or `- try:` (the instantiation on a test topic). These three kinds of lines may contain nouns. A post that goes against the rule is also written on an `- evidence:` line that begins with `against:`.
- `SKILL.md` has no evidence lines, so every line of it is a rule line.
- `instances.md` is entirely instances.

The noun check is your self-check. No code checks it. List your heading lines with `grep -n "^### " profiles/<author>/research-method.md` and read every one, then read every line of `SKILL.md`. Rewrite each line that fails.

## Step 4: Try every rule on two topics from other fields

For every rule, write one `- try:` line for each of the two test topics below. Each line says what the rule makes you search for or do on that topic. The test topics are unrelated to the traced posts:

- Test topic 1: a domestic software company's overseas acquisition.
- Test topic 2: a revision of domestic food-safety regulations.

(These two are the defaults. If one of them is close to a traced post's topic, replace it with another topic from a different field and write the replacement at the top of `research-method.md`.)

If you cannot instantiate a rule on a test topic, the rule is still at the level of an instance: rewrite it one level up (Step 2, item 2) and try again. A rule that cannot be instantiated on both test topics is not kept; move what it says into `instances.md`. Count how many rules you rewrote one level up after a failed instantiation; the completion report needs that number.

## Labels and quotations

- The label at the end of a rule heading line follows evidence.md. Use `[observed]` only when every traced post supports the rule. When only some posts support it, the rule is `[inferred: <ids of the supporting posts>]`. A rule supported by no post is not written.
- An evidence line carries the label of how its fact was confirmed (evidence.md).
- Quotations are 40 words or fewer, in the original language, and only on evidence lines and in `instances.md`.

## Output 1: profiles/<author>/research-method.md (core)

Put two lines at the top: `author:` (the `<author>` name of the profile folder, as given in the prompt) and `built_from:` (the run ids, separated by commas). If you replaced a test topic, write that next. Then the rule ledger, in seven layers. For a layer with no evidence, write "no evidence" and leave it empty. The number of rules is not fixed.

Stop conditions are meaning conditions only, for example "stop when the next step no longer explains the present state better" or "stop when you have one money figure, one home-country fact, and one next deadline". Never write a stop as a count or as a percentage of the unit count. Measured values (hours, depths, counts, shares) go on evidence lines or into `instances.md`, not into rule sentences.

For the B and F layers, take the stop condition of each chain from the evidence of where the author actually stopped in every material post: the farthest backward unit and the farthest forward unit in each `units.md`. Write the stop as a general move that reaches at least that far in every post. A stop may not be weaker than the evidence: if the author goes past the point where the present is explained, the rule says to go past it, in general terms (for example "keep asking what came before that until the answer is a change that started the subject's present form, even when the present is already explained"). Put each post's farthest unit on an `- evidence:` line under the rule. The example stop above ("stop when the next step no longer explains the present state better") fits B or F only when the evidence shows the author stopped there.

1. **계기 (trigger) (T)**: What kind of event, appearing in which kind of medium, becomes a post, and how fast? For a post with no event (a series or a seasonal subject), what is the trigger? Evidence: the Trigger and Timeline sections of `research-path.md` and the image upload times in `meta.json`.
2. **뒤쪽 (back) expansion (B)**: How does the author go down from the main topic into history, origin, and background? Which questions does the author ask (for example, "how did the main subject come to have its present owner?")? Which kinds of sources does the author go to (wikis, history books, long features)? Where does the author stop? Evidence: the units placed before the trigger in `units.md` and their sources.
3. **앞쪽 (front) expansion (F)**: How does the author go up from the main topic to money, politics, supply chains, and the domestic angle? Which questions and which kinds of sources (filings, government data, statistics, election data)? Evidence: the units after the trigger.
4. **Where rare sources come from (R)**: The kinds of sources with `표시: 희귀` (mark: rare) and the path that reached them. Write this layer as two parts:
   - The three routes to rare sources, each as one rule: (a) follow the sources that domestic articles name; (b) turn the numbers and proper nouns of the topic into English or the local language and search with them; (c) run long descriptive queries in the post's language (several slot names followed by descriptive words).
   - One rule per kind of rare source (for example trade papers, statistics pages, database records, original social posts, report PDFs, foreign-language media): how to search for that kind, written as a slot template that obeys Step 3, and what to do when it is paywalled or blocked.
5. **Base sources (U)**: The kinds of sources with `표시: 바탕` (mark: base) and how the author uses them (one document as the skeleton with only the numbers updated from recent articles, or several documents chained). Write the move as "pick one skeleton document". When the author's own earlier post is the base, do not write a rule about it: the agent that uses the profile cannot see the author's posts. Record the fact on an evidence line and keep only the move it stands for, "pick one skeleton document (a wiki article, a report, a long feature) that already tells the background in order".
6. **What the author adds (A)**: Calculations (ratios, conversions, truncation), comparisons (contrast with home-country figures), analogies, the one-line conclusion. What kinds of sentences are not in the sources. Evidence: "What the author added" in `research-path.md`.
7. **What the author does not do (N)**: Things a generic agent would have done but this author does not (for example: no source links, no summary opening, no direct quotes from English primary sources). These rules decide reproduction quality, so extract them by contrasting with an imagined generic draft.

## Output 2: profiles/<author>/instances.md (hints)

The first line is exactly: `This file is hints, not rules. The rules are research-method.md and SKILL.md.`

Then these sections. Every table row ends with a label cell (evidence.md).

1. `## Sites`: the sites actually reached in the traced posts. Start from the output of `rek source-sites runs/`; keep its domain, post-count, and source-count columns, drop its publisher and example-URL columns, and add two columns: the kind of source (trade paper, wiki, statistics page, …) and whether it was paywalled or blocked (from `sources.md`). If `runs/` holds runs of other authors, keep only the domains that appear in this author's `sources.md` files.
2. `## Queries`: the queries actually used that reached a source (the `## 평범한 검색` queries, the queries on "how it was reached" lines in `sources.md`, and the supplementary queries in `units.md`), each with the post id, the source id it reached, and the language.
3. `## Measured numbers`: the `rek stats` output for every traced `post.md`, pasted as is, and the measured values that the rules leave out (hours from the first report to publication, depth of the back chain, form values moved out of `writing-structure.md`). Copy a value that already appears in a trace file with its file and section; do not count anything yourself.
4. `## Moves`: the move table from Step 1.

`instances.md` contains no author name and no address of the author's blog (`excluded_domains` lives only in `units.md`). Write each post by its post id.

## Output 3: profiles/<author>/writing-structure.md (secondary, optional)

Write `optional: true` at the top. Then the macro structure (the opening, the placement of background → present → trigger → conclusion, the closing line), the kinds of style and the conditions that decide them, and the rules for sentences, numbers, and images. Write each rule as a move, for example "the last paragraph is a one-line conclusion that ends on a new fact or a comparison". Measured values (lengths, spacings, counts, ratios) go to `## Measured numbers` in `instances.md`, not here. Step 3 applies to the rule sentences here too. For each rule, give the evidence post ids.

Resolve the rules so that none conflict. In particular, decide each of the following as a single choice and write it down as a move: where images go relative to the text, the one notation for numbers and their units, what the closing line does, the relation between the rule for keeping base sentences and the frame sentences, and where new material goes in the base.

## Output 4: profiles/<author>/SKILL.md (execution procedure)

Frontmatter: `name: <author>-research`, `description:` (one sentence). The body is the order of steps that an agent that has never seen the author's posts follows after receiving only the three start lines (**main topic, one-sentence trigger, date**):

1. Research checklist: expand the T, B, F, R, and U rules into questions, slot templates, kinds of sources, and meaning stop conditions. Include a line saying not to read material dated after the date. Say that `instances.md` in the same folder lists sites and queries that worked before, as hints the agent may use or ignore.
2. Build the development units: connect what you found as back chain → main topic → front chain, and attach sources to each unit (`research.md`).
3. Put it in the frame: follow `writing-structure.md`, and state that it is optional.
4. Self-check: end with the N rules and "no fact that is not in research.md".

Every line of `SKILL.md` is a rule line, so Step 3 applies to every line: the questions, the templates, and the stop conditions. End each line with the label and the id of the rule it comes from (for example `[observed: B2]`). Examples are slot templates only. Do not copy sentences, numbers, or names from the author's posts. `SKILL.md` must be no longer than 188 lines (the length of the first, instance-level profile); check it with `wc -l` after you write it.

## Language

Write all four files in English. Keep quotations in their original language.

## Checklist before you report

- [ ] Every source id of every post appears in a `## Moves` block of `instances.md`.
- [ ] Every rule heading in `research-method.md` has the form `### <id>: <one sentence> <label>`, and every line under it starts with `- evidence:`, `- why:`, or `- try:`.
- [ ] Every rule has a `- try:` line for each of the two test topics.
- [ ] Every rule heading and every `SKILL.md` line passed the noun check (Step 3), including the words outside template slots.
- [ ] No stop condition is a count or a percentage, and none names a kind of endpoint (an event, document or actor kind); each states what to keep asking until what kind of answer. No rule assumes the author wrote about the topic before.
- [ ] Every B and F stop reaches at least as far as the farthest backward and the farthest forward unit in every `units.md`.
- [ ] A rule is `[observed]` only if every traced post supports it; otherwise `[inferred: <post ids>]`.
- [ ] Quotations are 40 words or fewer, in the original language, only on evidence lines and in `instances.md`.
- [ ] The first line of `instances.md` is the hints sentence; it has no author name and no blog address.
- [ ] `writing-structure.md` starts with `optional: true` and holds no measured values.
- [ ] `SKILL.md` is no longer than 188 lines (`wc -l`).

## Completion report

Report:
- the four file paths;
- the number of rules per layer (`grep -c "^### T" profiles/<author>/research-method.md`, and the same for B, F, R, U, A, N);
- the noun-check result as "N of N rules passed the noun check";
- the number of rules rewritten one level up after a failed instantiation;
- the three strongest N rules.
