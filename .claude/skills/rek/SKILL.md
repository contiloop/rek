---
name: rek
description: Reverse Engineering Knowledge. Given a published text (blog post, article, report), trace which sources the author used and in what order, reconstruct how the author researched and wrote it, distill the writing method into a reusable profile, and verify the profile by regenerating a post and diffing it against the original. Use when the user gives one or more URLs and asks where a text came from, how it was researched, how it was written, or wants an agent that writes the same way.
---

# REK loop

REK applies the REA investigation loop (route → summary-first inventory → evidence ledger with
observed/inferred/unknown → verified reconstruction) to text instead of binaries. The orchestrator
(this session) does routing, bookkeeping and the user gate; every analysis step runs in a worker
subagent launched with `model: opus`, `effort: max`, and one brief from `references/`.

Correspondence that must hold (REA → REK):

| REA | REK |
|---|---|
| binary / app target | the post; its images; the author's earlier posts |
| strings, symbols, functions | atomic claims: numbers, dates, names, quotes, causal links |
| decompiled pseudocode + xrefs | each claim's candidate sources, with fetched evidence |
| Evidence record: observed / inferred / unknown | same three words, same meaning, per claim and per conclusion |
| residual unknowns ledger | `unknowns` section in every output file |
| obligation ledger for reconstruction | writing-method rules, each citing the posts that prove it |
| verify_reconstruction | regenerate a post from traced sources, diff against the original |

## 1. Route and fetch

```bash
uv run rek fetch <url>            # → runs/<post_id>/{post.md, meta.json, images/, raw.html}
```

`meta.json.images[].uploaded_on` is decoded from the image host's URL. An image uploaded long
before `published_at` was reused from an earlier post by the same author: find that post (the
blog's post list around that date) and fetch it into `runs/<post_id>/prior/<prior_id>/`. Do this
before launching workers; reuse of the author's own prior work is the single most common source.

No adapter for the site → add one under `rek/adapters/` implementing `PostSource`; do not paste text by hand.

## 2. Trace sources (one worker per post, in parallel)

Launch `rek-source-tracer` with `references/source-tracer.md` and the run directory. It writes
`claims.md`, `sources.md`, `research-path.md` into the run directory. Launch all posts at once; they
do not depend on each other.

## 3. Distill the writing method (one worker, after step 2)

Launch `rek-style-analyst` with `references/style-analyst.md`, every run directory and the author
name. It writes `profiles/<author>/writing-method.md` (rules with evidence) and
`profiles/<author>/SKILL.md` (the writer skill another agent loads to write the same way).

## 4. Verify by reconstruction (one worker per held-out post)

Launch `rek-writer` with `references/writer.md`: it gets only `sources.md` + `research-path.md` of
one post and the profile, never `post.md`, and writes `runs/<post_id>/reconstruction.md`.
Then launch `rek-verifier` with `references/verifier.md` to score `reconstruction.md` against
`post.md` rule by rule and claim by claim; it writes `runs/<post_id>/verification.md`.
A rule that fails on every held-out post goes back to step 3 as a finding; fix the rule, not the output.

## 5. Report

Summarize per post: claims traced (observed / inferred / unknown counts), the reconstructed
research path in five lines, and the verification score. Keep unknowns visible; never present an
inferred source as observed.

Success thresholds (a run below them is reported as not done, with the failing stage named):

| measure | threshold |
|---|---|
| number/date/name/quote/event claims with a source line that is observed or inferred | ≥ 80 % |
| reconstruction: original number claims reproduced exactly (`hit`) | ≥ 70 % |
| reconstruction: fabricated facts | 0 |
| reconstruction: writing-method rules passed | ≥ 90 % |

Form numbers (sentence count, numbered items, register share, images, one-liner) always come from
`uv run rek stats <post.md> [...]`, never from reading by eye, so profile and verification agree.
