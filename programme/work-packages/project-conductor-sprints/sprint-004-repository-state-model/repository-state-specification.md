# Repository State Specification

## Purpose

Repository State is the canonical deterministic snapshot of the current repository state. It is derived from ArtifactRegistry.

## Top-Level Fields

| Field | Description |
| --- | --- |
| `version` | Repository State, registry, registry schema, and metadata contract versions. |
| `generator` | Generator name, version, and deterministic generated timestamp. |
| `repository` | Provider-independent repository summary. |
| `statistics` | Artifact and metadata aggregate counts. |
| `metadata` | Metadata completeness and durability summary. |
| `validation_summary` | Compact registry validation status. |
| `validation` | Repository State structural validation report. |
| `registry_validation` | Original ArtifactRegistry validation report. |
| `artifacts` | Deterministically ordered registry artifacts. |

## Determinism Rules

- Artifact ordering follows ArtifactRegistry ordering.
- Classification counts are sorted by key.
- JSON keys are sorted during serialization.
- Default generated timestamp is fixed.
- No filesystem, Git, database, network, prompt, agent, or AI dependency is used by the state model.
