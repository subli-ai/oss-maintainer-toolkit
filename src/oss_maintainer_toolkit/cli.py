from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .checker import inspect_repository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="oss-maintainer-toolkit",
        description="Check basic open-source repository hygiene.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="Inspect a repository.")
    check.add_argument("repository", type=Path, help="Repository path.")
    check.add_argument("--json", dest="json_path", type=Path, help="Write the report to a JSON file.")
    check.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="Exit with code 1 when any check is missing.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "check":
        try:
            report = inspect_repository(args.repository)
        except ValueError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 2

        rendered = json.dumps(report, indent=2)
        print(rendered)
        if args.json_path:
            try:
                args.json_path.write_text(rendered + "\n", encoding="utf-8")
            except OSError as exc:
                print(f"error writing JSON report: {exc}", file=sys.stderr)
                return 2
        if args.fail_on_missing and report["summary"]["missing"]:
            return 1
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
