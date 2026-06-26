# Sprint 3 Golden Output

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S3-EVD-GOLDEN |
| Title | Sprint 3 Golden Output |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-010 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-010 |
| Tags | evidence, golden-output, registry-schema |
| Review Date | 2026-07-02 |

## Golden Artifact

`tests/fixtures/repository-scanner/expected-artifact-registry.json`

## Sprint 3 Changes

- Registry version updated to `0.2.0`.
- Registry schema version added as `1.0.0`.
- Metadata contract version added as `1.0.0`.
- Metadata-backed IDs now use `metadata:<ID>`.
- Path-backed IDs now use `path:<sha1>`.
- `durable` flag added to registry artifacts.

