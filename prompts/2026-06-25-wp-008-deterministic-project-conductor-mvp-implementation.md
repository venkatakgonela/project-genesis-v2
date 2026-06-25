# WP-008 Prompt: Deterministic Project Conductor MVP Implementation

## Metadata

| Field | Value |
| --- | --- |
| ID | PROMPT-010 |
| Title | WP-008 Deterministic Project Conductor MVP Implementation Prompt |
| Created Date | 2026-06-25 |
| Related Work Packages | WP-008 |

## Prompt

# PROJECT GENESIS V2

## WP-008 – Deterministic Project Conductor MVP Implementation

### Context

WP-001 through WP-007 have been completed and accepted.

The repository now contains:

* Engineering Operating System
* Architecture Baseline
* Capability Hierarchy
* Capability Dependency Graph
* Technology Discovery Programme
* Product Definition
* Operating Model
* Deterministic Foundation Decisions
* Draft ADR Recommendations

Planning is complete.

Implementation now begins.

---

# Critical Implementation Principle

This work package must NOT implement the entire Project Conductor.

Instead, implementation proceeds through **small vertical slices**.

Each slice must be independently:

* designed
* implemented
* tested
* reviewed
* evidenced
* accepted

before the next slice begins.

Do not continue automatically to the next slice.

Stop after completing the assigned slice.

---

# Implementation Scope

Implement **Sprint 1 only**.

Sprint 1:

Repository Scanner

Purpose:

Create the deterministic repository scanner that discovers repository artifacts and builds an in-memory representation.

The scanner should become the foundation for every future Project Conductor capability.

Do not implement future capabilities.

---

# Source of Truth

Use only the repository artifacts already created.

Treat the following as authoritative:

* Architecture Baseline
* Project Conductor Product Definition
* Operating Model
* WP-007 Foundation Decisions
* Relevant ADR drafts

Do not redesign the architecture.

Do not change product scope.

---

# Required Deliverables

## 1. Sprint Design

Produce:

* Sprint objective
* Functional requirements
* Non-functional requirements
* Assumptions
* Risks
* Acceptance criteria

---

## 2. Technical Design

Produce:

* Component diagram
* Module responsibilities
* Public interfaces
* Repository layout
* Data flow
* Error handling approach

---

## 3. Implementation

Implement ONLY Sprint 1.

Do not implement Sprint 2.

Do not anticipate future work.

Keep implementation modular and extensible.

---

## 4. Testing

Create:

* Unit tests
* Integration tests (where appropriate)
* Test data
* Expected outputs

All tests should run locally.

---

## 5. Documentation

Generate:

* Sprint README
* Architecture notes
* Design rationale
* Developer notes

---

## 6. Evidence

Generate:

* Test results
* Coverage summary
* Example execution
* Screenshots or console output (where appropriate)
* Known limitations

---

## 7. Review Package

Create a dedicated review folder.

Include:

### Architecture Review Package

* Sprint summary
* Design decisions
* Trade-offs
* Outstanding questions

### Code Review Package

* File tree
* Major modules
* Public interfaces
* Testing summary

### Evidence Package

* Test results
* Logs
* Coverage
* Validation

### Next Sprint Recommendation

Recommend:

Continue

Refactor

Revisit architecture

Block

with justification.

---

## 8. Self Review

Review implementation against:

* Product Definition
* Operating Model
* Architecture Baseline
* WP-007 Foundation Decisions

Identify any architectural drift.

Do not silently modify the architecture.

---

# Constraints

Implement exactly one sprint.

Do not continue automatically.

Do not implement agentic capabilities.

Do not implement AI Gateway.

Do not implement LangGraph.

Do not implement MCP.

Do not implement Prompt Platform.

Do not implement Context Platform.

Do not implement Browser Automation.

Do not implement Knowledge Platform.

Stay strictly within Sprint 1.

---

# Final Output

At completion produce:

1. Sprint Report

2. Review Package

3. Evidence Package

4. Suggested Git Commit Message

5. Suggested Pull Request Description

6. Architecture Review Checklist

7. Questions requiring Chief Architect review

Stop.

Wait for review before continuing to Sprint 2.

The objective is to establish an implementation cadence where every sprint is independently reviewable and every architectural decision is deliberate.

