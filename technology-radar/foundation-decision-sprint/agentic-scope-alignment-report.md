# WP-005E Agentic Scope Alignment Report

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-008 |
| Title | WP-005E Agentic Scope Alignment Report |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005, ARCH-SPEC-001, ARCH-SPEC-002, ARCH-SPEC-004, ARCH-SPEC-005, ARCH-SPEC-006 |
| Related ADRs | ADR-002, ADR-003, ADR-005, ADR-006, ADR-007, ADR-009, ADR-010, ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-005, WP-005A, WP-005B, WP-005C, WP-005D |
| Tags | project-conductor, agentic-scope, alignment |
| Review Date | 2026-07-02 |

## Purpose

WP-005A through WP-005D correctly define the deterministic foundation for Project Conductor. They do not fully cover the longer-term Project Conductor vision as a reverse scrum master and engineering coordinator.

This report corrects that scope gap by adding a separate agentic decision path without collapsing deterministic Project Conductor and agentic Project Conductor into a single implementation step.

## WP-005A-D Review

| Work Package | Classification | Assessment | Action |
| --- | --- | --- | --- |
| WP-005A Deterministic Runtime and Tooling Evaluation | Deterministic substrate | Valid foundation for repository scanning, validation, indexing, and report generation. | Remain unchanged. |
| WP-005B Artifact Metadata and Registry Format Evaluation | Deterministic substrate | Valid foundation for machine-readable artifact metadata and registry validation. | Remain unchanged. |
| WP-005C Artifact State and Index Strategy Evaluation | Shared foundation | Required by deterministic reporting and later agentic state/context handoff. | Remain unchanged; supplement with checkpoint and workflow decisions later. |
| WP-005D Quality Gate and Reporting Strategy Evaluation | Shared foundation | Required by deterministic checks and later agentic review routing. | Remain unchanged; supplement with observability, evaluation, and human approval decisions later. |

## Gap Statement

WP-005A-D establish how Project Conductor can read the repository, build indexes, detect quality gaps, and report state.

They do not yet define how Project Conductor will:

- Prepare context packages for AI assistants.
- Generate prompt packages for GPT-5.5, Codex, Claude, Gemini, or future models.
- Coordinate implementation handoff.
- Support architecture review and ADR alignment with LLM assistance.
- Route review tasks to humans or future agents.
- Use model routing through AI Gateway.
- Maintain checkpointed multi-step workflows.
- Observe and evaluate agentic behavior.
- Invoke tools through MCP or a tool runtime.

## Scope Correction

Project Conductor should be planned as two implementation horizons:

1. Deterministic Project Conductor MVP.
2. Assisted and agentic Project Conductor extensions.

The deterministic MVP should not wait for every agentic technology decision.

The full Project Conductor vision does require additional technology evaluation before agentic implementation begins.

## Added Work Packages

| Work Package | Layer Supported | Purpose |
| --- | --- | --- |
| WP-005E | Layer 2 and Layer 3 | Agent Framework and Orchestration Evaluation. |
| WP-005F | Layer 2 | AI Gateway, Model Routing, and Model Provider Evaluation. |
| WP-005G | Layer 1 and Layer 2 | Prompt and Context Package Strategy Evaluation. |
| WP-005H | Layer 2 and Layer 3 | LLM Observability and Agent Evaluation Strategy. |
| WP-005I | Layer 2 | Human Approval and Checkpoint Workflow Evaluation. |
| WP-005J | Layer 2 and Layer 3 | MCP and Tool Runtime Assessment. |

## Recommendation

Keep WP-005A-D as the required path for deterministic Project Conductor MVP.

Add WP-005E-J as required before assisted or agentic Project Conductor implementation.

Do not start WP-005E-J before the deterministic substrate decisions are complete enough to provide artifact state, context sources, quality gates, and review outputs.

