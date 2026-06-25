# Technology Decision Gates

## Metadata

| Field | Value |
| --- | --- |
| ID | TD-005 |
| Title | Technology Decision Gates |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | TD-001, TD-002, TD-003, TD-004 |
| Related ADRs | ADR-012 |
| Related Work Packages | WP-003 |
| Tags | technology-discovery, decision-gates |
| Review Date | 2026-07-02 |

## Purpose

Decision gates prevent implementation from starting before technology choices are supported by evidence, ADRs, and architecture approval.

## Gate Model

| Gate | Name | Decision Question | Required Evidence | Allowed Outcome |
| --- | --- | --- | --- | --- |
| Gate 0 | Capability Readiness | Is the capability mature enough for technology discovery? | Capability roadmap entry, dependency position, related ADR placeholders. | Start discovery, defer, or refine capability scope. |
| Gate 1 | Discovery Intake | Is this technology or technology category worth evaluating? | Discovery intake, capability fit hypothesis, source signal. | Add to backlog, place on watch, or reject. |
| Gate 2 | Evaluation Plan Approval | Can the evaluation produce decision-grade evidence? | Evaluation plan, criteria, scope, non-goals, evidence plan. | Approve evaluation, revise, or defer. |
| Gate 3 | Evidence Review | Is the evidence sufficient and traceable? | Evidence pack, limitations, source links, scenario results where applicable. | Proceed to comparison, gather more evidence, or stop. |
| Gate 4 | Comparison Review | Are candidate differences visible and fair? | Comparison matrix using agreed criteria. | Proceed to recommendation, revise matrix, or narrow scope. |
| Gate 5 | Recommendation Review | Is the recommendation justified? | Evaluation report, recommendation, trade-offs, radar impact. | Draft ADR, keep Assess, hold, or run another evaluation. |
| Gate 6 | ADR Approval | Should this decision shape architecture? | ADR draft, evidence links, consequences, reversal conditions. | Approve, trial approve, reject, or revise. |
| Gate 7 | Implementation Authorization | Can implementation planning begin? | Approved ADR, work package, architecture artifact, evaluation plan, evidence plan. | Authorize implementation planning or block. |

## Gate Ownership

| Gate | Owner |
| --- | --- |
| Gate 0 | Chief Architect and Capability Owner |
| Gate 1 | Technology Discovery Owner |
| Gate 2 | Technology Discovery Owner and Reviewer |
| Gate 3 | Reviewer |
| Gate 4 | Reviewer and Capability Owner |
| Gate 5 | Chief Architect |
| Gate 6 | Chief Architect |
| Gate 7 | Chief Architect and Programme Owner |

## Non-Negotiable Blocks

Implementation planning is blocked when:

- No capability roadmap entry exists.
- No evaluation evidence exists.
- No ADR exists for architecture-shaping decisions.
- No work package exists.
- Technology adoption would invert platform/application dependency rules.
- Security, governance, data, or operational concerns are unresolved for the proposed use case.

## Gate Evidence Checklist

- Capability trace.
- Discovery brief.
- Evaluation criteria.
- Evidence pack.
- Comparison matrix.
- Recommendation.
- ADR impact assessment.
- Radar ring impact.
- Implementation authorization status.

