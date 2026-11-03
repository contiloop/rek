# 0009 Model and effort are defaults in the agent definitions, not a rule

**Situation.** The hard gate that every worker runs on one model at maximum effort sat in CLAUDE.md, standards, the module notes, both orchestrator skills and the orchestrator agent's body. The user wants to run workers on other models and at lower effort, and the gate made every such run a rule violation.

**Decision.** The gate is deleted everywhere. Each worker agent definition keeps `model: opus` and now `effort: high` as defaults, and the rules say only that the orchestrator may launch a worker with another model or effort. The orchestrator agent's own frontmatter is unchanged. Every run in this cycle (one re-extraction, two reproductions, two comparisons) ran at effort high.

**Rejected options.** Making "effort high" the new gate: the point is freedom to choose, not a different fixed value. Keeping the gate and overriding it per run: an overridden gate is noise.

**Result.** The round-1 and round-2 scores in status were produced at maximum effort; the new test ran at high, so the two sets are not compared. The cost note in operations is an estimate for effort high.
