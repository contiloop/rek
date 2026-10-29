optional: true
holdout: 224428298482

# The shape of posts by the reference author: the container for research results (holdout variant, rek-method-analyst, 2026-10-30)

- This file is optional. The replication scoring (verifier.md) does not look at style or structure. It counts only development units, 희귀 (rare), 바탕 (base), and fabrication [observed].
- `holdout:` is the id of the post removed from the evidence for the test. That post and the earlier (prior) posts of its run are left out of all statistics and evidence below [observed].
- The figures were measured with `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek stats` (the 2 remaining tracked posts + 14 prior posts from those runs) [observed]. Things that rek stats does not measure (spacing between numbers and units, image position) were measured with a temporary script and are marked as such [observed].
- The rule ids are W1–W18. The research rule ids (T·B·F·R·U·A·N) are in research-method.md in the same folder [observed]. Examples use only bracket templates [observed].

## 0. Measurement table (rek stats)

| id | kind | published (KST) | style | sentences | numbered_items | mean_sentence_chars | noun_ending_share | da_ending_share | sentences_with_number_share | images | one_liner_chars |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 223737564971 | prior | 2025-01-24 23:46 | B (diary) | 36 | 0 | 39.4 | 0.0 | 0.94 | 0.36 | 4 | 0 |
| 224140130757 | prior | 2026-01-09 11:00 | B | 40 | 0 | 40.6 | 0.0 | 0.93 | 0.42 | 4 | 67 |
| 224249713244 | prior | 2026-04-13 00:10 | A | 72 | 65 | 53.7 | 0.86 | 0.04 | 0.33 | 9 | 150 |
| 224256222982 | prior | 2026-04-17 22:43 | B | 26 | 0 | 50.0 | 0.0 | 0.96 | 0.27 | 6 | 155 |
| 224257587679 | prior | 2026-04-20 00:12 | A | 77 | 74 | 52.2 | 0.86 | 0.01 | 0.43 | 6 | 167 |
| 224258306390 | prior | 2026-04-20 08:25 | B | 31 | 0 | 54.0 | 0.0 | 0.9 | 0.29 | 6 | 99 |
| 224272172681 | prior | 2026-05-02 09:20 | B (diary) | 59 | 0 | 38.1 | 0.0 | 0.95 | 0.39 | 20 | 26 |
| 224276829265 | prior | 2026-05-07 00:10 | A | 67 | 61 | 51.6 | 0.84 | 0.04 | 0.22 | 6 | 284 |
| 224278535448 | prior | 2026-05-08 08:48 | B | 36 | 0 | 56.8 | 0.0 | 0.89 | 0.22 | 3 | 119 |
| 224313465740 | prior | 2026-06-12 05:50 | B | 25 | 0 | 48.6 | 0.0 | 0.88 | 0.08 | 3 | 189 |
| 224316120615 | prior | 2026-06-15 09:02 | B | 25 | 0 | 55.3 | 0.0 | 1.0 | 0.48 | 3 | 136 |
| 224319486464 | prior | 2026-06-18 08:15 | B | 62 | 0 | 51.0 | 0.0 | 0.76 | 0.48 | 4 | 175 |
| 224345852124 | prior | 2026-07-14 06:42 | B | 45 | 0 | 53.2 | 0.0 | 0.64 | 0.18 | 5 | 135 |
| 224398051587 | prior | 2026-09-02 06:38 | B | 44 | 0 | 50.9 | 0.0 | 1.0 | 0.45 | 7 | 168 |
| 224450743987 | tracked | 2026-10-24 00:10 | A | 68 | 64 | 47.0 | 0.87 | 0.01 | 0.5 | 12 | 120 |
| 224456106651 | tracked | 2026-10-28 11:00 | B | 46 | 0 | 52.3 | 0.0 | 0.96 | 0.46 | 8 | 137 |

- Every value in the table is rek stats output, except the "style" column, which this analysis derived from noun_ending_share (0.8 or above is A, 0.1 or below is B) [observed].
- Style A = a ~임 style (noun-form endings) with "N. " typed by hand on each line. Style B = an unnumbered ~다 style [observed].

## 1. Conditions for choosing the style

### W1: The publication time sets the style. If the time in `date:` is around 00:10 (00:10 to 00:12), write Style A. At any other time, write Style B [observed]
- All 4 posts published from 00:10 to 00:12 are A (noun_ending_share 0.84–0.87): 224249713244, 224257587679, 224276829265, 224450743987 [observed].
- All 12 posts published at other times are B (noun_ending_share 0.00). Examples: 224456106651 (11:00), 224398051587 (06:38), 224140130757 (11:00) [observed].
- A short reaction that takes up a 계기 (trigger event) directly becomes B regardless of the time [inferred].

## 2. Macro structure

### W2: Opening. Style A opens with one polite-register meta line. Style B opens with a dated event sentence [observed]
- In 3 of the 4 Style A posts, the first line is a polite-register meta sentence (for example, the first_line of 224450743987, 224257587679, 224276829265) [observed]. Template: `[왜 이 글인가 또는 '늘 그렇듯이' 배경 예고], [~합니다/~입니다].` [observed]
- In 8 of the 10 Style B posts (diaries excluded), the first line is an event sentence (for example, 224456106651, 224398051587, 224256222982) [observed]. Template: `[연·월·일], [주체]가 [사건]했다.` [observed]
- Exception: a follow-up or supplement post puts the title of its own earlier post on the first line (224140130757) [observed]. The replication does not use this form (N10) [inferred].

### W3: Unit placement. 뒤쪽 (backward) chain (oldest first) → 본 주제 (main topic) → 앞쪽 (forward) chain → 계기 and the answer to the title (last quarter) → 한줄 코멘트 (one-line comment) [observed]
- 224456106651: the company history is at 7% to 30%, the sentence turning to the 계기 is at 76%, and the answer to the title is at the 98% sentence [observed: position measured with rek's sentence splitting].
- 224450743987 (no 계기): the 뒤쪽 history starts at 3%, the newest-news unit (D13) is at 56%, the domestic-product unit is at 60%, and the individual restaurants start at 91% [observed: same method].
- Exception: in an everyday-topic post with no 계기, put an everyday unit (the current season, where to eat) in the 계기 slot [inferred: 224450743987].

### W4: Transition sentence. When moving from background to the present, use one short sentence [observed]
- Forms: `문제는 [X]임.` (224450743987 #29·#40) / `[행위자]가 가만히 있지 않았다.` (224456106651, at the 76% point) [observed]

### W5: Where new material enters the 바탕 post (decision 5). A new value that corrects a number in a 바탕 document is changed inside that unit. A new unit is inserted in its proper place on the chain (whichever of 뒤쪽, 본 주제, 앞쪽 the topic belongs to). Only the 계기 and the answer to the title go at the very end [observed]
- Changed inside the unit: 224450743987 D11 corrected the earlier post's number to a more precise value and added a percentage [observed: research-path §3].
- Inserted in place: 224456106651 D08 (Korean crew and government) and D11 (insurance premium) are new units inserted after the ownership structure and after the freight rates respectively [observed: units.md reuse column]. 224450743987 D12–D14 were also inserted between D11 and D15–D17, which the earlier post supplied [observed].
- At the very end: 224456106651 put the 계기 units D14–D16 last [observed].
- "Append new content after the last number" fits only the 계기 and new events. I decided that topics that belong to the 바탕 chain are inserted in place [inferred: decision].

### W6: Closing line (decision 3). The last paragraph is 1 to 4 sentences starting with "한줄 코멘트.", 110 to 220 characters [observed]
- Across the 14 posts that have a 한줄 코멘트 (diaries excluded), the median one_liner_chars is 144, and 11 fall within 110 to 220 [observed: count from the table in section 0].
- The two tracked posts are 120 and 137 characters, both within this range [observed].
- Template: `한줄 코멘트. [본문에 없던 사실 하나 또는 비교]. [단서 붙은 전망·조언·지켜볼 점].` [observed] The content rule is research-method.md A7 [observed].
- The old material had several different length ranges. I replaced them with this single range [observed].

## 3. Sentences

### W7: Style A. One line is "N. " plus one sentence, and numbered items are 90% to 96% of sentences [observed]
- numbered_items/sentences: 224450743987 64/68, 224249713244 65/72, 224257587679 74/77, 224276829265 61/67 [observed].
- Endings: noun_ending_share 0.84–0.87, da_ending_share 0.01–0.04 [observed]. Use `~하게 됨/~했음/~였음` for past events, `~임/~있음` for present facts, `~것임/~라는 말임/~이유임` for explanations, and `~전망임/~수 있음` for outlooks [observed: Style A post bodies].
- The replication numbers from 1 with no gaps [inferred].

### W8: Style B. No numbers, one sentence per line, ending in ~다 [observed]
- In news-reaction posts, da_ending_share is 0.64–1.00 and noun_ending_share is 0.00 (224456106651 0.96, 224398051587 1.0, 224316120615 1.0) [observed]. The low value (0.64) belongs to a post with long quotations and translations of original text (224345852124) [observed].
- Write explanations with `~것이다/~의미다/~구조다/~이유다` and estimates with `~것으로 보인다/~예상된다` [observed: 224456106651 body].

### W9: Sentence length. An average of 40 to 57 characters, with one main point per sentence [observed]
- mean_sentence_chars: Style A 47.0–53.7, Style B (diaries excluded) 40.6–56.8 [observed]. Diaries are shorter, at 38–39 characters (224272172681, 223737564971) [observed].

### W10: Template sentences and 바탕 sentences (decision 4). Write every sentence of the replication post fresh in this file's template. Do not copy sentences from a 바탕 document (wiki, article, column); take only the facts. Only quoted passages keep the domestic article's translation as it is [inferred]
- "Keep the base post's sentences and fix only numbers, place names, and years" is about the author reviving his own earlier post [observed]. The replication's 바탕 is someone else's writing, so that rule does not apply [inferred: decision].
- Basis for the quotation rule: the quotations in 224456106651 differ from the domestic article (S01) in only one place of spacing [observed: S01 judgment].

### W11: Spell out abbreviations and foreign institution names in parentheses on first use (research-method.md A8). Give a long original text (a statement, remarks) as an unnumbered quoted paragraph in Korean translation [observed]
- 224249713244 and 224345852124 put long remarks in unnumbered quoted paragraphs [observed].

## 4. Numbers

### W12: Number notation (decision 2). Write large numbers by mixing Arabic numerals with the 만 and 억 units (commas below 만), write units in Hangul, and close up the number and unit with no space [observed]
- Of 145 "number + unit" occurrences in 16 posts, measured with a temporary script, 127 (88%) were closed up [observed: auxiliary measurement].
- All 79 numbers ending in Arabic numerals were closed up (for example `[8,765톤]`, `[12척]`) [observed: auxiliary measurement].
- Of 66 numbers ending in 천·만·억, 48 (73%) were closed up [observed: auxiliary measurement].
- In the two tracked posts alone, 26 of 34 (76%) were closed up, and all 8 spaced ones are numbers ending in 천·만·억 [observed: auxiliary measurement].
- The old material's "close up" rule and its spaced examples disagreed. I settled on the majority, "close up" [observed].
- Do not use '$', 'USD', or 'billion' [observed: 0 occurrences in the body of the two posts].

### W13: Give the numbers that support the argument a comparison base (the earlier value, the share in %, the same value for Korea) (research-method.md A1), and add the year to dates [observed]
- The first sentence of 224456106651 added "2026년" to the earlier post's "8월 31일" [observed: research-path §3 table 1]. 224450743987 #28 also added the year to the date of the current event [observed: post.md].

## 5. Images

### W14: Image position and count (decision 1). Place images only at the boundaries of development units: in Style A right after the topic sentence that opens a new unit, in Style B at the end of a paragraph that groups units. The total is then one half to two thirds of the unit count. Do not use interval rules such as "one image every N items" [observed]
- Images per unit: 224450743987 12/18, 224456106651 8/17 [observed: rek stats images, units.md].
- In Style A a new image comes after the topic sentence: 224450743987 img_05 comes after #40 (the first sentence of D14) [observed: post.md]. This evidence is one post [inferred].
- In Style B images come at the end of a paragraph: all 8 images of 224456106651 are at the ends of paragraphs (para 1–7) [observed: post.md].
- Personal units with several photos get more images inside the unit (224450743987 D18 has 4) [observed].
- Result range (rek stats images): Style A 6 to 12, Style B news posts 3 to 8 [observed]. The exception is the diary 224272172681 (20 images) [observed].
- The old material's interval rule and total rule do not fit each other, so I replaced them with a single position rule [observed].

### W15: There are four kinds of images: mood stock photos; maps or screen captures with a red circle or arrow drawn on them; generated pictures for new parts that have no photos; and photos the author took himself for personal parts [observed]
- 224456106651 img_03 (OGQ stock), img_01·img_07 (map capture with a red line), img_04·img_05 (Gemini) [observed]; 224450743987 img_01–img_06·img_08 (OGQ stock), img_09–img_12 (restaurant photos) [observed: viewed the images].
- Stock photos appear in two posts; each of the other three kinds appears in only one post [inferred].
- The replication uses only the placeholder `![image: [무엇을 보여 줄지]]` (researcher.md) [observed].

### W16: Do not describe the pictures in the body (no figure numbers or caption sentences) [inferred]
- Of the 8 images in 224456106651, the body refers to none [observed: post.md].

## 6. Voice and format

### W17: State facts flatly and mark only estimates (research-method.md A6). Put one or two slangy spoken words in each post between the dry facts [inferred]
- Form of the spoken words: investor and internet slang such as `[크게 성공]을 '초대박'` ('초대박' = a huge hit) (224456106651 paragraph 6) [observed].

### W18: Do not use subheadings, bold text, bullet marks, tables, links, exclamation marks, or emoji (research-method.md N4·N9) [observed]
- The block_counts of the two posts contain only text and image, with quote, link, and rule at 0 [observed: meta.json].

## 7. The five contradictions I decided

| Contradiction | How the old material disagreed | What I decided | Rule |
|---|---|---|---|
| Image interval vs. total and position | The interval rule and the total rule do not fit in a long numbered post [observed] | Place images at unit boundaries; the total is one half to two thirds of the unit count (12/18, 8/17) [observed] | W14 |
| Spacing between number and unit | The "close up" rule and spaced examples [observed] | Close up (measured 88%) [observed] | W12 |
| Length of the closing line | Several different ranges [observed] | One range, 110–220 characters (median 144) [observed] | W6 |
| Template sentences vs. keeping base sentences | "keep the base post's sentences as they are" vs. "write in template sentences" [observed] | The replication writes fresh in the template and does not copy base sentences [inferred] | W10 |
| Where new material goes | "append after the last number" vs. "the 계기 goes in the last quarter" vs. "in an everyday post the new news goes in the middle" [observed] | Fix numbers in place, insert new units in place on the chain, and put only the 계기 and the answer at the end [observed] | W5 |
