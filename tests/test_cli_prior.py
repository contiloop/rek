"""`rek prior` wiring with fake adapters: confirmation by image path, present/fetched/rejected statuses, meta.json merge."""
import datetime as dt
import json
import os

import rek.cli as cli
from rek.core.models import Block, Image, Post, PostSummary

IMG = "https://postfiles.pstatic.net/MjAyNjAxMDlfMTAg/MDAxNzY3OTE3Mzk4NDM1.abc.PNG/image.png?type=w966"
POSTS = [
    PostSummary("900", "고등어 이야기 (feat 노르웨이)", dt.date(2026, 10, 24)),  # the target
    PostSummary("800", "무관한 글", dt.date(2026, 1, 10)),  # in the date window, image not on page → rejected
    PostSummary("700", "고등어 이야기 2", dt.date(2026, 1, 9)),  # in the window and carries the image → confirmed
    PostSummary("600", "고등어 정식", dt.date(2025, 6, 1)),  # title route, already on disk
]


class FakeSource:
    def __init__(self):
        self.fetched = []

    def supports(self, url):
        return True

    def blog_of(self, url):
        return "blog"

    def post_url(self, blog_id, post_id):
        return f"https://x/{blog_id}/{post_id}"

    def fetch(self, url):
        post_id = url.rsplit("/", 1)[1]
        self.fetched.append(post_id)
        blocks = (Block(kind="image", image=Image(1, IMG, "2026-01-09", None)),) if post_id == "700" else ()
        raw = f'<html><img src="{IMG}"/></html>' if post_id == "700" else "<html>other</html>"
        return Post(url, post_id, f"post {post_id}", "a", "2026. 1. 9.", blocks), raw


class FakeList:
    def __init__(self):
        self.calls = []

    def list_posts(self, blog_id, until):
        self.calls.append((blog_id, until))
        return POSTS


def test_prior_command(tmp_path, monkeypatch, capsys):
    run = tmp_path / "900"
    (run / "prior" / "600").mkdir(parents=True)
    (run / "prior" / "600" / "meta.json").write_text("{}")
    meta = {
        "source_url": "https://x/blog/900", "post_id": "900", "title": "고등어 이야기 (feat 노르웨이)",
        "published_at": "2026. 10. 24. 0:10", "keep_me": 1,
        "images": [{"index": 1, "url": IMG, "uploaded_on": "2026-01-09", "uploaded_at": "2026-01-09T09:09:58+09:00"}],
    }
    (run / "meta.json").write_text(json.dumps(meta, ensure_ascii=False))
    source, post_list = FakeSource(), FakeList()
    monkeypatch.setattr(cli, "SOURCES", [source])
    monkeypatch.setattr(cli, "POST_LISTS", {FakeSource: lambda: post_list})

    assert cli.main(["prior", str(run), "--no-images"]) == 0
    assert post_list.calls == [("blog", None)]
    assert source.fetched == ["800", "700"]  # 600 is present: never re-fetched
    saved = json.loads((run / "meta.json").read_text())
    assert saved["keep_me"] == 1 and saved["title"] == meta["title"]
    ps = saved["prior_search"]
    assert ps["date_route"]["candidates"] == ["800", "700"]
    assert ps["date_route"]["confirmed"] == [{"post_id": "700", "image_indexes": [1]}]
    assert ps["date_route"]["rejected"][0]["post_id"] == "800" and "image" in ps["date_route"]["rejected"][0]["reason"]
    assert ps["title_route"]["kept"] == ["700", "600"]
    status = {c["post_id"]: c["status"] for c in ps["candidates"]}
    assert status == {"800": "rejected", "700": "fetched", "600": "present"}
    assert os.path.isfile(run / "prior" / "700" / "post.md") and not os.path.exists(run / "prior" / "800")
    assert "800 rejected" in capsys.readouterr().out
