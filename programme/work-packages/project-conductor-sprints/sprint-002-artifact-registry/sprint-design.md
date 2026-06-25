# Sprint 2 Design

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-DESIGN |
| Title | Sprint 2 Artifact Registry Model Design |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009, PC-S1-DESIGN, DCF-002, DCF-003 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | project-conductor, sprint-design, artifact-registry |
| Review Date | 2026-07-02 |

## Sprint Objective

Create an Artifact Registry Model that deterministically normalizes Repository Discovery Capability, Filesystem Provider output into registry entries.

## Functional Requirements

- Accept a `RepositoryScan`.
- Convert scan artifacts into registry artifacts.
- Preserve deterministic path ordering.
- Generate stable artifact IDs.
- Include path, type, title, hash, metadata status, problems, and source provider.
- Preserve metadata IDs when present.
- Generate deterministic JSON.
- Validate registry structure.
- Produce validation report.
- Add golden output for fixture repository.

## Non-Functional Requirements

- Standard-library-only implementation.
- Deterministic JSON ordering.
- No database.
- No registry persistence beyond explicit JSON export and test golden file.
- No quality gate semantics.
- No Git enrichment.
- Python 3.9 compatible.

## Assumptions

- Metadata `ID` is the preferred stable artifact ID when present.
- Artifacts without metadata receive deterministic path-derived IDs.
- SHA-256 from Repository Discovery Capability, Filesystem Provider is the registry hash.
- Registry validation is structural only, not a quality gate.

## Risks

| Risk | Mitigation |
| --- | --- |
| Artifact ID strategy needs future refinement. | Keep ID generation isolated in `registry.py`. |
| Registry validation becomes a quality gate. | Return validation report without pass/fail workflow enforcement. |
| JSON export is mistaken for persisted registry generation. | Document that export is deterministic inspection, not repository persistence. |
| Metadata-free artifacts create warnings. | Preserve warnings in validation report without blocking registry validity. |

## Acceptance Criteria

| Criterion | Verification |
| --- | --- |
| Registry converts fixture scan into two entries. | Unit test. |
| Metadata artifact uses metadata ID. | Unit test. |
| Missing metadata artifact receives path-derived ID. | Unit test. |
| Registry JSON matches golden output. | Integration test. |
| Duplicate IDs are detected by validation. | Unit test. |
| CLI exports registry JSON. | Integration test. |

