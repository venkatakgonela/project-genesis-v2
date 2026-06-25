# Prompt: WP-005E Project Conductor Agentic Scope Alignment

## Metadata

| Field | Value |
| --- | --- |
| ID | PROMPT-009 |
| Title | WP-005E Project Conductor Agentic Scope Alignment |
| Created Date | 2026-06-25 |
| Source | User pasted prompt |
| Related Work Packages | WP-005E |
| Status | Archived |

## Prompt

```text
# PROJECT GENESIS V2

## WP-005E – Project Conductor Agentic Scope Alignment

### Context

WP-005 produced four useful foundation technology evaluation work packages:

* WP-005A Deterministic Runtime and Tooling Evaluation
* WP-005B Artifact Metadata and Registry Format Evaluation
* WP-005C Artifact State and Index Strategy Evaluation
* WP-005D Quality Gate and Reporting Strategy Evaluation

These are valid, but they represent only the deterministic substrate of Project Conductor.

They do not fully capture the originally agreed vision of Project Conductor.

Project Conductor is not merely a repository automation tool.

Project Conductor is intended to become the reverse scrum master / engineering coordinator for Project Genesis V2.

It should eventually:

* understand programme state
* understand current work package state
* understand architecture and ADRs
* prepare context packages
* generate prompts for GPT-5.5 / Codex / Claude / Gemini
* coordinate implementation handoff
* support architecture review
* detect drift
* enforce ADR alignment
* summarize progress
* recommend next actions
* support evidence capture
* orchestrate future agents

Therefore, Project Conductor has two layers:

1. Deterministic foundation
2. Agentic coordination layer

WP-005A-D cover mostly layer 1.

This work package must correct the gap and define the missing technology decision path for layer 2.

---

# Objective

Review WP-005A-D and determine what additional technology evaluation work packages are required for the agentic Project Conductor vision.

Do not implement anything.

Do not rewrite WP-005A-D unless they are factually wrong.

Instead, extend the WP-005 technology decision sprint with the missing agentic evaluations.

---

# Source of Truth

Use the existing repository artifacts, especially:

* Architecture Baseline
* Capability Map
* Capability Dependency Graph
* Project Conductor specification
* AI Gateway specification
* Prompt Platform specification
* Context Engineering Platform specification
* Evaluation Platform specification
* Technology Discovery Programme
* WP-005A-D outputs

---

# Required Analysis

## 1. Review WP-005A-D

For each existing work package, classify it as:

* Deterministic substrate
* Agentic layer
* Shared foundation

Explain whether it should remain unchanged, be renamed, or be supplemented.

---

## 2. Define Project Conductor Capability Layers

Create a layered model:

### Layer 0 – Repository Substrate

Examples:

* metadata parsing
* artifact registry
* index generation
* quality reports
* deterministic checks

### Layer 1 – Assisted Conductor

Examples:

* daily summary
* current work package summary
* prompt package generation
* context package generation
* next action recommendation

### Layer 2 – Agentic Conductor

Examples:

* LLM-assisted reasoning
* LangGraph / agent framework orchestration
* multi-step planning
* review routing
* human approval
* checkpointed workflows
* model routing via AI Gateway

### Layer 3 – Multi-Agent Coordination

Examples:

* architecture reviewer agent
* implementation reviewer agent
* technology scout agent
* evidence auditor agent
* publisher agent

---

## 3. Identify Missing Technology Decisions

Identify which technology decisions are missing from WP-005A-D.

Expected areas to consider:

* Agent Framework
* LangGraph
* Microsoft Agent Framework
* OpenAI Agents SDK
* PydanticAI
* CrewAI
* AI Gateway
* Model Routing
* Local and Cloud Model Providers
* Prompt Package Format
* Context Package Format
* LLM Observability
* Evaluation Framework for Agentic Behaviour
* Human Approval / Interrupt Workflow
* Checkpointing and State
* MCP / Tool Runtime
* ToolHive or equivalent tool runtime layer

Do not assume all are required immediately.

Classify each as:

* Required before deterministic Project Conductor MVP
* Required before assisted Project Conductor
* Required before agentic Project Conductor
* Deferred until later platform capabilities

---

## 4. Create Missing Work Packages

Create additional WP-005 sub-work-packages as needed.

Suggested examples:

* WP-005E Agent Framework Evaluation
* WP-005F AI Gateway and Model Routing Evaluation
* WP-005G Prompt and Context Package Strategy Evaluation
* WP-005H LLM Observability and Evaluation Strategy
* WP-005I Human Approval and Checkpoint Strategy
* WP-005J MCP and Tool Runtime Assessment

Use better names if appropriate.

For each work package include:

* Objective
* Scope
* Candidate technologies
* Evaluation criteria
* Expected evidence
* Expected deliverables
* Related ADR
* Dependencies
* Definition of Done

---

## 5. Update the Foundation Technology Decision Sprint

Produce an updated WP-005 decision map showing:

* Existing WP-005A-D
* New missing WP-005E onward
* Execution sequence
* Which Project Conductor layer each work package supports
* Which ADR each work package feeds

---

## 6. Explicitly Address the Contradiction

Answer this question directly:

"Was excluding Agent Framework, AI Gateway, and related agentic technologies from WP-005 correct?"

Use this answer structure:

* Correct for deterministic MVP?
* Correct for full Project Conductor vision?
* Required correction?
* Recommended updated scope?

---

# Constraints

Do not implement code.

Do not select final technologies.

Do not approve ADRs.

Do not remove WP-005A-D unless they are clearly invalid.

Do not collapse deterministic Project Conductor and agentic Project Conductor into one implementation step.

The goal is to clarify scope and sequencing.

---

# Final Deliverables

Produce:

1. WP-005 Agentic Scope Alignment Report
2. Project Conductor Layered Capability Model
3. Missing Technology Decision List
4. Additional WP-005E onward work packages
5. Updated WP-005 Execution Sequence
6. ADR Backlog Update
7. Explicit contradiction resolution

---

# Final Review

Verify that Project Conductor is represented both as:

* a deterministic engineering tool, and
* an eventually agentic coordination capability.

Verify that the updated WP-005 scope matches the original Project Genesis V2 vision.

Verify that implementation remains blocked until the required technology evaluations and ADRs are completed.
```

