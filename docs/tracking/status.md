# Where things stand

## Built (verified)

- 10 Python commands (`fetch`, `prior`, `stats`, `repro-stats`, `profile-hash`, `source-sites`, `verify-summary`, `research-init`, `research-summary`, `compare-summary`). 59 tests pass. The Naver Blog adapter is tested against real saved pages.
- Plugin structure (`.claude-plugin/plugin.json`, `marketplace.json`, `skills/rek/`, `skills/research/`, `agents/`). `claude plugin validate` passes. One orchestrator agent and seven worker agents (source tracer, method analyst, researcher, verifier, topic researcher, topic checker, comparator); model and effort in each definition are defaults (`opus`, `high`).
- Two orchestrator skills and seven worker briefs plus `evidence.md`.
- Source tracing of the reference author's 3 posts: 99, 59, and 109 claims; 18, 17, and 20 development units; 44, 50, and 56 sources; 3, 11, and 8 prior posts by the author.
- Reference-author profile (`reference-a`), rebuilt at the level of the author's moves: 53 rules (trigger 3, backward 6, forward 10, rare 11, base 5, additions 10, not-do 8), all free of the material posts' nouns, each tried on two unrelated topics; `instances.md` (sites, queries, measured numbers, the move table) as hints; `writing-structure.md` as moves without measured values; `SKILL.md` of 91 lines (was 188). `profile_hash` cb903f4d4ad0 (sha256 over SKILL.md + research-method.md + instances.md). The hold-out variants are gone.
- Round 1 and round 2 reproductions and scorings of the three material posts with the previous profile (kept in `runs/<id>/repro/1`, `repro/2`).
- The product entry `/rek:research` (skill, two worker briefs and agents, `research/<date>-<slug>/` folder, `check.md` contract, pass line by code). Not yet run on a real topic.
- The test-only path for a new post: fetch, four start lines written by the orchestrator, reproduction, comparison by `rek-comparator`, table by `rek compare-summary`.

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

`uv run rek compare-summary runs/`:

```
223137359486 | units 6/22 | facts 16/142 (conflict 7) | fabricated 5 | depth 17→12 | extra 11 | valid | cb903f4d4ad0
224314709934 | units 11/24 | facts 21/101 (conflict 2) | fabricated 6 | depth 20→17 | extra 15 | valid | cb903f4d4ad0
```

| Post | Date | Reproduction | Comparison |
|---|---|---|---|
| 컨테이너가 바꾼 역사와 부산항 이야기 (224314709934) | 2026-06-14 | 19 units (8 back, 5 main, 5 forward, 1 trigger), 39 sources (6 primary), 0 contacts | covers 11 of 24 original units; 21 of 101 facts same, 2 different; 6 unsourced facts ("first"/"largest" qualifiers, a Japanese-cargo label, alliance members); misses the trucking fines, the Vietnam War logistics, why shippers stayed; adds carriers, alliances, port fees, the Arctic route |
| 희토류 전쟁 근황 업데이트 3 (223137359486) | 2023-06-26 | 17 units (7 back, 3 main, 6 forward, 1 trigger), 39 sources (13 primary), 5 contacts (date checks only), 0 invalid | covers 6 of 22 original units; 16 of 142 facts same, 7 different; 5 unsourced facts (a minister's name, four caption names); misses Greenland, Myanmar's politics, the bacterial separation, Starship and the space-resource law; adds the 2010 trade dispute, Japan's and the US's responses, prices, the Korea–Vietnam contracts |

There is no pass line for these two. The reports are `runs/<id>/repro/1/comparison.md`. The two sets of results (previous profile at maximum effort scored by source match; generalized profile at effort high compared on the final post) are not comparable to each other.

## Remaining (in priority order)

0. Decide from the two comparison reports what to fix first: the backward chain stops at the industry level where the author goes into war, politics and law (a profile gap, B layer), and image captions and qualifiers keep producing unsourced facts (a researcher-brief gap).
1. Run `/rek:research` on one real topic and fix what the first run shows (brief wording, the checker's counting, the time it takes).
2. Decide whether the two test runs become profile material (full trace with `rek-source-tracer`, `rek prior`, then re-extraction) or stay test-only.
3. Widen the material to posts from other fields (food, history, domestic politics, corporate governance) so that author habit and field habit can be told apart.
4. Fill in the kind, how to search, language, and paywall status in the site ledger (`instances.md` now holds kind and paywall; the search method per site is still missing).
5. Adapters for other sites (Brunch, general article URLs, pasted text), connect the user's own notes to the "prior post slot", and a run mode that calls the API directly.

## Blocked

None. The problem of the Chrome extension tools not being visible to subagents is in `findings.md`.
