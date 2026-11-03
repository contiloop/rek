# Where things stand

## Built (verified)

- 10 Python commands (`fetch`, `prior`, `stats`, `repro-stats`, `profile-hash`, `source-sites`, `verify-summary`, `research-init`, `research-summary`, `compare-summary`). 70 tests pass. The Naver Blog adapter is tested against real saved pages.
- Plugin structure (`.claude-plugin/plugin.json`, `marketplace.json`, `skills/rek/`, `skills/research/`, `agents/`). `claude plugin validate` passes. One orchestrator agent and seven worker agents (source tracer, method analyst, researcher, verifier, topic researcher, topic checker, comparator); model and effort in each definition are defaults (`opus`, `high`).
- Two orchestrator skills and seven worker briefs plus `evidence.md`.
- Source tracing of the reference author's 4 posts: 99, 59, 109 and 104 claims; 18, 17, 20 and 20 development units; 44, 50, 56 and 19 sources; 3, 11, 8 and 3 prior posts by the author.
- Reference-author profile (`reference-a`), rebuilt at the level of the author's moves from the 4 traced posts: 58 rules (trigger 4, backward 7, forward 11, rare 13, base 5, additions 10, not-do 8), all free of the material posts' nouns, each tried on two unrelated topics; the backward and forward stop rules (B7, F11) reach as far as the farthest unit of every material post; `instances.md` as hints; `writing-structure.md` as moves without measured values; `SKILL.md` of 106 lines. `profile_hash` fe7b2c5cf535 (sha256 over SKILL.md + research-method.md + instances.md). The hold-out variants are gone.
- Round 1 and round 2 reproductions and scorings of the three material posts with the previous profile (kept in `runs/<id>/repro/1`, `repro/2`).
- The product entry `/rek:research` (skill, two worker briefs and agents, `research/<date>-<slug>/` folder, `check.md` contract, pass line by code). Not yet run on a real topic.
- The test-only path for a new post: fetch, four start lines written by the orchestrator, reproduction, comparison by `rek-comparator` (13 keys, depth per direction, failure routing), pass line by `rek compare-summary` (valid, fabricated 0, backward and forward depth at least the original's; exit 1 on any fail), at most three attempts per post with the responsible stage fixed between attempts.

## Test results

### Previous profile (64 instance-level rules; workers at maximum effort; scored by the source-based verifier)

| Post | Attempt | Units | Rare | Foundation | Fabrication | Reference-author criteria | Our criteria |
|---|---|---|---|---|---|---|---|
| 고등어 (Godeungeo) | Round 1 | 9/18 | 11/32 | 1/1 | 2 | Fail | Fail (fabrication: image descriptions) |
| 장금상선 (Janggeum Sangseon) | Round 1 | 10/17 | 19/33 | 0/0 | 0 | Fail | Pass |
| 알래스카 (Alaska) | Round 1 | 8/20 | 12/39 | 0/1 | 0 | Fail | (summary format unsupported) |
| 고등어 | Round 2 (hold-out) | 4/18 | 5/32 | 1/1 | 1 | Fail | Fail (fabrication: one image description) |
| 장금상선 | Round 2 (hold-out) | 7/17 | 16/33 | 0/0 | 0 | Fail | Pass |
| 알래스카 | Round 2 (hold-out) | 3/20 | 4/39 | 0/1 | 0 | Fail | Pass |

Failure responsibility (round 1 total): method extraction 54, reproduction 38, source tracing 1. Round 2 total: method extraction 77, reproduction 43, source tracing 2. Round-2 `profile_hash` values (41bef398f6a9, e2d6a98b6492, f81f88df16ab) identify the Korean profile files at commit 3c96656. The round 1 to round 2 drop (9→4, 10→7, 8→3 units) measured how much the un-held-out profile had leaked.

### Generalized profile (53 move-level rules; workers at effort high; two new posts, compared on the final post, no source matching)

`uv run rek compare-summary runs/` as printed at that time (the command's line format changed in the depth cycle; these files now print as "old format, no verdict"):

```
223137359486 | units 6/22 | facts 16/142 (conflict 7) | fabricated 5 | depth 17→12 | extra 11 | valid | cb903f4d4ad0
224314709934 | units 11/24 | facts 21/101 (conflict 2) | fabricated 6 | depth 20→17 | extra 15 | valid | cb903f4d4ad0
```

| Post | Date | Reproduction | Comparison |
|---|---|---|---|
| 컨테이너가 바꾼 역사와 부산항 이야기 (224314709934) | 2026-06-14 | 19 units (8 back, 5 main, 5 forward, 1 trigger), 39 sources (6 primary), 0 contacts | covers 11 of 24 original units; 21 of 101 facts same, 2 different; 6 unsourced facts ("first"/"largest" qualifiers, a Japanese-cargo label, alliance members); misses the trucking fines, the Vietnam War logistics, why shippers stayed; adds carriers, alliances, port fees, the Arctic route |
| 희토류 전쟁 근황 업데이트 3 (223137359486) | 2023-06-26 | 17 units (7 back, 3 main, 6 forward, 1 trigger), 39 sources (13 primary), 5 contacts (date checks only), 0 invalid | covers 6 of 22 original units; 16 of 142 facts same, 7 different; 5 unsourced facts (a minister's name, four caption names); misses Greenland, Myanmar's politics, the bacterial separation, Starship and the space-resource law; adds the 2010 trade dispute, Japan's and the US's responses, prices, the Korea–Vietnam contracts |

There is no pass line for these two. The reports are `runs/<id>/repro/1/comparison.md`. The two sets of results (previous profile at maximum effort scored by source match; generalized profile at effort high compared on the final post) are not comparable to each other.

### Four-post profile with the depth pass line (workers at effort high; two new posts, three attempts each)

`uv run rek compare-summary runs/` (latest attempt per run; the two first-cycle runs print in the old format):

```
222863642965 | fail (fabricated) | depth back 3→12, forward 8→17 | units 12/18 | facts 30/65 (conflict 2) | fabricated 1 | extra 25 | valid | fe7b2c5cf535
224458617394 | fail (fabricated) | depth back 9→15, forward 8→12 | units 13/22 | facts 33/78 (conflict 3) | fabricated 2 | extra 21 | valid | fe7b2c5cf535
```

| Post | Attempt | Depth back o→r | Depth forward o→r | Units covered | Facts same/different | Fabricated | Fix applied before the next attempt |
|---|---|---|---|---|---|---|---|
| 아파트 벌떼 입찰 근황 (222863642965, 2022-09-01, construction) | 1 | 1→6 | 8→15 | 9/15 | 30/1 | 4 (a motive, a data attribution, a label, a time relation) | researcher brief: connective phrases are facts |
| | 2 | 3→6 | 6→10 | 9/17 | 32/1 | 4 (a ministry named where the source said LH, a minister's office, a year, a sub-district) | researcher brief: attributions and specifics are facts |
| | 3 | 3→12 | 8→17 | 12/18 | 30/2 | 1 (a founder's given name joined to "정 회장") | budget exhausted |
| 체코원전 시공계약이 깨진 비밀 (224458617394, 2026-10-31, energy) | 1 | 6→10 | 9→13 | 9/20 | 31/2 | 4 (a coin's other name, a trade route, a causal clause, an offer by a deadline) | researcher brief: connective phrases are facts |
| | 2 | 6→12 | 11→13 | 12/21 | 28/4 | 1 (an image description, cooling towers, not stated by its source) | researcher brief: image sources must state what the image shows |
| | 3 | 9→15 | 8→12 | 13/22 | 33/3 | 2 ("spa town"; a given name and a ministry) | budget exhausted |

Researcher-brief version used by each attempt (commit on this branch): housing 1 and nuclear 1 — 5859c1c; housing 2 — cac0685; nuclear 2 — 7c76bee; housing 3 — 7c76bee (095398a landed minutes after it started); nuclear 3 — 095398a. Each post's later attempts therefore also carried the amendments made for the other post's routing. The comparator brief and the profile were unchanged throughout.

Every attempt was valid (no author-domain contact, no post-date content used). Depth passed in both directions on all six attempts; the pass line failed each time on fabrication alone, and the routing named the reproduction stage every time (the profile was never routed for a pass-line condition). The `units_total` of the original differs between attempts because each comparison worker splits the original anew.

Routing items outside the pass line (coverage of original units, reported only): the housing post's reproduction skipped the lot-level instances (F5), the firm-level figures (F1/F2), the provincial-council thread (F7/F9) and the closing reader clause (F11); the nuclear post's reproduction skipped the Westinghouse thread (B1–B3, F8, F1) and the cost-risk thread (F4/F7/F10, A4). One method-extraction item recurred: no A-layer rule judges the responsible public body against its own recent conduct.

## Remaining (in priority order)

0. The last-mile fabrication: every remaining unsourced item is a specific the worker fills in from general knowledge inside a sourced sentence (a given name, an office, a year, a cause, "spa town"). Three brief additions cut it from 4 to 1–2 but not to 0. Candidates: a final self-check step that lists every proper noun, office, year and causal clause of `post.md` with its source id before the worker finishes; or a lenient fabrication rule for a name link the sources make unambiguous (this would change the pass line and is the user's call).
1. Run `/rek:research` on one real topic and fix what the first run shows.
2. Decide whether the three test-only runs (223137359486, 222863642965, 224458617394) become profile material (full trace, then re-extraction) or stay test-only.
3. Widen the material to posts from other fields so that author habit and field habit can be told apart; the housing post showed the profile works in a new field for depth.
4. Fill in the search method per site in `instances.md` (kind and paywall status are there).
5. Adapters for other sites (Brunch, general article URLs, pasted text), connect the user's own notes to the "prior post slot", and a run mode that calls the API directly.

## Blocked

None. Login-walled pages now go through Aside; whether workers reach them that way is untested (`findings.md`).
