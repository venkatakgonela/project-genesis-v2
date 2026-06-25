# Sprint 2 Test Results

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-EVD-TESTS |
| Title | Sprint 2 Test Results |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | evidence, tests, artifact-registry |
| Review Date | 2026-07-02 |

## Local Unit and Integration Tests

Command:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'
```

Result:

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 0.110s

OK
```

## uv Execution

Command:

```bash
UV_CACHE_DIR=/private/tmp/project-genesis-v2-uv-cache PYTHONPATH=src uv run --no-sync python -m unittest discover -s tests -p 'test_*.py'
```

Result:

```text
Using CPython 3.14.3
Creating virtual environment at: .venv
...........
----------------------------------------------------------------------
Ran 11 tests in 0.069s

OK
```

## Added Sprint 2 Test Coverage

| Behavior | Test |
| --- | --- |
| Build registry from fixture scan. | `ArtifactRegistryTests.test_builds_registry_from_repository_scan` |
| Compare deterministic JSON to golden output. | `ArtifactRegistryTests.test_registry_json_matches_golden_output` |
| Detect duplicate registry artifact IDs. | `ArtifactRegistryTests.test_validation_detects_duplicate_ids` |
| CLI registry JSON output. | `RepositoryScannerCliTests.test_cli_outputs_registry_json` |

