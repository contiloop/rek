---
name: reference-a-research
description: A procedure for an agent that receives only a 본 주제 (main topic), a one-sentence 계기 (trigger event), and a date, and researches like the Naver blog author the reference author. Collect the domestic news wave around the 계기 and the first wave from a few months earlier. Fill the slots where the author's earlier posts used to sit with outside 바탕 (base) documents. Fill the 뒤쪽 (backward) chain that descends into history and origins and the 앞쪽 (forward) chain that climbs into money, Korea, supply chains, rules, and outlook, using 희귀 (rare) source query templates. Then assemble development units that put the 계기 at the end.
holdout: 224428298482
---

# the reference author research: procedure for a new topic (holdout variant)

- This file is the execution order. The evidence posts and exceptions for each rule are in `research-method.md` in the same folder, under the rule ids (T, B, F, R, U, A, N) [observed].
- This variant is a profile with the `holdout:` post removed from its evidence. Do not open profile files outside this folder (opening one invalidates the test) [inferred: test design].
- The label at the end of a line is the number of posts that supported the rule: [observed] means 2 posts, [inferred] means 1 post [observed].
- Square brackets `[ ]` mark slots for you to fill. Examples show only the shape [observed].
- The post template is in `writing-structure.md` (optional). Scoring looks only at the research (units and sources) [observed].

## 0. What you receive, and the boundary

- You receive three lines only: `main_topic`, `trigger` (none if absent), and `date` (KST, your "today") [observed].
- **The replication worker uses no material dated after `date:`.** Do not use the content of any page published later than `date:` (opening a page to check its date and closing it is allowed; record it as `[접촉]`), and do not open any other file in the run folder. Using such content makes the attempt invalid [observed].
- If the author's post appears in a search result list, do not open it. Only record it in log.md as "seen but not opened" [inferred].
- Subject list: from `main_topic` and `trigger`, pull out every proper noun (company, country, land, sea, product, person, institution), and write each one's English name and local-language name. These fill the `[주인공]` (subject) slot in every template below [observed: R12].
- Dating: for articles, use the input time. For wikis, use the version from before `date:` (Wayback snapshot, Wikipedia revision history). Use undated databases and homepages, but mark them [inferred] [observed: U5].
- Find domestic articles with Naver News (네이버 뉴스) search, with a date range set. If a news site is blocked, open the portal reprint (Daum, Nate, etc.). If that also fails, follow the 크롬 (Chrome) rule in evidence.md [observed: R1].
- Log every search query, every URL opened, and every Chrome use in log.md in time order [observed].

## 1. Research checklist (in this order, up to each stop condition)

- [ ] Before starting: the replication worker uses no material after `date:`. Copy the forbidden list from section 0 and `date:` to the top of log.md, then begin [observed: researcher.md].

### 1-1. 계기 wave: T1·T2·T3·T6

When a trigger is given [inferred]:
1. Find the first channel: a social post by an institution and the first wire story from the foreign press [inferred: T2].
2. Collect domestic articles from the first domestic report through `date:` from at least five outlets (wire, general daily, business daily, broadcaster, internet outlet, trade paper) [inferred: T2, N3].
3. For each outlet, record: publication time, quotations (verbatim), number notation (unit closed up, unit spaced, or with '천' (thousand) inserted), and any foreign source the article names [observed: N2, F7].
4. Open the wire or trade-paper story that the article names, through a free reprint. Also find English articles from the 12 hours just before `date:` [observed: T6 / inferred: R3].
5. Setup articles (판 깔기): find domestic articles on the same subjects from `[date−10일]~[사건일]` (share, scale). Many of the numbers come from here [inferred: T3].

When trigger is none [inferred: T4]:
6. Find seasonal articles from the 2 to 4 weeks before `date:`, and two or three of the latest data articles on the main topic (recommended levels, statistics, prices) [inferred].

- Stop: five domestic outlets, one foreign first channel, and one setup article (if none: one seasonal article and two data articles) [inferred].

### 1-2. First wave and the "prior-post slot": T5·U1–U7

- In both posts, the author had already written on the same topic two to ten months earlier, and that post supplied a large share of the background units [observed: T5]. Assume the new topic works the same way. You cannot see that post, so fill its slot with outside 바탕 sources [inferred: apply U4].
1. Find the first wave: widen the `[주인공]` news search to `[date−12개월]~[date]` and pick the months when articles clustered (the big event just before, the event first covered at scale) [inferred].
2. Collect domestic articles and foreign press from within 2 weeks either side of that month, as a separate set. The numbers and quotations of the background units come from here [observed: T5].
3. Find all three 바탕 candidates [observed: U4]:
   - The 나무위키 (Namuwiki) page for `[주제]`: its sections on types and chronology (the version from before `date:`) [observed]
   - Long columns or features in Korean newspapers: front-page features dissecting a company in business dailies, features of the form "[주제]의 모든 것" [observed]
   - The Korean Wikipedia page and the '연혁' (history) page of the company homepage [observed]
4. Pick one skeleton: the document that lays out the subject's history from oldest to newest and has the most distinctive wording not found in the other candidates [inferred: U1, U7].
5. Mark the numbers in the skeleton that differ from the latest domestic articles. Change the new value inside that unit [observed: U3].
6. If you cannot open the earlier wiki version, use a pre-`date:` article or column that covers the same history as the skeleton [observed: U5].

- Stop: one skeleton and two candidates, and at least three first-wave articles [inferred].

### 1-3. 뒤쪽 chain: B1–B7

For each subject, ask the questions below. When an answer comes, ask "why did that happen?" once more (2 to 3 levels deep) [observed: B1, B2]:
- `[회사]` (company): who founded it, when, and with what; when and why did the ownership or nationality change; what was the original business [inferred]
- `[산업·품목]` (industry or product): when and why did it start (depletion of an earlier resource); where was it first sold [inferred]
- `[자연 조건]` (natural conditions): what did migration, water temperature, or terrain decide? Keep this as a separate unit [observed: B4]
- `[이름·별명]` (name or nickname): where did it come from? One line [observed: B3]

Source order: skeleton document → wiki → long articles and columns → company history → (for a foreign industry history with no Korean material) English research reports, conference papers, and port or institution history pages [observed: B5, inferred: B6].

- Stop: stop when the next step no longer explains the present state of the main topic any better. Usually that is the first founding or first catch [observed: B7]. By unit count this was 18 to 28% of the total [inferred: classification of the two posts].

### 1-4. 앞쪽 chain: F1–F11

Questions [observed: F1–F4, F6 / inferred: F8]:
- Money: how much (freight, export value, import unit price) and the earlier value [observed]; both the money coming in and the money going out (insurance, labor) [inferred]
- Korea: Korea's annual consumption, the scope of responsibility of Koreans and the Korean government, domestic substitutes [observed]
- Supply chain: who carries it where, intermediate processing and transshipment points, tariffs [observed]
- Rules: the body and conditions that set supply (recommended levels, quotas, actions by authorities) and their numbers [observed]
- Outlook: when the next deadline or season comes, and what changes by then [observed]
- For everyday topics (food, neighborhoods, weather): the current season and a taste comparison; where it is sold (a restaurant in a producing-area market, a place that uses the imported product, a place near where the reader lives) [inferred: R11]

Source order: several domestic articles → the foreign primary source the articles name → trade papers and international body documents → databases [observed: F7].

- Stop: stop once you have at least one money number, one Korea-side fact, and one next deadline [observed: F11]. By unit count this was 44 to 47% of the total [inferred: classification of the two posts].

### 1-5. 희귀 source query templates: R1–R13 (you must actually run them)

- Most original-text sources lay outside the top results of a single search on the topic word (65 희귀 sources; only 7 to 9 per post were in the domains of the top results) [observed: N11].
- For each type, run at least one Korean query and one English query. Rerun with the number written closed up, spaced, and with '천'. Discard results later than `date:` [inferred: R13].
- If a paywall blocks you, search again with the same title and open a public abstract, a republished copy, or a reprint [observed: R2 / inferred: R3].

| Type | Query template | What it yields |
|---|---|---|
| Domestic articles (R1) | `[주인공] [사건 핵심어]`(period `[사건일]~[date]`) / `"[숫자 표기]" [주인공]` / `[주인공] [점유율·규모]`(period `[date−10일]~[사건일]`) / `[주인공] [첫 파도 사건어]`(period `[첫 파도일 ±14일]`) / `[기사 제목 앞부분] [포털 이름]` / `1인당 [품목] [소비량·섭취량] [나라]`(no period; include statistics articles several years old) / `[업계 단체] 보도자료 [품목] [YYYY]` | Five or more outlets, setup articles, the first wave, reprints, old statistics, articles based on press releases [observed] |
| Trade papers (R2) | `[영문 주인공] [영문 핵심어] [숫자] [Month YYYY]` / `"[국내 기사가 이름 댄 매체]" [영문 주인공]` / `[영문 주인공] [업종 영어] news [Month YYYY]` | Primary numbers, public abstracts [observed] |
| Wire reprints (R3) | `"[외신 제목 일부]"` / `[영문 주인공] [통신사] [핵심어] [Month YYYY]` | Free reprints on trade sites, local newspapers, and financial portals [inferred] |
| International bodies and associations (R4) | `[품목] market [국제기구] [YYYY]` / `[품목] consumption per capita [지역] [시장 관측 기관]` / `[교역국] chamber of commerce [품목] tariff statement` / `[권고 기관] advice [자원] [YYYY]` / `[품목] [감축률] [환경단체]` | Original tariff, quota, and recommended-level documents [inferred] |
| Domestic public bodies (R5) | `정책브리핑 사실은 이렇습니다 [사안]` / `[부처] 보도설명 [사안] [YYYY]` / `[분야 국책연구원] 해외 동향 [품목]` | Raw data tables, Korean-language editions of foreign trade papers [inferred] |
| Wiki and history (R6) | `[주제] 나무위키` / `[주제] 위키백과` / `[주제] 위키` / `[회사] 연혁` / `[회사 영문명] history` | History chains, name origins, version dates [observed] |
| Databases (R7) | `[선박·기체 이름] IMO owner manager` / `[항로] war risk premium [Month YYYY]` | Ownership and management fields, rates [inferred] |
| Local-language and reprints (R8) | `[매체명] [현지어 핵심어] [주인공]` / `[행사·품목 현지어명] [도착·발표 현지어] [YYYY]` | Investigative reports whose English edition is blocked, foreign wire reprints [observed] |
| Research and history (R9) | `collapse of the [국가] [자원] [산업]` / `[자원] [연대] crisis working paper` / `history of [산업] [항구·도시]` / `[사건] proceedings pdf` | Dates when an industry began or collapsed [inferred] |
| Everyday life (R11) | `[도시·동네] [음식] 맛집` / `[시장명] [음식] 백반` / `[음식] 혼밥 [칼럼]` | Where to eat, and prices [inferred] |

- Also run long descriptive Korean queries. The form `[고유명사] [고유명사] [특징 서술어] [특징 서술어]` reached wikis and old feature articles well [observed: R12].

### 1-6. Preparing calculations: A1·A2·A3·A9

- Korea comparison: for each foreign value, find the same kind of value for Korea (and neighboring countries) and put it beside it [inferred: A1].
- Count: do a one-step division such as `[총액] ÷ [1회 값] = [횟수]` and write the result as an integer [inferred: A2].
- Rounding: add "정도·가까운·넘게" (about, close to, over) to a trimmed value [inferred: A3].
- Write every formula and the source of every input value in research.md [observed].
- Do not change a source's reference point in time (such as compared with the same month of the previous year) [inferred: A9].
- Do not download raw data to build new statistics. Use only values that articles and press releases already gave, plus one-step arithmetic [observed: N6].

## 2. Assembling development units (research.md)

- Chain order: 뒤쪽 chain (oldest first) → the present state of the 본 주제 (main topic) → 앞쪽 chain → the 계기 and the answer to the title (at the very end) → material for the closing line [observed: N1].
- Where new material goes: a value that corrects a skeleton number is changed inside that unit, a new topic is inserted in its proper place on the chain, and only the 계기 goes at the very end [observed: U3].
- Use 12 to 20 units as the standard, with 18 to 28% 뒤쪽 and 44 to 47% 앞쪽 [inferred: classification of the two posts].
- For each unit, write: number (R01…), name, one-line summary, direction (뒤쪽/본 주제/앞쪽), and supporting sources (URL, publication date, quotation of 40 words or fewer, label) [observed].
- Attach two or more sources to each unit: one domestic article, and one primary source or trade paper that the article relies on [observed: N2 / inferred: N3].

```
R[번호] | [단위 이름] | [뒤쪽·본 주제·앞쪽] | [한 줄 요약]
  - [국내 기사 URL] ([발행일 시각]) "[인용]" [observed]
  - [1차 출처 URL] ([발행일]) "[인용]" [observed]
```

- `## 못 찾은 것` (Not found): the links you tried to find, the questions you asked, and the queries you tried [observed].
- `## 출처 목록` (source list): URL, publication date, primary or secondary, and how you reached it (a domestic article named it / English search / descriptive search / wiki version) [observed].
- Prior-post slot check: is a 바탕 document attached to the 뒤쪽 chain and to the background just before the 계기? [observed: U4]

## 3. Putting it into the template (optional: writing-structure.md)

- Style: if the time in `date:` is around 00:10, use Style A (each line is "N. " plus one sentence in the ~임 style). Otherwise use Style B (no numbers, the ~다 style) [observed: W1].
- Image slots `![image: [무엇을 보여 줄지]]` go only at unit boundaries: in Style A after the first sentence of a new unit, in Style B at the end of a paragraph [observed: W14].
- Write numbers and units closed up with no space, and mix Arabic numerals with the 만 and 억 units for large numbers [observed: W12].
- Do not copy sentences from a 바탕 document. Take only the facts and write them fresh in the template. Only quoted passages keep the domestic article's translation as it is [inferred: W10].

Style A template [observed: W2–W6]:
```
[왜 이 글인가 — 존댓말 한 줄]
1. [가장 오래된 사실]였음.
![image: [그 사실을 받치는 그림]]
2. [다음 사건]하게 됨.
… (뒤쪽 사슬, 몇 개마다 "[앞 사실]이라는 말임." 같은 풀이 한 줄)
[k]. 문제는 [X]임.
… (본 주제와 앞쪽 사슬, 숫자마다 비교 기준)
[n]. [제목의 물음에 답하는 문장] 이유임.
한줄 코멘트. [본문에 없던 사실 하나 또는 비교]. [단서 붙은 전망·조언·지켜볼 점].
```

Style B template [observed: W2–W6]:
```
[연·월·일], [주체]가 [사건]했다.
[처음 전한 매체] 기사가 나왔다.
![image: [위치에 표시를 한 지도]]
[주인공]은 [한국에서 알려진 이름]으로 알려진 [무엇]이다.
… (내력 → 돈·소유 구조 → 최근 데이터; 문단 끝마다 그림 자리)
[행위자]가 가만히 있지 않았다.
[행위자]는 [날짜] [채널]에 "[국내 기사의 번역 그대로]"고 경고했다.
[제목의 물음에 답하는 문장]이다.
한줄 코멘트. [새 사실이나 비교]. [지켜볼 점]이다.
```

- The 한줄 코멘트 (one-line comment) is the last paragraph, 1 to 4 sentences, 110 to 220 characters [observed: W6].

## 4. Self-check (if any answer is "yes", fix it and finish)

- [ ] N1 Did the research start from the 계기 news and end at the 계기? Are there fewer than three 뒤쪽 chain units? [observed]
- [ ] N2 Did you copy numbers and quotations directly from the English original? Did you use the primary source's value when a domestic article's notation exists? [observed]
- [ ] N3 Does a core fact cluster have only one domestic article? [inferred]
- [ ] N11 Did you fill units from only the top results of topic-word searches? Is there any type in 1-5 that you did not run? [observed]
- [ ] U4 Is the prior-post slot (뒤쪽 chain, background) empty, with no 바탕 document? [observed]
- [ ] N4 Does the post have links, references, footnotes, a summary lead, or subheadings? [observed]
- [ ] N5 Does it list pro and con or expert opinions and end without a judgment? [observed]
- [ ] N6 Did you build new statistics from raw data? Is there a calculation whose formula is not in research.md? [observed]
- [ ] N8 Is there any investment solicitation, stock recommendation, or target price? [observed]
- [ ] N9 Did you make a table or chart? [observed]
- [ ] A9 Is there a sentence that changes a source's reference point in time? [inferred]
- [ ] Facts not in research.md: is there even one number, name, date, or event in post.md that cannot be traced to a source in research.md (a quotation, or a document in the source list)? If so, delete that sentence [observed: researcher.md].
- [ ] Forbidden contact: does log.md record reading the body of a page after `date:`, another file in the run folder, or a profile file outside this folder? If so, that attempt is invalid, and you must not use even one character of what you saw there [observed: researcher.md].
