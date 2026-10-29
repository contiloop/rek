import datetime as dt

from rek.core.models import PostSummary
from rek.core.prior import STOP_WORDS, earliest_needed, parse_published, plan, reused_images, title_words

PUB = "2026. 10. 24. 0:10"
META = {
    "post_id": "224450743987",
    "title": "고등어 이야기 (feat 노르웨이 고등어 vs 국산 고등어)",
    "published_at": PUB,
    "images": [
        {"index": 1, "uploaded_on": "2026-10-23", "uploaded_at": "2026-10-23T07:45:41+09:00"},
        {"index": 6, "uploaded_on": "2026-01-09", "uploaded_at": "2026-01-09T09:09:58+09:00"},
        {"index": 7, "uploaded_on": "2026-01-09", "uploaded_at": "2026-01-09T09:12:11+09:00"},
        {"index": 9, "uploaded_on": "2026-05-02", "uploaded_at": None},
        {"index": 10, "uploaded_on": None, "uploaded_at": None},
    ],
}


def P(post_id, title, y, m, d):
    return PostSummary(post_id=post_id, title=title, date=dt.date(y, m, d))


POSTS = [
    P("224451942631", "미국국채 10년물이 4%대로 낮아진 비밀", 2026, 10, 24),
    P("224450743987", "고등어 이야기 (feat 노르웨이 고등어 vs 국산 고등어)", 2026, 10, 24),
    P("224450027915", "7만 전자, 20만 닉스 간다는 주장에 팩트체크를 해보자", 2026, 10, 23),
    P("224272172681", "주절주절..오랜만에 부산..친구와 만남..안금무와 고등어구이", 2026, 5, 2),
    P("224271000000", "무관한 글", 2026, 5, 4),
    P("224270000000", "무관한 글 2", 2026, 5, 5),
    P("224140130757", "고등어 이야기 2 (feat 노르웨이고등어, 참고등어, 망치고등어)", 2026, 1, 9),
    P("224139000000", "국산 반도체 이야기", 2026, 1, 7),
    P("223737564971", "주절주절... 게시중단... 미세먼지... 고등어 정식", 2025, 1, 24),
    P("224460000000", "고등어 이야기 3", 2026, 10, 30),  # later than the target: never a prior
]


def test_parse_published():
    assert parse_published(PUB) == dt.datetime(2026, 10, 24, 0, 10)
    assert parse_published("2026. 10. 2. 0:10") == dt.datetime(2026, 10, 2, 0, 10)
    assert parse_published("2025. 2. 11.") == dt.datetime(2025, 2, 11, 0, 0)
    assert parse_published(None) is None


def test_reused_images_skips_uploads_within_the_writing_window():
    # the image uploaded the evening before a 0:10 publication belongs to this post, not an earlier one
    assert [i["index"] for i in reused_images(META)] == [6, 7, 9]
    assert earliest_needed(META) == dt.date(2026, 1, 7)  # 2026-01-09 minus 2 days
    assert earliest_needed({"published_at": PUB, "images": []}) is None


def test_title_words():
    assert title_words("고등어 이야기 (feat 노르웨이 고등어 vs 국산 고등어)") == ["고등어", "노르웨", "국산"]
    assert title_words("이란이 한국 장금상선에 조치를 취하겠다고 경고한 이유") == ["이란", "장금상선", "조치", "취하겠다고", "경고한"]
    assert title_words("알래스카 LNG 프로젝트에 대해 알아보자") == ["알래스카", "LNG"]
    assert title_words("7만 전자, 20만 닉스 간다는 주장") == ["전자", "닉스", "간다", "주장"]
    assert "한국" in STOP_WORDS and "feat" in STOP_WORDS


def test_plan_both_routes():
    p = plan(META, POSTS)
    assert [w["uploaded_on"] for w in p.date_route["windows"]] == ["2026-01-09", "2026-05-02"]
    assert p.date_route["windows"][0]["image_indexes"] == [6, 7]
    assert p.date_route["windows"][0]["from"] == "2026-01-07" and p.date_route["windows"][0]["to"] == "2026-01-11"
    assert p.date_route["windows"][0]["matches"] == ["224140130757", "224139000000"]
    assert p.date_route["found"] == ["224272172681", "224271000000", "224140130757", "224139000000"]
    assert p.title_route["words"] == ["고등어", "노르웨", "국산"]
    assert p.title_route["found"] == ["224272172681", "224140130757", "224139000000", "223737564971"]
    # union, deduped, the target itself and later posts excluded
    assert [c.post_id for c in p.candidates] == ["224272172681", "224271000000", "224140130757", "224139000000", "223737564971"]
    both = next(c for c in p.candidates if c.post_id == "224140130757")
    assert both.routes == ["date", "title"]
    assert p.as_record()["published_on"] == "2026-10-24"
    assert p.as_record()["candidates"][0]["post_id"] == "224272172681"


def test_plan_without_title_words_or_images():
    p = plan({"post_id": "1", "title": "한국 이야기", "published_at": PUB, "images": []}, POSTS)
    assert p.candidates == [] and p.title_route["words"] == [] and p.date_route["windows"] == []
