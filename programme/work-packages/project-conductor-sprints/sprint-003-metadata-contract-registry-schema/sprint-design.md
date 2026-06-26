# Sprint 3 Design

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S3-DESIGN |
| Title | Sprint 3 Metadata Contract and Registry Schema Design |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-010, PC-S2-REPORT |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-010 |
| Tags | sprint-design, project-conductor, metadata-contract, registry-schema |
| Review Date | 2026-07-02 |

## Sprint Objective

Define and enforce a versioned metadata contract and explicit registry schema before registry persistence.

## Functional Requirements

- Define required metadata fields.
- Define optional metadata fields.
- Define allowed metadata status values.
- Define durable registry authority types.
- Update artifact ID generation rules.
- Add durable flag to registry artifacts.
- Add registry schema and metadata contract versions to registry root.
- Validate schema structure with standard library only.
- Preserve metadata-free artifact discoverability.
- Mark metadata-free artifacts non-durable.
- Update tests and golden output.

## Non-Functional Requirements

- Standard-library-only implementation.
- Deterministic JSON output.
- Backward-compatible in process because no persisted registry exists.
- No database, persistence, Git enrichment, quality gates, or AI/agent capability.

## Acceptance Criteria

| Criterion | Verification |
| --- | --- |
| Metadata contract constants exist. | Unit test. |
| Registry schema version appears in JSON. | Unit and golden tests. |
| Metadata-backed artifact IDs use `metadata:<ID>`. | Unit and golden tests. |
| Metadata-free artifact IDs use `path:<sha1>`. | Unit and golden tests. |
| Metadata-free artifacts are non-durable. | Unit and golden tests. |
| Invalid metadata status fails validation. | Negative unit test. |
| Unprefixed metadata artifact ID fails validation. | Negative unit test. |
| Metadata-free durable artifact fails validation. | Negative unit test. |

