# WP-008 Deterministic Project Conductor MVP Implementation

## Metadata

| Field | Value |
| --- | --- |
| ID | WP-008 |
| Title | Deterministic Project Conductor MVP Implementation |
| Version | 0.1.0 |
| Status | Sprint 1 Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-007, PC-PROD-001, ARCH-SPEC-001, ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-006, WP-007, WP-008 |
| Tags | project-conductor, implementation, deterministic-mvp, sprint-001 |
| Review Date | 2026-07-02 |

## Objective

Implement Sprint 1 only: a deterministic Repository Discovery Capability, Filesystem Provider that discovers repository Markdown artifacts and builds an in-memory representation.

## Scope

In scope:

- Python package scaffold.
- Deterministic Markdown artifact discovery.
- Exclusion of non-artifact tool directories such as `.git`, `.venv`, caches, and `node_modules`.
- Metadata table extraction from the current Project Genesis `## Metadata` table convention.
- Stable path ordering, file facts, SHA-256 hashes, titles, artifact type classification, and non-fatal scan problems.
- Thin CLI for local example execution.
- Unit and integration tests.
- Sprint documentation, evidence, and review package.

Out of scope:

- Generated artifact registry files.
- Quality gates.
- Link validation.
- Dependency validation.
- Git history or Git status enrichment.
- Prompt Platform, Context Platform, Knowledge Platform, AI Gateway, MCP, LangGraph, browser automation, or agentic behavior.
- Sprint 2 work.

## Deliverables

| Deliverable | Artifact | Status |
| --- | --- | --- |
| Sprint report | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/sprint-report.md` | Complete for Review |
| Sprint README | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/README.md` | Complete for Review |
| Sprint design | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/sprint-design.md` | Complete for Review |
| Technical design | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/technical-design.md` | Complete for Review |
| Architecture notes | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/architecture-notes.md` | Complete for Review |
| Design rationale | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/design-rationale.md` | Complete for Review |
| Developer notes | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/developer-notes.md` | Complete for Review |
| Evidence package | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/evidence/` | Complete for Review |
| Review package | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/review/` | Complete for Review |
| Implementation | `src/project_conductor/` | Complete for Review |
| Tests | `tests/project_conductor_tests/` and `tests/fixtures/repository-scanner/` | Complete for Review |

## Acceptance Status

| Criterion | Status |
| --- | --- |
| Scanner discovers Markdown artifacts deterministically. | Passed |
| Scanner builds an in-memory representation. | Passed |
| Scanner extracts current Markdown metadata tables. | Passed |
| Scanner reports missing metadata without failing the scan. | Passed |
| Scanner excludes `.git` and common tool/cache directories. | Passed |
| Tests run locally. | Passed |
| No future Project Conductor capabilities were implemented. | Passed |
| Review and evidence package created. | Passed |

## Stop Point

Sprint 1 is complete for review.

Do not continue to Sprint 2 until Chief Architect review accepts this slice.

