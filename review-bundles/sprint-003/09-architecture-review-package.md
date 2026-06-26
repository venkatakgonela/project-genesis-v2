# Sprint 3 Architecture Review Package

## Sprint Summary

Sprint 3 defined and enforced a versioned metadata contract and explicit registry schema hardening layer before generated registry persistence.

## Design Decisions

- Shared metadata contract module owns required fields.
- Registry schema is versioned independently from registry model version.
- Metadata-backed artifact IDs use `metadata:<ID>`.
- Metadata-free artifact IDs use `path:<sha1>`.
- Raw metadata ID remains available as `metadata_id`.
- Metadata-free artifacts remain discoverable and non-durable.
- Durable authority status requires complete metadata and an approved artifact type.
- Structural validation remains separate from future quality gates.

## Trade-Offs

| Trade-Off | Decision |
| --- | --- |
| Code constants vs external schema file | Chose code constants plus Markdown schema document for this slice. |
| Raw metadata ID vs prefixed registry ID | Chose prefixed registry IDs while preserving raw `metadata_id`. |
| Persist now vs harden first | Hardened first, no persistence. |
| Durable by metadata only vs type allow-list | Required complete metadata and approved durable authority type. |

## Outstanding Questions

- Should `repository` remain a durable authority type?
- Should prompt archive files become durable registry authority artifacts later?
- Should Sprint 4 create a machine-readable JSON Schema artifact before persistence?
