# ADR-DRAFT-017: Agent Framework and Orchestration Strategy

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-017 |
| Title | Agent Framework and Orchestration Strategy |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005E, ADR-DRAFT-018, ADR-DRAFT-020, ADR-DRAFT-021, ADR-DRAFT-022 |
| Related ADRs | ADR-002, ADR-005, ADR-009 |
| Related Work Packages | WP-005, WP-005E |
| Tags | adr-draft, project-conductor, agent-framework |
| Review Date | 2026-07-23 |

## Context

Agentic Project Conductor will eventually need orchestration for multi-step planning, review routing, human approval, checkpointed workflows, and future multi-agent coordination.

## Decision Question

Which agent framework or orchestration strategy should support the agentic Project Conductor layer?

## Candidate Options

- LangGraph.
- Microsoft Agent Framework.
- OpenAI Agents SDK.
- PydanticAI.
- CrewAI.
- Minimal custom deterministic orchestrator plus model calls.

## Evidence Required

- Capability-to-framework comparison.
- Human approval and checkpoint support.
- Tool runtime compatibility.
- Observability and evaluation integration.
- Migration and lock-in analysis.

## Draft Recommendation

No final framework selection yet.

Complete WP-005E before promoting this ADR.

