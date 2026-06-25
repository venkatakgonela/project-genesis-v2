# Questions Requiring Chief Architect Review

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-REV-QUESTIONS |
| Title | Sprint 1 Chief Architect Questions |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | review, questions, chief-architect |
| Review Date | 2026-07-02 |

## Questions

1. Should lightweight `README.md` index files be expected to contain metadata, or should the Repository Discovery Capability, Filesystem Provider later distinguish durable artifacts from navigational files?
2. Should the Repository Discovery Capability, Filesystem Provider include prompt archive files as artifacts by default, or should prompt archives be treated as source inputs outside the durable artifact registry?
3. Should generated registry output in the next sprint include every Markdown file or only metadata-bearing artifacts?
4. Is path-based artifact classification acceptable for Sprint 2, or should an explicit artifact type field be required?
5. Should the first persisted registry format be a direct `RepositoryScan.to_dict()` output or a narrower registry schema?

