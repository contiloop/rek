# 0007 The product is `/rek:research`; tracing and the reproduction test are the learning side

**Situation.** With the loop stopped at the project's own criteria (0006), the user said the tool will now be used only to research new topics and write posts. The tracing, profile extraction and reproduction test exist to learn a research procedure from an author, and that procedure (`profiles/reference-a/`) is the thing to use.

**Decision.** Add a second skill, `/rek:research`, that takes a topic, an optional trigger sentence and a date, runs the profile's procedure in a `research/<date>-<slug>/` folder (`rek research-init`, topic researcher, topic checker, `rek research-summary`), and passes by the own criteria minus the unit match that needs an original: a chain in all three directions, at least 20 sources with 5 primary, no fabricated fact, no source after the date. `/rek:rek` stays as the learning side that builds and repairs the profile.

**Rejected options.** Reusing the reproduction brief with a mode switch: its isolation rules (no original, no run files, told nothing about the author) have no object in product use and would confuse the worker. Running the worker directly through the API: 0004 stands.

**Result.** Two new briefs and agents, two commands, five tests. The MCP adapter and the ChatGPT plugin packaging were rolled back the same day and kept on the `mcp-work` branch for later.
