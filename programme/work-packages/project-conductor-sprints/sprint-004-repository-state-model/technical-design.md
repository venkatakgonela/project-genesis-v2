# Sprint 4 Technical Design

## Components

```text
RepositoryScan -> ArtifactRegistry -> RepositoryState
```

Repository State depends on ArtifactRegistry only. It does not import scanner, filesystem, Git, database, network, prompt, agent, or AI modules.

## Module Responsibilities

| Module | Responsibility |
| --- | --- |
| `project_conductor.state` | Repository State model, builder, validator, deterministic JSON export. |
| `project_conductor.registry` | Existing ArtifactRegistry source model. |
| `project_conductor.cli` | Optional local export path for scan, registry, or state JSON. |

## Public Interfaces

- `RepositoryState`
- `RepositoryStateBuilder`
- `RepositoryStateValidator`
- `RepositoryStatistics`
- `RepositorySummary`
- `MetadataSummary`
- `ValidationSummary`
- `GeneratorInformation`
- `VersionInformation`
- `build_repository_state(registry)`
- `validate_repository_state(state)`

## Error Handling

Repository State validation produces structured validation reports instead of raising for normal structural defects.

## Serialization

Serialization uses `json.dumps(..., indent=2, sort_keys=True)` and appends a trailing newline for deterministic text output.
