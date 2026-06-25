# Missing Agentic Technology Decision List

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-010 |
| Title | Missing Agentic Technology Decision List |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-008, FTD-009 |
| Related ADRs | ADR-DRAFT-017, ADR-DRAFT-018, ADR-DRAFT-019, ADR-DRAFT-020, ADR-DRAFT-021, ADR-DRAFT-022 |
| Related Work Packages | WP-005E, WP-005F, WP-005G, WP-005H, WP-005I, WP-005J |
| Tags | project-conductor, agentic-decisions, technology-decisions |
| Review Date | 2026-07-02 |

## Purpose

This list identifies the missing technology decisions required for the assisted and agentic Project Conductor vision.

## Decision Classification

| Area | Classification | Rationale | Work Package | Expected ADR |
| --- | --- | --- | --- | --- |
| Agent Framework | Required before agentic Project Conductor | Full agentic conductor needs orchestration, planning, routing, interrupts, and workflow state. | WP-005E | ADR-DRAFT-017 |
| LangGraph | Required before agentic Project Conductor as a candidate, not as a selected technology | Candidate orchestration framework to evaluate against alternatives. | WP-005E | ADR-DRAFT-017 |
| Microsoft Agent Framework | Required before agentic Project Conductor as a candidate, not as a selected technology | Candidate enterprise agent framework to evaluate. | WP-005E | ADR-DRAFT-017 |
| OpenAI Agents SDK | Required before agentic Project Conductor as a candidate, not as a selected technology | Candidate provider-aligned agent SDK to evaluate. | WP-005E | ADR-DRAFT-017 |
| PydanticAI | Required before agentic Project Conductor as a candidate, not as a selected technology | Candidate typed/structured agent framework to evaluate. | WP-005E | ADR-DRAFT-017 |
| CrewAI | Deferred until later platform capabilities | Multi-agent coordination candidate; not required for deterministic or assisted conductor. | WP-005E later scope | ADR-DRAFT-017 |
| AI Gateway | Required before agentic Project Conductor | Agentic conductor should use provider abstraction and policy, not direct model calls. | WP-005F | ADR-DRAFT-018 |
| Model Routing | Required before agentic Project Conductor | Agentic workflows need model selection, fallback, and cost/quality policy. | WP-005F | ADR-DRAFT-018 |
| Local and Cloud Model Providers | Required before assisted Project Conductor | Assisted summaries and prompt/context packages need model access decisions. | WP-005F | ADR-DRAFT-018 |
| Prompt Package Format | Required before assisted Project Conductor | Handoff prompts for Codex, Claude, Gemini, and future models need a consistent package format. | WP-005G | ADR-DRAFT-019 |
| Context Package Format | Required before assisted Project Conductor | Project Conductor must package programme state, work package state, ADRs, and evidence. | WP-005G | ADR-DRAFT-019 |
| LLM Observability | Required before agentic Project Conductor | Agentic behavior needs traces, inputs/outputs, costs, and reviewable evidence. | WP-005H | ADR-DRAFT-020 |
| Evaluation Framework for Agentic Behaviour | Required before agentic Project Conductor | Multi-step plans, review routing, and recommendations need evaluation criteria. | WP-005H | ADR-DRAFT-020 |
| Human Approval / Interrupt Workflow | Required before agentic Project Conductor | Agentic conductor must preserve human control over architecture and implementation handoff. | WP-005I | ADR-DRAFT-021 |
| Checkpointing and State | Required before agentic Project Conductor | Multi-step workflows need resumability, auditability, and rollback. | WP-005I | ADR-DRAFT-021 |
| MCP / Tool Runtime | Required before agentic Project Conductor | Tool use needs governed discovery, permissioning, invocation, and evidence. | WP-005J | ADR-DRAFT-022 |
| ToolHive or equivalent tool runtime layer | Required before agentic Project Conductor as a candidate, not as selected technology | Candidate managed tool runtime to evaluate with MCP and alternatives. | WP-005J | ADR-DRAFT-022 |

## Required Before Deterministic Project Conductor MVP

None of the agentic technologies above are required before deterministic Project Conductor MVP.

The deterministic MVP remains covered by WP-005A through WP-005D.

## Required Before Assisted Project Conductor

- Prompt Package Format.
- Context Package Format.
- Local and Cloud Model Provider access strategy.
- Initial LLM observability and evaluation criteria for assisted outputs.

## Required Before Agentic Project Conductor

- Agent Framework.
- AI Gateway.
- Model Routing.
- LLM Observability.
- Agentic Evaluation Framework.
- Human Approval / Interrupt Workflow.
- Checkpointing and State.
- MCP / Tool Runtime.

## Deferred Until Later Platform Capabilities

- Full multi-agent crew coordination.
- Specialized reviewer/scout/auditor/publisher agents.
- Production deployment platform.
- Browser automation unless a conductor workflow explicitly requires it.

