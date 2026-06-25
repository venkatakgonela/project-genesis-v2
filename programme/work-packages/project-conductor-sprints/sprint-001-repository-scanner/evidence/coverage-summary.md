# Sprint 1 Coverage Summary

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-EVD-COVERAGE |
| Title | Sprint 1 Coverage Summary |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008 |
| Related ADRs | ADR-DRAFT-013 |
| Related Work Packages | WP-008 |
| Tags | evidence, coverage, repository-scanner |
| Review Date | 2026-07-02 |

## Coverage Tool

The external `coverage` package was not installed locally, so Sprint 1 used Python standard-library `trace` to produce an executed-line coverage summary.

Command:

```bash
PYTHONPATH=src python3 -m trace --count --summary --coverdir /private/tmp/pgv2-trace --module unittest discover -s tests -p 'test_*.py'
```

Result:

```text
.......
----------------------------------------------------------------------
Ran 7 tests in 0.061s

OK
```

Relevant project modules:

| Module | Lines | Executed-Line Coverage |
| --- | ---: | ---: |
| `project_conductor.__init__` | 3 | 100% |
| `project_conductor.cli` | 33 | 100% |
| `project_conductor.scanner` | 152 | 100% |
| `project_conductor_tests.test_cli` | 33 | 100% |
| `project_conductor_tests.test_scanner` | 51 | 100% |

## Coverage Caveat

`trace` reports executed-line coverage, not branch coverage. Branch coverage should be introduced later if the programme approves a dedicated coverage dependency.

