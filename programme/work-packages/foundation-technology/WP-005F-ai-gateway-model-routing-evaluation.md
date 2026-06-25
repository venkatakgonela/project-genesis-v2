# WP-005F AI Gateway and Model Routing Evaluation

## Metadata

| Field | Value |
| --- | --- |
| ID | WP-005F |
| Title | AI Gateway and Model Routing Evaluation |
| Version | 0.1.0 |
| Status | Planned |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005A, WP-005G, ARCH-SPEC-002 |
| Related ADRs | ADR-003, ADR-010, ADR-DRAFT-018 |
| Related Work Packages | WP-005 |
| Tags | foundation-technology, project-conductor, ai-gateway, model-routing |
| Review Date | 2026-07-23 |

## Objective

Evaluate the minimum AI Gateway, model routing, and provider strategy required for assisted and agentic Project Conductor layers.

## Scope

- Provider abstraction.
- Model routing policy inputs.
- Local and cloud model provider categories.
- Cost, latency, quality, and fallback considerations.
- Evidence capture from model calls.
- Compatibility with prompt and context packages.

## Candidate Technologies

- OpenAI.
- Claude.
- Gemini.
- Ollama.
- LM Studio.
- Azure AI Foundry.
- Lightweight gateway abstraction.
- Future AI Gateway platform capability.

## Evaluation Criteria

- Model agnosticism.
- Provider reversibility.
- Cost visibility.
- Routing policy clarity.
- Evidence capture.
- Observability integration.
- Security and governance fit.
- Integration effort.

## Expected Evidence

- Provider/routing decision matrix.
- Model interaction evidence requirements.
- Gateway responsibility boundary analysis.
- Lock-in and migration risk assessment.
- Draft routing policy inputs.

## Expected Deliverables

- Evaluation report.
- Recommendation.
- Evidence pack.
- ADR-DRAFT-018 update.
- Inputs for ADR-003 and ADR-010.

## Definition of Done

AI Gateway and model routing decisions required for assisted or agentic Project Conductor are evaluated without implementing gateway or model access code.

