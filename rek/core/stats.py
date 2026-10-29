"""Form statistics of a post body. Pure functions over the markdown `rek fetch` writes.

Used by the style analyst (to state a rule with numbers) and the verifier (to compare a
reconstruction with the original using the same numbers), so both sides measure identically.
"""
from __future__ import annotations

import re
from dataclasses import asdict, dataclass

_NUMBERED = re.compile(r"^\s*(\d+)\s*[.)]\s*(.*)$")
_IMAGE = re.compile(r"^!\[")
_META = re.compile(r"^(#|- source:|- post_id:|- author:|- published_at:)")
_SPLIT = re.compile(r"(?<=[.!?。])\s+|\n")
_NOUN_END = re.compile(r"(임|함|됨|것임|이었음|했음|있음|없음|같음|음)\s*[.!?]?$")
_DA_END = re.compile(r"(다|까)\s*[.!?]?$")
_NUMBER = re.compile(r"\d[\d,.]*\s*(?:%|kg|km|톤|달러|억|만|천|배럴|척|석|년|월|일|㎥|cm)?")
_ONE_LINER = re.compile(r"^\s*한\s*줄\s*코멘트")
NOTES_HEADING = "## 작성 노트"  # the writer's notes after the body: never part of the form statistics


@dataclass(frozen=True)
class FormStats:
    sentences: int
    numbered_items: int
    max_item_number: int
    numbering_gaps: list[int]
    mean_sentence_chars: float
    noun_ending_share: float  # ~임/~함/~됨 register
    da_ending_share: float  # ~다 register
    sentences_with_number_share: float
    images: int
    has_one_liner: bool
    one_liner_chars: int
    first_line: str


def body_text(markdown: str) -> str:
    """The body alone: everything before the writer's notes heading."""
    lines = markdown.splitlines()
    for i, line in enumerate(lines):
        if line.strip() == NOTES_HEADING:
            lines = lines[:i]
            break
    return "\n".join(lines)


def paragraphs(markdown: str) -> list[list[str]]:
    """Body lines grouped by blank-line-separated paragraph, metadata lines dropped."""
    out: list[list[str]] = []
    current: list[str] = []
    for line in body_text(markdown).splitlines():
        if not line.strip():
            if current:
                out.append(current)
            current = []
            continue
        if _META.match(line):
            continue
        current.append(line.rstrip())
    if current:
        out.append(current)
    return out


def body_lines(markdown: str) -> list[str]:
    return [line for para in paragraphs(markdown) for line in para]


def sentences_of(paras: list[list[str]]) -> list[str]:
    sents: list[str] = []
    for para in paras:
        for i, line in enumerate(para):
            if _IMAGE.match(line):
                continue
            if _ONE_LINER.match(line):
                # the closing one-liner is one unit however many periods or lines it has: it runs to the end of its paragraph
                sents.append("\n".join(l.strip() for l in para[i:]))
                break
            line = _NUMBERED.sub(r"\2", line)  # "12. text" → "text", so the number is not a sentence
            for s in _SPLIT.split(line):
                s = s.strip()
                if s:
                    sents.append(s)
    return sents


def compute(markdown: str) -> FormStats:
    paras = paragraphs(markdown)
    lines = [line for para in paras for line in para]
    sents = sentences_of(paras)
    numbers = [int(m.group(1)) for line in lines if (m := _NUMBERED.match(line))]
    max_n = max(numbers) if numbers else 0
    gaps = sorted(set(range(1, max_n + 1)) - set(numbers)) if numbers else []
    n = len(sents) or 1
    noun = sum(1 for s in sents if _NOUN_END.search(s))
    da = sum(1 for s in sents if _DA_END.search(s))
    with_num = sum(1 for s in sents if _NUMBER.search(s))
    one = [s for s in sents if _ONE_LINER.match(s)]
    text_lines = [l for l in lines if not _IMAGE.match(l)]
    return FormStats(
        sentences=len(sents),
        numbered_items=len(numbers),
        max_item_number=max_n,
        numbering_gaps=gaps,
        mean_sentence_chars=round(sum(len(s) for s in sents) / n, 1),
        noun_ending_share=round(noun / n, 2),
        da_ending_share=round(da / n, 2),
        sentences_with_number_share=round(with_num / n, 2),
        images=sum(1 for l in lines if _IMAGE.match(l)),
        has_one_liner=bool(one),
        one_liner_chars=len(one[0]) if one else 0,
        first_line=text_lines[0][:60] if text_lines else "",
    )


def as_dict(stats: FormStats) -> dict:
    return asdict(stats)
