# Prompt: WP-002 Master Capability Roadmap and Programme Planning

## Metadata

| Field | Value |
| --- | --- |
| ID | PROMPT-004 |
| Title | WP-002 Master Capability Roadmap and Programme Planning |
| Created Date | 2026-06-25 |
| Source | User prompt |
| Related Work Packages | WP-002 |
| Status | Archived |

## Prompt

```text
# USER PROMPT

## WP-002 – Master Capability Roadmap & Programme Planning

The repository bootstrap (WP-001) has been completed successfully.

The repository now contains the initial architecture, repository structure, ADR placeholders, capability map, platform specifications, programme artifacts, templates, technology radar, and evaluation scaffolding.

The purpose of WP-002 is **NOT** to implement any platform capability.

The purpose is to establish the long-term implementation roadmap that will govern every future work package.

---

# Objective

Create the **Project Genesis V2 Master Capability Roadmap**.

This document becomes the primary planning artifact for the entire programme.

Every future capability, work package, sprint, ADR, and implementation should trace back to this roadmap.

The roadmap should minimize future scope drift.

---

# Important Rules

Do NOT invent large new capabilities.

Do NOT redesign the platform.

Do NOT introduce implementation details.

Use the existing repository as the source of truth.

Consolidate.

Organize.

Sequence.

Prioritize.

---

# Inputs

Use all existing repository artifacts including:

* Project Charter
* Architecture Baseline
* Capability Map
* Capability Dependency Map
* Technology Radar
* ADR placeholders
* Scope Register
* Programme Dashboard
* WP-001
* Platform Specifications
* Bootstrap Report
* Repository Coverage Report
* Architecture Review Report
* Bootstrap Validation Report

Treat these as the authoritative inputs.

---

# Required Deliverables

## 1. Master Capability Roadmap

Organize all platform capabilities into logical implementation phases.

For each capability include:

* Purpose
* Dependencies
* Priority
* Estimated Phase
* Status
* Future Work Packages
* Related ADRs

The roadmap should clearly distinguish:

Platform Capabilities

Business Applications

Future Extensions

---

## 2. Capability Dependency Graph

Review and refine the dependency ordering.

Identify the critical implementation path.

Ensure no circular dependencies exist.

---

## 3. Programme Roadmap

Organize the programme into phases.

Example:

Foundation

Platform Core

Platform Services

Knowledge

Evaluation

Applications

Production Readiness

The actual phases should be derived from the repository rather than copied from this example.

---

## 4. Suggested Work Package Sequence

Produce a recommended ordered list of future work packages.

Each work package should include:

ID

Purpose

Dependencies

Expected Deliverables

Definition of Done

No implementation details.

---

## 5. Scope Validation

Compare the roadmap against the repository.

Identify:

Capabilities already covered

Capabilities deferred

Capabilities missing

Capabilities duplicated

Recommend consolidations where appropriate.

---

## 6. Platform vs Application Validation

Ensure that:

Platform capabilities remain reusable.

Business applications depend on the platform.

The platform never depends on applications.

Highlight any violations.

---

## 7. Engineering Readiness

Recommend the next implementation milestone.

Only recommend work that should logically follow WP-001.

Do not skip architectural maturity.

---

# Constraints

Do NOT implement Python.

Do NOT implement FastAPI.

Do NOT implement LangGraph.

Do NOT implement AI Gateway.

Do NOT implement Project Conductor.

Do NOT write runtime code.

This work package is planning only.

---

# Final Deliverable

Produce:

* Master Capability Roadmap
* Programme Roadmap
* Capability Dependency Graph
* Future Work Package Sequence
* Scope Validation Report
* Programme Readiness Report

---

# Final Self Review

Before completing:

Verify that every platform capability discussed so far is represented somewhere in the roadmap.

Verify that no capability appears multiple times under different names.

Verify that implementation order follows architectural dependencies.

Verify that the roadmap minimizes future scope drift.

If any capability discussed during WP-001 appears to be missing, explicitly identify it instead of silently omitting it.

The objective is to create the definitive planning artifact that will guide Project Genesis V2 for the next 6–12 months.
```

