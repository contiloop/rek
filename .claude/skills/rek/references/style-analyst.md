# Brief: rek-style-analyst

Goal: turn several traced posts by one author into a writing method another agent can execute,
with every rule tied to the posts that prove it. Read `evidence.md` first.

Inputs: every `runs/<id>/` (post.md, meta.json, images/, claims.md, sources.md, research-path.md,
prior/). Read all of them before writing anything.

## Output 1 — profiles/<author>/writing-method.md

A ledger of rules. Each rule has: an id, the rule in one sentence an agent can follow, the
evidence (post ids and a quoted example from each), and exceptions seen. Cover these layers; add
layers the posts demand and drop any with no evidence:

1. **Topic selection and trigger** — what kind of event becomes a post, how soon after the event,
   how the title is formed (patterns such as "~의 비밀", "~알아보자", "(feat ...)", "A/S").
2. **Research pattern** — from the research paths: which source types, in which order, how much is
   reused from prior posts, which numbers are recomputed by the author.
3. **Macro structure** — opening line conventions, the numbered-sentence body, where history or
   background detours sit and how long they run, how the post returns to the present, the closing
   "한줄 코멘트" and what it does (forecast, caveat, personal note).
4. **Paragraph and sentence form** — numbered single sentences, the sentence-ending register
   (`~임`, `~함`, `~됨`, `~것임`) versus the plain `~다` register, when each is used, sentence
   length, one fact per sentence, how a number is always followed by a comparison.
5. **Number handling** — units, precision, how a foreign figure is converted or compared with a
   Korean figure, how percentages are derived.
6. **Images** — count per post, kind (stock photo with OGQ credit, chart screenshot, map,
   own photo), placement relative to the text, reuse of earlier images.
7. **Voice** — distance from the reader, humor markers, hedges ("뇌피셜", "~로 보임"), what is
   never said (no first-person investing advice, etc.), the "메르" persona markers.
8. **Anti-rules** — things a generic LLM would do that this author never does. These are the
   rules that matter most for reproduction; derive them by imagining the generic draft and diffing.

Mark each rule `[observed]` with ≥ 2 posts, `[inferred]` with 1. Quantify where possible
(sentences per post, numbered items per post, images per post, mean sentence length in characters,
share of sentences ending in `~임/~함/~됨`), computed from post.md files, and state the counts.

## Output 2 — profiles/<author>/SKILL.md

A Claude Code skill another agent loads to write a new post the same way. Frontmatter `name`
and `description`. Body: the research procedure (what to gather, in what order, how to pick the
trigger), then the writing procedure as an ordered checklist that references rule ids from
writing-method.md, then a final self-check list made from the anti-rules. Under 300 lines.
Write for an agent that has never seen the author's posts: it must be able to produce the post
from the skill plus sources alone.

Write both files in Korean, rule ids and quoted evidence as they are.
