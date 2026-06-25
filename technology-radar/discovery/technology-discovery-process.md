# Technology Discovery Process

## Metadata

| Field | Value |
| --- | --- |
| ID | TD-002 |
| Title | Technology Discovery Process |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | TD-001 |
| Related ADRs | ADR-012 |
| Related Work Packages | WP-003 |
| Tags | technology-discovery, process |
| Review Date | 2026-07-02 |

## Purpose

This process defines how a technology moves from initial signal to approved architecture decision.

## Process Stages

| Stage | Purpose | Required Output | Exit Criteria |
| --- | --- | --- | --- |
| 1. Discovery Intake | Capture a technology signal or capability need. | Discovery intake record. | Technology has a capability area and reason for review. |
| 2. Scope Framing | Define what question the evaluation should answer. | Discovery brief. | Evaluation scope, non-goals, and constraints are documented. |
| 3. Candidate Qualification | Decide whether a technology belongs in the evaluation set. | Candidate list. | Candidate meets minimum relevance and evidence availability criteria. |
| 4. Evaluation Planning | Define criteria, evidence, scenarios, and acceptance thresholds. | Evaluation plan. | Reviewer agrees the plan can produce decision-grade evidence. |
| 5. Evidence Collection | Gather structured evidence without selecting winners prematurely. | Evidence pack. | Evidence is traceable, sufficient, and reviewable. |
| 6. Comparison Matrix | Compare candidates against agreed criteria. | Comparison matrix. | Differences are visible without over-claiming certainty. |
| 7. Recommendation | Produce a recommendation for Adopt, Trial, Assess, or Hold. | Evaluation report and recommendation. | Recommendation is supported by evidence. |
| 8. ADR Drafting | Convert architecture-shaping recommendations into ADRs. | ADR draft. | ADR contains context, decision, alternatives, consequences, and review plan. |
| 9. Architecture Approval | Review and approve, revise, or reject the ADR. | Approved or rejected ADR. | Chief Architect decision recorded. |
| 10. Implementation Authorization | Permit implementation planning only after approval. | Implementation work package proposal. | Work package traces to approved ADR and evaluation evidence. |

## Intake Rules

Each discovery intake must identify:

- Capability area.
- Problem or decision question.
- Candidate technology or technology category.
- Source of signal.
- Urgency.
- Known constraints.
- Related ADRs.
- Related work packages.

## Evidence Rules

Evidence should be:

- Traceable to sources or experiments.
- Relevant to the capability.
- Comparable across candidates.
- Explicit about limitations.
- Stored as a version-controlled artifact.

## Promotion Rules

A technology may move:

- From Watch to Assess when it has capability relevance.
- From Assess to Trial when an evaluation plan and controlled scope exist.
- From Trial to Adopt only after evidence and ADR approval.
- From any ring to Hold when risk, complexity, cost, or lack of fit outweighs value.

## Stop Conditions

Pause or stop discovery when:

- The capability architecture is not mature enough to evaluate technology fit.
- The technology requires implementation before evaluation questions are clear.
- Evidence cannot be gathered credibly.
- The candidate duplicates an already evaluated option without new information.

