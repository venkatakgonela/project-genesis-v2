"""Artifact Registry Model for Project Conductor Sprint 2."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

from project_conductor.scanner import Artifact, RepositoryScan, ScanProblem


REGISTRY_VERSION = "0.1.0"
DEFAULT_SOURCE_PROVIDER = "filesystem"
VALID_METADATA_STATUSES = frozenset({"complete", "incomplete", "missing"})


@dataclass(frozen=True)
class RegistryArtifact:
    """A normalized artifact entry for deterministic registry consumers."""

    artifact_id: str
    path: str
    artifact_type: str
    title: Optional[str]
    hash: str
    metadata_status: str
    metadata_id: Optional[str]
    problems: Tuple[str, ...]
    source_provider: str

    def to_dict(self) -> Dict[str, object]:
        return {
            "artifact_id": self.artifact_id,
            "path": self.path,
            "type": self.artifact_type,
            "title": self.title,
            "hash": self.hash,
            "metadata_status": self.metadata_status,
            "metadata_id": self.metadata_id,
            "problems": list(self.problems),
            "source_provider": self.source_provider,
        }


@dataclass(frozen=True)
class RegistryValidationReport:
    """Validation result for an artifact registry structure."""

    valid: bool
    errors: Tuple[str, ...] = ()
    warnings: Tuple[str, ...] = ()

    def to_dict(self) -> Dict[str, object]:
        return {
            "valid": self.valid,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
        }


@dataclass(frozen=True)
class ArtifactRegistry:
    """Deterministic Artifact Registry representation."""

    registry_version: str
    source_provider: str
    artifacts: Tuple[RegistryArtifact, ...]
    validation: RegistryValidationReport

    @property
    def artifact_count(self) -> int:
        return len(self.artifacts)

    def to_dict(self) -> Dict[str, object]:
        return {
            "registry_version": self.registry_version,
            "source_provider": self.source_provider,
            "artifact_count": self.artifact_count,
            "validation": self.validation.to_dict(),
            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"


def build_artifact_registry(
    scan: RepositoryScan,
    *,
    source_provider: str = DEFAULT_SOURCE_PROVIDER,
) -> ArtifactRegistry:
    """Convert a RepositoryScan into a deterministic ArtifactRegistry."""

    artifacts = tuple(
        sorted(
            (_to_registry_artifact(artifact, source_provider=source_provider) for artifact in scan.artifacts),
            key=lambda artifact: artifact.path,
        )
    )
    validation = validate_registry_artifacts(artifacts, source_provider=source_provider)
    return ArtifactRegistry(
        registry_version=REGISTRY_VERSION,
        source_provider=source_provider,
        artifacts=artifacts,
        validation=validation,
    )


def validate_registry_artifacts(
    artifacts: Sequence[RegistryArtifact],
    *,
    source_provider: str = DEFAULT_SOURCE_PROVIDER,
) -> RegistryValidationReport:
    """Validate deterministic registry structure without running quality gates."""

    errors: List[str] = []
    warnings: List[str] = []
    seen_ids: Dict[str, str] = {}
    previous_path = ""

    for index, artifact in enumerate(artifacts):
        if not artifact.artifact_id:
            errors.append(f"artifact at index {index} has empty artifact_id")
        elif artifact.artifact_id in seen_ids:
            errors.append(
                f"duplicate artifact_id {artifact.artifact_id!r} for {seen_ids[artifact.artifact_id]!r} and {artifact.path!r}"
            )
        else:
            seen_ids[artifact.artifact_id] = artifact.path

        if not artifact.path:
            errors.append(f"artifact {artifact.artifact_id!r} has empty path")
        if artifact.path < previous_path:
            errors.append(f"artifact registry ordering is not deterministic at {artifact.path!r}")
        previous_path = artifact.path

        if not artifact.artifact_type:
            errors.append(f"artifact {artifact.path!r} has empty type")
        if not artifact.hash:
            errors.append(f"artifact {artifact.path!r} has empty hash")
        if artifact.metadata_status not in VALID_METADATA_STATUSES:
            errors.append(f"artifact {artifact.path!r} has invalid metadata_status {artifact.metadata_status!r}")
        if artifact.source_provider != source_provider:
            errors.append(
                f"artifact {artifact.path!r} source_provider {artifact.source_provider!r} does not match registry provider"
            )
        if artifact.metadata_status != "complete":
            warnings.append(f"artifact {artifact.path!r} metadata_status is {artifact.metadata_status}")

    return RegistryValidationReport(valid=not errors, errors=tuple(errors), warnings=tuple(warnings))


def _to_registry_artifact(artifact: Artifact, *, source_provider: str) -> RegistryArtifact:
    metadata_id = _metadata_id(artifact)
    return RegistryArtifact(
        artifact_id=_stable_artifact_id(artifact),
        path=artifact.path,
        artifact_type=artifact.artifact_type,
        title=artifact.title,
        hash=artifact.sha256,
        metadata_status=_metadata_status(artifact),
        metadata_id=metadata_id,
        problems=_problem_messages(artifact.problems),
        source_provider=source_provider,
    )


def _metadata_id(artifact: Artifact) -> Optional[str]:
    if artifact.metadata is None:
        return None
    value = artifact.metadata.fields.get("ID")
    if not value or value == "TODO":
        return None
    return value


def _stable_artifact_id(artifact: Artifact) -> str:
    metadata_id = _metadata_id(artifact)
    if metadata_id:
        return metadata_id
    path_digest = hashlib.sha1(artifact.path.encode("utf-8")).hexdigest()[:12]
    return f"PATH-{path_digest}"


def _metadata_status(artifact: Artifact) -> str:
    if artifact.metadata is None:
        return "missing"
    if artifact.metadata.has_required_fields:
        return "complete"
    return "incomplete"


def _problem_messages(problems: Iterable[ScanProblem]) -> Tuple[str, ...]:
    return tuple(problem.message for problem in problems)

