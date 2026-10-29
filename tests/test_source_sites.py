from rek.core.source_sites import parse_sources, registered_domain, render

SRC = """## S01 — 경향신문(최민지), 「제목」 (2026-10-27) [observed]
URL: https://khan.co.kr/article/1
Match: x
표시: 희귀 (도메인 khan.co.kr: 집합에 없음)

## S02 — 한겨레, 「제목」 (2026-10-27) [observed]
URL: https://supple.kr/news/abc (전재) / https://www.hani.co.kr/arti/2
표시: 바탕 (단위 3개)

## S03 — prior 123 (2026-09-02) [observed]
URL: https://blog.naver.com/x/123
표시: 바탕(저자 글) (저자)
"""


def test_registered_domain():
    assert registered_domain("https://n.news.naver.com/a") == "naver.com"
    assert registered_domain("https://www.khan.co.kr/x") == "khan.co.kr"
    assert registered_domain("https://mobile.busan.com/y") == "busan.com"
    assert registered_domain("not a url") is None


def test_ledger():
    sites = {}
    parse_sources(SRC, "r1", sites)
    assert set(sites) == {"khan.co.kr", "supple.kr", "hani.co.kr", "naver.com"}
    assert sites["khan.co.kr"].rare == 1 and sites["khan.co.kr"].upstream == 0
    assert sites["hani.co.kr"].upstream == 1 and sites["supple.kr"].upstream == 1
    assert sites["naver.com"].upstream == 0  # author's own post is not an upstream site
    table = render(sites)
    assert table.splitlines()[0].startswith("| 도메인 |") and "khan.co.kr" in table
