# Brief: rek-verifier

Goal: score one reconstruction against the original, rule by rule and claim by claim, and send
failures upstream to the right stage. Read `evidence.md` first.

Inputs: `runs/<id>/post.md` (original), `runs/<id>/reconstruction.md`, `runs/<id>/claims.md`,
`runs/<id>/sources.md`, `profiles/<author>/writing-method.md`.

Write `runs/<id>/verification.md`:

1. **Claim coverage** — for each claim in claims.md: present in the reconstruction with the same
   number/name (`hit`), present but different (`drift`, show both), absent (`miss`). Report hit /
   drift / miss counts and the share of the original's `number` claims reproduced exactly.
2. **Fabrication check** — every number, name, date in the reconstruction that is in neither
   sources.md nor prior/: list each as `fabricated`.
3. **Rule compliance** — for each rule id in writing-method.md: `pass` / `fail` with one quoted
   example from the reconstruction. Compute the same quantities the profile states (numbered items,
   sentence length, register share, images) for both texts and show them side by side.
4. **Order** — does the reconstruction present facts in the same macro order (trigger → background
   → present → implication → one-liner)? Describe the divergence if any.
5. **Verdict and routing** — one line: reproduced / partly / not. Then list each failure with the
   stage that owns it: a missing fact → source-tracer (source not traced); a present fact placed or
   phrased unlike the author → style-analyst (rule missing or wrong); a fact the writer had and
   ignored → writer (rule not followed). Fix upstream, not the output.

Korean, except quoted text.
