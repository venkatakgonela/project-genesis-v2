# Sprint 1 Known Limitations

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-EVD-LIMITATIONS |
| Title | Sprint 1 Known Limitations |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | evidence, limitations, repository-scanner |
| Review Date | 2026-07-02 |

## Known Limitations

| Limitation | Impact | Recommended Follow-Up |
| --- | --- | --- |
| Metadata parsing supports only the current `## Metadata` table convention. | Artifacts using other metadata styles will be treated as missing metadata. | Keep until metadata ADR is reviewed. |
| Scanner discovers Markdown artifacts only. | Non-Markdown files are not represented. | Review when future artifact types are explicitly introduced. |
| Missing metadata is diagnostic only. | No pass/fail quality gate exists yet. | Handle in a future quality gate sprint. |
| No generated registry file is written. | Future consumers cannot read a persisted registry yet. | Implement only after Sprint 1 review accepts the in-memory model. |
| No Git enrichment. | Modified/untracked/history state is unavailable. | Defer to a later repository state slice. |
| No link or dependency validation. | Broken links and dependency drift are not detected. | Defer to quality gate slices. |

