from pathlib import Path

import pytest

from oss_maintainer_toolkit.checker import inspect_repository


def test_detects_basic_files(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("# Demo", encoding="utf-8")
    (tmp_path / "LICENSE").write_text("MIT License", encoding="utf-8")
    (tmp_path / "CONTRIBUTING.md").write_text("# Contributing", encoding="utf-8")

    report = inspect_repository(tmp_path)

    assert report["checks"]["readme"]["present"] is True
    assert report["checks"]["licence"]["present"] is True
    assert report["checks"]["contributing_guide"]["present"] is True
    assert report["summary"]["present"] == 3


def test_detects_nonempty_workflow_and_test_file(tmp_path: Path) -> None:
    workflows = tmp_path / ".github" / "workflows"
    workflows.mkdir(parents=True)
    (workflows / "tests.yml").write_text("name: tests\n", encoding="utf-8")
    tests = tmp_path / "tests"
    tests.mkdir()
    (tests / "test_example.py").write_text("def test_ok(): pass\n", encoding="utf-8")

    report = inspect_repository(tmp_path)

    assert report["checks"]["github_actions"]["present"] is True
    assert report["checks"]["tests"]["present"] is True


def test_empty_workflow_and_test_directories_do_not_count(tmp_path: Path) -> None:
    (tmp_path / ".github" / "workflows").mkdir(parents=True)
    (tmp_path / "tests").mkdir()

    report = inspect_repository(tmp_path)

    assert report["checks"]["github_actions"]["present"] is False
    assert report["checks"]["tests"]["present"] is False


def test_empty_document_files_do_not_count(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("", encoding="utf-8")
    report = inspect_repository(tmp_path)
    assert report["checks"]["readme"]["present"] is False


def test_missing_or_non_directory_path_raises(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="not a directory"):
        inspect_repository(tmp_path / "missing")

    file_path = tmp_path / "not-a-folder"
    file_path.write_text("text", encoding="utf-8")
    with pytest.raises(ValueError, match="not a directory"):
        inspect_repository(file_path)
