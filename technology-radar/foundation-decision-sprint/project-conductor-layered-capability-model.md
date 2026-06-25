# Project Conductor Layered Capability Model

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-009 |
| Title | Project Conductor Layered Capability Model |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-008, ARCH-SPEC-001 |
| Related ADRs | ADR-002, ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016, ADR-DRAFT-017, ADR-DRAFT-018, ADR-DRAFT-019, ADR-DRAFT-020, ADR-DRAFT-021, ADR-DRAFT-022 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, layered-model, agentic-scope |
| Review Date | 2026-07-02 |

## Purpose

This model separates deterministic Project Conductor implementation from assisted, agentic, and multi-agent horizons.

## Layer 0: Repository Substrate

Purpose:

Provide deterministic repository understanding and governance checks.

Capabilities:

- Metadata parsing.
- Artifact registry.
- Work package registry.
- Artifact index generation.
- Review queue.
- Evidence index.
- Quality reports.
- Deterministic checks.
- Dashboard-ready outputs.

Technology decisions:

- WP-005A Deterministic Runtime and Tooling.
- WP-005B Artifact Metadata and Registry Format.
- WP-005C Artifact State and Index Strategy.
- WP-005D Quality Gate and Reporting Strategy.

Implementation gate:

Required before deterministic Project Conductor MVP.

## Layer 1: Assisted Conductor

Purpose:

Help the human Chief Architect and implementation engineer understand programme state and prepare work handoffs.

Capabilities:

- Daily summary.
- Current work package summary.
- Architecture and ADR summary.
- Prompt package generation.
- Context package generation.
- Next action recommendation.
- Implementation handoff package.
- Evidence capture prompts.

Technology decisions:

- WP-005G Prompt and Context Package Strategy.
- WP-005H LLM Observability and Agent Evaluation Strategy for assisted behavior.

Implementation gate:

Requires Layer 0 indexes and quality outputs. Does not require full agent orchestration.

## Layer 2: Agentic Conductor

Purpose:

Coordinate multi-step LLM-assisted planning, review, and handoff workflows with human approval.

Capabilities:

- LLM-assisted reasoning.
- Agent framework orchestration.
- Multi-step planning.
- Review routing.
- Human approval.
- Interrupt workflow.
- Checkpointed workflows.
- Model routing via AI Gateway.
- Tool access through governed runtime.

Technology decisions:

- WP-005E Agent Framework and Orchestration Evaluation.
- WP-005F AI Gateway, Model Routing, and Model Provider Evaluation.
- WP-005H LLM Observability and Agent Evaluation Strategy.
- WP-005I Human Approval and Checkpoint Workflow Evaluation.
- WP-005J MCP and Tool Runtime Assessment.

Implementation gate:

Requires Layer 0 and selected Layer 1 contracts. Requires ADR approval before implementation.

## Layer 3: Multi-Agent Coordination

Purpose:

Coordinate specialized future agents across architecture, implementation review, technology scouting, evidence auditing, and publishing.

Capabilities:

- Architecture reviewer agent.
- Implementation reviewer agent.
- Technology scout agent.
- Evidence auditor agent.
- Publisher agent.
- Multi-agent task routing.
- Cross-agent evidence capture.
- Human escalation.

Technology decisions:

- WP-005E Agent Framework and Orchestration Evaluation.
- WP-005H LLM Observability and Agent Evaluation Strategy.
- WP-005J MCP and Tool Runtime Assessment.

Implementation gate:

Deferred until Layer 2 is proven with evidence and reviewed ADRs.

## Layering Rule

Each layer may depend on lower layers. Lower layers must not depend on higher layers.

Deterministic Project Conductor must remain useful even if agentic layers are delayed or rejected.

