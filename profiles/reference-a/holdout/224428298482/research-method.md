author: reference-a
built_from: 224450743987, 224456106651
holdout: 224428298482

# the reference author research method: the rule ledger (holdout variant, rek-method-analyst, 2026-10-30)

## 0. How to read

- The header runs through the fourth line: `holdout:` is the id of the post that this variant removed from its evidence for the test [observed].
- The evidence of this variant is only the materials of the two runs in `built_from:`. It contains no unit numbers, source numbers, quotations, numbers, proper nouns, outlet names, queries, or format statistics from the holdout post [observed].
- The replication worker does not open profile files outside this folder. Opening one invalidates the holdout test [inferred: test design].
- The address of another subscription channel (for example, 네이버 프리미엄콘텐츠 (Naver Premium Content)) is not in the materials of the remaining runs, so none was added [unknown: searched, not found]. The replication worker also does not open any other channel that shows the author's name ('the reference author' (Mer)) or the blog name (researcher.md read ban) [observed].
- The evidence notation `224456106651 D14·S01` means unit D14 and source S01 of that post [observed]. Quotations are verbatim from post.md or from that run's tracking files, and are 40 words or fewer [observed].
- The label on a rule title line is the number of posts that supported the rule: [observed] for 2 posts, [inferred] for 1 post [observed]. The label on an evidence line is how the fact on that line was confirmed [observed].

| Post | main_topic | trigger | date | Units | Claims | 희귀 (rare) | 바탕 (base; author posts excluded) | Author's earlier posts |
|---|---|---|---|---|---|---|---|---|
| 224450743987 | 노르웨이 고등어와 국산 고등어 (Norwegian mackerel and domestic mackerel) | none | 2026-10-24 00:10 | 18 | 99 | 32 | 1 (S38) | 224140130757 and 2 others [observed] |
| 224456106651 | 장금상선의 호르무즈 해협 유조선 사업 (Jang Keum Marine's tanker business in the Strait of Hormuz) | 이란 당국의 장금상선 전 선박 법적 조치 경고 (Iranian authority's warning of legal action against all Jang Keum Marine ships) | 2026-10-28 11:00 | 17 | 59 | 33 (+S45 author post) | 0 | 224398051587 [observed] |

- Unit directions (뒤쪽 = backward, 본 주제 = main topic, 앞쪽 = forward, 계기 = trigger event; this ledger's classification): 224450743987 뒤쪽 D01·D02·D05·D07·D08, 본 주제 D09·D14–D17, 앞쪽 D03·D04·D06·D10–D13·D18, no 계기 [inferred]. 224456106651 뒤쪽 D02–D04, 본 주제 D01·D12·D13, 앞쪽 D05–D11·D17, 계기 D14–D16 [inferred].
- So 뒤쪽 is 18 to 28% of the units (3/17, 5/18) and 앞쪽 is 44 to 47% (8/18, 8/17) [inferred: count from the classification above].

---

## T: 계기

### T1: A news 계기 is an event in which a foreign government or institution singles out a Korean company [inferred]
- 224456106651 D14·S01: "이란 해협청은 10월 27일 X에 "시노코 해운회사 소속 선박들이 최근 3개월동안 가장 많은 통항 위반을 저질렀다"고 경고했다." [observed]
- Exception: 224450743987 has no 계기, and the head of its units.md reads "trigger: none" [observed]. In that case follow T4 [inferred].

### T2: A 계기 first appears on a foreign first channel (an institution's social account) and on the foreign wire services. Several domestic outlets then report it together on the same evening, and the post goes up within about 14 hours of the first domestic report [inferred]
- 224456106651 research-path §1: "한국일보 21:00(S04), 경향신문 21:07(S01), 재경일보 21:08(S08), 한겨레 21:12(S02), 아주경제 21:25(S07)이고, YTN(S05)과 머니투데이(S09)도 같은 날이다" [observed]
- 224456106651 research-path §1: "국내 첫 보도(한국일보 21:00)보다 14시간, 인용문이 글과 같은 경향 기사(S01)보다 13시간 53분 늦다" (14 hours later than the first domestic report, 13 hours 53 minutes later than the 경향 article S01 whose quotations match the post) [observed]. The English routes are S10 (Bloomberg, gCaptain reprint) and S13 (Reuters, Baird reprint) [observed].
- Exception: some posts were written before the domestic reports. The earlier post of 224456106651 (S45, 06:38) is earlier than the first domestic report S22 (08:08) [observed: S22 Probably reached via].

### T3: Within ten days before the 계기 there are "setup" (판 깔기) domestic articles on the same subject, and many of the numbers in the post come from them [inferred]
- 224456106651 D12·D16·S03 (연합뉴스 (Yonhap News) 2026-10-23 14:54): research-path §1 "7문단의 숫자는 거의 모두 이 기사에 있다" (almost all numbers of paragraph 7 are in this article) [observed]
- Exception: in a post with no 계기, the latest data article fills this slot (T4) [inferred]

### T4: The 계기 of a post without an event is the season and the series. The material is seasonal articles and the latest data articles from within 2 to 4 weeks of publication [inferred]
- 224450743987 para 0·D17: "불금이라 가벼운 내용입니다." / "53. 10월이 되면서 다시 참고등어 시즌이 오고 있음." [observed]
- 224450743987 D17·S42 (위키트리 2026-10-11, October seasonal seafood), D13·S11 (KMI 2026-10-06, the latest of the sources found) [observed]
- 224450743987 research-path §1: "'고등어 이야기' 연재의 세 번째 글로 보임" (appears to be the third post of the "고등어 이야기" (Mackerel Story) series) [inferred]

### T5: The main topic is one the author had already covered two to ten months earlier, and the material gathered during that "first wave" returns as background units in this post [observed]
- 224450743987: the 2026-01-09 post 224140130757 supplies D11 (in part) and D15–D17, and the original source of the quota number in the January post is presumed to be S02 (서울경제 2026-01-06) [observed: units.md reuse column / inferred: S02 Probably reached via].
- 224456106651: the 2026-09-02 post (S45) supplies seven consecutive units, D01–D07, and the wording of the domestic articles S22 (08:08) and S26 (10:53) from that morning entered this post [observed: S45 `표시:` (label) line, research-path §4].
- Implication for replication: the replication worker cannot see that earlier post but can find the first-wave articles and columns (U4) [inferred]

### T6: Writing happens in the few hours before publication (a 00:10 post was written the day before, an 11:00 post in the early hours of the same day), and English articles published in between also become material [observed]
- 224450743987 meta.json: images were uploaded from img_01 "2026-10-23T00:13:04+09:00" to img_12 "2026-10-23T07:57:36+09:00", and the post was published at 2026-10-24 00:10 [observed]
- 224456106651 meta.json: img_07 02:59:32, img_08 03:18:55, img_06 04:21:41 (10-28), and the post was published at 11:00 [observed]. D16·S14 (Maritime Executive, 10-28 02:40 KST): "has for the first time singled out one shipping company for “legal action.”" [observed]

---

## B: 뒤쪽 expansion (from the main topic to history, origin, and background)

### B1: For each subject (company, product), ask "how did it come to have its present owner and form?" and go down to the event where the answer starts (founding of the company, first catch) [observed]
- 224456106651 D03·S46·S47: "장금상선의 대표이사 였던 사람이 중국 지분을 사들여서 장금상선은 한국 국적사가 되었다." [observed]
- 224450743987 D02·S31: "4. 청어를 잡던 선단들은 일감을 잃었고, 이들이 새로 찾아낸 일감이 북해 고등어 였음." [observed]

### B2: After getting one answer, ask "why did that happen?" once more. The depth is 2 to 3 levels [observed]
- 224450743987 D02→D01: a two-level chain of North Sea mackerel → herring collapse [inferred: level split]. D01: "3. 1960년이 되자, 매년 수백만톤이 잡히던 청어가 멸종 직전까지 가게 된 것임." [observed]
- 224456106651 D04→D03→D02: a three-level chain of tanker buying-up → 1998 change of nationality → founding of the Korea-China joint venture [inferred: level split]. D03: "1998년 외환위기가 오자, 중국측이 장금상선에서 철수의향을 밝혔다." [observed]

### B3: Look for one line on the origin of a name or nickname [observed]
- 224456106651 D02·S46·S47: "장금상선의 앞글자 '장'은 중국의 장강(양쯔강)을 말하고, 뒷 글자 '금'은 한국의 금수강산에서 따왔다고 한다." [observed]
- 224450743987 D15·S38: "49. 망치고등어는 배와 등이 나뉘는쪽에 일렬로 점무늬가 주욱 있어서 점고등어라고 부르기도 함." [observed]

### B4: Where natural or geographic conditions decided an industry or an event, make those conditions a separate unit [observed]
- 224450743987 D07·S28: "21.북동대서양 고등어는 봄부터 초여름에 산란을 하고, 여름이 되면 플랑크톤과 작은 물고기를 찾아서 북쪽 노르웨이해로 올라옴." [observed]
- 224456106651 D13·S03·S18: "호르무즈해협을 통과하면 오만만에서 원유를 일반 유조선에 넘겨주고 있다." [observed]

### B5: 뒤쪽 sources are of four kinds: ① 나무위키 (Namuwiki) and Korean Wikipedia (위키백과) ② long columns and features in Korean newspapers ③ research and institutional materials on a foreign industry's history ④ the "연혁" (history) pages on company and institution homepages [observed]
- ①: 224450743987 S38(나무위키 「고등어」), 224456106651 S47(나무위키 「장금상선」)·S49(위키백과 「장금상선」) [observed]
- ②: 224456106651 S46(한국경제 front page 「유조선 쓸어담은 장금상선…세계 오일로드 단숨에 장악」), 224450743987 S39(부산일보 「[What] '국민 생선' 고등어의 모든 것」) [observed]
- ③: 224450743987 S30 (IIFET 2006 conference paper), S31 (SNF Working Paper), S32 (Nordfjord Havn "History of Fishery"), S33 (FAO expert meeting material) [observed]; this type appears in only one post [inferred].
- ④: 224456106651 S48 (장금상선 homepage "연혁"): "1989. 03 한중 합작 회사 ‘장금 유한공사’ 설립" [observed]; this type appears in only one post [inferred].

### B6: For a foreign industry history with no Korean material, go to English research reports, conference papers, and the history pages of port companies [inferred]
- 224450743987 D02·S32: "from the mid-60's from the ring net fishery of herring and mackerel in the North Sea" [observed]
- 224450743987 D02·S31: "The fishing fleet found substitute stocks, such as mackerel and capelin." [observed]

### B7: Stop when the next step no longer explains the present state of the main topic any better. Usually you stop at the first founding or first catch [observed]
- 224456106651 D02: "장금상선은 최초에 한중 합작회사로 설립되었다." [observed]
- 224450743987 D01: "1. 노르웨이는 청어의 나라였음." [observed]
- Size: 뒤쪽 units were 3 to 5, which is 18 to 28% of the total (the classification in section 0) [inferred].

---

## F: 앞쪽 expansion (from the main topic to money, supply chain, and the Korea angle)

### F1: Find the money number that answers "how much?" (freight, export value, import unit price) and compare it with the earlier value [observed]
- 224456106651 D10·S29: "전쟁전에는 한번 운송을 하면 200만달러 정도를 받았는데, 전쟁후 최고 2300~2500만달러까지 운임이 점프한 것이다." [observed]
- 224450743987 D12·S07: "36. 한국의 kg당 수입단가가 2025년 2.6달러에서 2026년 5.4달러로 두배가 넘게 오르는등 비싸게 받았기 때문임." [observed]

### F2: Look separately for Korea-side facts: Korea's annual consumption, the scope of responsibility of Koreans and the Korean government, and domestic substitutes [observed]
- 224456106651 D08·S22·S23: "장금상선 관련사가 재용선을 준 배라 한국인 선원은 타지 않았고, 한국 정부 관리 대상 선박도 아니다." [observed]
- 224450743987 D14·S08: "41. 국산 고등어 어획량 자체는 2025년보다 늘었지만, 중대형은 8,895톤에서 2,806톤으로 급감하고 있음." [observed]

### F3: Look for the supply chain route: who carries it where, intermediate processing and transshipment points, and tariffs [observed]
- 224450743987 D06·S21: "17. 베트남으로 무관세로 들어가서, 낮은 인건비로 가시등을 바르고, 필렛으로 손질한뒤에 일본에 무관세로 들어가고 있음." [observed]
- 224456106651 D13·S03: "이 선박들은 목적지까지 원유를 운송을 하는게 아니고, 호르무즈해협을 통과하면 오만만에서 원유를 일반 유조선에 넘겨주고 있다." [observed]

### F4: Find the body and conditions that set supply (recommending body, quota, actions by authorities) together with their numbers [observed]
- 224450743987 D11·S01·S27: "31. 국제해양탐사위원회(ICES)는 2026년 북동대서양 고등어 어획량을 17만4,357톤 이하로 줄이라고 권고함." [observed]
- 224456106651 D14·S01: "“모든 화물 소유주와 이해관계자 및 보험업자들에게 경고한다. 11월1일부터 이 회사의 모든 선박에 대해 법적 조치가 취해질 것이다"." [observed]

### F6: Close the 앞쪽 chain with when the next deadline or season comes and what changes by then [observed]
- 224450743987 D13·S11·S18: "39. 2027년 8월에 노르웨이가 고등어를 잡기 전까지는 2026년 냉동이 풀리고 있으니 고등어 가격은 내년여름까지 비쌀 전망임." [observed]
- 224456106651 D17·S41·S42: "11월 1일 이후 이런 배들의 통행이 완전히 막히면, 유가에 어떤 영향이 생길지도 지켜 볼 지점이다." [observed]

### F7: Go to foreign primary materials through the places that domestic articles name [observed]
- 224456106651 D12·S16: Probably reached via "S03·S02 경유" (via S03 and S02): a domestic article named it with "로이드 리스트는 … 덧붙였다" (Lloyd's List added ...) [observed: S03 Match / inferred: route]
- 224450743987 D14·S09: Probably reached via "S08이 인용" (S08 cites it): S08 named the raw data with "해양수산부에 따르면" (according to the Ministry of Oceans and Fisheries) [observed]

### F8: Look for both sides of the money: the side coming in (freight, sales) and the side going out (insurance, labor) [inferred]
- 224456106651 D11·S39·S40·S26: "운송시 배값의 10%에 가까운 전쟁보험료가 들어가고, 선원들에 대한 위험수당등 비용도 많이 들어가서 실수익은 좀 줄어들것이다." [observed]

### F11: Stop the 앞쪽 chain once you have at least one money number, one Korea-side fact, and one next deadline [observed]
- Both posts have at least one F1 unit, one F2 unit, and one F6 unit each: 224450743987 D12·D14·D13, 224456106651 D10·D08·D17 [observed: units.md].
- 앞쪽 units were 8 in both posts, which is 44 to 47% of the total (the classification in section 0) [inferred].

---

## R: Where 희귀 (rare) sources come from

- The `표시: 희귀` (label: rare) sources of the two remaining runs number 65: 224450743987 32, 224456106651 33 (excluding the author post S45) [observed: count of the `표시:` lines in sources.md].
- Only a few sources were in the domains of the top results of the ordinary search (평범한 검색: one Korean and one English search on the topic word): 7 in 224450743987 (S01·S17·S18·S37·S39·S40·S43) and 9 in 224456106651 (S03·S19·S22·S24·S27·S29·S30·S32·S41) [observed].
- The type split below was made by this ledger, and each source is placed in only one type [inferred].

| id | Type | 224450743987 | 224456106651 | Total |
|---|---|---|---|---|
| R1 | Domestic articles (general, business, broadcast, wire, internet, and trade papers, including portal reprints) | 12: S02 S03 S04 S05 S07 S08 S10 S12 S13 S14 S42 S44 | 14: S01 S02 S04 S05 S06 S07 S08 S23 S25 S26 S33 S35 S46 S50 | 26 [observed] |
| R2 | Foreign trade papers | 4: S19 S23 S26 S28 | 8: S12 S14 S16 S17 S21 S28 S31 S40 | 12 [observed] |
| R3 | Foreign wires and financial outlets (free reprints) | 0 | 5: S10 S13 S18 S34 S42 | 5 [observed] |
| R4 | International bodies, industry associations, and NGO documents | 5: S21 S22 S27 S33 S34 | 0 | 5 [observed] |
| R5 | Domestic public explainers, overseas-trend portal of state research institutes | 3: S06 S09 S11 | 0 | 3 [observed] |
| R6 | Wikis and company homepages | 2: S38 S41 | 3: S47 S48 S49 | 5 [observed] |
| R7 | Data and databases (ship DB, insurance premium quotes) | 0 | 2: S37 S39 | 2 [observed] |
| R8 | Local-language editions and provincial-paper reprints of foreign wires | 1: S20 | 1: S36 | 2 [observed] |
| R9 | Research and history materials | 3: S30 S31 S32 | 0 | 3 [observed] |
| R11 | Everyday-life sources (restaurant-review articles, reprints of columns) | 2: S15 S16 | 0 | 2 [observed] |
| | Total | 32 | 33 | 65 [observed] |

### R1: For each core fact, collect domestic articles that carry the same fact, outlet by outlet, and if an outlet's site is blocked, open the portal reprint [observed]
- 224456106651 S01 judgment: "PGSA 게시물을 인용한 국내 기사 8건(경향·한겨레·한국일보·YTN·뉴스핌·재경일보·아주경제·머니투데이)을 대조했다." [observed]
- 224450743987 S08 Probably reached via: "연도가 빠진 문장을 2026년 일로 읽은 점이 이 기사를 거쳤다는 근거." [observed]
- Reprints: daum.net (224450743987 S05), nate.com (224456106651 S05), supple.kr (224456106651 S02) [observed].
- Articles several years old also belong to this type: 224450743987 S13 (2017-02-13) and S14 (2019-07-19) [observed]. Articles based on an industry association's press release also belong: 224450743987 S12 (더퍼블릭) and S44 (인사이트, provided by the 노르웨이수산물위원회 (Norwegian Seafood Council)) [observed].

### R2: Find trade papers through the outlets that domestic articles name, or through searches with the numbers turned into English, and if paywalled, open the public abstract or a republished copy [observed]
- 224456106651 S16 (paywalled, abstract only): "with its vessels accounting for 47% of September transits and more than half during the first 10 days of October" [observed]; the route is "S03·S02 경유" (via S03 and S02) [inferred].
- 224450743987 S19: "Whole Norwegian mackerel entering Japan directly faces a 7% tariff and fillets 10%" [observed]; the route is [unknown: no record].

### R3: Open foreign wire stories through free reprints on trade sites, local newspapers, and financial portals, not on the original site [inferred]
- 224456106651 S10: opened the Bloomberg article as "gCaptain 전재 07:12 PDT" (gCaptain reprint) [observed]. S13 opened a Reuters article through a Baird Maritime reprint, and S34 through a financial portal reprint [observed].

### R4: For product-market and regulation numbers, find the originals in market reports of international bodies, statements of trading partners' chambers of commerce, and announcements of environmental groups [inferred]
- 224450743987 S21(FAO GLOBEFISH): "Whole mackerel from Norway faces a 7 percent tariff in Japan and fillets face a 10 percent tariff," [observed]
- 224450743987 S22 (PDF of the Norwegian chamber of commerce in Japan): "Current tariffs for Norwegian mackerel are 7% for whole round fish and 10% for fillet products." [observed]
- 224450743987 S27(Blue Marine Foundation): "This marks a 70% reduction from the catch limit recommended for 2025" [observed]

### R5: Find raw data and Korean-language editions of foreign trade papers in government ministries' rebuttal materials and in the overseas-trend portal of state research institutes [inferred]
- 224450743987 S09 (정책브리핑 (Policy Briefing) "사실은 이렇습니다" (The facts are these)): "중･대형 고등어 누적 생산량(8월 14일 기준, 톤): (평년) 7,581, (2024년) 8,895 → (2025년) 2,806" [observed]
- 224450743987 S06·S11 (KMI 해양수산해외산업정보포털, an overseas maritime industry information portal): the originals are SeafoodSource and Undercurrent News, respectively [observed].

### R6: Open 나무위키, 위키백과, AI wikis, and the "연혁" (history) pages of company homepages, and record the version date [observed]
- 224450743987 S38: confirmed with the Wayback versions of 2022-09-03 and 2026-05-27 [observed]. S41 (오늘의AI위키): "망치고등어는 식용, 낚시 미끼, 고양이 사료, 육류 결합제 등 다양한 용도로 활용된다." [observed]
- 224456106651 S47 (나무위키 연혁 section), S48 (homepage 연혁), S49 (위키백과) [observed]

### R7: When the subject is a ship, open the database screen (the ownership and management fields of a ship DB) and the insurance premium quotes directly [inferred]
- 224456106651 S37 (MagicPort): "HAUT BRION 11 SA is the registered owner of SENEGAL PROSPERITY." [observed] S39 (SunSirs Korean edition): "전쟁 위험 보험료가 선박 가치의 10% 까지 급증했으며" [observed]

### R8: Look for local-language editions of foreign outlets and provincial-paper reprints of foreign wires [observed]
- 224456106651 S36 (Forbes México): "Según Equasis, 31 de los buques no pertenecen a Sinokor, sino a empresas que comparten el nombre “Haut Brion”, seguido de un número." [observed] The post named it with "포브스가 … 추적해 보니" (when Forbes traced ...), and I could not find the English original [observed: S36 URL line].
- 224450743987 S20: opened a Kyodo News article through its 琉球新報 reprint [observed].

### R9: Foreign industry history is in research reports, conference papers, and the history pages of port companies (B6) [inferred]
- 224450743987 S30(IIFET 2006): "the Atlanto-Scandian stock between Iceland and Norway from millions of tons to the border of extinction in a decade" [observed] S31(SNF)·S32(Nordfjord Havn) [observed]

### R11: The last unit of an everyday-topic post (where to eat) is in reprints of restaurant-introduction articles and newspaper restaurant columns [inferred]
- 224450743987 S15(핫플헌터): "부평동에 자리한 ‘유성실비’는 낮에는 고급스러운 고등어구이를, 저녁에는 신선한 선어회와 술을 곁들일 수 있는 특별한 생선구이 전문점이다." [observed]
- 224450743987 S16: a reprint, on the 한국기자협회 (Journalists Association of Korea) site, of a 경향신문 restaurant column [observed].

### R12: There are three ways to reach 희귀 sources: (a) follow the sources that domestic articles and posts name, (b) turn numbers and proper nouns into English or the local language and search, (c) use a long Korean query of two or three proper nouns followed by descriptive words [observed]
- (a): 224456106651 S16 "S03·S02 경유" (via S03 and S02), 224450743987 S09 "S08이 인용" (S08 cites it) [observed]
- (b): 224450743987 S26: "320만 톤은 한국어 출처(S11)에 없어 영어 출처를 직접 읽었을 가능성이 큼." [inferred]
- (c): 224450743987 units.md: during the supplementary pass, the queries that reached S38–S44 were "나무위키 고등어 망치고등어 참고등어 점고등어" and "노르웨이 고등어 1년 내내 균일한 맛 가을 어획 급속 냉동 국산 참고등어 맛 편차" [observed]

### R13: Query templates. For each type, run at least one Korean query and one English query, rerun with the number written closed up, spaced, and with '천', and discard results later than `date:` [inferred]
- Basis for changing the notation: 224456106651 S02 "'천' 없이 쓴 "2억8630만"과 "(9730만 배럴)"이 글과 같은 표기다(연합 원문은 "2억8천630만", "9천730만")." (the notation without '천' matches the post; the Yonhap original uses '천') [observed]
- The `[ ]` in the templates below are slots to fill for the topic [observed].

| Type | Query template (brackets in the topic slots) | What it yields |
|---|---|---|
| R1 Domestic articles | `[주인공] [사건 핵심어]` (Naver News, period [사건일]~[date]) / `"[숫자 표기]" [주인공]` / `[주인공] [점유율·규모]` (period [date−10일]~[사건일]) / `[주인공] [첫 파도 사건어]` (period [첫 파도일 ±14일]) / `[기사 제목 앞부분] [포털 이름]` / `1인당 [품목] [소비량·섭취량] [나라]` (no period) / `[업계 단체] 보도자료 [품목] [YYYY]` | Five or more outlets, setup articles, first-wave articles, reprints, old statistics, articles based on press releases [observed] |
| R2 Trade papers | `[영문 주인공] [영문 핵심어] [숫자] [Month YYYY]` / `"[국내 기사가 이름 댄 매체]" [영문 주인공]` / `[영문 주인공] [업종 영어] news [Month YYYY]` | Primary numbers, public abstracts, republished copies [observed] |
| R3 Wire reprints | `"[외신 제목 일부]"` / `[영문 주인공] [통신사] [핵심어] [Month YYYY]` | Free reprints [inferred] |
| R4 International bodies and associations | `[품목] market [국제기구] [YYYY]` / `[품목] consumption per capita [지역] [시장 관측 기관]` / `[교역국] chamber of commerce [품목] tariff statement` / `[권고 기관] advice [자원] [YYYY]` / `[품목] [감축률] [환경단체]` | Original tariff, quota, and recommended-level documents [inferred] |
| R5 Domestic public bodies | `정책브리핑 사실은 이렇습니다 [사안]` / `[부처] 보도설명 [사안] [YYYY]` / `[분야 국책연구원] 해외 동향 [품목]` | Raw data tables, translations of foreign trade papers [inferred] |
| R6 Wiki and history | `[주제] 나무위키` / `[주제] 위키백과` / `[주제] 위키` / `[회사] 연혁` / `[회사 영문명] history` (versions: Wayback snapshot before `[YYYYMMDD]`, 위키백과 revision history) | History chains, name origins, version dates [observed] |
| R7 Databases | `[선박·기체 이름] IMO owner manager` / `[항로] war risk premium [Month YYYY]` | Ownership and management fields, rates [inferred] |
| R8 Local-language and reprints | `[매체명] [현지어 핵심어] [주인공]` / `[행사·품목 현지어명] [도착·발표 현지어] [YYYY]` | Investigative reports whose English edition is blocked, foreign wire reprints [observed] |
| R9 Research and history | `collapse of the [국가] [자원] [산업]` / `[자원] [연대] crisis working paper` / `history of [산업] [항구·도시]` / `[사건] proceedings pdf` | Dates when an industry began or collapsed [inferred] |
| R11 Everyday life | `[도시·동네] [음식] 맛집` / `[시장명] [음식] 백반` / `[가게 종류] [음식] 혼밥 [칼럼]` | Where to eat, and prices [inferred] |

---

## U: 바탕 (base) sources

- The `표시: 바탕` sources of the two remaining runs are 224450743987 S38 (나무위키 「고등어」) and 224456106651 S45 (author post) [observed]. Without the author post there is one [observed].
- units.md also recorded the author's earlier post 224140130757 (224450743987 D15–D17) as 바탕(저자 글) (base: the author's post) [observed].

### U1: The 바탕 is one document, and the author (in his earlier post) followed that document's chain and order as it was [inferred]
- 224450743987 S38: "'일렬로', '점고등어라 불리곤 한다', '참고등어 맛이 떨어지는 여름철', '7~9월', '품종이라 … 수온이 높은 곳'이 1월 글 L22–34와 같은 순서로 겹친다" [inferred]

### U2: The 바탕 document came out before the author's earlier post (articles 6 months ahead, wikis in an earlier version), and well before this post's `date:` [inferred]
- 224456106651 S46: an article of 2026-03-10, and the earlier post S45 is 2026-09-02 [observed]. The S46 note says that adding C12 makes three consecutive units, D02–D04, and that it becomes a 바탕 [inferred: S46 note].
- 224450743987 S38: the same sentences appear in the Wayback versions of 2022-09-03 and 2026-05-27, so I judge that they existed before the January post (2026-01-09) [inferred].

### U3: Keep the order of the 바탕 sentences and fix only the numbers with the latest domestic articles. Insert a new unit in its proper place on the chain, and attach the 계기 at the end [observed]
- 224450743987 research-path §3: "TAC "29만9000톤" → "29만9,010톤" (S01·S06의 정밀 수치), "48%" 추가" [observed]
- 224456106651 research-path §3 table 19: changed the earlier post's "선박 중개인들의 추정" to "로이드 리스트 데이터로는 9월 … 47%" [observed].
- Inserting new units: 224456106651 D08 (Korean crew and government) and D11 (insurance premium) are new units whose reuse column says '아니오' (no), and they went in after the ownership structure and after the freight rates [observed: units.md].

### U4: Prior-post slot (for replication). For the units that the author's earlier post supplied, find the 바탕 sources that post leaned on, instead of the post itself: ① the 나무위키 topic page (sections on types and chronology), ② long columns and features in Korean newspapers (front-page features of business dailies, "[주제]의 모든 것" features), ③ 위키백과 and the 연혁 of company homepages [observed]
- 224450743987 D15–D17 slot: S38 나무위키 「고등어」 (바탕); the alternatives are S39 (부산일보 feature of 2013), S41 (오늘의AI위키), and S42 (위키트리 October seasonal article) [observed].
- 224456106651 D02–D03 slot: S46 (한국경제 article of 2026-03-10), S47 (나무위키 「장금상선」 연혁), S48 (homepage), S49 (위키백과) [observed].
- The replication worker cannot see the author's post, and leaving this slot empty loses those units from units_total in verification (verifier.md) [observed].

### U5: Confirm a wiki 바탕 with a version from before `date:`. If you cannot open the earlier version, use a pre-`date:` article or column that covers the same history as the 바탕 [observed]
- 224450743987 S38 Note: "1월 글 발행(2026-01-09) 시점의 판은 직접 보지 못했다. 나무위키 역사 페이지와 원문(raw) 경로는 자바스크립트로만 그려져 열리지 않았고," [observed]
- 224456106651 U14: "웨이백 CDX 조회(2026-01-01~09-02)는 빈 결과였고, 가용성 API는 429였다." [observed]

### U6: Prior-post slot map: the units the author's earlier posts supplied, and the outside sources that fill those slots [observed]

| Post | Author's earlier post | Units supplied | Outside sources for the slot |
|---|---|---|---|
| 224450743987 | 224140130757 (2026-01-09) | D09 (part)·D11 (part)·D15–D17 | D15–D17 S38(바탕)·S39·S40·S41·S42, D09 S43·S44, D11 S01–S06 [observed] |
| 224450743987 | 224272172681·223737564971 | D18 | S15·S16 [observed] |
| 224456106651 | 224398051587 (S45, 2026-09-02) | D01–D07·D09·D10·D12 (part) | D01 S21·S22, D02–D03 S46–S49, D04 S27·S28·S30·S31, D05 S33–S35, D06 S36, D07 S37, D09 S50, D10 S28·S29 [observed] |

### U7: When there are several 바탕 candidates, pick as the skeleton the one that overlaps the post most in order and in distinctive wording (source fingerprints) [inferred]
- 224456106651 S47 note: "'한중 합작회사', '철수', '사들여', '국적선사', '대표'가 글과 같은 말이고, S46에는 없는 표현이다" [observed]

---

## A: What the author adds (kinds of sentences that are not in the sources)

### A1: Put the foreign number next to the same kind of number for Korea (and Japan) [inferred]
- 224450743987 D03·S14: "8. 한국이 연 2.8kg, 일본이 3kg인것에 비하면 고등어를 많이 먹지 않고 있음." [observed]
- Exception: 224456106651 has no comparison with Korean numbers and compares with the competitors' sum: D16 "2~4위인 바흐리,쿠웨이트석유탱커,ADNOC를 합친 물량(9730만 배럴)보다 많다." [observed]

### A2: Do a one-step calculation of division, subtraction, or addition, and write only the result as an integer [inferred]
- 224456106651 research-path §5: "척당 매입가 약 8,120만 달러(5,925÷73, S30)를 1회 운임 2,300~2,500만 달러(S29)로 나누면 3.2~3.5회다" (dividing the purchase price per ship by the freight of one trip gives 3.2 to 3.5 trips). The post says "서너번 왕복하면" (if it makes three or four round trips) [inferred]

### A3: Trim or round a source number and add "정도·가까운·넘게" (about, close to, over) [inferred]
- 224456106651 D04: "중고 유조선 73척을 59억 달러에 사들인 것이다." This is a trimmed value of the "USD 5,925 mil" in S30 [inferred: research-path §5].

### A4: Join facts from two sources into one interpretive sentence that is in neither ("결국 ~라는 말", "~로 보인다") [observed]
- 224450743987 D06: "19. 결국, 노르웨이 고등어를 주로 먹는 곳은 한국과 일본이라는 말임." research-path §5 "C20(S17)과 C25–C28(S21·S19)을 합친 결론" (a conclusion joining C20 (S17) and C25–C28 (S21·S19)) [observed]
- 224456106651 D15: "11월 1일부터 장금상선 소속 모든 선박에게 이런 공격이 있을 수 있다고 경고하는 것으로 보인다." This joined the PGSA's '조치' (action) and Lloyd's '7척 피격' (7 ships hit) [observed: research-path §5].

### A6: Mark an estimate as an estimate ("예상된다", "전망임") [observed]
- 224456106651 D09: "시노코와 MSC간에 위험과 손익 배분 계약내용은 비공개라서 알 수 없지만, 수익을 나누는 구조로 예상된다." [observed]
- 224450743987 D13: "… 고등어 가격은 내년여름까지 비쌀 전망임." [observed]

### A7: The last line (the 한줄 코멘트, one-line comment) is one judgment that ties several sources together, plus one thing the reader can do or watch [observed]
- 224450743987 한줄 코멘트: "내년 여름까지 노르웨이 고등어가 비쌀 예정이니, 가성비 좋은 소형 참고등어를 먹는 것도 괜찮은 방법 같음." [observed]
- 224456106651 한줄 코멘트: "11월 1일 이후 이런 배들의 통행이 완전히 막히면, 유가에 어떤 영향이 생길지도 지켜 볼 지점이다." [observed] research-path §4: "두 생각을 한 문장으로 묶은 출처는 없다." [observed]

### A8: Spell out abbreviations, foreign institution names, and terms in parentheses on first use [observed]
- 224456106651: "VLCC(초대형유조선)", "SPC(특수목적법인)", "PGSA(이란 페르시아만 해협청)", "AIS(위치식별장치)" [observed]
- 224450743987: "국제해양탐사위원회(ICES)", "'사바 누보(Saba Nouveau)'" [observed]

### A9: The author sometimes changes a source's reference point in time, but the replication keeps the source's reference as it is [inferred]
- 224450743987 S07 Note: "출처는 '2026년 2월, 전년 동월 대비' 수치인데 본문은 연도 비교(2025년→2026년)처럼 썼음." [observed]
- Implication for replication: a sentence that was rewritten does not reach a source in research.md, so it can be counted as fabrication (verifier.md fabricated) [inferred]

---

## N: What the author does not do

- A general draft imagined for comparison: search the topic word, read the top results (English wiki, general explainers), open with the 계기 news, summarize a few lines of background, pros and cons, and outlook, quote numbers and sentences from English primary materials as in the original, and add a summary lead, subheadings, and reference links [inferred: imagined draft].

### N1: Do not run research that starts from the 계기 news and ends at the 계기. The 계기 comes at the end of the unit list, and the first quarter or so is history and origins from before the 계기 [observed]
- 224456106651 D14: "이란이 가만히 있지 않았다.", which turns to the 계기, is sentence 35 of 46 (76%) [observed: rek sentence splitting]
- 224450743987: has no 계기, and its first unit is D01 "청어의 나라 노르웨이와 청어 남획·붕괴" (Norway, the herring country, and the overfishing and collapse of herring) [observed]

### N2: Do not copy numbers and sentences straight from English primary materials. Use the number notation and translations of the domestic articles, and name foreign sources only as a name inside a sentence [observed]
- 224456106651 S18 note: "본문은 "almost 40%"라고 썼고 286.3백만 배럴과 37%는 없다 … 글의 37%와 2억8630만은 S03 계열 수치다" [observed]
- 224450743987 S01: "표기·문장 구조가 가장 강하게 일치하는 한국어 출처." The post's "17만4,357톤" follows the domestic article's notation, not the "174,357 tonnes" of S27 [observed]
- Exception: a number with no domestic intermediate source matches only the English source: 224450743987 S26 "320만 톤" [inferred].

### N3: Do not finish a fact cluster with one article. Pick quotations, number notation, and wording from several domestic articles of the same day [inferred]
- 224456106651 research-path §4: "인용문 3개는 경향(S01)과 글자까지 같다. '천' 없는 숫자 표기 "2억8630만", "(9730만 배럴)"은 한겨레(S02)와 같다." [observed]

### N4: Do not add source links, references, footnotes, a summary lead, or subheadings [observed]
- The meta.json of both posts has "outbound_links": [] and link, quote, and rule at 0 in block_counts [observed].
- The opening lines are 224450743987 "불금이라 가벼운 내용입니다." and 224456106651 "2026년 8월 31일, 사우디의 원유를 실은 VLCC(초대형유조선) 두척이 호르무즈 해협을 빠져나가다가 피격되었다." [observed: rek stats first_line].

### N5: Do not list pros, cons, and expert opinions and defer judgment. Close with one judgment [observed]
- 224456106651 D16: "이란의 메인 타깃이 될만한 비중이다." [observed]
- 224450743987 한줄 코멘트 (A7): ends with one judgment and one recommendation [observed].

### N6: Do not take raw data (statistics DBs, recommendation documents, original reports) and calculate anew. Use values that articles and press releases already gave, and make your own calculation only as one-step arithmetic (A2) [observed]
- 224450743987 S09 Probably reached via: "S08이 인용 (저자가 이 문서를 직접 읽었다는 증거 없음)." [observed]
- 224456106651 research-path §5: "37%와 78%는 출처에 있는 값이다(검산: 105.6÷286.3 = 36.9%, 35÷45 = 77.8%)." [observed]

### N8: Do not write investment solicitation, stock recommendations, or target prices [observed]
- The opinion claims in the claims.md of the two posts (11 and 6) contain no buy or sell call and no stock recommendation [observed].

### N9: Do not turn numbers into tables or charts. The pictures are stock photos, hand-marked maps and screen captures, generated pictures, and photos the author took himself [observed]
- 224456106651 img_07: "MarineTraffic 실시간 지도 캡처 … 작성자가 빨간 선을 그었다." [observed: sources.md §1]
- 224450743987 img_01–img_08 are OGQ stock photos and detailed illustrations, and img_09–img_12 are restaurant photos [observed: viewed the images].

### N10: Do not reveal or cite the author's own earlier post. Revive it [observed]
- Self-reference is 25/99 in 224450743987 and 31/59 in 224456106651, yet no sentence or link in the body points to the earlier post [observed: tally of claims.md, meta.json outbound_links].
- Implication for replication: the replication cannot see the earlier post, so fill that slot with U4 [observed].

### N11: Do not end the research with the top results of a single search on the topic word. Only 7 to 9 of the original-text sources per run were in the domains of those results [observed]
- 224450743987: 11 domains in the ordinary search, 7 sources within them, 32 희귀 [observed].
- 224456106651: 14 domains, 9 sources within them, 33 희귀 (author post excluded) [observed].

---

## Tally

| Layer | Rules | [observed] | [inferred] |
|---|---|---|---|
| T 계기 | 6 (T1–T6) | 2 | 4 (T1·T2·T3·T4) |
| B 뒤쪽 expansion | 7 (B1–B7) | 6 | 1 (B6) |
| F 앞쪽 expansion | 8 (F1–F4·F6–F8·F11) | 7 | 1 (F8) |
| R 희귀 sources | 12 (R1–R9·R11–R13) | 5 | 7 (R3·R4·R5·R7·R9·R11·R13) |
| U 바탕 sources | 7 (U1–U7) | 4 | 3 (U1·U2·U7) |
| A What the author adds | 8 (A1–A4·A6–A9) | 4 | 4 (A1·A2·A3·A9) |
| N What the author does not do | 10 (N1–N6·N8–N11) | 9 | 1 (N3) |
| Total | 58 | 37 | 21 |

- The count tallies the labels on the rule title lines [observed]. Rule ids are kept the same as in the original ledger, and the ids of rules with no remaining evidence are empty [observed]. The label of the "Total" column in the R type table means that sources were counted [observed].
- The three strongest N rules are N1, N2, and N11. All three have evidence in both remaining posts [inferred: judgment].

## unknowns

- The addresses of other subscription channels are not in the materials of the remaining runs [unknown: searched, not found].
- The sources.md of 224456106651 marks the author post S45 as `희귀, 바탕(저자 글)`, which under the verifier.md counting method makes rare_total 34 [observed]. Whether to align the marking needs checking during back-tracing [inferred].
- For most trade papers (R2), how the author reached them is not recorded [observed]. Which of search tools, translators, and AI research tools he used is also unknown (224450743987 research-path §6) [unknown].
- The classification of unit directions and the level split of B2 are this ledger's judgment [inferred].
