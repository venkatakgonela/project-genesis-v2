# Sprint 3 Coverage Summary

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S3-EVD-COVERAGE |
| Title | Sprint 3 Coverage Summary |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-010 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-010 |
| Tags | evidence, coverage, metadata-contract, registry-schema |
| Review Date | 2026-07-02 |

## Coverage Command

```bash
PYTHONPATH=src python3 -m trace --count --summary --coverdir /private/tmp/pgv2-trace --module unittest discover -s tests -p 'test_*.py'
```

## Result

```text
...............
----------------------------------------------------------------------
Ran 15 tests in 0.124s

OK
```

Relevant project modules:

| Module | Lines | Executed-Line Coverage |
| --- | ---: | ---: |
| `project_conductor.__init__` | 5 | 100% |
| `project_conductor.cli` | 39 | 100% |
| `project_conductor.metadata_contract` | 28 | 100% |
| `project_conductor.registry` | 149 | 100% |
| `project_conductor.scanner` | 154 | 100% |
| `project_conductor_tests.test_cli` | 46 | 100% |
| `project_conductor_tests.test_registry` | 107 | 100% |
| `project_conductor_tests.test_scanner` | 51 | 100% |

Coverage caveat: `trace` reports executed-line coverage, not branch coverage.

