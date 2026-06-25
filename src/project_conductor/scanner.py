"""Deterministic repository scanner for Project Conductor Sprint 1."""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple


DEFAULT_ARTIFACT_SUFFIXES: Tuple[str, ...] = (".md",)
DEFAULT_EXCLUDED_DIRECTORIES = frozenset(
    {
        ".git",
        ".mypy_cache",
        ".pytest_cache",
        ".ruff_cache",
        ".tox",
        ".venv",
        "__pycache__",
        "node_modules",
    }
)
REQUIRED_METADATA_FIELDS: Tuple[str, ...] = (
    "ID",
    "Title",
    "Version",
    "Status",
    "Owner",
    "Created Date",
    "Updated Date",
    "Dependencies",
    "Related ADRs",
    "Related Work Packages",
    "Tags",
    "Review Date",
)


class RepositoryScanError(ValueError):
    """Raised when a repository scan cannot be started."""


@dataclass(frozen=True)
class ScanProblem:
    """A non-fatal scanner problem attached to a repository path."""

    path: str
    message: str

    def to_dict(self) -> Dict[str, str]:
        return {"path": self.path, "message": self.message}


@dataclass(frozen=True)
class MetadataTable:
    """Parsed Project Genesis Markdown metadata table."""

    fields: Mapping[str, str] = field(default_factory=dict)
    missing_fields: Tuple[str, ...] = ()

    @property
    def has_required_fields(self) -> bool:
        return not self.missing_fields

    def to_dict(self) -> Dict[str, object]:
        return {
            "fields": dict(sorted(self.fields.items())),
            "missing_fields": list(self.missing_fields),
            "has_required_fields": self.has_required_fields,
        }


@dataclass(frozen=True)
class Artifact:
    """A discovered repository artifact."""

    path: str
    artifact_type: str
    title: Optional[str]
    suffix: str
    size_bytes: int
    line_count: int
    sha256: str
    metadata: Optional[MetadataTable]
    problems: Tuple[ScanProblem, ...] = ()

    @property
    def has_metadata(self) -> bool:
        return self.metadata is not None

    def to_dict(self) -> Dict[str, object]:
        return {
            "path": self.path,
            "artifact_type": self.artifact_type,
            "title": self.title,
            "suffix": self.suffix,
            "size_bytes": self.size_bytes,
            "line_count": self.line_count,
            "sha256": self.sha256,
            "has_metadata": self.has_metadata,
            "metadata": self.metadata.to_dict() if self.metadata else None,
            "problems": [problem.to_dict() for problem in self.problems],
        }


@dataclass(frozen=True)
class RepositoryScan:
    """In-memory representation of a repository scan."""

    root: str
    artifacts: Tuple[Artifact, ...]
    problems: Tuple[ScanProblem, ...] = ()

    @property
    def metadata_count(self) -> int:
        return sum(1 for artifact in self.artifacts if artifact.has_metadata)

    def to_dict(self) -> Dict[str, object]:
        return {
            "root": self.root,
            "artifact_count": len(self.artifacts),
            "metadata_count": self.metadata_count,
            "problem_count": len(self.problems),
            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
            "problems": [problem.to_dict() for problem in self.problems],
        }


def scan_repository(
    root: Path,
    *,
    artifact_suffixes: Sequence[str] = DEFAULT_ARTIFACT_SUFFIXES,
    excluded_directories: Iterable[str] = DEFAULT_EXCLUDED_DIRECTORIES,
) -> RepositoryScan:
    """Discover repository artifacts and return a deterministic in-memory scan."""

    resolved_root = root.expanduser().resolve()
    if not resolved_root.exists():
        raise RepositoryScanError(f"repository root does not exist: {root}")
    if not resolved_root.is_dir():
        raise RepositoryScanError(f"repository root is not a directory: {root}")

    suffix_set = frozenset(suffix.lower() for suffix in artifact_suffixes)
    excluded_set = frozenset(excluded_directories)
    artifacts: List[Artifact] = []
    scan_problems: List[ScanProblem] = []

    for path in _iter_repository_files(resolved_root, excluded_set):
        if path.suffix.lower() not in suffix_set:
            continue
        artifact, problems = _scan_artifact(resolved_root, path)
        artifacts.append(artifact)
        scan_problems.extend(problems)

    ordered_artifacts = tuple(sorted(artifacts, key=lambda artifact: artifact.path))
    ordered_problems = tuple(sorted(scan_problems, key=lambda problem: (problem.path, problem.message)))
    return RepositoryScan(root=str(resolved_root), artifacts=ordered_artifacts, problems=ordered_problems)


def _iter_repository_files(root: Path, excluded_directories: Iterable[str]) -> Iterator[Path]:
    excluded_set = frozenset(excluded_directories)
    directories = [root]

    while directories:
        current = directories.pop(0)
        try:
            children = sorted(current.iterdir(), key=lambda child: child.name)
        except OSError:
            continue

        for child in children:
            if child.is_dir():
                if child.name not in excluded_set:
                    directories.append(child)
            elif child.is_file():
                yield child


def _scan_artifact(root: Path, path: Path) -> Tuple[Artifact, Tuple[ScanProblem, ...]]:
    relative_path = path.relative_to(root).as_posix()
    problems: List[ScanProblem] = []

    try:
        raw_bytes = path.read_bytes()
    except OSError as exc:
        problem = ScanProblem(relative_path, f"could not read artifact: {exc}")
        return (
            Artifact(
                path=relative_path,
                artifact_type=_classify_artifact(relative_path),
                title=None,
                suffix=path.suffix,
                size_bytes=0,
                line_count=0,
                sha256="",
                metadata=None,
                problems=(problem,),
            ),
            (problem,),
        )

    text = raw_bytes.decode("utf-8", errors="replace")
    lines = text.splitlines()
    title = _extract_title(lines)
    metadata = _extract_metadata(lines)
    if metadata is None:
        problems.append(ScanProblem(relative_path, "metadata section not found"))
    elif metadata.missing_fields:
        problems.append(
            ScanProblem(
                relative_path,
                "metadata missing required fields: " + ", ".join(metadata.missing_fields),
            )
        )

    artifact = Artifact(
        path=relative_path,
        artifact_type=_classify_artifact(relative_path),
        title=title,
        suffix=path.suffix,
        size_bytes=len(raw_bytes),
        line_count=len(lines),
        sha256=hashlib.sha256(raw_bytes).hexdigest(),
        metadata=metadata,
        problems=tuple(problems),
    )
    return artifact, tuple(problems)


def _extract_title(lines: Sequence[str]) -> Optional[str]:
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip() or None
    return None


def _extract_metadata(lines: Sequence[str]) -> Optional[MetadataTable]:
    metadata_start = None
    for index, line in enumerate(lines):
        if line.strip() == "## Metadata":
            metadata_start = index + 1
            break

    if metadata_start is None:
        return None

    fields: Dict[str, str] = {}
    for line in lines[metadata_start:]:
        stripped = line.strip()
        if stripped.startswith("## ") and stripped != "## Metadata":
            break
        if not stripped.startswith("|") or not stripped.endswith("|"):
            continue

        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if len(cells) != 2:
            continue
        key, value = cells
        if key in {"Field", "---"} or set(key) == {"-"}:
            continue
        if not key:
            continue
        fields[key] = value

    missing_fields = tuple(field_name for field_name in REQUIRED_METADATA_FIELDS if field_name not in fields)
    return MetadataTable(fields=fields, missing_fields=missing_fields)


def _classify_artifact(relative_path: str) -> str:
    parts = tuple(relative_path.split("/"))
    if not parts:
        return "unknown"

    if parts[0] == "adr":
        return "adr"
    if parts[0] == "architecture":
        return "architecture"
    if parts[0] == "platform":
        if "product" in parts:
            return "platform-product"
        if "specs" in parts:
            return "platform-specification"
        return "platform"
    if parts[0] == "programme":
        if len(parts) > 1 and parts[1] == "work-packages":
            return "work-package"
        if len(parts) > 1 and parts[1] == "baseline":
            return "baseline"
        return "programme"
    if parts[0] == "technology-radar":
        return "technology-radar"
    if parts[0] == "docs":
        return "documentation"
    if parts[0] == "evaluation":
        return "evaluation"
    if parts[0] == "golden":
        return "golden-asset"
    if parts[0] == "knowledge":
        return "knowledge"
    if parts[0] == "prompts":
        return "prompt-source"
    if parts[0] == "templates":
        return "template"
    if parts[0] == "web-review":
        return "review"
    return "repository"

