optional: true
holdout: 224456106651

# The shape of posts by the reference author: the container for research results (holdout variant, rek-method-analyst, 2026-10-30)

- This file is optional. The replication scoring (verifier.md) does not look at style or structure. It counts only development units, 희귀 (rare), 바탕 (base), and fabrication [observed].
- `holdout:` is the id of the post removed from the evidence for the test. That post and the earlier (prior) posts of its run are left out of all statistics and evidence below [observed].
- The figures were measured with `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek stats` (the 2 remaining tracked posts + 11 prior posts from those runs) [observed]. Things that rek stats does not measure (spacing between numbers and units, image position) were measured with a temporary script and are marked as such [observed].
- The rule ids are W1–W18. The research rule ids (T·B·F·R·U·A·N) are in research-method.md in the same folder [observed]. Examples use only bracket templates [observed].

## 0. Measurement table (rek stats)

| id | kind | published (KST) | style | sentences | numbered_items | mean_sentence_chars | noun_ending_share | da_ending_share | sentences_with_number_share | images | one_liner_chars |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 223714326525 | prior | 2025-01-05 00:10 | A | 71 | 63 | 53.2 | 0.85 | 0.03 | 0.44 | 8 | 333 |
| 223737564971 | prior | 2025-01-24 23:46 | B (diary) | 36 | 0 | 39.4 | 0.0 | 0.94 | 0.36 | 4 | 0 |
| 223755523008 | prior | 2025-02-11 00:10 | A | 69 | 64 | 55.7 | 0.86 | 0.04 | 0.39 | 12 | 273 |
| 223784816464 | prior | 2025-03-06 00:10 | mixed | 71 | 28 | 47.0 | 0.37 | 0.58 | 0.32 | 4 | 145 |
| 223840861084 | prior | 2025-04-21 07:38 | B | 62 | 0 | 57.0 | 0.0 | 0.87 | 0.55 | 13 | 152 |
| 224058494349 | prior | 2025-10-30 08:39 | B (list) | 22 | 12 | 45.5 | 0.0 | 0.27 | 0.59 | 1 | 135 |
| 224059473094 | prior | 2025-10-31 00:17 | B | 89 | 18 | 45.4 | 0.06 | 0.64 | 0.65 | 8 | 205 |
| 224140130757 | prior | 2026-01-09 11:00 | B | 40 | 0 | 40.6 | 0.0 | 0.93 | 0.42 | 4 | 67 |
| 224207962250 | prior | 2026-03-08 00:10 | A | 72 | 58 | 45.4 | 0.81 | 0.03 | 0.33 | 12 | 115 |
| 224223174613 | prior | 2026-03-20 11:00 | B | 35 | 0 | 55.5 | 0.0 | 0.91 | 0.46 | 4 | 169 |
| 224272172681 | prior | 2026-05-02 09:20 | B (diary) | 59 | 0 | 38.1 | 0.0 | 0.95 | 0.39 | 20 | 26 |
| 224428298482 | tracked | 2026-10-02 00:10 | A | 103 | 96 | 54.3 | 0.86 | 0.04 | 0.49 | 14 | 219 |
| 224450743987 | tracked | 2026-10-24 00:10 | A | 68 | 64 | 47.0 | 0.87 | 0.01 | 0.5 | 12 | 120 |

- Every value in the table is rek stats output, except the "style" column, which this analysis derived from noun_ending_share (0.8 or above is A, 0.1 or below is B) [observed].
- Style A = a ~임 style (noun-form endings) with "N. " typed by hand on each line. Style B = an unnumbered ~다 style [observed].

## 1. Conditions for choosing the style

### W1: The publication time sets the style. If the time in `date:` is around 00:10, write Style A. At any other time, write Style B [observed]
- Of the 6 posts published at 00:10, 5 are A (noun_ending_share 0.81–0.87): 223714326525, 223755523008, 224207962250, 224428298482, 224450743987 [observed].
- All 7 posts published at other times are B (noun_ending_share 0.00–0.06). Examples: 224140130757 (11:00), 224223174613 (11:00), 224059473094 (00:17) [observed].
- Exception: 223784816464 (00:10) is a reaction post to an event, so it is a mix: an old numbered list inserted into a B body (noun 0.37, da 0.58) [observed]. A short reaction that takes up a 계기 (trigger event) directly becomes B regardless of the time [inferred].

## 2. Macro structure

### W2: Opening. Style A opens with one polite-register meta line. Style B opens with a dated event sentence [observed]
- In all 5 Style A posts, the first line is a polite-register meta sentence (for example, the first_line of 224428298482, 224450743987, 224207962250) [observed]. Template: `[왜 이 글인가 또는 '늘 그렇듯이' 배경 예고], [~합니다/~입니다].` [observed]
- Among the 5 Style B posts (diaries excluded), only one opens with an event sentence: 224223174613 [inferred]. Template: `[주체]가 [사건]했다.` [inferred]
- Exception: follow-up and supplement posts put the title of their own earlier post on the first line (224140130757, 223840861084) [observed]. The replication does not use this form (N10) [inferred].

### W3: Unit placement. 뒤쪽 (backward) chain (oldest first) → 본 주제 (main topic) → 앞쪽 (forward) chain → 계기 and the answer to the title (last quarter) → 한줄 코멘트 (one-line comment) [observed]
- 224428298482: the 뒤쪽 units sit at 2% to 45% of the sentences, the midterm-election unit starts at 84%, and the 계기 sentence "100. …" is at 99% [observed: position measured with rek's sentence splitting].
- 224450743987 (no 계기): the 뒤쪽 history starts at 3%, the newest-news unit (D13) is at 56%, the domestic-product unit is at 60%, and the individual restaurants start at 91% [observed: same method].
- Exception: in an everyday-topic post with no 계기, put an everyday unit (the current season, where to eat) in the 계기 slot [inferred: 224450743987].

### W4: Transition sentence. When moving from background to the present, use one short sentence [observed]
- Forms: `[사건]하면서 상황이 바뀜.` (224428298482 #43, at the 42% point) / `문제는 [X]임.` (224428298482 #53, 224450743987 #29·#40) [observed]

### W5: Where new material enters the 바탕 post (decision 5). A new value that corrects a number in a 바탕 document is changed inside that unit. A new unit is inserted in its proper place on the chain (whichever of 뒤쪽, 본 주제, 앞쪽 the topic belongs to). Only the 계기 and the answer to the title go at the very end [observed]
- Changed inside the unit: 224450743987 D11 corrected the earlier post's number to a more precise value and added a percentage [observed: research-path §3]. 224428298482 D08 changed the earlier post's 440억달러 to 545억달러 [observed: research-path §3-1].
- Inserted in place: 224450743987 D12–D14 are new units inserted between D11 and D15–D17, which the earlier post supplied [observed: units.md reuse column].
- At the very end: 224428298482 appended new units D11–D20 after D01–D10, which the earlier post supplied, and put the 계기 last [observed].
- "Append new content after the last number" fits only the 계기 and new events. I decided that topics that belong to the 바탕 chain are inserted in place [inferred: decision].

### W6: Closing line (decision 3). The last paragraph is 1 to 4 sentences starting with "한줄 코멘트.", 110 to 220 characters [observed]
- Across the 11 posts that have a 한줄 코멘트 (diaries excluded), the median one_liner_chars is 152, and 8 fall within 110 to 220 [observed: count from the table in section 0].
- The two tracked posts are 120 and 219 characters, both within this range [observed].
- Template: `한줄 코멘트. [본문에 없던 사실 하나 또는 비교]. [단서 붙은 전망·조언·지켜볼 점].` [observed] The content rule is research-method.md A7 [observed].
- The old material had several different length ranges. I replaced them with this single range [observed].

## 3. Sentences

### W7: Style A. One line is "N. " plus one sentence, and numbered items are 81% to 94% of sentences [observed]
- numbered_items/sentences: 224428298482 96/103, 224450743987 64/68, 223755523008 64/69, 224207962250 58/72 [observed].
- Endings: noun_ending_share 0.81–0.87, da_ending_share 0.01–0.04 [observed]. Use `~하게 됨/~했음/~였음` for past events, `~임/~있음` for present facts, `~것임/~라는 말임/~이유임` for explanations, and `~전망임/~수 있음` for outlooks [observed: Style A post bodies].
- The author numbers by hand and tends not to renumber after deleting a line (224428298482 numbering_gaps [1, 34, 42, 54]) [observed]. The replication numbers from 1 with no gaps [inferred].

### W8: Style B. No numbers, one sentence per line, ending in ~다 [observed]
- In explanatory and reaction posts, da_ending_share is 0.64–0.93 and noun_ending_share is 0.00–0.06 (224140130757 0.93, 224223174613 0.91, 223840861084 0.87) [observed]. The low value (0.64) belongs to a post with long quotations and lists (224059473094) [observed].
- Write explanations with `~이유다/~말이 된다` and estimates with `~것 같다` [observed: 224140130757 body].

### W9: Sentence length. An average of 40 to 57 characters, with one main point per sentence [observed]
- mean_sentence_chars: Style A 45.4–55.7, Style B (diaries excluded) 40.6–57.0 [observed]. Diaries are shorter, at 38–39 characters (224272172681, 223737564971) [observed].

### W10: Template sentences and 바탕 sentences (decision 4). Write every sentence of the replication post fresh in this file's template. Do not copy sentences from a 바탕 document (wiki, article, column); take only the facts. Only quoted passages keep the domestic article's translation as it is [inferred]
- "Keep the base post's sentences and fix only numbers, place names, and years" is about the author reviving his own earlier post [observed]. The replication's 바탕 is someone else's writing, so that rule does not apply [inferred: decision].
- Basis for the quotation rule: the note of 224428298482 S49 records that the quoted remarks in the earlier post and in this post are wording from the same-day domestic wire article [observed].

### W11: Spell out abbreviations and foreign institution names in parentheses on first use (research-method.md A8). For a long original text (a social post, a statement), point to it with "아래와 같은" (as below), then give a capture slot and an unnumbered Korean translation [observed]
- In 224428298482, after #82 come img_13 (a capture) and two unnumbered translation paragraphs [observed]. 224059473094 also puts "한글로 해석하면 다음과 같다." (in Korean, it reads as follows) and an unnumbered translation after a capture [observed].

## 4. Numbers

### W12: Number notation (decision 2). Write large numbers by mixing Arabic numerals with the 만 and 억 units (commas below 만), write units in Hangul, and close up the number and unit with no space [observed]
- Of 290 "number + unit" occurrences in 13 posts, measured with a temporary script, 235 (81%) were closed up [observed: auxiliary measurement].
- All 108 numbers ending in Arabic numerals were closed up (for example `[8,765톤]`, `[0.12kg]`) [observed: auxiliary measurement].
- Of 182 numbers ending in 천·만·억, 127 (70%) were closed up. The spaced ones are mostly in translated quotations or carried-over sentences (for example, all 3 spaced ones in 224428298482 are translations or lists from the earlier post) [observed: auxiliary measurement].
- In the two tracked posts alone, 79 of 86 (92%) were closed up [observed: auxiliary measurement].
- The old material's "close up" rule and its spaced examples disagreed. I settled on the majority, "close up" [observed].
- Do not use '$', 'USD', or 'billion' [observed: 0 occurrences in the body of the two posts].

### W13: Give the numbers that support the argument a comparison base (the earlier value, the share in %, the same value for Korea) (research-method.md A1), and add the year to dates [observed]
- 224428298482 #60 added "2025년" to the earlier post's date [observed: research-path §3-1]. 224450743987 #28 also added the year to the date of the current event [observed: post.md].

## 5. Images

### W14: Image position and count (decision 1). Place images only at the boundaries of development units: in Style A right after the topic sentence that opens a new unit, in Style B at the end of a paragraph that groups units. The total is then about two thirds of the unit count. Do not use interval rules such as "one image every N items" [observed]
- Images per unit: 224450743987 12/18, 224428298482 14/20 [observed: rek stats images, units.md].
- In Style A a new image comes after the topic sentence. In 224428298482, img_12 comes after #69 (the first sentence of D12) and img_14 after #85 (the first sentence of D16) [observed: post.md]. In 224450743987, img_05 comes after #40 (the first sentence of D14) [observed].
- In Style B images come at the end of a paragraph: the pictures of 224140130757 and 224223174613 all sit between text paragraphs [observed: post.md].
- Long units and personal units with several photos get more images inside the unit (224450743987 D18 has 4, 224428298482 D02 has 4) [observed].
- Result range (rek stats images): Style A 8 to 14, Style B 4 to 8 [observed]. The exceptions are the Style B planning post 223840861084 (13 images) and the diary 224272172681 (20 images) [observed].
- The old material's interval rule and total rule do not fit each other, so I replaced them with a single position rule [observed].

### W15: There are five kinds of images: mood stock photos; maps or screen captures with a red circle or arrow drawn on them; captures of original text to be quoted; generated pictures for new parts that have no photos; and photos the author took himself for personal parts [observed]
- 224428298482 img_02·img_03 (stock), img_08·img_11 (map with a red arrow), img_13 (capture of a social post), img_12·img_14 (Gemini) [observed]; 224450743987 img_01–img_06·img_08 (OGQ stock), img_09–img_12 (restaurant photos) [observed: viewed the images].
- Stock photos appear in two posts; each of the other four kinds appears in only one post [inferred].
- The replication uses only the placeholder `![image: [무엇을 보여 줄지]]` (researcher.md) [observed].

### W16: Do not describe the pictures in the body (no figure numbers or caption sentences) [inferred]
- Only when quoting a captured post does it point to it with "아래와 같은" (224428298482 #82) [observed].

## 6. Voice and format

### W17: State facts flatly and mark only estimates (research-method.md A6). Put one or two slangy spoken words in each post between the dry facts [inferred]
- Form of the spoken words: investor and internet slang such as `[가치가 크게 오름]을 '떡상'` ('떡상' = skyrocketing) (224428298482 #35) [observed].

### W18: Do not use subheadings, bold text, bullet marks, tables, links, exclamation marks, or emoji (research-method.md N4·N9) [observed]
- The block_counts of the two posts contain only text and image, with quote, link, and rule at 0 [observed: meta.json].

## 7. The five contradictions I decided

| Contradiction | How the old material disagreed | What I decided | Rule |
|---|---|---|---|
| Image interval vs. total and position | The interval rule and the total rule do not fit in a long numbered post [observed] | Place images at unit boundaries; the total is about two thirds of the unit count (12/18, 14/20) [observed] | W14 |
| Spacing between number and unit | The "close up" rule and spaced examples [observed] | Close up (measured 81%) [observed] | W12 |
| Length of the closing line | Several different ranges [observed] | One range, 110–220 characters (median 152) [observed] | W6 |
| Template sentences vs. keeping base sentences | "keep the base post's sentences as they are" vs. "write in template sentences" [observed] | The replication writes fresh in the template and does not copy base sentences [inferred] | W10 |
| Where new material goes | "append after the last number" vs. "the 계기 goes in the last quarter" vs. "in an everyday post the new news goes in the middle" [observed] | Fix numbers in place, insert new units in place on the chain, and put only the 계기 and the answer at the end [observed] | W5 |
