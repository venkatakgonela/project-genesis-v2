# Sprint 2 Artifact Registry Model

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-README |
| Title | Sprint 2 Artifact Registry Model README |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009, PC-S1-REPORT |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | project-conductor, sprint-002, artifact-registry |
| Review Date | 2026-07-02 |

## Purpose

Sprint 2 implements the Artifact Registry Model.

It converts the in-memory `RepositoryScan` produced by Repository Discovery Capability, Filesystem Provider into deterministic `ArtifactRegistry` entries and JSON output.

## Implementation Files

| Path | Purpose |
| --- | --- |
| `src/project_conductor/registry.py` | Artifact Registry data model, conversion, JSON export, and validation. |
| `src/project_conductor/cli.py` | Adds `--registry-json` for deterministic registry inspection. |
| `tests/project_conductor_tests/test_registry.py` | Registry unit and integration tests. |
| `tests/fixtures/repository-scanner/expected-artifact-registry.json` | Golden expected registry JSON. |

## Local Commands

Run tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'
```

Run registry export:

```bash
PYTHONPATH=src python3 -m project_conductor.cli --root tests/fixtures/repository-scanner/basic-repo --registry-json
```

## Boundary

Sprint 2 does not persist the registry as a generated repository artifact. JSON export is available for deterministic inspection and test golden comparison only.

