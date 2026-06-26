# Metadata Contract

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S3-METADATA-CONTRACT |
| Title | Sprint 3 Metadata Contract |
| Version | 1.0.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-010, DOC-001 |
| Related ADRs | ADR-DRAFT-014 |
| Related Work Packages | WP-010 |
| Tags | metadata-contract, project-conductor |
| Review Date | 2026-07-02 |

## Contract Version

`1.0.0`

## Required Metadata Fields

- ID
- Title
- Version
- Status
- Owner
- Created Date
- Updated Date
- Dependencies
- Related ADRs
- Related Work Packages
- Tags
- Review Date

## Optional Metadata Fields

- Supersedes
- Superseded By
- Reviewers
- Evidence
- Lifecycle State
- Schema Version

## Metadata Status Values

| Status | Meaning |
| --- | --- |
| `complete` | Metadata exists and includes all required fields. |
| `incomplete` | Metadata exists but one or more required fields are missing. |
| `missing` | No supported metadata table was found. |

## Artifact ID Rules

| Artifact Case | Rule |
| --- | --- |
| Metadata-backed artifact | `artifact_id = metadata:<ID>` |
| Metadata-free artifact | `artifact_id = path:<sha1>` |
| Raw metadata ID | Preserved separately as `metadata_id`. |

## Durable Registry Authority Rules

An artifact is durable only when:

- It has complete metadata.
- Its artifact type is one of the approved durable authority types.

Approved durable registry authority types:

- `adr`
- `architecture`
- `baseline`
- `documentation`
- `platform-product`
- `platform-specification`
- `programme`
- `repository`
- `review`
- `technology-radar`
- `template`
- `work-package`

Metadata-free artifacts remain discoverable but are non-durable unless a future reviewed decision explicitly allows otherwise.

