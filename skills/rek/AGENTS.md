# skills/rek/ and agents/ — the agent loop

## Scope
The two orchestrator procedures (`SKILL.md` here for learning a profile; `../research/SKILL.md` for researching a new topic), the seven briefs under `references/` and the agent definitions under `../agents/`.
These files are instructions; they contain no author name, no run data and no results.

## Not this part's job
Fetching or counting (the `rek` commands do that); storing knowledge about a specific author (that lives in
`profiles/<author>/`); deciding pass/fail (computed by `rek verify-summary` and `rek research-summary`).

## Invariants
- `references/evidence.md` is the single home of the three labels, the Chrome lock protocol, the status-line format and
  the definitions of development unit, rare source and upstream source. Other briefs refer to it; they do not restate it.
- Every brief names exactly the files its worker may write and the folder it may write them in. A worker that writes
  elsewhere, reads a forbidden file or runs git is a brief defect, not a worker quirk.
- Paths in briefs and agent bodies are `${CLAUDE_PLUGIN_ROOT}/skills/rek/...` and
  `uv run --project "${CLAUDE_PLUGIN_ROOT}" rek ...`; never a working-folder-relative or absolute path.
- The reproduction brief gives the worker only the four start lines, the profile folder and the output folder, and
  forbids the author's domains, the original post, the run's other files and the content of pages after `date:`.
- The verifier brief's example yaml block is byte-identical to `tests/fixtures/verification_example.md`. The topic-checker brief's yaml keys are `fabricated`, `late_sources`, `checker_verdict`, read by `rek research-summary`.
- The topic-researcher brief receives only `topic.md` and the profile folder; its `research.md` and `log.md` use the same markers as the reproduction brief so `rek repro-stats` counts both.
- Counts come from `rek stats` / `rek repro-stats`; a brief never asks a worker to count by hand.
- File markers prescribed by the briefs (`R<nn> |`, `## 출처 목록`, `S<nn>`, `[검색]`, `표시:`, `무효:`, the three header
  lines `main_topic:` / `trigger:` / `date:`) are parsed by code and stay as written.

## Patterns
- A worker agent body is four sentences: read the brief and evidence.md first, follow the brief literally, label every
  statement, write only the named files, report paths and counts.
- Workers for different posts run in parallel; two workers never work on the same run at the same time; the orchestrator
  reads `status.md` before launching.
- Launch workers with `model: opus`, `effort: max`; when the plugin agent names are not available, launch a
  general-purpose agent with the agent body pasted in and the brief path given.

## Tests
No automated tests. Check a brief change by grepping for the strings the counters and the verifier depend on (see
Invariants), by `grep -ril "<author name>" skills agents` returning nothing, and by one real worker run on an existing
run folder.
