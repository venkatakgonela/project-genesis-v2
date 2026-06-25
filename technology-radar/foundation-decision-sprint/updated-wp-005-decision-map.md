# Updated WP-005 Decision Map

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-011 |
| Title | Updated WP-005 Decision Map |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-002, FTD-008, FTD-009, FTD-010 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016, ADR-DRAFT-017, ADR-DRAFT-018, ADR-DRAFT-019, ADR-DRAFT-020, ADR-DRAFT-021, ADR-DRAFT-022 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, decision-map, execution-sequence |
| Review Date | 2026-07-02 |

## Purpose

This map extends the original WP-005 deterministic decision sprint with the missing assisted and agentic Project Conductor decision path.

## Decision Map

| Work Package | Layer | Decision Area | Feeds ADR | Implementation Gate |
| --- | --- | --- | --- | --- |
| WP-005A | Layer 0 | Deterministic runtime and tooling strategy | ADR-DRAFT-013 | Required before deterministic MVP. |
| WP-005B | Layer 0 | Artifact metadata and registry format | ADR-DRAFT-014 | Required before deterministic MVP. |
| WP-005C | Layer 0 and shared foundation | Artifact state and index strategy | ADR-DRAFT-015 | Required before deterministic MVP and later checkpointing. |
| WP-005D | Layer 0 and shared foundation | Quality gate and reporting strategy | ADR-DRAFT-016 | Required before deterministic MVP and later review routing. |
| WP-005G | Layer 1 and Layer 2 | Prompt and context package strategy | ADR-DRAFT-019 | Required before assisted conductor. |
| WP-005F | Layer 2 | AI Gateway, model routing, and provider strategy | ADR-DRAFT-018 | Required before model-assisted conductor behavior. |
| WP-005H | Layer 2 and Layer 3 | LLM observability and agent evaluation strategy | ADR-DRAFT-020 | Required before agentic conductor. |
| WP-005I | Layer 2 | Human approval and checkpoint workflow strategy | ADR-DRAFT-021 | Required before agentic conductor. |
| WP-005E | Layer 2 and Layer 3 | Agent framework and orchestration strategy | ADR-DRAFT-017 | Required before agentic conductor. |
| WP-005J | Layer 2 and Layer 3 | MCP and tool runtime strategy | ADR-DRAFT-022 | Required before agentic tool use. |

## Execution Sequence

```text
Layer 0 Deterministic MVP:
WP-005A -> WP-005B -> WP-005C -> WP-005D

Layer 1 Assisted Conductor:
WP-005G -> WP-005F -> WP-005H

Layer 2 Agentic Conductor:
WP-005I -> WP-005E -> WP-005J

Layer 3 Multi-Agent Coordination:
Deferred until Layer 2 is proven.
```

## Sequencing Notes

- WP-005G should precede model-assisted execution because models need well-formed prompt and context packages.
- WP-005F should precede agent orchestration because agent workflows should use the AI Gateway and model routing policy.
- WP-005H should precede agentic implementation because agent behavior must be observable and evaluable.
- WP-005I should precede full orchestration because agentic workflows require human approval and checkpoint state.
- WP-005E should not run as a selection exercise until WP-005F, WP-005H, and WP-005I clarify gateway, observability, and approval requirements.
- WP-005J should follow WP-005E because tool runtime needs to fit the orchestration strategy.

