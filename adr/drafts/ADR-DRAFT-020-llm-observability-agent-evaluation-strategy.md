# ADR-DRAFT-020: LLM Observability and Agent Evaluation Strategy

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-020 |
| Title | LLM Observability and Agent Evaluation Strategy |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005H, ARCH-SPEC-004 |
| Related ADRs | ADR-005 |
| Related Work Packages | WP-005, WP-005H |
| Tags | adr-draft, project-conductor, observability, evaluation |
| Review Date | 2026-07-23 |

## Context

Assisted and agentic Project Conductor will require reviewable traces, model interaction evidence, evaluation criteria, and drift detection.

## Decision Question

What LLM observability and agent evaluation strategy should govern assisted and agentic Project Conductor behavior?

## Candidate Options

- Langfuse.
- OpenTelemetry.
- Evaluation report artifacts.
- DeepEval.
- Promptfoo.
- Ragas for retrieval/context-related scenarios.
- Custom trace schema.

## Evidence Required

- Trace data requirements.
- Agent evaluation criteria.
- Cost and privacy implications.
- Integration with AI Gateway.
- Evidence retention and reviewability analysis.

## Draft Recommendation

No final observability or evaluation tool selection yet.

Complete WP-005H before promoting this ADR.

