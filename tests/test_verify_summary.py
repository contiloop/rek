import os

import pytest

from rek.core.verify_summary import KEYS, evaluate, latest_verification, parse_front_matter, render, summarize

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "verification_example.md")


def read_fixture():
    with open(FIXTURE, encoding="utf-8") as f:
        return f.read()


def test_parse_front_matter_reads_all_keys():
    d = parse_front_matter(read_fixture())
    assert set(d) == set(KEYS)
    assert d["units_total"] == 12 and d["units_found"] == 11
    assert d["profile_hash"] == "ab12cd34ef56" and d["verifier_verdict"] == "pass"
    assert parse_front_matter("no yaml here") == {}


def test_evaluate_passing_example():
    r = evaluate(parse_front_matter(read_fixture()))
    assert r.passed and r.verdict == "pass"
    assert r.checks == {"units": True, "rare": True, "upstream": True, "fabricated": True}
    assert r.mismatch is False


def base():
    return parse_front_matter(read_fixture())


@pytest.mark.parametrize(
    "change, failing",
    [
        ({"units_found": 10}, "units"),  # 10/12 < 0.90
        ({"units_total": 0, "units_found": 0}, "units"),
        ({"rare_found": 3}, "rare"),  # 3/5 < 0.80
        ({"upstream_found": 1}, "upstream"),
        ({"fabricated": 1}, "fabricated"),
    ],
)
def test_evaluate_failures(change, failing):
    r = evaluate({**base(), **change})
    assert not r.passed and r.checks[failing] is False
    assert r.mismatch is True  # the file still says pass


def test_thresholds_include_equality():
    assert evaluate({**base(), "units_total": 10, "units_found": 9}).checks["units"] is True
    assert evaluate({**base(), "rare_total": 5, "rare_found": 4}).checks["rare"] is True
    assert evaluate({**base(), "rare_total": 0, "rare_found": 0}).checks["rare"] is True
    assert evaluate({**base(), "upstream_total": 0, "upstream_found": 0}).checks["upstream"] is True
    r = evaluate({**base(), "units_total": 0})
    assert r.reason == "단위 없음"


def test_missing_keys_is_incomplete():
    d = base()
    del d["fabricated"]
    r = evaluate(d)
    assert not r.passed and r.verdict == "미실행/불완전"
    r = evaluate({})
    assert not r.passed and r.verdict == "미실행/불완전"


def make_runs(tmp_path):
    good = tmp_path / "111"
    (good / "repro" / "1").mkdir(parents=True)
    (good / "repro" / "3").mkdir(parents=True)
    (good / "meta.json").write_text("{}")
    (good / "repro" / "1" / "verification.md").write_text(read_fixture().replace("fabricated: 0", "fabricated: 2"))
    (good / "repro" / "3" / "verification.md").write_text(read_fixture())
    bare = tmp_path / "222"
    bare.mkdir()
    (bare / "meta.json").write_text("{}")
    (tmp_path / "not_a_run").mkdir()  # no meta.json: ignored
    return tmp_path


def test_latest_verification_picks_highest_number(tmp_path):
    make_runs(tmp_path)
    assert latest_verification(str(tmp_path / "111")) == str(tmp_path / "111" / "repro" / "3" / "verification.md")
    assert latest_verification(str(tmp_path / "222")) is None


def test_summarize_tree(tmp_path):
    rows, all_pass = summarize(str(make_runs(tmp_path)))
    assert [r.run_id for r in rows] == ["111", "222"]
    assert rows[0].result.passed and rows[1].result.verdict == "미실행/불완전"
    assert all_pass is False
    text = render(rows, all_pass)
    assert "111" in text and "11/12" in text and "ab12cd34ef56" in text and "미실행/불완전" in text
    assert text.rstrip().splitlines()[-1].startswith("전체:")


def test_summarize_all_pass(tmp_path):
    make_runs(tmp_path)
    import shutil

    shutil.rmtree(tmp_path / "222")
    rows, all_pass = summarize(str(tmp_path))
    assert all_pass is True and len(rows) == 1


def test_cli_exit_codes(tmp_path, capsys):
    from rek.cli import main

    make_runs(tmp_path)
    assert main(["verify-summary", str(tmp_path)]) == 1
    out = capsys.readouterr().out
    assert "불일치" not in out and "미실행/불완전" in out
    import shutil

    shutil.rmtree(tmp_path / "222")
    assert main(["verify-summary", str(tmp_path)]) == 0


def test_mismatch_is_displayed(tmp_path, capsys):
    from rek.cli import main

    run = tmp_path / "333"
    (run / "repro" / "2").mkdir(parents=True)
    (run / "meta.json").write_text("{}")
    (run / "repro" / "2" / "verification.md").write_text(read_fixture().replace("fabricated: 0", "fabricated: 1"))
    assert main(["verify-summary", str(tmp_path)]) == 1
    assert "불일치" in capsys.readouterr().out
