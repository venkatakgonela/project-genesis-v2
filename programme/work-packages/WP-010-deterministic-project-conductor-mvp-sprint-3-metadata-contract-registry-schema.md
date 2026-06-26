# WP-010 Deterministic Project Conductor MVP Sprint 3 Metadata Contract and Registry Schema

## Metadata

| Field | Value |
| --- | --- |
| ID | WP-010 |
| Title | Deterministic Project Conductor MVP Sprint 3 Metadata Contract and Registry Schema |
| Version | 0.1.0 |
| Status | Sprint 3 Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008, WP-009, WP-010 |
| Tags | project-conductor, implementation, deterministic-mvp, sprint-003, metadata-contract, registry-schema |
| Review Date | 2026-07-02 |

## Objective

Implement Sprint 3 only: harden the deterministic metadata contract and explicit versioned registry schema before any registry persistence work begins.

## Scope

In scope:

- Versioned metadata contract.
- Required metadata fields.
- Optional metadata fields.
- Allowed metadata status values.
- Artifact ID rules.
- Durable registry authority rules.
- Explicit registry schema document.
- Standard-library schema validation logic.
- Registry model updates.
- Negative tests for invalid metadata and invalid registry structure.
- Golden output update.
- Sprint 3 evidence and review package.

Out of scope:

- Database.
- Generated registry persistence.
- Git enrichment.
- Quality gates workflow.
- AI, LangGraph, MCP, AI Gateway, Prompt Platform, Context Platform, Knowledge Platform, Browser Automation, or agents.
- Sprint 4 work.

## Deliverables

| Deliverable | Artifact | Status |
| --- | --- | --- |
| Sprint design | `programme/work-packages/project-conductor-sprints/sprint-003-metadata-contract-registry-schema/sprint-design.md` | Complete for Review |
| Technical design | `programme/work-packages/project-conductor-sprints/sprint-003-metadata-contract-registry-schema/technical-design.md` | Complete for Review |
| Metadata contract document | `programme/work-packages/project-conductor-sprints/sprint-003-metadata-contract-registry-schema/metadata-contract.md` | Complete for Review |
| Registry schema document | `programme/work-packages/project-conductor-sprints/sprint-003-metadata-contract-registry-schema/registry-schema.md` | Complete for Review |
| Implementation updates | `src/project_conductor/metadata_contract.py`, `src/project_conductor/registry.py`, `src/project_conductor/scanner.py` | Complete for Review |
| Unit and integration tests | `tests/project_conductor_tests/test_registry.py` | Complete for Review |
| Golden output update | `tests/fixtures/repository-scanner/expected-artifact-registry.json` | Complete for Review |
| Evidence package | `programme/work-packages/project-conductor-sprints/sprint-003-metadata-contract-registry-schema/evidence/` | Complete for Review |
| Review package | `programme/work-packages/project-conductor-sprints/sprint-003-metadata-contract-registry-schema/review/` | Complete for Review |

## Acceptance Status

| Criterion | Status |
| --- | --- |
| Metadata contract is versioned and explicit. | Passed |
| Registry schema is versioned and explicit. | Passed |
| Artifact IDs follow `metadata:<ID>` and `path:<sha1>`. | Passed |
| Metadata-free artifacts remain discoverable and non-durable. | Passed |
| Durable registry authority rules are defined. | Passed |
| Standard-library validation logic exists. | Passed |
| Negative tests cover invalid metadata and ID structure. | Passed |
| Golden registry output updated. | Passed |
| No forbidden capabilities were implemented. | Passed |

## Stop Point

Sprint 3 is complete for review.

Do not continue to Sprint 4 until Chief Architect review accepts this slice.

