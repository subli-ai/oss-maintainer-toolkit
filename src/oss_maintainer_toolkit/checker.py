from __future__ import annotations

from pathlib import Path
from typing import Any

CHECKS = {
    "readme": ("README.md", "README.rst", "README"),
    "licence": ("LICENSE", "LICENCE", "LICENSE.md", "LICENCE.md", "COPYING"),
    "contributing_guide": ("CONTRIBUTING.md", "CONTRIBUTING.rst", "CONTRIBUTING"),
    "security_policy": ("SECURITY.md", "SECURITY.rst", ".github/SECURITY.md"),
    "code_of_conduct": ("CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT.rst", ".github/CODE_OF_CONDUCT.md"),
    "changelog": ("CHANGELOG.md", "CHANGES.md", "HISTORY.md"),
    "github_actions": (".github/workflows",),
    "tests": ("tests", "test"),
}


def _candidate_is_present(root: Path, check: str, candidate: str) -> bool:
    path = root / candidate
    if check == "github_actions":
        if not path.is_dir():
            return False
        return any(
            file.is_file() and file.suffix.lower() in {".yml", ".yaml"} and file.stat().st_size > 0
            for file in path.rglob("*")
        )
    if check == "tests":
        if not path.is_dir():
            return False
        return any(
            file.is_file()
            and file.suffix == ".py"
            and (file.name.startswith("test_") or file.name.endswith("_test.py"))
            for file in path.rglob("*.py")
        )
    return path.is_file() and path.stat().st_size > 0


def inspect_repository(root: Path) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Repository path is not a directory: {root}")

    results: dict[str, dict[str, Any]] = {}
    for key, candidates in CHECKS.items():
        found = [name for name in candidates if _candidate_is_present(root, key, name)]
        results[key] = {
            "present": bool(found),
            "paths": found,
            "note": "Non-empty file or matching project file found; content and applicability are not validated.",
        }

    missing = [key for key, result in results.items() if not result["present"]]
    return {
        "repository": str(root),
        "checks": results,
        "summary": {
            "total": len(results),
            "present": len(results) - len(missing),
            "missing": missing,
        },
        "limitations": [
            "This is a repository-hygiene checklist, not a security audit or compliance certification.",
            "A licence file's presence does not establish that all repository contents may legally be redistributed.",
            "Workflow presence does not establish that tests pass.",
            "Test-file presence does not establish test quality or coverage.",
            "The tool does not measure usage, package downloads, dependent repositories, contributors, or OpenSSF criticality.",
        ],
    }
