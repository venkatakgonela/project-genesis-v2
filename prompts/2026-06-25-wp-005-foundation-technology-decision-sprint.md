# Prompt: WP-005 Foundation Technology Decision Sprint

## Metadata

| Field | Value |
| --- | --- |
| ID | PROMPT-008 |
| Title | WP-005 Foundation Technology Decision Sprint |
| Created Date | 2026-06-25 |
| Source | User goal prompt |
| Related Work Packages | WP-005 |
| Status | Archived |

## Prompt

```text
# PROJECT GENESIS V2

## WP-005 – Foundation Technology Decision Sprint

### Context

WP-001 through WP-004 have been completed.

The repository now contains:

- Engineering Operating System
- Programme Structure
- Architecture Baseline
- Capability Map
- Capability Dependency Model
- Technology Discovery Programme
- Governance
- Templates
- ADR scaffolding
- Repository baseline

The programme has intentionally remained in the Planning phase.

No runtime implementation has started.

The next objective is NOT to evaluate every technology.

The objective is to identify and evaluate ONLY the technology decisions that block implementation of the first platform capability.

---

# Objective

Determine the minimum technology decisions required before Project Genesis can begin implementing its first platform capability.

The first platform capability is:

Project Conductor

The outcome of this work package should be a small number of evidence-based technology recommendations together with draft ADRs.

Do not attempt to evaluate technologies unrelated to Project Conductor.

---

# Source of Truth

Use the existing repository.

Treat the following as authoritative:

- Architecture Baseline
- Master Capability Roadmap
- Capability Map
- Capability Dependency Graph
- Technology Discovery Programme
- Authoritative Artifact Register
- Readiness Assessment
- Phase Transition Recommendation

Do not recreate these artifacts.

Extend them only where necessary.

---

# Step 1

Analyse Project Conductor.

Identify:

Responsibilities

Inputs

Outputs

Interfaces

Dependencies

Future integrations

Required platform services

Required runtime capabilities

---

# Step 2

Determine which technology decisions actually block implementation.

For every dependency answer:

Can implementation begin without this decision?

Yes / No

Explain why.

---

# Step 3

Create a Foundation Technology Decision List.

Only include technologies that are genuinely required before Project Conductor implementation.

For each decision provide:

Question

Why it matters

Dependencies

Priority

Suggested future work package

Expected ADR

---

# Step 4

Create Technology Evaluation Work Packages.

One work package per technology decision.

Example:

WP-005A

Agent Framework Evaluation

WP-005B

AI Gateway Evaluation

WP-005C

Context & Prompt Management

WP-005D

State & Checkpoint Strategy

Do not invent work packages unnecessarily.

Only create those justified by Project Conductor.

---

# Step 5

For each work package define:

Objective

Scope

Candidate technologies

Evaluation criteria

Expected evidence

Expected deliverables

Definition of Done

No implementation.

---

# Step 6

Recommend execution order.

The order must follow architectural dependencies.

Explain why.

---

# Constraints

Do not implement code.

Do not generate Python.

Do not generate FastAPI.

Do not implement LangGraph.

Do not select final technologies without evidence.

Do not evaluate technologies unrelated to Project Conductor.

Do not modify the platform architecture.

---

# Deliverables

Produce:

1. Project Conductor dependency analysis

2. Foundation Technology Decision List

3. Technology Evaluation Work Packages

4. Recommended execution sequence

5. Draft ADR backlog

6. Programme impact assessment

---

# Final Review

Verify that every proposed technology decision directly supports implementation of Project Conductor.

Verify that no unnecessary technology evaluations have been introduced.

Verify that every future evaluation has a clear architectural purpose.

The goal is to minimise research while maximising implementation readiness.

The deliverable should become the official Foundation Technology Decision Sprint for Project Genesis V2.
```

