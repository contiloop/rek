# Brief: rek-source-tracer

Goal: for one post, find where every claim came from and reconstruct the order in which the
author gathered them. Output three files into the run directory. Read `evidence.md` first.

Inputs in the run directory: `post.md` (body with images in place), `meta.json` (dates, image
upload dates), `images/` (read each one), `prior/<id>/` (the author's earlier posts that this post
reuses; compare their text and images with this post).

## Step 1 — claims.md: inventory before search

Split the body into atomic claims in reading order. One line per claim:

```
C07 | number | "EU의 1인당 고등어 소비량은 연 0.67kg" | para 7
```

Types: `number`, `date`, `name` (person, company, ship, law), `quote` (someone's words), `event`,
`causal` (X because Y), `opinion` (the author's own view), `self-reference` (restates an earlier
post). Mark every claim that already appears, verbatim or near-verbatim, in a `prior/` post as
`self-reference` with the prior post id. This step takes no web access; finish it before searching.

## Step 2 — sources.md: trace each non-self-reference claim

Group claims that would share a source (the same article usually carries several numbers).
Search in both languages: the author writes in Korean, so first look for a Korean article
published within 10 days before `published_at` that contains the same numbers; then find the
primary (FT, Bloomberg, Reuters, Lloyd's List, Forbes, a government or industry statistics page,
an X post). Fetch, match, label. Format per source:

```
## S03 — Lloyd's List, "..." (2026-10-21) [observed]
URL: ...
Claims: C21, C22
Match: "9월 호르무즈 VLCC 통항의 47%" ↔ "47% of VLCC transits in September" (quote both)
Probably reached via: Korean article S02 cites it / direct / unknown
```

Also record, per image: what it is, what source it names in its pixels, and whether
`uploaded_on` predates the post (then name the prior post it came from).

Stop condition: every `number`, `date`, `name`, `quote`, `event` claim has a source line or an
explicit `[unknown]` line with the queries you tried. Do not stop at 80%.

## Step 3 — research-path.md: reconstruct the process

Write, in this order:
1. **Trigger** — the event or article that made this post exist, with its date and time relative to
   `published_at`. (The author often publishes within 24 hours of a news event.)
2. **Timeline** — every source by publication date, then the post. Point out any source dated after
   the post (then it cannot be the source; find the earlier one).
3. **Reuse** — which paragraphs and images came from `prior/` posts, and what changed between the
   prior text and this one (added numbers, dropped sentences, softened/strengthened claims).
4. **Probable reading order** — the order the author read things, argued from dates, from which
   numbers appear only in which sources, and from the post's own paragraph order.
5. **What the author added** — computations (ratios, conversions), analogies, opinions, the
   closing one-liner; label each `opinion` claim's basis if any.
6. **Tools the author plausibly used** — only what the evidence supports (e.g., a MarineTraffic
   screenshot implies MarineTraffic; a Korean wire-service phrasing implies a Naver news search).
7. **Coverage** — counts: claims total / observed / inferred / unknown / self-reference.
8. **Unknowns** — what you could not settle and what evidence would settle it.

Language: write the three files in Korean; keep quoted source passages in their original language.
Do not rewrite or judge the post's content; this is provenance, not fact-checking (note a claim the
sources contradict, but do not chase it).
