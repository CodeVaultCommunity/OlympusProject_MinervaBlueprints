"""Exercise complete inventory coverage, byte mutations and actual Git archives."""
import copy
import json
import os
from pathlib import Path
import random
import stat
import subprocess
import sys
import warnings
import zipfile

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_distribution
import check_archive
import content_inventory as inventory


@pytest.fixture
def files():
    result = {
        "CITATION.cff": b"version: Stable-v1.0.0\n",
        "README.md": b"exact\r\nbytes\n",
        "Z.txt": b"upper", "a.txt": b"lower", "Alpha.txt": b"mixed",
        ".github/workflows/check.yml": b"workflow\n",
        "versioning/Alpha-v0.1.0/frozen.txt": b"historical\r\n",
        "versioning/Stable-v1.0.0/verification/evidence/run.txt": b"evidence\n",
    }
    result[inventory.INVENTORY] = json.dumps(inventory.inventory(result)).encode()
    return result


@pytest.mark.parametrize("order", ["windows", "posix", "shuffled"])
def test_record_order_is_not_content(files, order):
    manifest = json.loads(files[inventory.INVENTORY])
    rows = manifest["files"]
    if order == "shuffled":
        random.Random(18).shuffle(rows)
    else:
        rows.sort(key=lambda row: row["path"].casefold() if order == "windows" else row["path"])
    files[inventory.INVENTORY] = json.dumps(manifest).encode()
    assert inventory.verify(files) == []


@pytest.mark.parametrize("mutation,diagnostic", [("byte", "hash"), ("size", "size"),
                                                 ("add", "added"), ("remove", "missing"),
                                                 ("duplicate", "duplicate")])
def test_changes_are_not_hidden(files, mutation, diagnostic):
    if mutation == "byte":
        files["a.txt"] = b"other"
    elif mutation == "size":
        files["a.txt"] = b"longer"
    elif mutation == "add":
        files["extra.txt"] = b"extra"
    elif mutation == "remove":
        del files["a.txt"]
    else:
        manifest = json.loads(files[inventory.INVENTORY])
        manifest["files"].append(copy.deepcopy(manifest["files"][0]))
        files[inventory.INVENTORY] = json.dumps(manifest).encode()
    assert any(diagnostic in error for error in inventory.verify(files))


def test_inventory_includes_alpha_evidence_and_ci_without_normalization(files):
    manifest = inventory.inventory(files)
    names = [row["path"] for row in manifest["files"]]
    assert names == sorted(set(files) - {inventory.INVENTORY})
    assert all("\\" not in name for name in names)
    assert next(row for row in manifest["files"] if row["path"] == "README.md")["size_bytes"] == 13
    files["README.md"] = files["README.md"].replace(b"\r\n", b"\n")
    assert any("hash differs: README.md" == error for error in inventory.verify(files))


@pytest.mark.parametrize("name", ["../escape", "/absolute", "C:/drive", "a\\b", "a//b", "./file"])
def test_nonportable_paths_rejected(files, name):
    files[name] = b"bad path"
    assert any("relative POSIX" in error for error in inventory.verify(files))


@pytest.mark.parametrize("field,value", [("algorithm", "SHA-1"), ("minerva_edition", "Alpha-v0.1.0"),
                                         ("excluded_paths", ["CONTENT-SHA256.json", "README.md"]),
                                         ("scope", "partial")])
def test_metadata_drift_rejected(files, field, value):
    manifest = json.loads(files[inventory.INVENTORY])
    manifest[field] = value
    files[inventory.INVENTORY] = json.dumps(manifest).encode()
    assert any(f"metadata differs: {field}" in error for error in inventory.verify(files))


@pytest.mark.parametrize("field,value", [("size_bytes", True), ("sha256", "invalid"), ("unexpected", 1)])
def test_malformed_records_rejected(files, field, value):
    manifest = json.loads(files[inventory.INVENTORY])
    manifest["files"][0][field] = value
    files[inventory.INVENTORY] = json.dumps(manifest).encode()
    assert inventory.verify(files)


def test_self_reference_rejected(files):
    manifest = json.loads(files[inventory.INVENTORY])
    row = copy.deepcopy(manifest["files"][0])
    row["path"] = inventory.INVENTORY
    manifest["files"].append(row)
    files[inventory.INVENTORY] = json.dumps(manifest).encode()
    assert any("include itself" in error for error in inventory.verify(files))


def write_zip(path, files, prefix=""):
    with zipfile.ZipFile(path, "w") as archive:
        for name, raw in files.items():
            archive.writestr(prefix + name, raw)


@pytest.mark.parametrize("prefix", ["", "Atlas_Stable/"])
def test_archive_and_extraction_without_git(files, tmp_path, prefix):
    path = tmp_path / "release.zip"
    write_zip(path, files, prefix)
    loaded = check_archive.read_archive(path)
    assert inventory.verify(loaded) == []
    extracted = tmp_path / "extracted"
    for name, raw in loaded.items():
        target = extracted / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    assert inventory.verify(check_archive.read_archive(extracted)) == []
    (extracted / "unintended.txt").write_bytes(b"extra")
    assert "added file: unintended.txt" in inventory.verify(check_archive.read_archive(extracted))


def test_duplicate_zip_members_rejected(files, tmp_path):
    path = tmp_path / "duplicates.zip"
    write_zip(path, files)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        with zipfile.ZipFile(path, "a") as archive:
            archive.writestr("README.md", b"duplicate")
    with pytest.raises(ValueError, match="duplicate"):
        check_archive.read_archive(path)


def test_standalone_check_does_not_create_caches(files, tmp_path):
    source = Path(inventory.__file__).parent
    for name in ("content_inventory.py", "check_archive.py"):
        files["scripts/" + name] = (source / name).read_bytes()
    files[inventory.INVENTORY] = json.dumps(inventory.inventory(files)).encode()
    for name, raw in files.items():
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    env = dict(os.environ)
    env.pop("PYTHONDONTWRITEBYTECODE", None)
    result = subprocess.run([sys.executable, str(tmp_path / "scripts/check_archive.py"), str(tmp_path)],
                            env=env, cwd=tmp_path, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert not list(tmp_path.rglob("__pycache__"))


def test_zip_symlink_rejected(files, tmp_path):
    path = tmp_path / "symlink.zip"
    write_zip(path, files)
    link = zipfile.ZipInfo("link")
    link.create_system = 3
    link.external_attr = (stat.S_IFLNK | 0o777) << 16
    with zipfile.ZipFile(path, "a") as archive:
        archive.writestr(link, "README.md")
    with pytest.raises(ValueError, match="symlink"):
        check_archive.read_archive(path)


def test_file_outside_zip_prefix_rejected(files, tmp_path):
    path = tmp_path / "outside.zip"
    write_zip(path, files, "Atlas_Stable/")
    with zipfile.ZipFile(path, "a") as archive:
        archive.writestr("extra.txt", b"outside")
    with pytest.raises(ValueError, match="outside"):
        check_archive.read_archive(path)


@pytest.fixture
def checkout(files, tmp_path):
    root = tmp_path / "repository"
    root.mkdir()
    subprocess.run(["git", "init", "-q"], cwd=root, check=True)
    # Force literal test bytes; the real repository declares its own attributes.
    subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=root, check=True)
    for name, raw in files.items():
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    return root


def test_index_scope_tracks_intended_additions_and_deletions(checkout):
    assert inventory.check(checkout) == []
    (checkout / "untracked.txt").write_bytes(b"local only")
    assert inventory.check(checkout) == []
    subprocess.run(["git", "add", "untracked.txt"], cwd=checkout, check=True)
    assert "added file: untracked.txt" in inventory.check(checkout)
    subprocess.run(["git", "rm", "--cached", "a.txt"], cwd=checkout, check=True, capture_output=True)
    assert "missing file: a.txt" in inventory.check(checkout)


def test_missing_indexed_file_rejected(checkout):
    (checkout / "a.txt").unlink()
    with pytest.raises(ValueError, match="missing file: a.txt"):
        inventory.build(checkout)


def commit(checkout):
    subprocess.run(["git", "-c", "user.name=Atlas Test", "-c", "user.email=atlas@example.invalid",
                    "-c", "commit.gpgsign=false", "commit", "-qm", "fixture"], cwd=checkout, check=True)


def test_distribution_is_checked_and_refuses_overwrite_or_dirty_sources(checkout, tmp_path):
    commit(checkout)
    output = tmp_path / "release.zip"
    build_distribution.build(checkout, output)
    assert inventory.verify(check_archive.read_archive(output)) == []
    with pytest.raises(ValueError, match="already exists"):
        build_distribution.build(checkout, output)
    (checkout / "a.txt").write_bytes(b"changed")
    with pytest.raises(subprocess.CalledProcessError):
        build_distribution.build(checkout, tmp_path / "dirty.zip")
    assert not (tmp_path / "dirty.zip").exists()


def test_distribution_rejects_stale_inventory(checkout, tmp_path):
    (checkout / "a.txt").write_bytes(b"changed")
    subprocess.run(["git", "add", "a.txt"], cwd=checkout, check=True)
    commit(checkout)
    with pytest.raises(ValueError, match="differs: a.txt"):
        build_distribution.build(checkout, tmp_path / "stale.zip")
    assert not (tmp_path / "stale.zip").exists()
