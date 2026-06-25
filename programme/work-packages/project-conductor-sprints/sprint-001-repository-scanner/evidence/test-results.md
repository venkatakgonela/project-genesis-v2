# Sprint 1 Test Results

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-EVD-TESTS |
| Title | Sprint 1 Test Results |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | evidence, tests, repository-scanner |
| Review Date | 2026-07-02 |

## Local Unit and Integration Tests

Command:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'
```

Result:

```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.062s

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
.......
----------------------------------------------------------------------
Ran 7 tests in 0.035s

OK
```

## Test Coverage by Behavior

| Behavior | Test |
| --- | --- |
| Markdown artifact discovery with metadata | `RepositoryScannerTests.test_discovers_markdown_artifacts_with_metadata` |
| Deterministic path ordering | `RepositoryScannerTests.test_scan_order_is_deterministic` |
| `.git` exclusion | `RepositoryScannerTests.test_excludes_git_directory` |
| Missing metadata diagnostics | `RepositoryScannerTests.test_reports_missing_metadata_without_failing_scan` |
| Missing root rejection | `RepositoryScannerTests.test_rejects_missing_root` |
| CLI JSON output | `RepositoryScannerCliTests.test_cli_outputs_json_scan` |
| CLI summary output | `RepositoryScannerCliTests.test_cli_outputs_summary` |

