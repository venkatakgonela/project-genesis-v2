# ADR-DRAFT-018: AI Gateway and Model Routing for Project Conductor

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-018 |
| Title | AI Gateway and Model Routing for Project Conductor |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005F, ARCH-SPEC-002 |
| Related ADRs | ADR-003, ADR-010 |
| Related Work Packages | WP-005, WP-005F |
| Tags | adr-draft, project-conductor, ai-gateway, model-routing |
| Review Date | 2026-07-23 |

## Context

Assisted and agentic Project Conductor should use model access through governed provider abstraction and routing rather than direct provider calls.

## Decision Question

What AI Gateway, model routing, and provider access strategy is required for assisted and agentic Project Conductor?

## Candidate Options

- OpenAI.
- Claude.
- Gemini.
- Ollama.
- LM Studio.
- Azure AI Foundry.
- Lightweight gateway abstraction.
- Future AI Gateway platform capability.

## Evidence Required

- Provider and routing comparison.
- Cost, quality, latency, and fallback analysis.
- Evidence capture requirements.
- Gateway boundary analysis.
- Lock-in and migration assessment.

## Draft Recommendation

No final gateway, routing, provider, or model selection yet.

Complete WP-005F before promoting this ADR.

