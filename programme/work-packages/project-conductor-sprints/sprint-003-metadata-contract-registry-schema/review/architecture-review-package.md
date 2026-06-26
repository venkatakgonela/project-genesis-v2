# Sprint 3 Architecture Review Package

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S3-REV-ARCH |
| Title | Sprint 3 Architecture Review Package |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-010 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-010 |
| Tags | review, architecture, metadata-contract, registry-schema |
| Review Date | 2026-07-02 |

## Sprint Summary

Sprint 3 defined and enforced the versioned metadata contract and registry schema.

## Design Decisions

- Shared metadata contract module owns required fields.
- Registry schema is versioned independently from registry model version.
- Metadata-backed artifact IDs use `metadata:<ID>`.
- Metadata-free artifact IDs use `path:<sha1>`.
- Metadata-free artifacts remain discoverable and non-durable.
- Structural validation remains separate from quality gates.

## Trade-Offs

| Trade-Off | Decision |
| --- | --- |
| Code constants vs external schema file | Chose code constants plus Markdown schema document for this slice. |
| Raw metadata ID vs prefixed ID | Chose prefixed registry IDs while preserving raw `metadata_id`. |
| Persist now vs harden first | Hardened first, no persistence. |
| Durable by metadata only vs type allow-list | Required complete metadata and approved durable authority type. |

## Outstanding Questions

- Should `repository` remain a durable authority type?
- Should prompt archive files be durable registry authorities later?
- Should Sprint 4 create a machine-readable JSON Schema artifact?

