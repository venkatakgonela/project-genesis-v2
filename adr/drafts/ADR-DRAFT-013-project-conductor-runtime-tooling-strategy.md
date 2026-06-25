# ADR-DRAFT-013: Project Conductor Runtime and Tooling Strategy

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-013 |
| Title | Project Conductor Runtime and Tooling Strategy |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005A, ARCH-SPEC-001 |
| Related ADRs | ADR-002, ADR-012 |
| Related Work Packages | WP-005, WP-005A |
| Tags | adr-draft, project-conductor, runtime-tooling |
| Review Date | 2026-07-09 |

## Context

Project Conductor requires deterministic repository scanning, metadata validation, dependency checks, registry generation, and reporting.

## Decision Question

What runtime and tooling strategy should be used for Project Conductor implementation?

## Candidate Options

- Python with uv.
- Node.js/TypeScript with pnpm.
- Go single-binary tooling.
- POSIX shell with Make.

## Evidence Required

- Capability fit comparison.
- Maintainability assessment.
- Testing and packaging implications.
- Migration risk analysis.
- Local and future CI execution implications.

## Draft Recommendation

No final technology selection yet.

Complete WP-005A before promoting this ADR.

