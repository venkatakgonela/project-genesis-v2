# Registry Schema

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S3-REGISTRY-SCHEMA |
| Title | Sprint 3 Registry Schema |
| Version | 1.0.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-010, PC-S3-METADATA-CONTRACT |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-010 |
| Tags | registry-schema, project-conductor |
| Review Date | 2026-07-02 |

## Schema Version

`1.0.0`

## Registry Root

| Field | Type | Required | Meaning |
| --- | --- | --- | --- |
| `registry_version` | string | Yes | Registry model version. Current value: `0.2.0`. |
| `registry_schema_version` | string | Yes | Registry schema version. Current value: `1.0.0`. |
| `metadata_contract_version` | string | Yes | Metadata contract version. Current value: `1.0.0`. |
| `source_provider` | string | Yes | Source provider. Current value: `filesystem`. |
| `artifact_count` | integer | Yes | Count of artifact entries. |
| `validation` | object | Yes | Structural validation report. |
| `artifacts` | array | Yes | Deterministically ordered registry entries. |

## Registry Artifact

| Field | Type | Required | Meaning |
| --- | --- | --- | --- |
| `artifact_id` | string | Yes | Stable ID following `metadata:<ID>` or `path:<sha1>`. |
| `path` | string | Yes | Repository-relative path. |
| `type` | string | Yes | Artifact type from Repository Discovery Capability, Filesystem Provider. |
| `title` | string or null | Yes | First Markdown H1 title, if found. |
| `hash` | string | Yes | SHA-256 file content hash from discovery. |
| `metadata_status` | string | Yes | One of `complete`, `incomplete`, `missing`. |
| `metadata_id` | string or null | Yes | Raw metadata `ID`, if present. |
| `durable` | boolean | Yes | Whether the artifact is a durable registry authority. |
| `problems` | array | Yes | Non-fatal discovery or metadata problem messages. |
| `source_provider` | string | Yes | Source provider for this artifact. |

## Validation Rules

- Artifact IDs must be non-empty.
- Artifact IDs must be unique.
- Metadata-backed IDs must start with `metadata:`.
- Path-backed IDs must start with `path:`.
- Metadata-free artifacts cannot be durable.
- Durable artifacts must use approved durable authority types.
- Paths, types, and hashes must be non-empty.
- Metadata status must be allowed by the metadata contract.
- Registry artifact ordering must be path-deterministic.
- Artifact source providers must match the registry source provider.

## Sprint 2 Compatibility Note

Sprint 2 registry output used raw metadata IDs as `artifact_id` values and did not include `durable`, `metadata_contract_version`, or `registry_schema_version`.

Sprint 3 intentionally changes the schema:

- `FIXTURE-001` becomes `metadata:FIXTURE-001`.
- `PATH-ce3a89079780` becomes `path:ce3a89079780`.
- `metadata_id` remains `FIXTURE-001`.
- `durable` identifies durable registry authorities.
- Registry root now includes explicit schema and metadata contract versions.

No persistence migration is required because registry persistence has not been implemented.

