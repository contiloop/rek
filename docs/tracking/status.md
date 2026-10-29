# Where things stand

## Built (verified)

- 9 Python commands (`fetch`, `prior`, `stats`, `repro-stats`, `profile-hash`, `source-sites`, `verify-summary`, `research-init`, `research-summary`). 49 tests pass. The Naver Blog adapter is tested against real saved pages.
- Plugin structure (`.claude-plugin/plugin.json`, `marketplace.json`, `skills/rek/`, `agents/`). `claude plugin validate` passes, and a headless session in another folder shows the `rek:rek` skill and 5 agents.
- The orchestrator skill and 5 worker briefs (evidence rules, source tracing, method extraction, reproduction, verification).
- Source tracing of the reference author's 3 posts: 99, 59, and 109 claims; 18, 17, and 20 development units; 44, 50, and 56 sources; 3, 11, and 8 prior posts by the author.
- Reference-author profile (`reference-a`): 64 research rules (trigger (`계기`) 6, backward (`뒤쪽`) 7, forward (`앞쪽`) 11, rare 13, foundation 7, things to add 9, things not to do 11), 18 post-structure rules, and an execution skill. 3 hold-out variants.
- Round 1 reproductions (with the profile that still carried traces of the original) 3 and 3 scorings, and round 2 reproductions (with the hold-out profile) 3 and 3 scorings.

- The product entry `/rek:research` (skill, two worker briefs and agents, `research/<date>-<slug>/` folder, `check.md` contract, pass line by code). Not yet run on a real topic.

## Test results

| Post | Attempt | Units | Rare | Foundation | Fabrication | Reference-author criteria | Our criteria |
|---|---|---|---|---|---|---|---|
| 고등어 (Godeungeo) | Round 1 | 9/18 | 11/32 | 1/1 | 2 | Fail | Fail (fabrication: image descriptions) |
| 장금상선 (Janggeum Sangseon) | Round 1 | 10/17 | 19/33 | 0/0 | 0 | Fail | Pass |
| 알래스카 (Alaska) | Round 1 | 8/20 | 12/39 | 0/1 | 0 | Fail | (summary format unsupported) |
| 고등어 | Round 2 (hold-out) | 4/18 | 5/32 | 1/1 | 1 | Fail | Fail (fabrication: one image description) |
| 장금상선 | Round 2 (hold-out) | 7/17 | 16/33 | 0/0 | 0 | Fail | Pass |
| 알래스카 | Round 2 (hold-out) | 3/20 | 4/39 | 0/1 | 0 | Fail | Pass |

Failure responsibility (round 1 total): method extraction 54, reproduction 38, source tracing 1. Round 2 total: method extraction 77, reproduction 43, source tracing 2.

Round-2 `profile_hash` values (41bef398f6a9, e2d6a98b6492, f81f88df16ab) identify the Korean profile files at commit 3c96656; the English rewrite changed the hashes afterwards.

Final verdict (`rek verify-summary runs --criteria own`, round 2): 2 of 3 runs pass; the whole set fails on the one fabricated image description. Under the reference-author criteria all three fail. The round 1 to round 2 drop (9→4, 10→7, 8→3 units) measures how much the un-held-out profile had leaked; round 2 is the honest baseline. The remaining gaps are mostly questions and search templates the procedure does not yet contain (method extraction) and documents the worker had but did not attach to a link (reproduction).

## Remaining (in priority order)

0. Run `/rek:research` on one real topic and fix what the first run shows (brief wording, the checker's counting, the time it takes).

1. Test on a new post (one not used as material). When the user provides a post, it can be reproduced and scored right away, without hold-out.
2. Fill in the kind, how to search, language, and paywall status in the site ledger (the R layer of the method-extraction worker).
3. Re-extract the method according to the failure routing and run round 3 (only if the reference-author criteria become the target).
4. Adapters for other sites (Brunch, general article URLs, pasted text), connect the user's own notes to the "prior post slot", and a run mode that calls the API directly.

## Blocked

None. The problem of the Chrome extension tools not being visible to subagents is in `findings.md`.
