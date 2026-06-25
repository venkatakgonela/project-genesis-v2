# Sprint 1 Design Rationale

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-RATIONALE |
| Title | Sprint 1 Design Rationale |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | DCF-001, DCF-002, DCF-003 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | rationale, project-conductor, repository-scanner |
| Review Date | 2026-07-02 |

## Rationale

The Repository Discovery Capability, Filesystem Provider is intentionally small because Sprint 1 is the foundation slice for future Project Conductor work.

## Key Choices

| Choice | Rationale |
| --- | --- |
| Python standard library only | Matches WP-007 standard-library-first recommendation and avoids dependency sprawl. |
| In-memory model first | Satisfies Sprint 1 without implementing the generated registry slice. |
| Markdown-only artifact discovery | Matches current repository artifact format and avoids premature format expansion. |
| Non-fatal scan problems | Keeps scanner separate from future quality gates. |
| `to_dict()` methods | Enables CLI inspection and future serialization without writing generated artifacts. |
| Path-based artifact classification | Provides useful initial structure without building a full artifact graph. |
| Thin argparse CLI | Gives local evidence and smoke testing while avoiding Typer/Rich dependency decisions. |

## Deferred Choices

- Pydantic schema validation.
- Typer command structure.
- Rich console rendering.
- Generated JSON registry files.
- Markdown report generation.
- Quality gate severity model.
- Git state enrichment.
- Incremental indexing.
- SQLite.

