# Brief: rek-source-tracer

Goal: Find where every claim in one post came from, and reconstruct the order in which the author gathered them. Write four files in the run directory: `claims.md`, `sources.md`, `research-path.md`, `units.md`. First read `evidence.md` (it has the labels, the Chrome rules, the status records, and the definitions of development unit, rare source, and base source).

There are two modes. If the prompt names no mode, look at the run directory and choose.
- **Full mode**: `claims.md`, `sources.md`, and `research-path.md` do not exist. Do all of steps 1 to 4.
- **Supplement mode**: those three files already exist. Do not redo the tracing. Follow the "Supplement mode" section below.

Input (the run directory): `post.md` (the body, with images in place), `meta.json` (publication time, image upload times), `images/` (read all of them), `prior/<id>/` (the author's prior posts that this post reused; compare their text and images with this post).

Status records: Append one line to `runs/<id>/status.md` in the format from evidence.md when you start, each time a step ends (`claims`, `sources`, `research-path`, `units`, `marks`), and when you finish.

## Step 1: claims.md, the inventory before searching

Split the body into atomic claims, in reading order. One claim per line:

```
C07 | number | "EU의 1인당 고등어 소비량은 연 0.67kg" | para 7
```

Types: `number`, `date`, `name` (a person, company, ship, or law), `quote` (someone's words), `event`, `causal` (X because of Y), `opinion` (the author's opinion), `self-reference` (repeats a prior post). Mark a claim that appears in a `prior/` post as is or nearly as is as `self-reference`, and give the prior post's id. Do not use the web in this step. Finish it before you search.

## Step 2: sources.md, trace a source for every claim that is not a self-reference

Group the claims that share a source (one article usually holds several numbers). Search in two languages. The author writes in Korean, so first look for a Korean article that has the same number and appeared within 10 days before `published_at`. Then look for the primary source (FT, Bloomberg, Reuters, Lloyd's List, Forbes, government or industry statistics pages, X posts). Open it, compare, and attach a label. Open pages that need a login with the Chrome rules in evidence.md. Format for each source:

```
## S03 — Lloyd's List, "..." (2026-10-21) [observed]
URL: ...
Claims: C21, C22
Match: "9월 호르무즈 VLCC 통항의 47%" ↔ "47% of VLCC transits in September" (quote both sides)
Probably reached via: cited via Korean article S02 / direct / unknown
표시: -
```

Fill in the `표시:` (mark) line in step 4. Record the author's prior post (`prior/`) as a source entry too (with the list of self-reference claims). For every image, record what it is, which source is inside its pixels, and whether `uploaded_on` is earlier than the publication date (if so, which prior post it came from).

Stop condition: Every `number`, `date`, `name`, `quote`, and `event` claim has a source entry, or an `[unknown]` line with the search terms you tried. Do not stop at 80%.

## Step 3: research-path.md, reconstruct the process

Write it in this order:
1. **Trigger**: The event or article that prompted this post. Its date and the time gap to `published_at` (the author often posts within 24 hours of the event).
2. **Timeline**: All sources in order of publication date, then the post. Flag any source dated after the post (it cannot be the source, so look for an earlier one).
3. **Reuse**: Which paragraphs and images came from `prior/`, and what changed from the prior post (a number added, a sentence deleted, a claim softened or strengthened).
4. **Probable reading order**: The order in which the author read. Argue it from the dates, from which numbers exist only in which source, and from the paragraph order of the post.
5. **What the author added**: Calculations (ratios, conversions), analogies, opinions, the last line. For each `opinion` claim, record the basis if there is one.
6. **Tools the author plausibly used**: Only what the evidence supports (for example: a MarineTraffic capture → MarineTraffic; the style of a Korean wire service → Naver News search).
7. **Coverage**: Counts: total / observed / inferred / unknown / self-reference.
8. **Unknowns**: What you could not resolve, and what would resolve it.

## Step 4: units.md and the rare and base marks

**units.md**: The list of development units (the definition is in evidence.md). Read the body from the start and cut at each point where the topic changes. 8 to 20 units is typical (adjustable). Fix them before the reproduction runs, and do not change them after you see the reproduction result. Write only three fields in the file header. The orchestrator passes these three lines as they are to the reproduction worker, so do not put in the title, the outlet, source names, or URLs.

- `main_topic:` One phrase for the post's topic. It is not the title (for example: "알래스카 LNG 프로젝트").
- `excluded_domains:` The domains and paths of the post's author (the blog, its mobile address, any social account found in the trace), comma-separated. Only the verifier reads this line; the orchestrator never passes it to the reproduction worker, who is told nothing about the author.
- `trigger:` One sentence for the trigger event. No outlet, source name, or URL. `none` if there is no trigger.
- `date:` The original's publication time (`published_at` in `meta.json`).

```
main_topic: 알래스카 LNG 프로젝트
excluded_domains: blog.example.com/<blog_id>, m.blog.example.com/<blog_id>
trigger: 미국 정부가 한국에 알래스카 LNG 프로젝트 참여를 공식 요청했다
date: 2026-10-28 11:00 KST

| 번호 | 이름 | 범위 | 뒷받침 출처 | 저자 이전 글 재사용 |
|---|---|---|---|---|
| D01 | 1970년대 구상과 좌초 | para 1 문장 1 – para 2 문장 3 (C01–C05) | S01, S02 | 아니오 |
| D02 | 가스관 노선과 비용 | para 2 문장 4 – para 3 끝 (C06–C09) | S03 | 예 (prior <id> para 2) |
```

For the range, use the same para numbers as claims.md, and put the numbers of the claims inside the unit in parentheses. The supporting sources are the numbers in `sources.md` (`-` if none). Below the unit table, put `## unknowns` and list the places where a boundary was unclear.

**Ordinary search**: Append a `## 평범한 검색` (ordinary search) section to the end of `sources.md`. Run a web search tool on `main_topic` once in Korean and once in English. Record the two queries, the URLs of the top 10 results of each, the set of registered domains taken from them (at most 20), and the date and time of the search.

**Marks**: Fill in the `표시:` line of every source entry. The value is `희귀` (rare), `바탕` (base), or `바탕(저자 글)` (base, the author's own post), joined by commas, or `-` if none applies. Follow the definitions in evidence.md for the criteria: rare is an `[observed]` source whose registered domain is not in the set. Base is a source that supports 3 or more consecutive units or supplies at least one quarter of all claims. The author's prior post is `바탕(저자 글)`. Write the basis for the decision (unit numbers, or claim count over total, and the domain) in parentheses after the `표시:` line.

## Supplement mode

When `claims.md`, `sources.md`, and `research-path.md` already exist. Read those three files and `post.md`. Do not redo the tracing. Keep the source numbers and claim numbers as they are. What you do:
1. Write `units.md` anew (in the format above).
2. Append a `## 평범한 검색` section to `sources.md`, and put a `표시:` line in every source entry (add the line to entries that lack one). Do not change anything else, not a single character. Edit in place. Do not create a new file.
3. Append the start, `units`, `marks`, and done lines to `status.md`.

Language: Write all four files in English. Keep quoted source passages in their original language. Do not correct or judge the content of the post. This is source tracing, not fact verification (record a claim that conflicts with its source, but do not chase it).
