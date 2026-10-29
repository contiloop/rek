import hashlib

import pytest

from rek.core.profile_hash import profile_hash


def test_hash_is_first_12_hex_of_sha256_over_skill_then_method(tmp_path):
    (tmp_path / "SKILL.md").write_bytes(b"skill\n")
    (tmp_path / "research-method.md").write_bytes("방법\n".encode())
    expected = hashlib.sha256(b"skill\n" + "방법\n".encode()).hexdigest()[:12]
    assert profile_hash(str(tmp_path)) == expected
    assert len(expected) == 12


def test_missing_file_raises(tmp_path):
    (tmp_path / "SKILL.md").write_bytes(b"x")
    with pytest.raises(FileNotFoundError):
        profile_hash(str(tmp_path))


def test_cli(tmp_path, capsys):
    from rek.cli import main

    assert main(["profile-hash", str(tmp_path)]) == 2
    (tmp_path / "SKILL.md").write_bytes(b"a")
    (tmp_path / "research-method.md").write_bytes(b"b")
    assert main(["profile-hash", str(tmp_path)]) == 0
    assert capsys.readouterr().out.strip() == hashlib.sha256(b"ab").hexdigest()[:12]
