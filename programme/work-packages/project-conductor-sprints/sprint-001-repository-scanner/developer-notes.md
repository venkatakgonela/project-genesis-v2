# Sprint 1 Developer Notes

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-DEV-NOTES |
| Title | Sprint 1 Developer Notes |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | developer-notes, project-conductor, scanner |
| Review Date | 2026-07-02 |

## Local Setup

The implementation has no third-party runtime dependencies.

Use `PYTHONPATH=src` for local execution until packaging workflow is reviewed.

## Test Command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'
```

## uv Command

```bash
UV_CACHE_DIR=/private/tmp/project-genesis-v2-uv-cache PYTHONPATH=src uv run --no-sync python -m unittest discover -s tests -p 'test_*.py'
```

The explicit `UV_CACHE_DIR` keeps uv cache writes inside the sandbox-safe temporary directory.

## Scanner Command

```bash
PYTHONPATH=src python3 -m project_conductor.cli --root tests/fixtures/repository-scanner/basic-repo --json
```

## Implementation Notes

- `scan_repository()` is the public entry point.
- `RepositoryScan`, `Artifact`, `MetadataTable`, and `ScanProblem` are immutable dataclasses.
- Sorting is path-based and deterministic.
- Missing metadata is reported as a scan problem.
- The Repository Discovery Capability, Filesystem Provider does not write files.

