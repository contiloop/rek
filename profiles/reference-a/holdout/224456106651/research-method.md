author: reference-a
built_from: 224450743987, 224428298482
holdout: 224456106651

# the reference author research method: the rule ledger (holdout variant, rek-method-analyst, 2026-10-30)

## 0. How to read

- The header runs through the fourth line: `holdout:` is the id of the post that this variant removed from its evidence for the test [observed].
- The evidence of this variant is only the materials of the two runs in `built_from:`. It contains no unit numbers, source numbers, quotations, numbers, proper nouns, outlet names, queries, or format statistics from the holdout post [observed].
- The replication worker does not open profile files outside this folder. Opening one invalidates the holdout test [inferred: test design].
- The address of another subscription channel (for example, 네이버 프리미엄콘텐츠 (Naver Premium Content)) is not in the materials of the remaining runs, so none was added [unknown: searched, not found]. The replication worker also does not open any other channel that shows the author's name ('the reference author' (Mer)) or the blog name (researcher.md read ban) [observed].
- The evidence notation `224428298482 D03·S34` means unit D03 and source S34 of that post [observed]. Quotations are verbatim from post.md or from that run's tracking files, and are 40 words or fewer [observed].
- The label on a rule title line is the number of posts that supported the rule: [observed] for 2 posts, [inferred] for 1 post [observed]. The label on an evidence line is how the fact on that line was confirmed [observed].

| Post | main_topic | trigger | date | Units | Claims | 희귀 (rare) | 바탕 (base; author posts excluded) | Author's earlier posts |
|---|---|---|---|---|---|---|---|---|
| 224450743987 | 노르웨이 고등어와 국산 고등어 (Norwegian mackerel and domestic mackerel) | none | 2026-10-24 00:10 | 18 | 99 | 32 | 1 (S38) | 224140130757 and 2 others [observed] |
| 224428298482 | 알래스카 LNG 프로젝트 (Alaska LNG project) | 트럼프의 한국 540억달러 투자 발표 (Trump's announcement of a 54 billion dollar Korean investment) | 2026-10-02 00:10 | 20 | 109 | 39 | 1 (S52) | 223755523008 and 2 others [observed] |

- Unit directions (뒤쪽 = backward, 본 주제 = main topic, 앞쪽 = forward, 계기 = trigger event; this ledger's classification): 224450743987 뒤쪽 D01·D02·D05·D07·D08, 본 주제 D09·D14–D17, 앞쪽 D03·D04·D06·D10–D13·D18, no 계기 [inferred]. 224428298482 뒤쪽 D01–D06, 본 주제 D11–D13, 앞쪽 D07–D10·D14–D17·D19, 계기 D18·D20 [inferred].
- So 뒤쪽 is 28 to 30% of the units (5/18, 6/20) and 앞쪽 is 44 to 45% (8/18, 9/20) [inferred: count from the classification above].

---

## T: 계기

### T1: A news 계기 is an event in which a foreign government, leader, or institution singles out a Korean company or Korean money [inferred]
- 224428298482 D20·S03: "트럼프는 9월 30일 발표에서 한국의 투자금액을 540억달러로 발언함." [observed]
- Exception: 224450743987 has no 계기, and the head of its units.md reads "trigger: none" [observed]. In that case follow T4 [inferred].

### T2: A 계기 first appears on a foreign first channel (a government release) and on the foreign wire services. Several domestic outlets then report it together on the same morning, and the post goes up within a day of the 계기 announcement (about 18 to 20 hours) [inferred]
- 224428298482 research-path §1: "발표 후 약 18시간 15분~20시간 41분 만에 게시(2026-10-02 00:10)." [observed] The domestic morning wave is S03 08:43, S14 11:22, S04 11:52, S02 14:57 [observed].
- 224428298482 S01 (연합뉴스 09-30 07:30) reported the content of the announcement first, citing a foreign wire service [observed: S01 Match].

### T3: Within ten days before the 계기 there are "setup" (판 깔기) domestic articles on the same subject, and many of the numbers in the post come from them [inferred]
- 224428298482 D08·D14·S12 (한국경제TV 2026-09-29 fact check): "총 사업비는 당초 440억달러에서 글렌파른 추산 545억달러까지 불었습니다." [observed] S01 (연합뉴스 09-30 07:30) is an advance-notice article of the announcement [observed].
- Exception: in a post with no 계기, the latest data article fills this slot (T4) [inferred]

### T4: The 계기 of a post without an event is the season and the series. The material is seasonal articles and the latest data articles from within 2 to 4 weeks of publication [inferred]
- 224450743987 para 0·D17: "불금이라 가벼운 내용입니다." / "53. 10월이 되면서 다시 참고등어 시즌이 오고 있음." [observed]
- 224450743987 D17·S42 (위키트리 2026-10-11, October seasonal seafood), D13·S11 (KMI 2026-10-06, the latest of the sources found) [observed]
- 224450743987 research-path §1: "'고등어 이야기' 연재의 세 번째 글로 보임" (appears to be the third post of the "고등어 이야기" (Mackerel Story) series) [inferred]

### T5: The main topic is one the author had already covered nine months to a year and a half earlier, and the material gathered during that "first wave" returns as background units in this post [observed]
- 224450743987: the 2026-01-09 post 224140130757 supplies D11 (in part) and D15–D17, and the original source of the quota number in the January post is presumed to be S02 (서울경제 2026-01-06) [observed: units.md reuse column / inferred: S02 Probably reached via].
- 224428298482: the 2025-02-11 post (P1) supplies D01–D10, and its materials are S49, S52, S53, S54, and S55, published 2025-01-20 to 02-06 [observed: units.md, sources.md §13].
- Implication for replication: the replication worker cannot see that earlier post but can find the first-wave articles and columns (U4) [inferred]

### T6: Writing happens in the few hours before publication, and a post published at 00:10 is written the day before [observed]
- 224450743987 meta.json: images were uploaded from img_01 "2026-10-23T00:13:04+09:00" to img_12 "2026-10-23T07:57:36+09:00", and the post was published at 2026-10-24 00:10 [observed]
- 224428298482 meta.json: img_12 "2026-10-01T15:04:35+09:00" and img_14 "2026-10-01T15:06:35+09:00" are 7 minutes after S02 (14:57), and the post was published at 10-02 00:10 [observed]

---

## B: 뒤쪽 expansion (from the main topic to history, origin, and background)

### B1: For each subject (land, product), ask "how did it come to have its present owner and form?" and go down to the event where the answer starts (acquisition of territory, first catch) [observed]
- 224428298482 D03·S34: "25. 크림전쟁 이후 재정난에 빠진 러시아는 알래스카를 영국에 뺏기느니 미국에 파는게 낫겠다는 생각을 했고, 미국에 매각을 타진함." [observed]
- 224450743987 D02·S31: "4. 청어를 잡던 선단들은 일감을 잃었고, 이들이 새로 찾아낸 일감이 북해 고등어 였음." [observed]

### B2: After getting one answer, ask "why did that happen?" once more. The depth is 2 to 5 levels [observed]
- 224428298482 D06→D05→D03→D02→D01: a five-level chain of gas pipeline plan → oil pipeline and freezing → purchase → defeat in the Crimean War → first entry [inferred: level split]. D02: "24. 이런 상황에서 알래스카는 러시아가 신경쓰기 힘든 먼곳에 있는 가치없는 영토로 보이게 됨." [observed]
- 224450743987 D02→D01: a two-level chain of North Sea mackerel → herring collapse [inferred: level split]. D01: "3. 1960년이 되자, 매년 수백만톤이 잡히던 청어가 멸종 직전까지 가게 된 것임." [observed]

### B3: Look for one line on the origin of a name or nickname [observed]
- 224428298482 D03·S34: "29. 오랫동안 미국의 알래스카 매입은 매입을 주관한 국무장관 슈어드의 이름을 붙여서 "슈어드의 어리석은 짓"으로 불리었음." [observed]
- 224450743987 D15·S38: "49. 망치고등어는 배와 등이 나뉘는쪽에 일렬로 점무늬가 주욱 있어서 점고등어라고 부르기도 함." [observed]

### B4: Where natural or geographic conditions decided an industry or an event, make those conditions a separate unit [observed]
- 224428298482 D05·S52: "36. 유전은 개발되었지만, 원유 매장지가 북극쪽 해안이라 바다가 얼어있어 … 접근이 불가능했음." [observed]
- 224450743987 D07·S28: "21.북동대서양 고등어는 봄부터 초여름에 산란을 하고, 여름이 되면 플랑크톤과 작은 물고기를 찾아서 북쪽 노르웨이해로 올라옴." [observed]

### B5: 뒤쪽 sources are of three kinds: ① 나무위키 (Namuwiki) and Korean Wikipedia (위키백과) ② long columns and features in Korean newspapers ③ research and institutional materials on a foreign industry's history [observed]
- ①: 224450743987 S38(나무위키 「고등어」), 224428298482 S34(위키백과 「알래스카 매입」)·S35(위키백과 「알래스카주」) [observed]
- ②: 224428298482 S52(이데일리 「미국내 마지막 기회의 땅 알래스카[공관에서 온 편지]」), 224450743987 S39(부산일보 「[What] '국민 생선' 고등어의 모든 것」) [observed]
- ③: 224450743987 S30 (IIFET 2006 conference paper), S31 (SNF Working Paper), S32 (Nordfjord Havn "History of Fishery"), S33 (FAO expert meeting material) [observed]; this type appears in only one post [inferred].
- Exception: the 나무위키 pages of 224428298482 (S46–S48) were versions received after the post was published, so they remain only as [inferred] [observed].

### B6: For a foreign industry history with no Korean material, go to English research reports, conference papers, and the history pages of port companies [inferred]
- 224450743987 D02·S32: "from the mid-60's from the ring net fishery of herring and mackerel in the North Sea" [observed]
- 224450743987 D02·S31: "The fishing fleet found substitute stocks, such as mackerel and capelin." [observed]

### B7: Stop when the next step no longer explains the present state of the main topic any better. Usually you stop at the first settlement or first catch [observed]
- 224428298482 D01: "알래스카에는 원주민들이 오래전부터 살고 있었음." [observed]
- 224450743987 D01: "1. 노르웨이는 청어의 나라였음." [observed]
- Size: 뒤쪽 units were 5 to 6, which is 28 to 30% of the total (the classification in section 0) [inferred].

---

## F: 앞쪽 expansion (from the main topic to money, politics, supply chain, and the Korea angle)

### F1: Find the money number that answers "how much?" (project cost, export value, import unit price) and compare it with the earlier value [observed]
- 224428298482 D08·S12: "53. 문제는 파이프라인과 LNG설비등 전체 프로젝트의 건설비용 545억달러임." [observed]
- 224450743987 D12·S07: "36. 한국의 kg당 수입단가가 2025년 2.6달러에서 2026년 5.4달러로 두배가 넘게 오르는등 비싸게 받았기 때문임." [observed]

### F2: Look separately for Korea-side facts: Korea's annual imports or consumption, the share of Korean companies and state firms, and domestic substitutes [observed]
- 224428298482 D08: "56. 한국이 1년에 수입하는 LNG가 4천700만톤이라, 연간 2천만톤은 43% 수준임." [observed]
- 224450743987 D14·S08: "41. 국산 고등어 어획량 자체는 2025년보다 늘었지만, 중대형은 8,895톤에서 2,806톤으로 급감하고 있음." [observed]

### F3: Look for the supply chain route: who carries it where, intermediate processing points, distance, and tariffs [observed]
- 224450743987 D06·S21: "17. 베트남으로 무관세로 들어가서, 낮은 인건비로 가시등을 바르고, 필렛으로 손질한뒤에 일본에 무관세로 들어가고 있음." [observed]
- 224428298482 D07: "51. 알래스카의 니키스키에서 부산항까지는 해상항로로 7,500km 정도인데, 카타르에서 부산항까지는 11,700km거리임." [observed] I could not find the source of these distance numbers [unknown: searched with the five queries in sources.md §11, not found].

### F4: Find the body and conditions that set supply or decisions (recommending body, quota, conditions for a final decision) together with their numbers [observed]
- 224450743987 D11·S01·S27: "31. 국제해양탐사위원회(ICES)는 2026년 북동대서양 고등어 어획량을 17만4,357톤 이하로 줄이라고 권고함." [observed]
- 224428298482 D12·S17·S19·S20: "69. 알래스카 천연가스 파이프라인이, 착공에 들어가기 위해서는 연간 생산능력 2천만톤의 80%를 장기계약으로 확보해야 함." [observed]

### F5: Find the politician who stood at the announcement and the coming election, and count the seats [inferred]
- 224428298482 D18·S02: "100. 9월 30일, 트럼프가 알래스카 LNG투자를 발표하는 자리에 알래스카의 상원의원인 설리번이 동석한 이유임." [observed]
- 224428298482 D16·S28·S31: "87. 현재 상원은 공화 53석, 민주 47석인데, 공화당과 민주당이 동수일때는 부통령이 캐스팅보트를 쥐고 있음." [observed]

### F6: Close the 앞쪽 chain with when the next deadline, season, or decision comes and what changes by then [observed]
- 224450743987 D13·S11·S18: "39. 2027년 8월에 노르웨이가 고등어를 잡기 전까지는 2026년 냉동이 풀리고 있으니 고등어 가격은 내년여름까지 비쌀 전망임." [observed]
- 224428298482 D14·S12·S13: "79. 알래스카 천연가스 사업은 2025년 12월 FID가 목표였는데, 아직까지 확정되지 않고 있음." [observed]

### F7: Go to foreign primary materials through the places that domestic articles name [observed]
- 224428298482 D12·S13 Match: "300만t을 추가로 확보하고 기존 구매 약속도 법적 구속력이 있는 계약으로 바꿔야 한다고 로이터는 지적했다." [observed] S18 (the Reuters original) is thought to have been reached through this secondhand citation [inferred: S18 Probably reached via].
- 224450743987 D14·S09: Probably reached via "S08이 인용" (S08 cites it): S08 named the raw data with "해양수산부에 따르면" (according to the Ministry of Oceans and Fisheries) [observed]

### F9: Pick one term that decides the next decision, and unpack its meaning and the before-and-after difference as one unit [inferred]
- 224428298482 D13·S56: "73. FID(Final Investment Decision,최종투자결정)는 "이제 진짜 돈을 쏟아붓고 착공한다"고 확정하는 시점을 말함." [observed]

### F10: Add one line linking how another big event of the same period (a war, a blockade) changed the worth of the main topic [inferred]
- 224428298482 D19·S33·S17: "한국 입장에서 LNG공급선을 다양화할 필요성은 높아진 상황임." [observed] The front part of the same sentence gives the maritime blockade of that period as the reason [observed].

### F11: Stop the 앞쪽 chain once you have at least one money number, one Korea-side fact, and one next deadline [observed]
- Both posts have at least one F1 unit, one F2 unit, and one F6 unit each: 224450743987 D12·D14·D13, 224428298482 D08·D10·D14 [observed: units.md].
- 앞쪽 units were 8 to 9, which is 44 to 45% of the total (the classification in section 0) [inferred].

---

## R: Where 희귀 (rare) sources come from

- The `표시: 희귀` (label: rare) sources of the two remaining runs number 71: 224450743987 32, 224428298482 39 [observed: count of the `표시:` lines in sources.md].
- Only a few sources were in the domains of the top results of the ordinary search (평범한 검색: one Korean and one English search on the topic word): 7 in 224450743987 (S01·S17·S18·S37·S39·S40·S43) and 2 in 224428298482 (S08·S22) [observed].
- The type split below was made by this ledger, and each source is placed in only one type [inferred].

| id | Type | 224450743987 | 224428298482 | Total |
|---|---|---|---|---|
| R1 | Domestic articles (general, business, broadcast, wire, internet, and trade papers, including portal reprints) | 12: S02 S03 S04 S05 S07 S08 S10 S12 S13 S14 S42 S44 | 15: S01 S02 S03 S04 S12 S13 S14 S17 S19 S26 S27 S28 S52 S54 S55 | 27 [observed] |
| R2 | Foreign trade papers | 4: S19 S23 S26 S28 | 3: S16 S24 S25 | 7 [observed] |
| R3 | Foreign wires, broadcasters, and financial outlets (free reprints) | 0 | 6: S05 S06 S18 S23 S33 S51 | 6 [observed] |
| R4 | International bodies, industry associations, NGOs, institutional documents | 5: S21 S22 S27 S33 S34 | 1: S56 | 6 [observed] |
| R5 | Domestic public explainers, boards of state research institutes | 3: S06 S09 S11 | 1: S49 | 4 [observed] |
| R6 | Wikis | 2: S38 S41 | 2: S34 S35 | 4 [observed] |
| R7 | Data and original documents (election tables, fact sheets, original social posts) | 0 | 5: S29 S30 S31 S41 S42 | 5 [observed] |
| R8 | Local outlets and provincial-paper reprints of foreign wires | 1: S20 | 4: S07 S09 S15 S53 | 5 [observed] |
| R9 | Research and history materials | 3: S30 S31 S32 | 0 | 3 [observed] |
| R10 | Corporate press releases | 0 | 2: S20 S21 | 2 [observed] |
| R11 | Everyday-life sources (restaurant-review articles, reprints of columns) | 2: S15 S16 | 0 | 2 [observed] |
| | Total | 32 | 39 | 71 [observed] |

### R1: For each core fact, collect domestic articles that carry the same fact, outlet by outlet, and if an outlet's site is blocked, open the portal reprint [observed]
- 224428298482 S01 Probably reached via: "네이버 뉴스 (다음 게재본으로 확인)." [observed]
- 224450743987 S08 Probably reached via: "연도가 빠진 문장을 2026년 일로 읽은 점이 이 기사를 거쳤다는 근거." [observed]
- Reprints: daum.net (224428298482 S01·S17·S19, 224450743987 S05), koreadaily.com (224428298482 S13) [observed].
- Articles several years old also belong to this type: 224450743987 S13 (2017-02-13) and S14 (2019-07-19) [observed]. Articles based on an industry association's press release also belong: 224450743987 S12 (더퍼블릭) and S44 (인사이트, provided by the 노르웨이수산물위원회 (Norwegian Seafood Council)) [observed].

### R2: Find trade papers through the outlets that domestic articles name, or through searches with the numbers turned into English, and if paywalled, open the public abstract or a republished copy [observed]
- 224450743987 S19: "Whole Norwegian mackerel entering Japan directly faces a 7% tariff and fillets 10%" [observed]; the route is [unknown: no record].
- 224428298482 S16: "US energy firm Glenfarne expects both phases of the Alaska LNG project to cost up to $54.5 billion." [observed]

### R3: Open foreign wire stories through free reprints on trade sites, local newspapers, financial portals, and broadcasters, not on the original site [inferred]
- 224428298482 S18·S51·S33: opened Reuters as "EnergyNow 게재", "Business Recorder 게재", and "Arab News 게재" (published on EnergyNow, Business Recorder, and Arab News) [observed].
- 224428298482 S04 Match: "로이터는 규모가 540억달러(약 73조원)에 달한다고 전했다." This is the form in which a domestic article names the wire service [observed].

### R4: For product-market and regulation numbers, find the originals in market reports of international bodies, statements of trading partners' chambers of commerce, announcements of environmental groups, and explainer PDFs of institutions [observed]
- 224450743987 S21(FAO GLOBEFISH): "Whole mackerel from Norway faces a 7 percent tariff in Japan and fillets face a 10 percent tariff," [observed]
- 224450743987 S22 (PDF of the Norwegian chamber of commerce in Japan): "Current tariffs for Norwegian mackerel are 7% for whole round fish and 10% for fillet products." [observed]
- 224450743987 S27(Blue Marine Foundation): "This marks a 70% reduction from the catch limit recommended for 2025" [observed]
- 224428298482 S56 (PDF of the Federal Coordinator's office, held by ARLIS): "Before FID, spending on a project is typically less than 10 percent of total costs" [observed]

### R5: Find raw data and Korean-language editions of foreign trade papers in government ministries' rebuttal materials and in the overseas-trend boards of state research institutes [observed]
- 224450743987 S09 (정책브리핑 (Policy Briefing) "사실은 이렇습니다" (The facts are these)): "중･대형 고등어 누적 생산량(8월 14일 기준, 톤): (평년) 7,581, (2024년) 8,895 → (2025년) 2,806" [observed]
- 224450743987 S06·S11 (KMI 해양수산해외산업정보포털, an overseas maritime industry information portal): the originals are SeafoodSource and Undercurrent News, respectively [observed].
- 224428298482 S49: opened the 연합뉴스 article through the copy posted on the board of the 에너지경제연구원 (Korea Energy Economics Institute) [observed].

### R6: Open 나무위키, 위키백과, and AI wikis, and record the version date [observed]
- 224450743987 S38: confirmed with the Wayback versions of 2022-09-03 and 2026-05-27 [observed]. S41 (오늘의AI위키): "망치고등어는 식용, 낚시 미끼, 고양이 사료, 육류 결합제 등 다양한 용도로 활용된다." [observed]
- 224428298482 S34·S35: the last edit of the 위키백과 pages was before publication, so I labeled them [observed] [observed].

### R7: When the subject is an election or a leader's remarks, open the original documents directly (election forecast tables, government fact sheets, a leader's social posts) [inferred]
- 224428298482 S31 (270toWin): "The U.S. Senate has 53 Republicans and 47 Democrats (including two independents)." [observed] S29 (Fox News, 12 competitive seats), S30 (위키백과 2026 Senate election), S41 (White House fact sheet, UCSB copy), S42 (Truth Social, img_13 pixels) [observed]

### R8: Look for local outlets at the scene of the event (public broadcasters, local dailies) and provincial-paper reprints of foreign wires [observed]
- 224428298482 S09(Alaska Public Media): "three million tons short of the figure it has said it needs" [observed] S07·S53(Anchorage Daily News) [observed]
- 224450743987 S20: opened a Kyodo News article through its 琉球新報 reprint [observed].

### R9: Foreign industry history is in research reports, conference papers, and the history pages of port companies (B6) [inferred]
- 224450743987 S30(IIFET 2006): "the Atlanto-Scandian stock between Iceland and Norway from millions of tons to the border of extinction in a decade" [observed] S31(SNF)·S32(Nordfjord Havn) [observed]

### R10: Confirm contract volumes and terms in the original text of corporate press releases (press-release distribution sites, company newsrooms) [inferred]
- 224428298482 S20(Glenfarne, Business Wire·Yahoo Finance 게재): "Glenfarne intends to contract 80%, or 16 MTPA, of Alaska LNG's 20 MTPA volume to finance the project." [observed]
- 224428298482 S21 (TotalEnergies): "subject to the project's final investment decision." [observed] The route is "한국 기사(S19 등) 경유" (via a Korean article such as S19) [inferred].

### R11: The last unit of an everyday-topic post (where to eat) is in reprints of restaurant-introduction articles and newspaper restaurant columns [inferred]
- 224450743987 S15(핫플헌터): "부평동에 자리한 ‘유성실비’는 낮에는 고급스러운 고등어구이를, 저녁에는 신선한 선어회와 술을 곁들일 수 있는 특별한 생선구이 전문점이다." [observed]
- 224450743987 S16: a reprint, on the 한국기자협회 (Journalists Association of Korea) site, of a newspaper restaurant column [observed].

### R12: There are three ways to reach 희귀 sources: (a) follow the sources that domestic articles and posts name, (b) turn numbers and proper nouns into English or the local language and search, (c) use a long Korean query of two or three proper nouns followed by descriptive words [observed]
- (a): 224428298482 S20 "한국 기사(S19 등) 경유" (via a Korean article such as S19), 224450743987 S09 "S08이 인용" (S08 cites it) [observed]
- (b): 224450743987 S26: "320만 톤은 한국어 출처(S11)에 없어 영어 출처를 직접 읽었을 가능성이 큼." [inferred]
- (c): 224450743987 units.md: during the supplementary pass, the queries that reached S38–S44 were "나무위키 고등어 망치고등어 참고등어 점고등어" and "노르웨이 고등어 1년 내내 균일한 맛 가을 어획 급속 냉동 국산 참고등어 맛 편차" [observed]

### R13: Query templates. For each type, run at least one Korean query and one English query, rerun with the number written closed up, spaced, and with '천', and discard results later than `date:` [inferred]
- Basis for changing the notation: 224450743987 S01 Match shows that the post rewrote the source's "17만4357t" as "17만4,357톤" [observed].
- The `[ ]` in the templates below are slots to fill for the topic [observed].

| Type | Query template (brackets in the topic slots) | What it yields |
|---|---|---|
| R1 Domestic articles | `[주인공] [사건 핵심어]` (Naver News, period [사건일]~[date]) / `"[숫자 표기]" [주인공]` / `[주인공] [규모·예고·팩트체크]` (period [date−10일]~[사건일]) / `[주인공] [첫 파도 사건어]` (period [첫 파도일 ±14일]) / `[기사 제목 앞부분] [포털 이름]` / `1인당 [품목] [소비량·섭취량] [나라]` (no period) / `[업계 단체] 보도자료 [품목] [YYYY]` | Five or more outlets, setup articles, first-wave articles, reprints, old statistics, articles based on press releases [observed] |
| R2 Trade papers | `[영문 주인공] [영문 핵심어] [숫자] [Month YYYY]` / `"[국내 기사가 이름 댄 매체]" [영문 주인공]` / `[영문 주인공] [업종 영어] news [Month YYYY]` | Primary numbers, public abstracts, republished copies [observed] |
| R3 Wire reprints | `"[외신 제목 일부]"` / `[영문 주인공] [통신사] [핵심어] [Month YYYY]` | Free reprints [inferred] |
| R4 International bodies and associations | `[품목] market [국제기구] [YYYY]` / `[품목] consumption per capita [지역] [시장 관측 기관]` / `[교역국] chamber of commerce [품목] tariff statement` / `[권고 기관] advice [자원] [YYYY]` / `[품목] [감축률] [환경단체]` / `[결정 용어] explained [사업 종류] pdf` | Original tariff, quota, and recommended-level documents; explainer PDFs [observed] |
| R5 Domestic public bodies | `정책브리핑 사실은 이렇습니다 [사안]` / `[부처] 보도설명 [사안] [YYYY]` / `[분야 국책연구원] 해외 동향 [품목]` | Raw data tables, translations of foreign trade papers, reprints of articles [observed] |
| R6 Wiki | `[주제] 나무위키` / `[주제] 위키백과` / `[주제] 위키` (versions: Wayback snapshot before `[YYYYMMDD]`, 위키백과 revision history) | History chains, name origins, version dates [observed] |
| R7 Original texts | `[YYYY] [의회] elections` / `[지역] [선거] race ratings [Month YYYY]` / `Fact Sheet [정상] [국가] [방문·협정]` / `[정상] [소셜 서비스] [키워드] [날짜]` | Seat tables, original texts [inferred] |
| R8 Local | `[지역] public media [사안]` / `[지역 대표 일간지] [사안] [Month YYYY]` / `[행사·품목 현지어명] [도착·발표 현지어] [YYYY]` | On-site reports, foreign wire reprints [observed] |
| R9 Research and history | `collapse of the [국가] [자원] [산업]` / `[자원] [연대] crisis working paper` / `history of [산업] [항구·도시]` / `[사건] proceedings pdf` | Dates when an industry began or collapsed [inferred] |
| R10 Press releases | `[회사] press release [계약 상대] [YYYY]` / `[회사] [보도자료 배포 사이트] [사안]` / `[계약 상대] [물량] [사업명]` | Original text of contract volumes and terms [inferred] |
| R11 Everyday life | `[도시·동네] [음식] 맛집` / `[시장명] [음식] 백반` / `[가게 종류] [음식] 혼밥 [칼럼]` | Where to eat, and prices [inferred] |

---

## U: 바탕 (base) sources

- The `표시: 바탕` sources of the two remaining runs are 224450743987 S38 (나무위키 「고등어」) and 224428298482 S52 (이데일리 column), and neither is an author post [observed].
- units.md also recorded the author's earlier posts 224140130757 (224450743987 D15–D17) and 223755523008 (224428298482 D01–D10) as 바탕(저자 글) (base: the author's post) [observed].

### U1: The 바탕 is one document, and the author (in his earlier post) followed that document's chain and order as it was [observed]
- 224428298482 S52: "P1 #32–#41이 이 기사의 순서(1896년 금광 → 채플린 → 1967·1968 프루도베이 → 결빙 → 1977년 송유관 → 연방정부의 억제 → 별도 가스관)를 그대로 따른다." [observed]
- 224450743987 S38: "'일렬로', '점고등어라 불리곤 한다', '참고등어 맛이 떨어지는 여름철', '7~9월', '품종이라 … 수온이 높은 곳'이 1월 글 L22–34와 같은 순서로 겹친다" [inferred]

### U2: The 바탕 document came out before the author's earlier post (articles 11 days ahead, wikis in an earlier version), and well before this post's `date:` [inferred]
- 224428298482 S52: a column of 2025-01-31, and P1 is 2025-02-11 [observed].
- 224450743987 S38: the same sentences appear in the Wayback versions of 2022-09-03 and 2026-05-27, so I judge that they existed before the January post (2026-01-09) [inferred].

### U3: Keep the order of the 바탕 sentences and fix only the numbers with the latest domestic articles. Insert a new unit in its proper place on the chain, and attach the 계기 at the end [observed]
- 224428298482 research-path §3-1: "| #53 | #52 | 수정 | '파이프라인 건설비용 440억달러' → '파이프라인과 LNG설비등 전체 프로젝트의 건설비용 545억달러' |" [observed]
- 224450743987 research-path §3: "TAC "29만9000톤" → "29만9,010톤" (S01·S06의 정밀 수치), "48%" 추가" [observed]
- Inserting new units: 224450743987 D12–D14 are new units whose reuse column says '아니오' (no), and they went in between D11 and D15–D17, which the earlier post supplied [observed: units.md].

### U4: Prior-post slot (for replication). For the units that the author's earlier post supplied, find the 바탕 sources that post leaned on, instead of the post itself: ① the 나무위키 topic page (sections on types and history), ② long columns and features in Korean newspapers (serial columns from diplomatic missions abroad, "[주제]의 모든 것" features), ③ 위키백과 [observed]
- 224450743987 D15–D17 slot: S38 나무위키 「고등어」 (바탕); the alternatives are S39 (부산일보 feature of 2013), S41 (오늘의AI위키), and S42 (위키트리 October seasonal article) [observed].
- 224428298482 D03–D07 slot: S52 이데일리 「공관에서 온 편지」 column (바탕); the alternatives for D03–D04 are S34·S35 (위키백과) [observed].
- The replication worker cannot see the author's post, and leaving this slot empty loses those units from units_total in verification (verifier.md) [observed].

### U5: Confirm a wiki 바탕 with a version from before `date:`. If you cannot open the earlier version, use a pre-`date:` article or column that covers the same history as the 바탕 [observed]
- 224450743987 S38 Note: "1월 글 발행(2026-01-09) 시점의 판은 직접 보지 못했다. 나무위키 역사 페이지와 원문(raw) 경로는 자바스크립트로만 그려져 열리지 않았고," [observed]
- 224428298482 S46: "Why inferred: 받은 판이 두 글보다 늦음." [observed]

### U6: Prior-post slot map: the units the author's earlier posts supplied, and the outside sources that fill those slots [observed]

| Post | Author's earlier post | Units supplied | Outside sources for the slot |
|---|---|---|---|
| 224450743987 | 224140130757 (2026-01-09) | D09 (part)·D11 (part)·D15–D17 | D15–D17 S38(바탕)·S39·S40·S41·S42, D09 S43·S44, D11 S01–S06 [observed] |
| 224450743987 | 224272172681·223737564971 | D18 | S15·S16 [observed] |
| 224428298482 | 223755523008 (P1, 2025-02-11) | D01–D10 | D01–D02 S46·S47(inferred), D03–D07 S52(바탕)·S34·S35, D06 S53·S54, D08 S51, D09 S49, D10 S55 [observed] |
| 224428298482 | 224059473094·224058494349 (2025-10-30·31) | D15 | S41 (fact sheet)·S42 (social original) [observed] |

### U7: When there are several 바탕 candidates, pick as the skeleton the one that overlaps the post most in order and in distinctive wording (source fingerprints) [inferred]
- 224428298482 S48 Note: "(하원 표결은 113 대 43으로 알려져 있으나 S34와 P1이 같은 48을 씀 — 출처 지문. 새 글은 이 숫자를 지움.)" [observed]

---

## A: What the author adds (kinds of sentences that are not in the sources)

### A1: Put the foreign number next to the same kind of number for Korea (and Japan) [observed]
- 224428298482 D08: "57. 일본이 1년에 수입하는 LNG가 6,590만톤이라, 일본 입장에서도 2천만톤은 30% 비중으로 적지않은 규모임." [observed]
- 224450743987 D03·S14: "8. 한국이 연 2.8kg, 일본이 3kg인것에 비하면 고등어를 많이 먹지 않고 있음." [observed]

### A2: Do a one-step calculation of division, subtraction, or addition, and write only the result as an integer [inferred]
- 224428298482 research-path §5: "#56 43% = 20 ÷ 47 = 42.6%" / "#70·#72 300만톤 = 20 × 0.8 − 13 = 3" [observed]
- 224428298482 D17: "94. 민주당은 미선거 34석 + 안정권 9석 = 43석이 고정이라, 35석 중 양당 안정권 23석을 빼면 남는 경합은 12석"임." [observed]

### A3: Trim or round a source number and add "정도·거의·가까운·넘게" (about, nearly, close to, over) [inferred]
- 224428298482 D20: "전체 사업비 545억달러와 거의 같은 금액으로 액면대로 해석하면 100% 한국자금으로 전체 프로젝트를 건설한다는 의미가 됨." [observed]

### A4: Join facts from two sources into one interpretive sentence that is in neither ("결국 ~라는 말", "~수 있음") [observed]
- 224450743987 D06: "19. 결국, 노르웨이 고등어를 주로 먹는 곳은 한국과 일본이라는 말임." research-path §5 "C20(S17)과 C25–C28(S21·S19)을 합친 결론" (a conclusion joining C20 (S17) and C25–C28 (S21·S19)) [observed]
- 224428298482 D14: "80. 한국의 자금 투자와 LNG 추가구매 계약이 들어오면, 300만톤 문제와 공사비가 해결되어 FID를 선언하고 달리기 시작할 수 있음." [observed]

### A5: Compare it to a system or phenomenon familiar to Korean readers [inferred]
- 224428298482 D13: "76. FID는 부동산PF의 본PF와 비슷한 단계임." [observed] D17: "한국의 지역적인 몰표와 비슷하게" [observed]
- Exception: the analogies of 224450743987 ("보졸레 누보처럼", "진공청소기") were already in the sources S18 and S29 [observed: research-path §5].

### A6: Mark an estimate as an estimate ("뇌피셜로 추정하면" (if I guess from my own head), "전망임") [observed]
- 224428298482 D14: "81. 뇌피셜로 추정하면, 한국은 이미 300만톤 이상을 계약했을 수 있음." [observed]
- 224450743987 D13: "… 고등어 가격은 내년여름까지 비쌀 전망임." [observed]

### A7: The last line (the 한줄 코멘트, one-line comment) is one judgment that ties several sources together, plus one thing the reader can do or watch [observed]
- 224450743987 한줄 코멘트: "내년 여름까지 노르웨이 고등어가 비쌀 예정이니, 가성비 좋은 소형 참고등어를 먹는 것도 괜찮은 방법 같음." [observed]
- 224428298482 한줄 코멘트: "트럼프식의 과장이겠지만, 최종 협상과정에서 적절한 수준으로 조정되어야 할 것임." [observed]

### A8: Spell out abbreviations, foreign institution names, and terms in parentheses on first use [observed]
- 224428298482: "FID(Final Investment Decision,최종투자결정)", "미국 전략국제문제연구소(CSIS)" [observed]
- 224450743987: "국제해양탐사위원회(ICES)", "'사바 누보(Saba Nouveau)'" [observed]

### A9: The author sometimes changes a source's reference point or scope, but the replication keeps the source's reference as it is [observed]
- 224450743987 S07 Note: "출처는 '2026년 2월, 전년 동월 대비' 수치인데 본문은 연도 비교(2025년→2026년)처럼 썼음." [observed]
- 224428298482 S17 Note: "이 기사에서 80%(1,600만t) 조건은 2단계 터미널 자금 조건인데, 본문 #69는 "파이프라인이, 착공에 들어가기 위해서는"이라고 씀." [observed]
- Implication for replication: a sentence that was rewritten does not reach a source in research.md, so it can be counted as fabrication (verifier.md fabricated) [inferred]

---

## N: What the author does not do

- A general draft imagined for comparison: search the topic word, read the top results (English wiki, general explainers), open with the 계기 news, summarize a few lines of background, pros and cons, and outlook, quote numbers and sentences from English primary materials as in the original, and add a summary lead, subheadings, and reference links [inferred: imagined draft].

### N1: Do not run research that starts from the 계기 news and ends at the 계기. The 계기 comes at the end of the unit list, and the first quarter or so is history and origins from before the 계기 [observed]
- 224428298482 research-path §1: "계기 사건은 글 맨 끝에만 나오고, 앞쪽 65개 문장은 1년 8개월 전 P1을 다시 쓴 배경 설명임." [observed]
- 224450743987: has no 계기, and its first unit is D01 "청어의 나라 노르웨이와 청어 남획·붕괴" (Norway, the herring country, and the overfishing and collapse of herring) [observed]

### N2: Do not copy numbers and sentences straight from English primary materials. Use the number notation and translations of the domestic articles, and name foreign sources only as a name inside a sentence [observed]
- 224428298482 S09 Note: "트럼프가 입으로 한 말은 "more than $50 billion"이고 540억달러는 백악관 문서 수치." The post used the 540억달러 of the domestic article [observed]
- 224450743987 S01: "표기·문장 구조가 가장 강하게 일치하는 한국어 출처." The post's "17만4,357톤" follows the domestic article's notation, not the "174,357 tonnes" of S27 [observed]
- Exception: a number with no domestic intermediate source matches only the English source: 224450743987 S26 "320만 톤", 224428298482 S29 12 competitive seats [inferred].

### N3: Do not finish a fact cluster with one article. Pick quotations, number notation, and wording from several domestic articles of the same day [inferred]
- 224428298482 research-path §4: "일본 200만(S03, 10-01)·포스코 100만(S26 …)·프랑스 200만(S19 …)·대만 600만(S23)·태국 200만(S24)이 출처마다 흩어져 있음." [observed]

### N4: Do not add source links, references, footnotes, a summary lead, or subheadings [observed]
- The meta.json of both posts has "outbound_links": [] and link, quote, and rule at 0 in block_counts [observed].
- The opening lines are 224450743987 "불금이라 가벼운 내용입니다." and 224428298482 "늘 그렇듯이, 돌아갑니다." [observed: rek stats first_line].

### N5: Do not list pros, cons, and expert opinions and defer judgment. Close with one judgment, and from a critical article take only the numbers [observed]
- 224428298482 S14 title: "'비용 예상치 넘을 위험 커'…'알래스카 LNG' 수익성 회의론" (the risk of exceeding the cost estimate is large; skepticism about Alaska LNG's profitability). The post took only 545억달러, 1300만t, and France from this article (Claims C044·C063·C065) [observed]
- 224450743987 한줄 코멘트 (A7): ends with one judgment and one recommendation [observed].

### N6: Do not take raw data (statistics DBs, recommendation documents, original reports) and calculate anew. Use values that articles and press releases already gave, and make your own calculation only as one-step arithmetic (A2) [observed]
- 224450743987 S09 Probably reached via: "S08이 인용 (저자가 이 문서를 직접 읽었다는 증거 없음)." [observed]
- 224428298482 S27: "연간 2000만t 생산을 목표로 하고 있으며, 이는 일본 전체 수요의 30%에 해당한다." ↔ #57 [observed]

### N7: Do not make a separate unit of risk, opposing opinion, or environmental issues [inferred]
- 224428298482 units.md: among the 20 units there is none on the environment, indigenous people, or the risk of cost overruns, and the critical articles S03 and S14 were used only for numbers [observed: units.md, S03·S14 Claims].

### N8: Do not write investment solicitation, stock recommendations, or target prices [observed]
- The opinion claims in the claims.md of the two posts (11 and 10) contain no buy or sell call and no stock recommendation [observed].

### N9: Do not turn numbers into tables or charts. The pictures are stock photos, hand-marked maps and screen captures, captures of original text, generated pictures, and photos the author took himself [observed]
- 224428298482 img_12·img_14 are Gemini-generated, and img_13 is a Truth Social capture [observed].
- 224450743987 img_01–img_08 are OGQ stock photos and detailed illustrations, and img_09–img_12 are restaurant photos [observed: viewed the images].

### N10: Do not reveal or cite the author's own earlier post. Revive it [observed]
- Self-reference is 25/99 in 224450743987 and 55/109 in 224428298482, yet no sentence or link in the body points to the earlier post [observed: tally of claims.md, meta.json outbound_links].
- Implication for replication: the replication cannot see the earlier post, so fill that slot with U4 [observed].

### N11: Do not end the research with the top results of a single search on the topic word. Only 2 to 7 of the original-text sources per run were in the domains of those results [observed]
- 224450743987: 11 domains in the ordinary search, 7 sources within them, 32 희귀 [observed].
- 224428298482: 14 domains, 2 sources within them (S08·S22), 39 희귀 [observed].

---

## Tally

| Layer | Rules | [observed] | [inferred] |
|---|---|---|---|
| T 계기 | 6 (T1–T6) | 2 | 4 (T1·T2·T3·T4) |
| B 뒤쪽 expansion | 7 (B1–B7) | 6 | 1 (B6) |
| F 앞쪽 expansion | 10 (F1–F7·F9–F11) | 7 | 3 (F5·F9·F10) |
| R 희귀 sources | 13 (R1–R13) | 7 | 6 (R3·R7·R9·R10·R11·R13) |
| U 바탕 sources | 7 (U1–U7) | 5 | 2 (U2·U7) |
| A What the author adds | 9 (A1–A9) | 6 | 3 (A2·A3·A5) |
| N What the author does not do | 11 (N1–N11) | 9 | 2 (N3·N7) |
| Total | 63 | 42 | 21 |

- The count tallies the labels on the rule title lines [observed]. Rule ids are kept the same as in the original ledger, and the ids of rules with no remaining evidence are empty [observed]. The label of the "Total" column in the R type table means that sources were counted [observed].
- The three strongest N rules are N1, N2, and N11. All three have evidence in both remaining posts [inferred: judgment].

## unknowns

- The addresses of other subscription channels are not in the materials of the remaining runs [unknown: searched, not found].
- For most trade papers (R2), how the author reached them is not recorded [observed]. Which of search tools, translators, and AI research tools he used is also unknown (224450743987 research-path §6, 224428298482 research-path §6) [unknown].
- Where 224428298482 got the distances (7,500km, 11,700km) and the country-by-country volumes in one place is unknown [unknown: research-path §8].
- The classification of unit directions and the level split of B2 are this ledger's judgment [inferred].
