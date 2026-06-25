# ADR-DRAFT-014: Artifact Metadata and Registry Format

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-014 |
| Title | Artifact Metadata and Registry Format |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005B, DOC-001 |
| Related ADRs | ADR-002 |
| Related Work Packages | WP-005, WP-005B |
| Tags | adr-draft, project-conductor, metadata |
| Review Date | 2026-07-09 |

## Context

Project Conductor must parse artifact metadata reliably. Current artifacts use Markdown metadata tables, while future validation may benefit from more structured metadata.

## Decision Question

What metadata and registry format should Project Conductor parse and validate?

## Candidate Options

- Existing Markdown metadata tables.
- YAML front matter.
- TOML front matter.
- Sidecar YAML or TOML manifests.
- Generated JSON schema-compatible metadata.

## Evidence Required

- Current artifact sample analysis.
- Authoring ergonomics.
- Machine-readability comparison.
- Migration impact.
- Schema validation strategy.

## Draft Recommendation

No final format selection yet.

Complete WP-005B before promoting this ADR.

