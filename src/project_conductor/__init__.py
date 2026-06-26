"""Deterministic Project Conductor implementation slices."""

from project_conductor.registry import (
    ArtifactRegistry,
    RegistryArtifact,
    RegistryValidationReport,
    build_artifact_registry,
    validate_registry_artifacts,
)

from project_conductor.metadata_contract import (
    MetadataContract,
    default_metadata_contract,
)

from project_conductor.scanner import (
    Artifact,
    MetadataTable,
    RepositoryScan,
    RepositoryScanError,
    ScanProblem,
    scan_repository,
)

from project_conductor.state import (
    GeneratorInformation,
    MetadataSummary,
    RepositoryState,
    RepositoryStateBuilder,
    RepositoryStateValidationReport,
    RepositoryStateValidator,
    RepositoryStatistics,
    RepositorySummary,
    ValidationSummary,
    VersionInformation,
    build_repository_state,
    validate_repository_state,
)

__all__ = [
    "Artifact",
    "ArtifactRegistry",
    "GeneratorInformation",
    "MetadataTable",
    "MetadataContract",
    "MetadataSummary",
    "RepositoryScan",
    "RepositoryScanError",
    "RepositoryState",
    "RepositoryStateBuilder",
    "RepositoryStateValidationReport",
    "RepositoryStateValidator",
    "RepositoryStatistics",
    "RepositorySummary",
    "RegistryArtifact",
    "RegistryValidationReport",
    "ScanProblem",
    "ValidationSummary",
    "VersionInformation",
    "build_artifact_registry",
    "build_repository_state",
    "default_metadata_contract",
    "scan_repository",
    "validate_registry_artifacts",
    "validate_repository_state",
]
