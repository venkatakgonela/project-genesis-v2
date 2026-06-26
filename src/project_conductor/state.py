"""Repository State Model for deterministic Project Conductor."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Dict, Iterable, List, Sequence, Tuple

from project_conductor.registry import ArtifactRegistry, RegistryArtifact, RegistryValidationReport


REPOSITORY_STATE_VERSION = "0.1.0"
GENERATOR_NAME = "project-conductor-repository-state-builder"
GENERATOR_VERSION = "0.1.0"
DETERMINISTIC_GENERATED_AT = "1970-01-01T00:00:00Z"


@dataclass(frozen=True)
class CountByKey:
    """Deterministic count for a named classification."""

    key: str
    count: int

    def to_dict(self) -> Dict[str, object]:
        return {
            "key": self.key,
            "count": self.count,
        }


@dataclass(frozen=True)
class RepositorySummary:
    """Provider-independent summary of the current repository snapshot."""

    source_provider: str
    artifact_count: int
    durable_artifact_count: int
    problem_count: int

    def to_dict(self) -> Dict[str, object]:
        return {
            "source_provider": self.source_provider,
            "artifact_count": self.artifact_count,
            "durable_artifact_count": self.durable_artifact_count,
            "problem_count": self.problem_count,
        }


@dataclass(frozen=True)
class RepositoryStatistics:
    """Deterministic aggregate statistics for a repository state."""

    artifact_count: int
    durable_artifact_count: int
    metadata_backed_artifact_count: int
    metadata_free_artifact_count: int
    artifact_types: Tuple[CountByKey, ...]
    metadata_statuses: Tuple[CountByKey, ...]

    def to_dict(self) -> Dict[str, object]:
        return {
            "artifact_count": self.artifact_count,
            "durable_artifact_count": self.durable_artifact_count,
            "metadata_backed_artifact_count": self.metadata_backed_artifact_count,
            "metadata_free_artifact_count": self.metadata_free_artifact_count,
            "artifact_types": [item.to_dict() for item in self.artifact_types],
            "metadata_statuses": [item.to_dict() for item in self.metadata_statuses],
        }


@dataclass(frozen=True)
class MetadataSummary:
    """Metadata completeness and durability summary."""

    complete_count: int
    incomplete_count: int
    missing_count: int
    metadata_backed_artifact_count: int
    metadata_free_artifact_count: int
    durable_artifact_count: int
    non_durable_artifact_count: int

    def to_dict(self) -> Dict[str, object]:
        return {
            "complete_count": self.complete_count,
            "incomplete_count": self.incomplete_count,
            "missing_count": self.missing_count,
            "metadata_backed_artifact_count": self.metadata_backed_artifact_count,
            "metadata_free_artifact_count": self.metadata_free_artifact_count,
            "durable_artifact_count": self.durable_artifact_count,
            "non_durable_artifact_count": self.non_durable_artifact_count,
        }


@dataclass(frozen=True)
class ValidationSummary:
    """Compact validation status for the repository state."""

    valid: bool
    error_count: int
    warning_count: int

    def to_dict(self) -> Dict[str, object]:
        return {
            "valid": self.valid,
            "error_count": self.error_count,
            "warning_count": self.warning_count,
        }


@dataclass(frozen=True)
class GeneratorInformation:
    """Information about the deterministic state generator."""

    name: str
    version: str
    generated_at: str

    def to_dict(self) -> Dict[str, object]:
        return {
            "name": self.name,
            "version": self.version,
            "generated_at": self.generated_at,
        }


@dataclass(frozen=True)
class VersionInformation:
    """Version lineage for state, registry, and metadata contract."""

    repository_state_version: str
    registry_version: str
    registry_schema_version: str
    metadata_contract_version: str

    def to_dict(self) -> Dict[str, object]:
        return {
            "repository_state_version": self.repository_state_version,
            "registry_version": self.registry_version,
            "registry_schema_version": self.registry_schema_version,
            "metadata_contract_version": self.metadata_contract_version,
        }


@dataclass(frozen=True)
class RepositoryStateValidationReport:
    """Validation result for RepositoryState structure."""

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
class RepositoryState:
    """Deterministic current-state snapshot derived from ArtifactRegistry."""

    version: VersionInformation
    generator: GeneratorInformation
    repository: RepositorySummary
    statistics: RepositoryStatistics
    metadata: MetadataSummary
    validation_summary: ValidationSummary
    validation: RepositoryStateValidationReport
    registry_validation: RegistryValidationReport
    artifacts: Tuple[RegistryArtifact, ...]

    def to_dict(self) -> Dict[str, object]:
        return {
            "version": self.version.to_dict(),
            "generator": self.generator.to_dict(),
            "repository": self.repository.to_dict(),
            "statistics": self.statistics.to_dict(),
            "metadata": self.metadata.to_dict(),
            "validation_summary": self.validation_summary.to_dict(),
            "validation": self.validation.to_dict(),
            "registry_validation": self.registry_validation.to_dict(),
            "artifacts": [artifact.to_dict() for artifact in self.artifacts],
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2, sort_keys=True) + "\n"


class RepositoryStateBuilder:
    """Build RepositoryState solely from ArtifactRegistry."""

    def build(
        self,
        registry: ArtifactRegistry,
        *,
        generated_at: str = DETERMINISTIC_GENERATED_AT,
    ) -> RepositoryState:
        artifacts = tuple(registry.artifacts)
        metadata_summary = _build_metadata_summary(artifacts)
        statistics = _build_repository_statistics(artifacts, metadata_summary=metadata_summary)
        repository = RepositorySummary(
            source_provider=registry.source_provider,
            artifact_count=len(artifacts),
            durable_artifact_count=metadata_summary.durable_artifact_count,
            problem_count=sum(len(artifact.problems) for artifact in artifacts),
        )
        validation_summary = ValidationSummary(
            valid=registry.validation.valid,
            error_count=len(registry.validation.errors),
            warning_count=len(registry.validation.warnings),
        )
        state_without_validation = RepositoryState(
            version=VersionInformation(
                repository_state_version=REPOSITORY_STATE_VERSION,
                registry_version=registry.registry_version,
                registry_schema_version=registry.registry_schema_version,
                metadata_contract_version=registry.metadata_contract_version,
            ),
            generator=GeneratorInformation(
                name=GENERATOR_NAME,
                version=GENERATOR_VERSION,
                generated_at=generated_at,
            ),
            repository=repository,
            statistics=statistics,
            metadata=metadata_summary,
            validation_summary=validation_summary,
            validation=RepositoryStateValidationReport(valid=True),
            registry_validation=registry.validation,
            artifacts=artifacts,
        )
        validation = RepositoryStateValidator().validate(state_without_validation)
        return RepositoryState(
            version=state_without_validation.version,
            generator=state_without_validation.generator,
            repository=state_without_validation.repository,
            statistics=state_without_validation.statistics,
            metadata=state_without_validation.metadata,
            validation_summary=state_without_validation.validation_summary,
            validation=validation,
            registry_validation=state_without_validation.registry_validation,
            artifacts=state_without_validation.artifacts,
        )


class RepositoryStateValidator:
    """Validate RepositoryState structure without running quality gates."""

    def validate(self, state: RepositoryState) -> RepositoryStateValidationReport:
        errors: List[str] = []
        warnings: List[str] = []

        if state.version.repository_state_version != REPOSITORY_STATE_VERSION:
            errors.append(
                "repository_state_version "
                f"{state.version.repository_state_version!r} does not match {REPOSITORY_STATE_VERSION!r}"
            )
        if state.generator.name != GENERATOR_NAME:
            errors.append(f"generator name {state.generator.name!r} is not recognized")
        if not state.generator.generated_at:
            errors.append("generator generated_at is empty")
        if state.repository.artifact_count != len(state.artifacts):
            errors.append("repository artifact_count does not match artifacts")
        if state.statistics.artifact_count != len(state.artifacts):
            errors.append("statistics artifact_count does not match artifacts")
        if state.validation_summary.error_count != len(state.registry_validation.errors):
            errors.append("validation_summary error_count does not match registry validation")
        if state.validation_summary.warning_count != len(state.registry_validation.warnings):
            errors.append("validation_summary warning_count does not match registry validation")

        expected_metadata = _build_metadata_summary(state.artifacts)
        if state.metadata != expected_metadata:
            errors.append("metadata summary does not match artifacts")

        expected_statistics = _build_repository_statistics(state.artifacts, metadata_summary=expected_metadata)
        if state.statistics != expected_statistics:
            errors.append("repository statistics do not match artifacts")

        previous_path = ""
        for artifact in state.artifacts:
            if artifact.path < previous_path:
                errors.append(f"repository state artifact ordering is not deterministic at {artifact.path!r}")
                break
            previous_path = artifact.path

        if state.repository.problem_count:
            warnings.append(f"repository state includes {state.repository.problem_count} artifact problem(s)")
        if state.registry_validation.warnings:
            warnings.extend(state.registry_validation.warnings)

        return RepositoryStateValidationReport(valid=not errors, errors=tuple(errors), warnings=tuple(warnings))


def build_repository_state(registry: ArtifactRegistry) -> RepositoryState:
    """Build deterministic RepositoryState from an ArtifactRegistry."""

    return RepositoryStateBuilder().build(registry)


def validate_repository_state(state: RepositoryState) -> RepositoryStateValidationReport:
    """Validate deterministic RepositoryState structure."""

    return RepositoryStateValidator().validate(state)


def _build_metadata_summary(artifacts: Sequence[RegistryArtifact]) -> MetadataSummary:
    status_counts = _count_by_key(artifact.metadata_status for artifact in artifacts)
    metadata_backed_count = sum(1 for artifact in artifacts if artifact.metadata_id is not None)
    durable_count = sum(1 for artifact in artifacts if artifact.durable)
    return MetadataSummary(
        complete_count=status_counts.get("complete", 0),
        incomplete_count=status_counts.get("incomplete", 0),
        missing_count=status_counts.get("missing", 0),
        metadata_backed_artifact_count=metadata_backed_count,
        metadata_free_artifact_count=len(artifacts) - metadata_backed_count,
        durable_artifact_count=durable_count,
        non_durable_artifact_count=len(artifacts) - durable_count,
    )


def _build_repository_statistics(
    artifacts: Sequence[RegistryArtifact],
    *,
    metadata_summary: MetadataSummary,
) -> RepositoryStatistics:
    return RepositoryStatistics(
        artifact_count=len(artifacts),
        durable_artifact_count=metadata_summary.durable_artifact_count,
        metadata_backed_artifact_count=metadata_summary.metadata_backed_artifact_count,
        metadata_free_artifact_count=metadata_summary.metadata_free_artifact_count,
        artifact_types=_count_items(artifact.artifact_type for artifact in artifacts),
        metadata_statuses=_count_items(artifact.metadata_status for artifact in artifacts),
    )


def _count_items(values: Iterable[str]) -> Tuple[CountByKey, ...]:
    counts = _count_by_key(values)
    return tuple(CountByKey(key=key, count=counts[key]) for key in sorted(counts))


def _count_by_key(values: Iterable[str]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts
