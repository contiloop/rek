import datetime as dt
import os

from rek.cli import main
from rek.core import research
from rek.core.verify_summary import INCOMPLETE

RESEARCH = """| 번호 | 이름 | 방향 | 요약 | 출처 |
|---|---|---|---|---|
| R01 | a | 뒤쪽 | … | S01 |
| R02 | b | 본 주제 | … | S02 |
| R03 | c | 앞쪽 | … | S03 |

## 출처 목록
| 번호 | URL | 발행일 | 1차/2차 | 경로 |
|---|---|---|---|---|
""" + "".join(f"| S{i:02d} | https://x/{i} | 2026-01-01 | {'1차' if i <= 6 else '2차'} | 검색 |\n" for i in range(1, 23))

CHECK = "```yaml\nfabricated: {fab}\nlate_sources: {late}\nchecker_verdict: {v}\n```\n"


def write(d, name, text):
    with open(os.path.join(d, name), "w", encoding="utf-8") as f:
        f.write(text)


def test_slug_and_folder_name():
    now = dt.datetime(2026, 10, 30, 9, 0)
    assert research.folder_name("알래스카 LNG 프로젝트", now) == "20261030-알래스카-lng-프로젝트"
    assert research.slug("  --  ") == "topic"


def test_topic_lines_order_and_none_trigger():
    text = research.topic_lines("t", "", "2026-10-30 09:00 KST", "Korean", "/p")
    assert text.splitlines() == ["main_topic: t", "trigger: none", "date: 2026-10-30 09:00 KST", "language: Korean", "profile: /p"]


def test_evaluate_pass_fail_incomplete():
    stats = {"units_by_direction": {"뒤쪽": 1, "본 주제": 1, "앞쪽": 1}, "sources": 22, "primary": 6}
    assert research.evaluate(stats, {"fabricated": 0, "late_sources": 0, "checker_verdict": "pass"}).passed
    v = research.evaluate(stats, {"fabricated": 1, "late_sources": 0, "checker_verdict": "pass"})
    assert v.verdict == "fail" and v.checks["fabricated"] is False and "fabricated" in v.reason
    v = research.evaluate({"units_by_direction": {"뒤쪽": 1}, "sources": 3, "primary": 0}, {"fabricated": 0, "late_sources": 2, "checker_verdict": "fail"})
    assert v.verdict == "fail" and v.reason.startswith("chain incomplete, too few sources, source after date")
    assert research.evaluate(None, {}).verdict == INCOMPLETE
    assert research.evaluate(stats, {"fabricated": 0}).verdict == INCOMPLETE


def test_summarize_folder_and_cli(tmp_path, capsys):
    d = str(tmp_path)
    write(d, "research.md", RESEARCH)
    write(d, "log.md", "[검색] 09:00 q\n")
    assert research.summarize(d).verdict == INCOMPLETE
    write(d, "check.md", CHECK.format(fab=0, late=0, v="pass"))
    assert main(["research-summary", d]) == 0
    assert "pass (chain 1/1/1, sources 22 (6 primary)" in capsys.readouterr().out
    write(d, "check.md", CHECK.format(fab=0, late=0, v="fail"))
    assert main(["research-summary", d]) == 0
    assert "불일치" in capsys.readouterr().out


def test_research_init_creates_topic_and_hash(tmp_path, capsys):
    profile = tmp_path / "profiles" / "p"
    profile.mkdir(parents=True)
    (profile / "SKILL.md").write_text("s", encoding="utf-8")
    (profile / "research-method.md").write_text("m", encoding="utf-8")
    out = tmp_path / "research" / "x"
    assert main(["research-init", "알래스카 LNG", "--trigger", "미국이 참여를 요청했다", "--profile", str(profile), "--out", str(out)]) == 0
    assert capsys.readouterr().out.strip() == str(out)
    topic = (out / "topic.md").read_text(encoding="utf-8").splitlines()
    assert topic[0] == "main_topic: 알래스카 LNG" and topic[1] == "trigger: 미국이 참여를 요청했다"
    assert topic[2].startswith("date: ") and topic[2].endswith(" KST") and topic[3] == "language: Korean"
    assert topic[4] == f"profile: {profile}"
    assert len((out / "profile_hash.txt").read_text().strip()) == 12
    assert main(["research-init", "x", "--profile", str(profile), "--out", str(out)]) == 2
    assert main(["research-init", "x", "--profile", str(tmp_path / "nope"), "--out", str(out)]) == 2
