# Questions Requiring Chief Architect Review

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-REV-QUESTIONS |
| Title | Sprint 2 Chief Architect Questions |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | review, questions, chief-architect |
| Review Date | 2026-07-02 |

## Questions

1. Should metadata-free artifacts remain in the registry with generated path IDs, or should future persisted registries include only metadata-bearing durable artifacts?
2. Should `artifact_id` use raw metadata IDs, or should metadata-backed IDs be namespaced in the registry?
3. Should the registry schema become an explicit versioned schema artifact before any persisted registry output is introduced?
4. Should the next sprint persist generated registry JSON, or should it first harden the metadata contract?
5. Should validation warnings remain inside registry output, or should validation reports become separate artifacts later?

