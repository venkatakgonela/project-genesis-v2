# Sprint 3 Corrective Chief Architect Review Context

## Current Sprint Objective

WP-010 Sprint 3 implements Metadata Contract and Registry Schema Hardening for the deterministic Project Conductor MVP.

The sprint does not persist generated registry output. It defines and enforces the deterministic metadata contract and explicit versioned registry schema required before persistence can be considered.

## Architecture Decisions Touched

- Metadata contract is versioned independently as `1.0.0`.
- Registry schema is versioned independently as `1.0.0`.
- Registry model version is advanced to `0.2.0`.
- Metadata-backed artifacts use `artifact_id = metadata:<ID>`.
- Metadata-free artifacts use `artifact_id = path:<sha1>`.
- Raw metadata ID is preserved as `metadata_id`.
- Metadata-free artifacts remain discoverable.
- Metadata-free artifacts are non-durable unless explicitly allowed in future architecture decisions.
- Durable registry authorities require complete metadata and an approved artifact type.

## Suggested Next Decision

Chief Architect should decide whether Sprint 4 should create a machine-readable JSON Schema artifact before any generated registry persistence is introduced.
