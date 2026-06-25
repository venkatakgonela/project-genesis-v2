# Sprint 1 Repository Discovery Capability, Filesystem Provider

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-README |
| Title | Sprint 1 Repository Discovery Capability, Filesystem Provider README |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | project-conductor, sprint-001, repository-scanner |
| Review Date | 2026-07-02 |

## Purpose

Sprint 1 implements the first vertical slice of deterministic Project Conductor: repository scanning.

The Repository Discovery Capability, Filesystem Provider discovers Markdown artifacts, reads their current metadata table shape, computes stable file facts, and returns an in-memory representation for future slices.

## Scope Boundary

This sprint does not generate registry files, run quality gates, validate links, inspect Git history, implement dashboards, or add assisted or agentic capabilities.

## Implementation Files

| Path | Purpose |
| --- | --- |
| `src/project_conductor/scanner.py` | Repository Discovery Capability, Filesystem Provider model and repository scanning logic. |
| `src/project_conductor/cli.py` | Thin local CLI for example execution. |
| `src/project_conductor/__init__.py` | Public package exports. |
| `tests/project_conductor_tests/` | Unit and integration tests. |
| `tests/fixtures/repository-scanner/` | Stable scanner fixture data. |

## Local Commands

Run tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'
```

Run through uv with a sandbox-safe cache:

```bash
UV_CACHE_DIR=/private/tmp/project-genesis-v2-uv-cache PYTHONPATH=src uv run --no-sync python -m unittest discover -s tests -p 'test_*.py'
```

Run the Repository Discovery Capability, Filesystem Provider:

```bash
PYTHONPATH=src python3 -m project_conductor.cli --root tests/fixtures/repository-scanner/basic-repo --json
```

