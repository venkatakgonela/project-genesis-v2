# Sprint 2 Technical Design

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-TECH-DESIGN |
| Title | Sprint 2 Artifact Registry Model Technical Design |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009, PC-S2-DESIGN |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | project-conductor, technical-design, artifact-registry |
| Review Date | 2026-07-02 |

## Component Diagram

```text
Repository Discovery Capability, Filesystem Provider
  -> RepositoryScan
      -> build_artifact_registry(scan)
          -> RegistryArtifact entries
          -> validate_registry_artifacts(entries)
          -> ArtifactRegistry
              -> deterministic JSON export
```

## Module Responsibilities

| Module | Responsibility |
| --- | --- |
| `project_conductor.registry` | Registry data model, scan conversion, stable IDs, validation, deterministic JSON export. |
| `project_conductor.scanner` | Existing Repository Discovery Capability, Filesystem Provider source model. |
| `project_conductor.cli` | Adds local `--registry-json` inspection output. |

## Public Interfaces

| Interface | Purpose |
| --- | --- |
| `build_artifact_registry(scan)` | Convert a `RepositoryScan` into `ArtifactRegistry`. |
| `ArtifactRegistry` | Registry root object with deterministic JSON export. |
| `RegistryArtifact` | Normalized registry entry. |
| `RegistryValidationReport` | Structural validation result. |
| `validate_registry_artifacts(artifacts)` | Validate registry artifact structure. |

## Registry Entry Fields

| Field | Source |
| --- | --- |
| `artifact_id` | Metadata `ID` when available, otherwise deterministic path digest. |
| `path` | `Artifact.path`. |
| `type` | `Artifact.artifact_type`. |
| `title` | `Artifact.title`. |
| `hash` | `Artifact.sha256`. |
| `metadata_status` | Derived from metadata presence and required fields. |
| `metadata_id` | Metadata `ID`, if present. |
| `problems` | Scan problem messages for that artifact. |
| `source_provider` | `filesystem`. |

## Data Flow

1. Repository Discovery Capability, Filesystem Provider produces `RepositoryScan`.
2. `build_artifact_registry()` sorts scan artifacts by path.
3. Each artifact becomes a `RegistryArtifact`.
4. Registry structure is validated.
5. `ArtifactRegistry.to_json()` emits deterministic JSON using sorted keys.

## Error Handling Approach

- Registry conversion does not raise for missing metadata.
- Missing or incomplete metadata becomes `metadata_status` and validation warning.
- Duplicate artifact IDs become validation errors.
- Invalid source provider, empty path, empty type, empty hash, or non-deterministic ordering become validation errors.

## Explicit Non-Implementation

No database, persistence layer, Git enrichment, quality gate workflow, link validation, dependency validation, AI, LangGraph, MCP, AI Gateway, Prompt Platform, Context Platform, Knowledge Platform, Browser Automation, or agents are implemented.

