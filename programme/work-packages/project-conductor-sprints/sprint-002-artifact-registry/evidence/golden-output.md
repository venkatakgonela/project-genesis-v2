# Sprint 2 Golden Output

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-EVD-GOLDEN |
| Title | Sprint 2 Golden Output |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | evidence, golden-output, artifact-registry |
| Review Date | 2026-07-02 |

## Golden Artifact

`tests/fixtures/repository-scanner/expected-artifact-registry.json`

## Purpose

The golden JSON output proves that registry export is deterministic for the existing fixture repository.

## Verification

`ArtifactRegistryTests.test_registry_json_matches_golden_output` compares `ArtifactRegistry.to_json()` with the golden file byte-for-byte as text.

