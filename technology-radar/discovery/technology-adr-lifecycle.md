# Technology ADR Lifecycle

## Metadata

| Field | Value |
| --- | --- |
| ID | TD-004 |
| Title | Technology ADR Lifecycle |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | TD-001, TD-002, TD-003 |
| Related ADRs | ADR-012 |
| Related Work Packages | WP-003 |
| Tags | technology-discovery, adr, lifecycle |
| Review Date | 2026-07-02 |

## Purpose

This lifecycle defines how technology evaluations become architecture decisions.

## Lifecycle

```text
Technology Discovery
-> Evaluation
-> Comparison Matrix
-> Recommendation
-> ADR
-> Architecture Approval
-> Implementation
```

## ADR Entry Conditions

A technology recommendation should become an ADR when it:

- Shapes platform architecture.
- Creates provider, data, deployment, or operational lock-in.
- Becomes a default for a capability.
- Affects security, privacy, observability, cost, or maintainability.
- Changes the Technology Radar ring to Adopt or Hold.

## ADR Content Requirements

Technology ADRs must include:

- Capability area.
- Decision question.
- Options considered.
- Evaluation evidence.
- Recommendation.
- Consequences.
- Migration and lock-in analysis.
- Cost and operational impact.
- Review date.
- Reversal conditions.

## ADR Status Flow

| Status | Meaning |
| --- | --- |
| Placeholder | Decision area exists, but evaluation has not begun. |
| Proposed | Recommendation exists and ADR is ready for review. |
| Approved | Chief Architect accepts the decision for a defined scope. |
| Trial Approved | Controlled use is permitted under a work package. |
| Superseded | Replaced by a later ADR. |
| Deprecated | Decision should no longer guide new work. |
| Rejected | Recommendation was reviewed and not accepted. |

## Architecture Approval Rules

- ADR approval is required before implementation planning.
- Trial approval must define scope, duration, evidence expectations, and rollback conditions.
- Adopt approval must define the default use case and limits.
- Hold decisions must explain what evidence could reopen the decision.

## Implementation Authorization

Implementation may be planned only when:

- The relevant capability has an architecture artifact.
- The technology evaluation is complete.
- The ADR is approved or trial-approved.
- A work package exists.
- Evaluation and evidence plans exist.

## Review and Reversal

Each technology ADR must define:

- Review date.
- Evidence that would confirm the decision.
- Evidence that would challenge the decision.
- Migration path if reversed.
- Technology Watch signals that should trigger re-review.

