# Sprint 1 Design

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-DESIGN |
| Title | Sprint 1 Repository Discovery Capability, Filesystem Provider Design |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008, PC-PROD-001, DCF-001, DCF-002, DCF-003 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | project-conductor, sprint-design, repository-scanner |
| Review Date | 2026-07-02 |

## Sprint Objective

Create the deterministic Repository Discovery Capability, Filesystem Provider that discovers repository artifacts and builds an in-memory representation.

## Functional Requirements

- Accept a repository root path.
- Reject a missing or non-directory root.
- Traverse files in deterministic order.
- Exclude `.git`, `.venv`, `venv`, Python cache folders, test/tool caches, and `node_modules`.
- Discover Markdown artifacts only.
- Extract the first Markdown H1 as artifact title.
- Extract Project Genesis `## Metadata` tables into a structured object.
- Identify missing required metadata fields without failing the whole scan.
- Compute file size, line count, suffix, relative path, artifact type, and SHA-256 hash.
- Return an in-memory `RepositoryScan` object.
- Provide `to_dict()` methods for local inspection and future serialization.
- Provide a thin CLI for human smoke testing.

## Non-Functional Requirements

- Deterministic path ordering.
- Standard-library-first implementation.
- No network dependency.
- No runtime service.
- No generated registry output.
- Testable with local unit and integration tests.
- Python 3.9 compatible.
- Modular enough to support future registry and quality gate slices.

## Assumptions

- Markdown artifacts are the initial repository artifact type.
- The current `## Metadata` table shape remains the Sprint 1 source metadata convention.
- Missing metadata is a discovery diagnostic, not a quality gate failure in this sprint.
- Artifact type classification can be path-based for the first slice.
- Git enrichment is deferred.

## Risks

| Risk | Mitigation |
| --- | --- |
| Scanner behavior drifts into quality gate validation. | Keep scan problems non-fatal and avoid pass/fail policy. |
| Metadata parsing is too permissive or too brittle. | Parse only the current table convention and report gaps without failing. |
| Future registry generation leaks into Sprint 1. | Expose in-memory model and JSON CLI output only for inspection. |
| Python version mismatch. | Keep syntax compatible with local Python 3.9. |

## Acceptance Criteria

| Criterion | Verification |
| --- | --- |
| Markdown artifacts are discovered. | Unit test. |
| Metadata tables are extracted. | Unit test. |
| Missing metadata is reported. | Unit test. |
| `.git` directory is excluded. | Unit test. |
| Scan order is deterministic. | Unit test. |
| CLI returns JSON output. | Integration test. |
| CLI returns summary output. | Integration test. |

