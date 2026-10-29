# Brief: rek-writer (reconstruction)

Goal: write the post the author would have written, from the traced sources and the method
profile only. You are the test of the profile, so follow it literally; where it is silent, say so
in a note at the end rather than improvising.

Inputs: `profiles/<author>/SKILL.md`, `runs/<id>/sources.md`, `runs/<id>/research-path.md`,
`runs/<id>/prior/` (the author's earlier posts, which the author reused). You must not open
`runs/<id>/post.md`, `claims.md`, `images/`, or `profiles/<author>/writing-method.md` (it quotes
the originals); the original is the answer key, and the skill alone is what is being tested.

Procedure:
1. Read the trigger and timeline from research-path.md; fetch the sources listed `[observed]`
   in sources.md (URLs are given) and read them yourself. Use only facts found in them or in
   `prior/`.
2. Write `runs/<id>/reconstruction.md`: the title, then the body exactly in the author's form
   (numbered sentences, register, closing one-liner), with `![image: <what it would show>]`
   placeholders where the method says an image goes.
3. End the file with `## 작성 노트`: which rules you applied, where the profile was silent or
   contradictory, which source facts you left out and why.

Do not use any fact not in the given sources or prior posts; the verifier checks this.
