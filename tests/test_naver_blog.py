import os

import pytest

from rek.adapters.naver_blog import decode_upload_date, decode_upload_time, full_size, parse, parse_post_url

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "naver_post_sample.html")
URL = "https://blog.naver.com/sampleblog/224456106651"


@pytest.fixture(scope="module")
def post():
    with open(FIXTURE, encoding="utf-8") as f:
        return parse(f.read(), URL)


def test_url_forms():
    assert parse_post_url(URL) == ("sampleblog", "224456106651")
    assert parse_post_url("https://m.blog.naver.com/sampleblog/224456106651") == ("sampleblog", "224456106651")
    assert parse_post_url("https://blog.naver.com/PostView.naver?blogId=sampleblog&logNo=224456106651") == ("sampleblog", "224456106651")
    with pytest.raises(ValueError):
        parse_post_url("https://example.com/x")


def test_title_author_date(post):
    assert post.title == "샘플 글 제목"
    assert post.author == "샘플작성자"  # the display name, not the platform badge
    assert post.published_at.startswith("2026. 10. 28.")


def test_body_in_reading_order(post):
    texts = [b.text for b in post.blocks if b.kind == "text"]
    assert texts[0].startswith("2026년 8월 31일")
    assert any(t.startswith("한줄 코멘트") for t in texts)
    assert "​" not in post.to_markdown()


def test_images_with_upload_dates(post):
    assert len(post.images) == 2
    # the first five images were uploaded 2026-09-02, i.e. reused from an earlier post
    assert [i.uploaded_on for i in post.images] == ["2026-09-02", "2026-10-28"]
    assert all(i.url.endswith("?type=w966") for i in post.images)


def test_upload_date_decoder():
    assert decode_upload_date("https://postfiles.pstatic.net/MjAyNTAyMTBfNTYg/MDAx.png?type=w80") == "2025-02-10"
    assert decode_upload_date("https://example.com/a.png") is None
    assert decode_upload_time("https://postfiles.pstatic.net/MjAyNjA5MDJfMTgz/MDAxNzg4Mjk4MjI2ODA5.aJ.png") == "2026-09-02T06:30:26+09:00"
    assert decode_upload_time("https://example.com/a.png") is None
    assert full_size("https://x.pstatic.net/a/b.png?type=w80_blur_webp") == "https://x.pstatic.net/a/b.png?type=w966"


def test_markdown_has_images_in_place(post):
    md = post.to_markdown()
    assert "![img_01 (uploaded 2026-09-02T06:30:26+09:00)" in md
    assert md.index("# 샘플 글 제목") < md.index("![img_01")


def test_caption_inside_se_module_div():
    doc = (
        '<title>t : 네이버 블로그</title><div class="se-main-container">'
        '<div class="se-component se-image se-l-default"><img class="se-image-resource" '
        'data-lazy-src="https://postfiles.pstatic.net/MjAyNjEwMjNfMjI1/MDAxNzkyNjgxOTg0MzY1.x.png?type=w80"/>'
        '<div class="se-module se-module-text se-caption"><p class="se-text-paragraph"><span>© CoolPubilcDomains, 출처 OGQ</span></p></div>'
        '</div></div>'
    )
    post = parse(doc, "https://blog.naver.com/x/1")
    assert post.images[0].caption == "© CoolPubilcDomains, 출처 OGQ"
