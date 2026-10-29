# What you need to know

## Naver Blog

- A desktop post address (`blog.naver.com/<id>/<post number>`) wraps the body in an iframe, so the page has no body text. Request the mobile address (`m.blog.naver.com/<id>/<post number>`) with a mobile User-Agent to get the body. For a post that does not exist, the server returns 200 with a redirect script containing `errorType=noPost`. Search the body for that string and turn it into an error.
- The first path segment of an image URL is the base64 of `YYYYMMDD_n`. The second segment is the base64 of the upload time in epoch milliseconds. So you can recover the upload date and time (KST) of each image. An upload earlier than the publication date is evidence that the author copied an old post. Upload times in the few hours before publication show when the author was writing. An upload within 24 hours counts as belonging to that post.
- An image caption sits inside `<div class="se-module se-module-text se-caption">`. `se-caption` does not come first in the class attribute, so searching for `class="se-caption"` misses it.
- The post list comes as JSON from `PostTitleListAsync.naver?blogId=<id>&currentPage=<p>&countPerPage=30&categoryNo=0`. Titles are URL-encoded (`+` means a space). The date of today's posts is a relative expression such as "12시간 전" (12 hours ago). The body contains `\'` escapes that must be replaced before `json.loads`. There are about 2,700 posts over 91 pages.
- If the date route of the prior-post search is "all posts within ±2 days", it catches 20 posts per post, because the author publishes three posts a day. Check whether the candidate's HTML contains the same image file path. Only then do the posts that really reused the image remain. Match the title route by word, not by substring, and cut it to the 10 most recent posts (the word `이란` ("Iran") once matched 79 posts).

## Running workers

- If you tell a worker to "count and report", it rereads its own 80KB file several times and spends an hour. Do the aggregation with `rek repro-stats` and have the worker paste the output.
- If workers create work files with the same name in the shared temporary folder (scratchpad), parallel workers overwrite each other. Give each worker a subfolder named by its run number.
- In the environment used so far, the Chrome extension tools were not visible to subagents. Paid and 403 pages were replaced with the Wayback Machine and reposts, and when that failed they stayed `[inferred]`. In an environment where Chrome works, use it under the lock rules in `evidence.md`.
- The web search tool is US-based, so even Korean searches return almost no Korean outlets. As a result the "ordinary search" domain set has no Korean outlets, and almost every domestic article is classified as rare. This is why the rare count under the author criteria is large.
- The times in a worker's `log.md` are the worker's own estimates and can differ from the real clock. The order is correct. For real times, trust the ISO time on the `status.md` lines.
- Reproduction workers put marks such as `[observed: R06, S33]` on every sentence of the post body, even without instructions. The brief now says explicitly "do not put marks in the body" (round 2 reproduction started before that, so its marks remain).
- If you test a post with a profile built from that same post, the quotes and source names inside the profile give away the answer. In the round 1 test, almost all the units that were found had been exposed in the profile. You must strip that post's traces with a hold-out variant.

## Scoring

- A development unit that relied only on a prior post by the author cannot meet the "same primary source" condition, so it can never be found. In the tracing reinforcement, find and attach the original source of that old post (a 나무위키 (Namuwiki) document, an op-ed, a company history). Only then is the denominator fair.
- The descriptions of image placeholders are also subject to the fabrication check. Both fabrications in the first reproduction of the 고등어 (Godeungeo) post were invented events inside image descriptions.
- Search results do not show dates, so you have to open a page to know. If the rule is "invalid if opened", diligent workers are caught first. The current rule is: closing a page after a date check is allowed, and if the body was read, check whether a fact found only on that page entered the result.

## Tools

- macOS has no `timeout` command. Run long external commands in the background, or cap them with `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS`.
- In zsh, `echo =====` fails because of `=cmd` expansion. Wrap separator lines in quotes.
- Plugin agents carry a prefix, as in `rek:rek-source-tracer`. This differs from the bare name used when they sit in the project's `.claude/agents/`. `${CLAUDE_PLUGIN_ROOT}` is substituted in skill and agent bodies, but it does not exist as a Bash environment variable.
