import os
import re

from rek.cli import main
from rek.core.compare_summary import KEYS, line, parse

HERE = os.path.dirname(__file__)
FIXTURE = os.path.join(HERE, "fixtures", "comparison_example.md")
BRIEF = os.path.join(HERE, "..", "skills", "rek", "references", "comparator.md")
EXPECTED = "111 | units 7/12 | facts 14/30 (conflict 2) | fabricated 0 | depth 9→6 | extra 3 | valid | ab12cd34ef56"


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def yaml_block(text):
    m = re.search(r"^```yaml\n.*?^```\n", text, re.S | re.M)
    assert m, "no yaml block"
    return m.group(0).encode("utf-8")


def test_keys_in_order():
    assert KEYS == ("units_total", "units_covered", "facts_total", "facts_matched", "facts_conflicting", "fabricated",
                    "depth_original", "depth_repro", "extra_units", "invalid", "profile_hash")


def test_fixture_starts_with_the_block():
    text = read(FIXTURE)
    assert text.startswith("```yaml\n")
    d = parse(text)
    assert list(d) == list(KEYS)
    assert d["units_total"] == 12 and d["invalid"] == 0 and d["profile_hash"] == "ab12cd34ef56"


def test_brief_block_is_byte_identical_to_fixture():
    assert yaml_block(read(BRIEF)) == yaml_block(read(FIXTURE))


def test_line_copies_values():
    assert line("111", read(FIXTURE)) == EXPECTED


def test_missing_key_is_incomplete():
    text = read(FIXTURE).replace("extra_units: 3\n", "")
    assert line("111", text) == "111 | 미실행/불완전"
    assert line("111", "no yaml") == "111 | 미실행/불완전"
    text = read(FIXTURE).replace("depth_repro: 6", "depth_repro: six")  # not an integer: missing
    assert line("111", text) == "111 | 미실행/불완전"


def test_invalid_line_decides():
    text = read(FIXTURE).replace("invalid: 0", "invalid: 1").replace("```\n\n", "```\n무효: S03 read after date\n\n", 1)
    out = line("111", text)
    assert out.endswith("| invalid | ab12cd34ef56") and "불일치" not in out


def test_key_disagreeing_with_line_is_flagged():
    with_line = read(FIXTURE).replace("```\n\n", "```\n무효: author blog opened\n\n", 1)
    assert "| invalid 불일치 |" in line("111", with_line)
    key_only = read(FIXTURE).replace("invalid: 0", "invalid: 1")
    assert "| valid 불일치 |" in line("111", key_only)


def make_runs(tmp_path):
    run = tmp_path / "111"
    for n in ("1", "2", "10"):
        (run / "repro" / n).mkdir(parents=True)
    (run / "meta.json").write_text("{}")
    (run / "repro" / "1" / "comparison.md").write_text(read(FIXTURE).replace("units_covered: 7", "units_covered: 1"), encoding="utf-8")
    (run / "repro" / "2" / "comparison.md").write_text(read(FIXTURE).replace("units_covered: 7", "units_covered: 2"), encoding="utf-8")
    (run / "repro" / "10" / "comparison.md").write_text(read(FIXTURE), encoding="utf-8")
    bare = tmp_path / "222"
    (bare / "repro" / "1").mkdir(parents=True)  # a reproduction without comparison.md: skipped
    (bare / "meta.json").write_text("{}")
    other = tmp_path / "333"
    (other / "repro" / "1").mkdir(parents=True)  # no meta.json: not a run
    (other / "repro" / "1" / "comparison.md").write_text(read(FIXTURE), encoding="utf-8")
    return tmp_path


def test_cli_one_line_per_run_largest_n_exit_0(tmp_path, capsys):
    make_runs(tmp_path)
    assert main(["compare-summary", str(tmp_path)]) == 0
    assert capsys.readouterr().out == EXPECTED + "\n"


def test_cli_exit_0_when_incomplete_or_invalid(tmp_path, capsys):
    run = tmp_path / "444"
    (run / "repro" / "1").mkdir(parents=True)
    (run / "meta.json").write_text("{}")
    (run / "repro" / "1" / "comparison.md").write_text("```yaml\nunits_total: 3\n```\n무효: x\n", encoding="utf-8")
    assert main(["compare-summary", str(tmp_path)]) == 0
    assert capsys.readouterr().out == "444 | 미실행/불완전\n"
    assert main(["compare-summary", str(tmp_path / "nope")]) == 0
