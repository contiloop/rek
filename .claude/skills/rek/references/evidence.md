# Evidence vocabulary (shared by every REK worker)

Every statement a worker writes carries one of three labels. Use the word, in brackets, at the end
of the line.

- `[observed]` — you fetched the source and the claim's number, name, date or wording appears in it.
  Quote the matching passage (≤ 40 words) and give the URL and the source's publication date.
- `[inferred]` — the source is likely (same numbers appear, timing fits) but you could not fetch
  or match it, or the match is partial. Say what is missing.
- `[unknown]` — you looked and found nothing, or did not look. Say which.

Rules:
1. A search result snippet is not an observation. Fetch the page before writing `[observed]`.
2. A Korean news article that quotes a foreign source is a secondary source. Record both: the
   Korean article (what the author most likely read) and the primary (where the number was born).
   Prefer the secondary as the author's probable source when its wording matches the post's.
3. Dates matter more than URLs. Record each source's publication date; the research path is built
   from the order of those dates against the post's `published_at`.
4. Paywalled or dead pages: record the URL, say `[inferred]`, and look for a cached or syndicated copy.
5. Images are evidence. Read every file in `images/`. A chart or screenshot names its source in
   its own pixels (logo, axis labels, byline). An `uploaded_on` earlier than the post date means
   the image came from the author's own earlier post in `prior/`.
6. Never fabricate a URL. A URL you did not fetch is written as `(not fetched)`.
