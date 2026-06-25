# Sprint 2 Coverage Summary

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-EVD-COVERAGE |
| Title | Sprint 2 Coverage Summary |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | evidence, coverage, artifact-registry |
| Review Date | 2026-07-02 |

## Coverage Tool

Python standard-library `trace` was used for executed-line coverage.

Command:

```bash
PYTHONPATH=src python3 -m trace --count --summary --coverdir /private/tmp/pgv2-trace --module unittest discover -s tests -p 'test_*.py'
```

Result:

```text
...........
----------------------------------------------------------------------
Ran 11 tests in 0.121s

OK
```

Relevant project modules:

| Module | Lines | Executed-Line Coverage |
| --- | ---: | ---: |
| `project_conductor.__init__` | 4 | 100% |
| `project_conductor.cli` | 39 | 100% |
| `project_conductor.registry` | 128 | 100% |
| `project_conductor.scanner` | 154 | 100% |
| `project_conductor_tests.test_cli` | 45 | 100% |
| `project_conductor_tests.test_registry` | 46 | 100% |
| `project_conductor_tests.test_scanner` | 51 | 100% |

## Coverage Caveat

`trace` reports executed-line coverage, not branch coverage.

