# Updated WP-005 Execution Sequence

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-015 |
| Title | Updated WP-005 Execution Sequence |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-011 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016, ADR-DRAFT-017, ADR-DRAFT-018, ADR-DRAFT-019, ADR-DRAFT-020, ADR-DRAFT-021, ADR-DRAFT-022 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, execution-sequence, agentic-scope |
| Review Date | 2026-07-02 |

## Purpose

This sequence extends the original deterministic WP-005 execution order with assisted and agentic Project Conductor evaluations.

## Sequence

| Order | Work Package | Layer | Dependency Rationale |
| --- | --- | --- | --- |
| 1 | WP-005A Deterministic Runtime and Tooling Evaluation | Layer 0 | Runtime/tooling constrains all later repository automation and evaluation work. |
| 2 | WP-005B Artifact Metadata and Registry Format Evaluation | Layer 0 | Metadata parsing is needed before artifact registry and prompt/context generation. |
| 3 | WP-005C Artifact State and Index Strategy Evaluation | Layer 0 and shared foundation | State/index strategy is needed before checkpoints, context packages, and review routing. |
| 4 | WP-005D Quality Gate and Reporting Strategy Evaluation | Layer 0 and shared foundation | Quality outputs become inputs to assisted summaries and agentic review routing. |
| 5 | WP-005G Prompt and Context Package Strategy Evaluation | Layer 1 and Layer 2 | Assisted and agentic behavior needs a package format before model use. |
| 6 | WP-005F AI Gateway and Model Routing Evaluation | Layer 2 | Model access should be governed after prompt/context needs are known. |
| 7 | WP-005H LLM Observability and Agent Evaluation Strategy | Layer 2 and Layer 3 | Agentic behavior must be traceable and evaluable before orchestration is implemented. |
| 8 | WP-005I Human Approval and Checkpoint Workflow Evaluation | Layer 2 | Human control and resumability must precede agentic workflows. |
| 9 | WP-005E Agent Framework and Orchestration Evaluation | Layer 2 and Layer 3 | Framework choice depends on gateway, observability, package, and approval requirements. |
| 10 | WP-005J MCP and Tool Runtime Assessment | Layer 2 and Layer 3 | Tool runtime must align with the orchestration strategy and governance model. |

## Implementation Gate

Deterministic MVP implementation planning requires WP-005A-D and ADR-DRAFT-013 through ADR-DRAFT-016 to be reviewed.

Assisted conductor implementation planning additionally requires WP-005G, WP-005F, and WP-005H.

Agentic conductor implementation planning additionally requires WP-005I, WP-005E, and WP-005J.

Layer 3 multi-agent coordination remains deferred until Layer 2 is proven.

