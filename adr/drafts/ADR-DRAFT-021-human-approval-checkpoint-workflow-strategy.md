# ADR-DRAFT-021: Human Approval and Checkpoint Workflow Strategy

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-021 |
| Title | Human Approval and Checkpoint Workflow Strategy |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005I, ADR-DRAFT-015, ADR-DRAFT-019 |
| Related ADRs | ADR-002 |
| Related Work Packages | WP-005, WP-005I |
| Tags | adr-draft, project-conductor, human-approval, checkpointing |
| Review Date | 2026-07-23 |

## Context

Agentic Project Conductor must preserve human control over architecture, implementation handoff, review routing, and evidence publication.

## Decision Question

How should Project Conductor represent human approval, interrupts, checkpoints, and resumable workflow state?

## Candidate Options

- File-based checkpoint records.
- JSON/YAML workflow state.
- SQLite workflow state.
- Agent framework-native checkpointing.
- Git-backed review artifacts.
- Human approval manifests.

## Evidence Required

- Approval scenario analysis.
- Checkpoint shape examples.
- Failure and resume model.
- Audit trail requirements.
- Integration with artifact registry and agent framework options.

## Draft Recommendation

No final checkpoint or approval strategy selection yet.

Complete WP-005I before promoting this ADR.

