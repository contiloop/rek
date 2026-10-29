import datetime as dt
import os

from rek.adapters.naver_blog import parse_post_list

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "naver_postlist_ranto28_p1.json")
TODAY = dt.date(2026, 10, 29)


def test_parse_real_page():
    with open(FIXTURE, encoding="utf-8") as f:
        posts = parse_post_list(f.read(), today=TODAY)
    assert len(posts) == 30
    assert posts[0].post_id == "224457360826"
    assert posts[0].title == "구글 실적쇼크 뜯어보기"
    assert posts[0].date == TODAY  # "15시간 전"
    assert posts[3].post_id == "224456106651" and posts[3].date == dt.date(2026, 10, 28)
    assert posts[14].title == "고등어 이야기 (feat 노르웨이 고등어 vs 국산 고등어)"
    assert posts[-1].date == dt.date(2026, 10, 16)


def test_parse_relative_dates_and_escapes():
    body = (
        '{"resultCode":"S","postList":[{"logNo":"1","title":"a+b","addDate":"3일 전"},'
        '{"logNo":"2","title":"c%27d","addDate":"방금 전"}],"pagingHtml":"<a class=\\\'x\\\'>"}'
    )
    posts = parse_post_list(body, today=TODAY)
    assert [(p.post_id, p.title, p.date) for p in posts] == [
        ("1", "a b", dt.date(2026, 10, 26)),
        ("2", "c'd", TODAY),
    ]
    assert parse_post_list('{"resultCode":"S","postList":[]}', today=TODAY) == []
