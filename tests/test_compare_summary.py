import os
import re

from rek.cli import main
from rek.core.compare_summary import KEYS, OLD_KEYS, line, parse, row

HERE = os.path.dirname(__file__)
FIXTURE = os.path.join(HERE, "fixtures", "comparison_example.md")
BRIEF = os.path.join(HERE, "..", "skills", "rek", "references", "comparator.md")
TAIL = "| units 7/12 | facts 14/30 (conflict 2) | fabricated 0 | extra 3 | valid | ab12cd34ef56"
EXPECTED = "111 | pass | depth back 5→6, forward 4→4 " + TAIL
OLD = """```yaml
units_total: 12
units_covered: 7
facts_total: 30
facts_matched: 14
facts_conflicting: 2
fabricated: 0
depth_original: 9
depth_repro: 6
extra_units: 3
invalid: 0
profile_hash: ab12cd34ef56
```

# Comparison
"""
OLD_EXPECTED = ("111 | old format, no verdict | units 7/12 | facts 14/30 (conflict 2) | fabricated 0 | depth 9→6 "
                "| extra 3 | valid | ab12cd34ef56")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def fixture(**values):
    """The fixture with some yaml values replaced."""
    text = read(FIXTURE)
    for key, value in values.items():
        text, n = re.subn(rf"^{key}: .*$", f"{key}: {value}", text, count=1, flags=re.M)
        assert n == 1, key
    return text


def with_invalid_line(text, reason="S03 read after date"):
    return text.replace("```\n\n", f"```\n무효: {reason}\n\n", 1)


def yaml_block(text):
    m = re.search(r"^```yaml\n.*?^```\n", text, re.S | re.M)
    assert m, "no yaml block"
    return m.group(0).encode("utf-8")


def test_keys_in_order():
    assert KEYS == ("units_total", "units_covered", "facts_total", "facts_matched", "facts_conflicting", "fabricated",
                    "depth_back_original", "depth_back_repro", "depth_forward_original", "depth_forward_repro",
                    "extra_units", "invalid", "profile_hash")
    assert OLD_KEYS == ("units_total", "units_covered", "facts_total", "facts_matched", "facts_conflicting",
                        "fabricated", "depth_original", "depth_repro", "extra_units", "invalid", "profile_hash")


def test_fixture_starts_with_the_block():
    text = read(FIXTURE)
    assert text.startswith("```yaml\n")
    d = parse(text)
    assert list(d) == list(KEYS)
    assert d["units_total"] == 12 and d["invalid"] == 0 and d["profile_hash"] == "ab12cd34ef56"


def test_fixture_body_has_sections_1_to_8():
    text = read(FIXTURE)
    for n in range(1, 9):
        assert re.search(rf"^## {n}\. ", text, re.M), n
    assert "Failure routing" in text


def test_brief_block_is_byte_identical_to_fixture():
    assert yaml_block(read(BRIEF)) == yaml_block(read(FIXTURE))


def test_pass_line():
    r = row("111", read(FIXTURE))
    assert r.line == EXPECTED and r.verdict == "pass"
    assert line("111", read(FIXTURE)) == EXPECTED


def test_equal_depth_passes():
    r = row("111", fixture(depth_back_repro=5, depth_forward_repro=4))
    assert r.verdict == "pass"
    assert r.line == "111 | pass | depth back 5→5, forward 4→4 " + TAIL


def test_invalid_fails_alone():
    r = row("111", with_invalid_line(fixture(invalid=1)))
    assert r.verdict == "fail"
    assert r.line == ("111 | fail (valid) | depth back 5→6, forward 4→4 | units 7/12 | facts 14/30 (conflict 2) "
                      "| fabricated 0 | extra 3 | invalid | ab12cd34ef56")


def test_fabricated_fails_alone():
    r = row("111", fixture(fabricated=2))
    assert r.verdict == "fail"
    assert r.line.startswith("111 | fail (fabricated) | depth back 5→6, forward 4→4 |")
    assert "| fabricated 2 |" in r.line


def test_depth_back_fails_alone():
    r = row("111", fixture(depth_back_repro=4))
    assert r.verdict == "fail"
    assert r.line == "111 | fail (depth_back) | depth back 5→4, forward 4→4 " + TAIL


def test_depth_forward_fails_alone():
    r = row("111", fixture(depth_forward_repro=3))
    assert r.verdict == "fail"
    assert r.line == "111 | fail (depth_forward) | depth back 5→6, forward 4→3 " + TAIL


def test_failed_names_in_fixed_order():
    r = row("111", fixture(depth_back_repro=1, fabricated=3))
    assert r.line.startswith("111 | fail (fabricated, depth_back) |")
    r = row("111", with_invalid_line(fixture(depth_forward_repro=0, depth_back_repro=0, fabricated=1, invalid=1)))
    assert r.line.startswith("111 | fail (valid, fabricated, depth_back, depth_forward) |")


def test_units_facts_and_extra_never_decide():
    r = row("111", fixture(units_covered=0, facts_matched=0, facts_conflicting=30, extra_units=0))
    assert r.verdict == "pass"


def test_old_format_has_no_verdict():
    r = row("111", OLD)
    assert r.line == OLD_EXPECTED and r.verdict is None


def test_missing_key_is_incomplete():
    text = read(FIXTURE).replace("extra_units: 3\n", "")
    assert line("111", text) == "111 | 미실행/불완전"
    assert row("111", text).verdict is None
    assert line("111", "no yaml") == "111 | 미실행/불완전"
    assert line("111", fixture(depth_back_repro="six")) == "111 | 미실행/불완전"  # not an integer: missing
    assert line("111", read(FIXTURE).replace("depth_forward_repro: 4\n", "")) == "111 | 미실행/불완전"
    assert line("111", OLD.replace("depth_repro: 6\n", "")) == "111 | 미실행/불완전"
    mixed = OLD.replace("extra_units: 3\n", "depth_back_original: 5\nextra_units: 3\n")  # old keys plus part of the new
    assert line("111", mixed) == "111 | 미실행/불완전"


def test_invalid_line_decides():
    out = line("111", with_invalid_line(fixture(invalid=1)))
    assert out.endswith("| invalid | ab12cd34ef56") and "불일치" not in out


def test_key_disagreeing_with_line_is_flagged():
    r = row("111", with_invalid_line(read(FIXTURE), "author blog opened"))
    assert "| invalid 불일치 |" in r.line and r.line.startswith("111 | fail (valid) |")
    r = row("111", fixture(invalid=1))
    assert "| valid 불일치 |" in r.line and r.verdict == "pass"
    assert "| valid 불일치 |" in line("111", OLD.replace("invalid: 0", "invalid: 1"))


def make_runs(tmp_path):
    run = tmp_path / "111"
    for n in ("1", "2", "10"):
        (run / "repro" / n).mkdir(parents=True)
    (run / "meta.json").write_text("{}")
    (run / "repro" / "1" / "comparison.md").write_text(fixture(fabricated=5), encoding="utf-8")
    (run / "repro" / "2" / "comparison.md").write_text(fixture(depth_back_repro=0), encoding="utf-8")
    (run / "repro" / "10" / "comparison.md").write_text(read(FIXTURE), encoding="utf-8")
    bare = tmp_path / "222"
    (bare / "repro" / "1").mkdir(parents=True)  # a reproduction without comparison.md: skipped
    (bare / "meta.json").write_text("{}")
    other = tmp_path / "333"
    (other / "repro" / "1").mkdir(parents=True)  # no meta.json: not a run
    (other / "repro" / "1" / "comparison.md").write_text(fixture(fabricated=5), encoding="utf-8")
    return tmp_path


def add_run(tmp_path, run_id, text):
    run = tmp_path / run_id
    (run / "repro" / "1").mkdir(parents=True)
    (run / "meta.json").write_text("{}")
    (run / "repro" / "1" / "comparison.md").write_text(text, encoding="utf-8")


def test_cli_one_line_per_run_largest_n_exit_0(tmp_path, capsys):
    make_runs(tmp_path)
    assert main(["compare-summary", str(tmp_path)]) == 0
    assert capsys.readouterr().out == EXPECTED + "\n"


def test_cli_exit_1_when_any_run_fails(tmp_path, capsys):
    make_runs(tmp_path)
    add_run(tmp_path, "444", fixture(depth_forward_repro=1))
    assert main(["compare-summary", str(tmp_path)]) == 1
    out = capsys.readouterr().out.splitlines()
    assert out[0] == EXPECTED
    assert out[1].startswith("444 | fail (depth_forward) |")


def test_cli_old_format_and_incomplete_do_not_affect_exit(tmp_path, capsys):
    add_run(tmp_path, "444", "```yaml\nunits_total: 3\n```\n무효: x\n")
    add_run(tmp_path, "555", OLD)
    assert main(["compare-summary", str(tmp_path)]) == 0
    assert capsys.readouterr().out == "444 | 미실행/불완전\n" + OLD_EXPECTED.replace("111", "555", 1) + "\n"
    assert main(["compare-summary", str(tmp_path / "nope")]) == 0
