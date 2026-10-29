# Brief: rek-topic-checker (checking a new-topic research folder)

Goal: Check one research folder (`research/<name>/`) without an original post to compare with: count the facts in the post that reach no source, the sources dated after `date:`, and point out the weak links. First read `evidence.md`. Count an ambiguous case as a defect and write the reason.

## Input

`research/<name>/topic.md`, `research.md`, `post.md`, `log.md`, `profile_hash.txt`. Open nothing else.

## Output: research/<name>/check.md

The file **starts** with this yaml block; the three keys in this order with these names. `rek research-summary` reads only this block, so a missing or misnamed key makes the folder "미실행/불완전" (not run / incomplete).

```yaml
fabricated: 0
late_sources: 0
checker_verdict: pass
```

- `fabricated` = the number of numbers, names, dates, events and image descriptions in `post.md` that reach no source in `research.md` (a quote or a document in the source list). A value that comes out correctly from a calculation whose formula is in `research.md` counts as reached; check the formula and count a wrong one as fabricated.
- `late_sources` = the number of rows in `## 출처 목록` whose publication date is after `date:` in `topic.md`, plus the facts in `research.md` or `post.md` that exist only on a page recorded as `[접촉]` in `log.md` after its body was read.
- `checker_verdict`: `pass` or `fail`, your opinion. The verdict itself is computed by `rek research-summary` (chain in all three directions, at least 20 sources with 5 primary, `fabricated` 0, `late_sources` 0).

## The body after the block

1. **Fabrication list**: for each item, the passage in `post.md`, what is missing (number, name, date, event, image description), and where in `research.md` you looked.
2. **Late sources**: for each, the source id, its date, and `date:`.
3. **Weak links**: units whose every source is `2차` (secondary) or `[inferred]`; directions (`뒤쪽`, `본 주제`, `앞쪽`) with no unit; the `## 못 찾은 것` items that the profile's rare-source templates should have reached, with the template id from `research-method.md`.
4. **Status**: append a start line and a done line to `status.md`.

Write `check.md` in English. Write nothing else in the folder.
