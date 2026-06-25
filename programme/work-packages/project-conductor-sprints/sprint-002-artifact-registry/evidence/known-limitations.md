# Sprint 2 Known Limitations

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-EVD-LIMITATIONS |
| Title | Sprint 2 Known Limitations |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | evidence, limitations, artifact-registry |
| Review Date | 2026-07-02 |

## Known Limitations

| Limitation | Impact | Recommended Follow-Up |
| --- | --- | --- |
| Metadata-free artifact IDs are path-derived. | File moves change generated ID. | Decide whether all durable artifacts must have metadata IDs. |
| Registry validation is structural only. | It does not enforce metadata completeness or architecture rules. | Defer to quality gate sprint. |
| Registry export is not persisted. | No generated repository registry artifact exists yet. | Decide in a later sprint if persisted registry output is required. |
| No duplicate ID remediation. | Validation can report duplicates but does not fix them. | Add remediation guidance later if needed. |
| No Git enrichment. | Registry has no changed/untracked state. | Defer to repository state sprint. |

