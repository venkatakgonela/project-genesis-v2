"""Command line entry point for the Sprint 1 repository scanner."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Optional, Sequence

from project_conductor.registry import build_artifact_registry
from project_conductor.scanner import RepositoryScanError, scan_repository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="project-conductor-scan",
        description="Scan repository Markdown artifacts into an in-memory representation.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to scan. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print the scan representation as JSON instead of a short summary.",
    )
    parser.add_argument(
        "--registry-json",
        action="store_true",
        help="Print the Artifact Registry representation as deterministic JSON.",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        scan = scan_repository(Path(args.root))
    except RepositoryScanError as exc:
        parser.exit(status=2, message=f"scan error: {exc}\n")

    if args.registry_json:
        registry = build_artifact_registry(scan)
        sys.stdout.write(registry.to_json())
        return 0

    if args.json:
        json.dump(scan.to_dict(), sys.stdout, indent=2, sort_keys=True)
        sys.stdout.write("\n")
        return 0

    sys.stdout.write(f"Repository root: {scan.root}\n")
    sys.stdout.write(f"Artifacts discovered: {len(scan.artifacts)}\n")
    sys.stdout.write(f"Artifacts with metadata: {scan.metadata_count}\n")
    sys.stdout.write(f"Scan problems: {len(scan.problems)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
