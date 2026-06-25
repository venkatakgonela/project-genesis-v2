# Sprint 2 Design Rationale

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-RATIONALE |
| Title | Sprint 2 Design Rationale |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009, DCF-002, DCF-003 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | rationale, project-conductor, artifact-registry |
| Review Date | 2026-07-02 |

## Key Choices

| Choice | Rationale |
| --- | --- |
| Metadata `ID` as preferred artifact ID | Reuses existing durable artifact identity where available. |
| Path-derived ID for metadata-free artifacts | Gives every discovered artifact a stable registry identity without forcing metadata migration. |
| SHA-1 path digest for generated IDs | Used only as a deterministic path identifier, not for content integrity. |
| SHA-256 content hash from scan | Preserves Sprint 1 content identity. |
| Structural validation only | Avoids implementing Sprint 3 quality gates. |
| JSON export with sorted keys | Makes golden output deterministic and reviewable. |
| Source provider field | Records that registry entries come from Repository Discovery Capability, Filesystem Provider. |

## Deferred Choices

- Persisted generated registry files.
- Registry schema version migration policy.
- Duplicate metadata ID remediation workflow.
- Link and dependency validation.
- Git state enrichment.
- Quality gate severity model.
- SQLite or other database storage.

