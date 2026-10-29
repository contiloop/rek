import os

import pytest

from rek.adapters.naver_blog import decode_upload_date, full_size, parse, parse_post_url

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "naver_224456106651.html")
URL = "https://blog.naver.com/ranto28/224456106651"


@pytest.fixture(scope="module")
def post():
    with open(FIXTURE, encoding="utf-8") as f:
        return parse(f.read(), URL)


def test_url_forms():
    assert parse_post_url(URL) == ("ranto28", "224456106651")
    assert parse_post_url("https://m.blog.naver.com/ranto28/224456106651") == ("ranto28", "224456106651")
    assert parse_post_url("https://blog.naver.com/PostView.naver?blogId=ranto28&logNo=224456106651") == ("ranto28", "224456106651")
    with pytest.raises(ValueError):
        parse_post_url("https://example.com/x")


def test_title_author_date(post):
    assert post.title == "이란이 한국 장금상선에 조치를 취하겠다고 경고한 이유"
    assert post.author == "메르"
    assert post.published_at.startswith("2026. 10. 28.")


def test_body_in_reading_order(post):
    texts = [b.text for b in post.blocks if b.kind == "text"]
    assert texts[0].startswith("2026년 8월 31일")
    assert any(t.startswith("한줄 코멘트") for t in texts)
    assert "​" not in post.to_markdown()


def test_images_with_upload_dates(post):
    assert len(post.images) == 8
    # the first five images were uploaded 2026-09-02, i.e. reused from an earlier post
    assert [i.uploaded_on for i in post.images][:5] == ["2026-09-02"] * 5
    assert all(i.url.endswith("?type=w966") for i in post.images)


def test_upload_date_decoder():
    assert decode_upload_date("https://postfiles.pstatic.net/MjAyNTAyMTBfNTYg/MDAx.png?type=w80") == "2025-02-10"
    assert decode_upload_date("https://example.com/a.png") is None
    assert full_size("https://x.pstatic.net/a/b.png?type=w80_blur_webp") == "https://x.pstatic.net/a/b.png?type=w966"


def test_markdown_has_images_in_place(post):
    md = post.to_markdown()
    assert "![img_01 (uploaded 2026-09-02)" in md
    assert md.index("# 이란이") < md.index("![img_01")
