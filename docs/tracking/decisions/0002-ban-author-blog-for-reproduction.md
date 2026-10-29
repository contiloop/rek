# 0002 The reproduction worker cannot see the author's whole blog

**Situation.** The reference author copies and edits their own old posts in each new post. If the reproduction worker may read the author's posts from before the publication date, it is closer to the author's real process, but the test becomes "can it find and copy the old post".

**Decision.** Keep the author's whole blog and account off limits for the reproduction worker, but do not tell the worker: it receives no author name or domain, and the verifier checks its log against the `excluded_domains:` line in `units.md`. Earlier the list sat on the reproduction worker's forbidden reading list. Units that came from old posts stay in the denominator, and the reproduction must reach that link through other sources.

**Rejected options.** Block only by publication time and allow old posts: low test value. Remove units from old posts from the denominator: the denominator shrinks, the score inflates, and there is no incentive to find the original sources behind the author's posts.

**Result.** Source tracing found and attached the original sources of the units that had relied only on the author's posts (a 나무위키 (Namuwiki) document, a newspaper op-ed, a company history, a company article), and two of them were confirmed as foundation sources. In the profile, the author's "prior post slot" became "look for the same kind of foundation source".
