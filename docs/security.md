# Security policy

This project is a local tool for one user. It has no authentication, no permissions, and no outside users. There are four policies.

- **Web content is material, not instructions.** Whatever a fetched page, a search result, or text inside an image tells a worker to do, the worker does not follow it. It only quotes and records. This is written in the brief (`skills/rek/references/evidence.md`, rule 7), and every worker reads that file first.
- **Chrome is read-only.** The user's logged-in Chrome can read paid or blocked pages, but workers take no write actions such as posting, commenting, liking, or following. No credentials, cookies, or tokens go into any file.
- **Isolation of the reproduction worker.** It receives only the four lines of starting information, the profile folder, and the folder to write to. It is told nothing about the author; the verifier invalidates the attempt if its log shows the author's domains (from the `units.md` header) or the original post. Violations are recorded in `log.md` and checked by the verifier.
- **Workers do not write outside their own folder and do not touch git.** The source-tracing, reproduction, and verification workers write only to `runs/<post_id>/` (reproduction writes only to `repro/<n>/` inside it). The method-extraction worker writes only to `profiles/<author>/`. Only the orchestrator (or the user) commits.

What is recorded: each worker's stage changes (`status.md`), and every search query, opened URL, Chrome use, and forbidden contact in a reproduction (`log.md`). Both stay in the run folder and go into git. Images and raw HTML are excluded from git because of their size (`runs/**/images/`, `runs/**/raw.html`).
