# Sprint 1 Technical Design

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-TECH-DESIGN |
| Title | Sprint 1 Repository Discovery Capability, Filesystem Provider Technical Design |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008, PC-S1-DESIGN |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | project-conductor, technical-design, repository-scanner |
| Review Date | 2026-07-02 |

## Component Diagram

```text
CLI
  -> scan_repository(root)
      -> file traversal
      -> artifact scanner
          -> title extraction
          -> metadata table extraction
          -> hash and file facts
          -> artifact classification
      -> RepositoryScan
```

## Module Responsibilities

| Module | Responsibility |
| --- | --- |
| `project_conductor.scanner` | Repository traversal, artifact scanning, metadata extraction, in-memory model creation. |
| `project_conductor.cli` | Argument parsing and local summary or JSON output. |
| `project_conductor.__init__` | Public package exports. |

## Public Interfaces

| Interface | Purpose |
| --- | --- |
| `scan_repository(root)` | Main Sprint 1 scanner entry point. |
| `RepositoryScan` | In-memory representation of a completed scan. |
| `Artifact` | In-memory representation of one discovered artifact. |
| `MetadataTable` | Parsed metadata table and missing-field state. |
| `ScanProblem` | Non-fatal scan diagnostic. |
| `RepositoryScanError` | Fatal scan startup error. |

## Repository Layout

```text
src/project_conductor/
  __init__.py
  cli.py
  scanner.py

tests/project_conductor_tests/
  __init__.py
  test_cli.py
  test_scanner.py

tests/fixtures/repository-scanner/basic-repo/
  README.md
  docs/no-metadata.md
```

## Data Flow

1. Caller provides repository root.
2. Scanner validates the root.
3. Scanner traverses files in sorted order while excluding tool/cache directories.
4. Scanner filters to Markdown artifacts.
5. Scanner reads each artifact as bytes and text.
6. Scanner extracts title and metadata table.
7. Scanner computes file facts and SHA-256 hash.
8. Scanner classifies artifact by path.
9. Scanner returns `RepositoryScan` containing sorted artifacts and non-fatal problems.

## Error Handling Approach

- Missing root or non-directory root raises `RepositoryScanError`.
- Per-file read errors become `ScanProblem` entries instead of aborting the whole scan.
- Missing metadata becomes a `ScanProblem`.
- Missing metadata fields become a `ScanProblem`.
- Decode errors are handled with UTF-8 replacement so scanning can continue.

## Explicit Non-Implementation

This design does not include generated registries, quality gates, Git enrichment, SQLite, YAML migration, link validation, dependency validation, prompt/context generation, or agentic workflows.

