# WP-005B Artifact Metadata and Registry Format Evaluation

## Metadata

| Field | Value |
| --- | --- |
| ID | WP-005B |
| Title | Artifact Metadata and Registry Format Evaluation |
| Version | 0.1.0 |
| Status | Planned |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005A, DOC-001 |
| Related ADRs | ADR-DRAFT-014 |
| Related Work Packages | WP-005 |
| Tags | foundation-technology, project-conductor, metadata |
| Review Date | 2026-07-09 |

## Objective

Evaluate how Project Conductor should read and validate artifact metadata.

## Scope

- Current Markdown artifacts.
- Future templates.
- Metadata representation.
- Parseability.
- Schema validation.
- Author ergonomics.

## Candidate Technologies

- Existing Markdown metadata tables.
- YAML front matter.
- TOML front matter.
- Sidecar YAML or TOML manifests.
- Generated JSON schema-compatible metadata.

## Evaluation Criteria

- Capability fit.
- Authoring simplicity.
- Machine readability.
- Migration risk.
- Validation quality.
- Future extensibility.
- Template consistency.

## Expected Evidence

- Current artifact sample analysis.
- Metadata extraction strategy.
- Migration impact assessment.
- Schema validation approach.

## Expected Deliverables

- Evaluation report.
- Evidence pack.
- Recommendation.
- ADR-DRAFT-014 update.

## Definition of Done

A metadata and registry format strategy is recommended with evidence and no artifact migration is performed.

