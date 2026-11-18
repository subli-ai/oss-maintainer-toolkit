"""Offline repository hygiene checklist; intentionally dependency-free."""
from __future__ import annotations

import argparse
import json
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


def inspect_repository(root: Path) -> dict[str, Any]:
    """Return presence-only repository hygiene checks for an existing directory."""
    root = root.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Repository path is not a directory: {root}")

    results: dict[str, dict[str, Any]] = {}
    for key, candidates in CHECKS.items():
        found = [name for name in candidates if (root / name).exists()]
        results[key] = {
            "present": bool(found),
            "paths": found,
            "note": "Presence only; inspect content and applicability manually.",
        }

    missing = [key for key, result in results.items() if not result["present"]]
    return {
        "repository": str(root),
        "checks": results,
        "summary": {"total": len(results), "present": len(results) - len(missing), "missing": missing},
        "limitations": [
            "This is not a security audit or compliance certification.",
            "A licence file's presence does not establish that all repository contents may legally be redistributed.",
            "Workflow presence does not establish that tests pass.",
            "The tool does not measure usage, package downloads, dependent repositories, contributors, or OpenSSF criticality.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect basic open-source repository hygiene.")
    parser.add_argument("repository", type=Path, help="Path to a repository to inspect")
    parser.add_argument("--json", dest="json_path", type=Path, help="Optional output JSON file")
    args = parser.parse_args()
    try:
        report = inspect_repository(args.repository)
    except ValueError as exc:
        parser.error(str(exc))
    rendered = json.dumps(report, indent=2)
    if args.json_path:
        args.json_path.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
