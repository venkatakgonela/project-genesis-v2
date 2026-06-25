# Project Conductor Architecture Specification

## Metadata

| Field | Value |
| --- | --- |
| ID | ARCH-SPEC-001 |
| Title | Project Conductor Architecture Specification |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | ARCH-001, ARCH-002, ARCH-003 |
| Related ADRs | ADR-002 |
| Related Work Packages | WP-001 |
| Tags | platform, conductor, governance |
| Review Date | 2026-07-16 |

## Purpose

Project Conductor is the coordination capability for artifact lifecycle, work package sequencing, review cadence, and evidence expectations.

## Responsibilities

- Maintain the relationship between capabilities, ADRs, work packages, evaluation plans, evidence, reviews, and lessons learned.
- Provide a consistent view of current programme state.
- Enforce lifecycle expectations before implementation begins.
- Support future automation of repository health checks and artifact traceability.

## Non-Responsibilities

- It does not implement AI workflows.
- It does not select model providers.
- It does not replace architecture review.
- It does not own business application logic.

## Conceptual Interfaces

| Interface | Description |
| --- | --- |
| Artifact Registry | Future index of artifacts and lifecycle states. |
| Work Package Registry | Future index of planned, active, blocked, and completed work packages. |
| Review Queue | Future list of artifacts requiring review. |
| Evidence Index | Future link between claims and evidence artifacts. |

## Future Implementation Direction

Start deterministic: repository scans, metadata validation, dependency checks, and dashboard generation. Avoid agentic orchestration until artifact structure and lifecycle rules are stable.

## Evaluation

Project Conductor should be evaluated on traceability coverage, metadata completeness, stale artifact detection, and correctness of generated programme state.

## Open Questions

- Should Project Conductor begin as scripts, CI checks, or a static report generator?
- What artifact graph format should become canonical?

