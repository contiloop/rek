from rek.core.stats import compute

SAMPLE = """# 제목

- source: x
- published_at: y

늘 그렇듯이, 돌아갑니다.

1. 노르웨이는 청어의 나라였음.
2. 1960년이 되자, 청어가 멸종 직전까지 가게 된 것임.

![img_01 (uploaded 2026-01-09)](images/img_01.png)

4. EU의 1인당 고등어 소비량은 연 0.67kg임.
이란이 가만히 있지 않았다.
한줄 코멘트. 내년 여름까지 비쌀 예정임.
"""


def test_counts_and_register():
    s = compute(SAMPLE)
    assert s.numbered_items == 3 and s.max_item_number == 4 and s.numbering_gaps == [3]
    assert s.images == 1
    assert s.has_one_liner and s.one_liner_chars > 0
    assert s.sentences == 6
    assert s.noun_ending_share == round(4 / 6, 2)  # 였음, 것임, 임, 예정임
    assert s.da_ending_share == round(2 / 6, 2)  # 돌아갑니다, 않았다
    assert 0 < s.sentences_with_number_share < 1
    assert s.first_line.startswith("늘 그렇듯이")


def test_empty():
    s = compute("# t\n")
    assert s.sentences == 0 and s.numbered_items == 0 and s.numbering_gaps == []


def test_stops_at_writing_notes():
    md = SAMPLE + "\n## 작성 노트\n\n1. 이 글은 테스트임.\n2. 둘째 메모임.\n\n세 번째 문장이다.\n"
    assert compute(md) == compute(SAMPLE)
    s = compute(SAMPLE + "\n## 작성 노트\n")
    assert s.numbered_items == 3 and s.sentences == 6


def test_one_liner_paragraph_is_one_unit_across_lines():
    md = "# t\n\n첫 문장임.\n\n한줄 코멘트. 첫째 문장임. 둘째 문장임.\n셋째 줄도 이어짐. 넷째 문장임.\n\n이건 다른 문단이다.\n"
    s = compute(md)
    assert s.sentences == 3
    assert s.has_one_liner and s.one_liner_chars == len("한줄 코멘트. 첫째 문장임. 둘째 문장임.\n셋째 줄도 이어짐. 넷째 문장임.")
