# 0004 A Claude Code plugin (skill + subagents), with no direct API calls

**Situation.** Workers had to run on Opus 5.5 at max effort, and the user wanted to start one REK agent and hand work to it even while working in another project. There was no API key.

**Decision.** Make the repository root a Claude Code plugin (and marketplace). The skill `rek:rek` is the orchestrator procedure. The agent `rek:rek` runs the same procedure as a subagent, and the 4 worker types start as subagents inside it (session → rek → worker, 2 levels). Python handles only fetching and aggregation, and all judgment lives in the briefs.

**Rejected options.** A standalone program that calls the Anthropic API directly: it reproduces anywhere, but it needs an API key and separate billing, and the briefs would have to be kept in two copies. Skills and agents inside the project's `.claude/`: they are visible only in sessions opened in that folder.

**Result.** Component names carry the `rek:` prefix, and script paths are based on `${CLAUDE_PLUGIN_ROOT}`. Data goes into the working folder where the tool runs, not into the plugin. A run mode that calls the API directly remains as future scope.
