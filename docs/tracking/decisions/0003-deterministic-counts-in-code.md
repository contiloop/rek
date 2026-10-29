# 0003 Calculations with a fixed answer are done by code, not by workers

**Situation.** A reproduction worker spent an hour counting 82 sources and 20 units by hand. If the pass verdict also depends on the worker's opinion, it differs from worker to worker.

**Decision.** Code does format statistics (`rek stats`), reproduction aggregation (`rek repro-stats`), the pass verdict (`rek verify-summary`), profile identification (`rek profile-hash`), and the domain ledger (`rek source-sites`). Workers write files with the fixed marks (`R<nn> |`, `S<nn>`, `[검색]` (search), and so on), run the commands, and paste the output. The verification worker's `verifier_verdict` is an opinion and is shown only as a mark.

**Rejected options.** Workers count and the orchestrator trusts them: slow, expensive, and unverifiable.

**Result.** Briefs now fix the file formats. A file that breaks the format aggregates to 0, so a format violation shows up at once.
