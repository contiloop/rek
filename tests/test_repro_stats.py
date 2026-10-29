from rek.core.repro_stats import compute

RESEARCH = """# research.md

| 번호 | 이름 | 방향 | 요약 | 출처 |
|---|---|---|---|---|
| R01 | 청어 붕괴 | 뒤쪽 | … | S01 |
| R02 | 북해 고등어 | 뒤쪽 | … | S01, S02 |
| R03 | 쿼터 | 본 주제 | … | S03 |
| R04 | 한국 수입가 | 앞쪽 | … | S04 |

## 못 찾은 것
- 없음

## 출처 목록
| 번호 | URL | 발행일 | 1차/2차 | 경로 |
|---|---|---|---|---|
| S01 | https://a | 2024-01-01 | 1차 | 검색 |
| S02 | https://b | 2026-07-02 | 2차(S01 인용) | 검색 |
| S03 | https://c | 2026-10-06 | 2차 | 검색 |
| S04 | https://d | 2026-05-10 | 1차 | 검색 |
"""

LOG = """# log.md
[검색] 00:01 노르웨이 고등어 쿼터
[열람] 00:02 https://a 2024-01-01
[검색] 00:03 Norwegian mackerel quota
[열람] 00:04 https://b
[접촉] 00:05 https://late 2026-10-25 날짜 확인 후 닫음
[크롬] 00:06 https://paywalled
"""


def test_counts():
    s = compute(RESEARCH, LOG)
    assert s.units == 4 and s.units_by_direction == {"뒤쪽": 2, "본 주제": 1, "앞쪽": 1}
    assert s.sources == 4 and s.primary == 2 and s.secondary == 2
    assert (s.searches, s.pages, s.chrome, s.contacts) == (2, 2, 1, 1)


def test_sources_only_counted_inside_section():
    s = compute("| S99 | x | y | 1차 | z |\n## 출처 목록\n| S01 | u | d | 2차 | p |\n", "")
    assert s.sources == 1 and s.secondary == 1


def test_unnumbered_url_list_counts_as_sources():
    research = "## 출처 목록 (URL, 발행일)\n\n1차\n- https://a.example/x | 2025-01-01 | 1차 | 검색\n- https://b.example/y | 2026-02-02 | 2차 | 검색\n"
    s = compute(research, "")
    assert s.sources == 2 and s.primary == 1 and s.secondary == 1
