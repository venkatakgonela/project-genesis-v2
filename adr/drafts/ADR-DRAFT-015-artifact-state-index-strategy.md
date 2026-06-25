# ADR-DRAFT-015: Artifact State and Index Strategy

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-015 |
| Title | Artifact State and Index Strategy |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005C, ADR-DRAFT-013, ADR-DRAFT-014 |
| Related ADRs | ADR-002 |
| Related Work Packages | WP-005, WP-005C |
| Tags | adr-draft, project-conductor, artifact-index |
| Review Date | 2026-07-16 |

## Context

Project Conductor requires Artifact Registry, Work Package Registry, Review Queue, and Evidence Index interfaces.

## Decision Question

How should Project Conductor represent artifact state, registries, review queues, and evidence indexes?

## Candidate Options

- Generated JSON index.
- Generated YAML index.
- SQLite database.
- Markdown summary reports backed by structured index.
- Graph export formats.

## Evidence Required

- Interface-to-state mapping.
- Diffability and reviewability analysis.
- Query needs.
- Local-first operation analysis.
- Dashboard integration implications.

## Draft Recommendation

No final state/index strategy selection yet.

Complete WP-005C before promoting this ADR.

