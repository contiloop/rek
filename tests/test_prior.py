import datetime as dt

from rek.core.models import PostSummary
from rek.core.prior import (
    STOP_WORDS, TITLE_KEEP, confirm, earliest_needed, image_path, parse_published, plan, reused_image_paths,
    reused_images, title_tokens, title_words,
)

PUB = "2026. 10. 24. 0:10"
IMG6 = "https://postfiles.pstatic.net/MjAyNjAxMDlfMTAg/MDAxNzY3OTE3Mzk4NDM1.abc.PNG/image.png?type=w966"
IMG9 = "https://postfiles.pstatic.net/MjAyNjA1MDJfMjEg/MDAxNzc3NzA1MjQ1MTIw.def.JPEG/x.jpg?type=w966"
META = {
    "post_id": "224450743987",
    "title": "고등어 이야기 (feat 노르웨이 고등어 vs 국산 고등어)",
    "published_at": PUB,
    "images": [
        {"index": 1, "url": "https://postfiles.pstatic.net/MjAyNjEwMjNfMQ/MDAx.png?type=w966", "uploaded_on": "2026-10-23", "uploaded_at": "2026-10-23T07:45:41+09:00"},
        {"index": 6, "url": IMG6, "uploaded_on": "2026-01-09", "uploaded_at": "2026-01-09T09:09:58+09:00"},
        {"index": 7, "url": IMG6.replace("image.png", "image2.png"), "uploaded_on": "2026-01-09", "uploaded_at": "2026-01-09T09:12:11+09:00"},
        {"index": 9, "url": IMG9, "uploaded_on": "2026-05-02", "uploaded_at": None},
        {"index": 10, "url": "https://example.com/plain.png", "uploaded_on": None, "uploaded_at": None},
    ],
}


def P(post_id, title, y, m, d):
    return PostSummary(post_id=post_id, title=title, date=dt.date(y, m, d))


POSTS = [
    P("224451942631", "미국국채 10년물이 4%대로 낮아진 비밀", 2026, 10, 24),
    P("224450743987", "고등어 이야기 (feat 노르웨이 고등어 vs 국산 고등어)", 2026, 10, 24),
    P("224450027915", "7만 전자, 20만 닉스 간다는 주장에 팩트체크를 해보자", 2026, 10, 23),
    P("224272172681", "주절주절..오랜만에 부산..친구와 만남..안금무와 고등어구이", 2026, 5, 2),  # 고등어구이 is not the token 고등어
    P("224271000000", "무관한 글", 2026, 5, 4),
    P("224270000000", "무관한 글 2", 2026, 5, 5),
    P("224140130757", "고등어 이야기 2 (feat 노르웨이고등어, 참고등어, 망치고등어)", 2026, 1, 9),
    P("224139000000", "국산 반도체 이야기", 2026, 1, 7),
    P("224100000000", "중국산 철강 이야기", 2025, 12, 1),  # 중국산 contains 국산 but is another token
    P("223737564971", "주절주절... 게시중단... 미세먼지... 고등어 정식", 2025, 1, 24),
    P("223400000000", "고등어 정식 옛날 글", 2023, 5, 29),  # older than the title-route age window
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


def test_image_paths_and_confirmation():
    assert image_path(IMG6) == "MjAyNjAxMDlfMTAg/MDAxNzY3OTE3Mzk4NDM1.abc.PNG/image.png"
    assert image_path("https://example.com/plain.png") == "plain.png"
    paths = reused_image_paths(META)
    assert paths == {
        "MjAyNjAxMDlfMTAg/MDAxNzY3OTE3Mzk4NDM1.abc.PNG/image.png": [6],
        "MjAyNjAxMDlfMTAg/MDAxNzY3OTE3Mzk4NDM1.abc.PNG/image2.png": [7],
        "MjAyNjA1MDJfMjEg/MDAxNzc3NzA1MjQ1MTIw.def.JPEG/x.jpg": [9],
    }
    page = '<img src="https://blogfiles.pstatic.net/MjAyNjAxMDlfMTAg/MDAxNzY3OTE3Mzk4NDM1.abc.PNG/image.png?type=w80"/>'
    assert confirm(page, paths) == [6]
    assert confirm("<html>nothing reused</html>", paths) == []


def test_title_words_and_tokens():
    assert title_words("고등어 이야기 (feat 노르웨이 고등어 vs 국산 고등어)") == ["고등어", "노르웨", "국산"]
    assert title_words("이란이 한국 장금상선에 조치를 취하겠다고 경고한 이유") == ["이란", "장금상선", "조치", "취하겠다고", "경고한"]
    assert title_words("알래스카 LNG 프로젝트에 대해 알아보자") == ["알래스카", "LNG"]
    assert title_words("7만 전자, 20만 닉스 간다는 주장") == ["전자", "닉스", "간다", "주장"]
    assert title_tokens("중국산 철강 이야기 (feat 노르웨이)") == ["중국산", "철강", "이야기", "feat", "노르웨"]
    assert "한국" in STOP_WORDS and "feat" in STOP_WORDS


def test_plan_both_routes():
    p = plan(META, POSTS)
    assert [w["uploaded_on"] for w in p.date_route["windows"]] == ["2026-01-09", "2026-05-02"]
    assert p.date_route["windows"][0]["image_indexes"] == [6, 7]
    assert p.date_route["windows"][0]["from"] == "2026-01-07" and p.date_route["windows"][0]["to"] == "2026-01-11"
    assert p.date_route["windows"][0]["matches"] == ["224140130757", "224139000000"]
    assert p.date_route["candidates"] == ["224272172681", "224271000000", "224140130757", "224139000000"]
    assert p.title_route["words"] == ["고등어", "노르웨", "국산"]
    assert p.title_route["matches"] == {"고등어": ["224140130757", "223737564971", "223400000000"], "노르웨": [], "국산": ["224139000000"]}
    assert p.title_route["found"] == ["224140130757", "224139000000", "223737564971", "223400000000"]
    assert p.title_route["kept"] == ["224140130757", "224139000000", "223737564971"]  # the 2023 post is too old
    # union, deduped, the target itself and later posts excluded; date candidates still need confirmation
    assert [(c.post_id, c.routes) for c in p.candidates] == [
        ("224272172681", ["date"]), ("224271000000", ["date"]), ("224140130757", ["date", "title"]),
        ("224139000000", ["date", "title"]), ("223737564971", ["title"]),
    ]
    rec = p.as_record()
    assert rec["published_on"] == "2026-10-24" and rec["candidates"][0]["post_id"] == "224272172681"
    assert rec["title_route"]["keep"] == TITLE_KEEP


def test_title_route_keeps_the_most_recent_matches():
    posts = [P(str(300 - i), f"고등어 글 {i}", 2026, 10, 1 + (20 - i) % 20) for i in range(20)]
    p = plan({"post_id": "x", "title": "고등어 이야기", "published_at": PUB, "images": []}, posts)
    assert len(p.title_route["found"]) == 20 and len(p.title_route["kept"]) == TITLE_KEEP
    kept = [c for c in p.candidates]
    assert len(kept) == TITLE_KEEP
    assert all(kept[i].post.date >= kept[i + 1].post.date for i in range(len(kept) - 1))


def test_plan_without_title_words_or_images():
    p = plan({"post_id": "1", "title": "한국 이야기", "published_at": PUB, "images": []}, POSTS)
    assert p.candidates == [] and p.title_route["words"] == [] and p.date_route["windows"] == []
