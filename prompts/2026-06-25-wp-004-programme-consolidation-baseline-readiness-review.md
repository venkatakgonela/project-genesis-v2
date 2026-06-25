# Prompt: WP-004 Programme Consolidation and Baseline Readiness Review

## Metadata

| Field | Value |
| --- | --- |
| ID | PROMPT-007 |
| Title | WP-004 Programme Consolidation and Baseline Readiness Review |
| Created Date | 2026-06-25 |
| Source | User goal prompt |
| Related Work Packages | WP-004 |
| Status | Archived |

## Prompt

```text
# PROJECT GENESIS V2

## WP-004 – Programme Consolidation & Baseline Readiness Review

### Context

WP-001 (Genesis Foundation Pack), WP-002 (Architecture & Capability Planning), and WP-003 (Technology Discovery Programme) have been completed.

Over multiple iterations, the repository has grown through architectural refinement, new capabilities, dependency modelling, governance improvements, and planning discussions.

Before implementation begins, the programme requires a formal consolidation.

The purpose of WP-004 is to establish a stable engineering baseline.

---

## Objective

Review the entire repository and consolidate the programme into a coherent, internally consistent baseline.

Do not redesign the architecture.

Do not implement platform capabilities.

Do not generate runtime code.

Instead:

* remove duplication
* identify inconsistencies
* identify superseded artifacts
* recommend authoritative artifacts
* establish a stable baseline for implementation

---

## Review Scope

Review all repository artifacts including:

* Programme
* Architecture
* ADRs
* Capability Maps
* Dependency Maps
* Dependency Graphs
* Technology Discovery Programme
* Technology Radar
* Templates
* Registers
* Evaluation
* Knowledge
* Platform Specifications

---

## Produce

### 1. Consolidation Report

Identify:

* duplicate artifacts
* overlapping documents
* conflicting terminology
* superseded documents
* inconsistent naming
* unnecessary complexity

---

### 2. Authoritative Artifact Register

Identify which document becomes the authoritative source for each engineering concern.

Examples:

Architecture Baseline

Capability Map

Dependency Graph

Technology Discovery Programme

Scope Register

Roadmap

---

### 3. Repository Cleanup Recommendations

Recommend:

* merge
* archive
* rename
* keep
* deprecate

Do not perform the cleanup.

---

### 4. Readiness Assessment

Determine whether the repository is ready to begin platform implementation.

Identify any remaining planning work that must be completed first.

---

### 5. Phase Transition

Recommend whether the programme is ready to transition from

Planning

to

Implementation.

Provide evidence supporting the recommendation.

---

## Constraints

Do not implement any runtime code.

Do not modify architecture.

Do not redesign capabilities.

Do not create new platform capabilities unless a genuine architectural gap is discovered.

---

## Final Review

Verify that the repository now has:

* one authoritative architecture baseline
* one authoritative capability hierarchy
* one authoritative dependency model
* one authoritative technology discovery programme

The goal is to create a clean, stable engineering baseline that will support all future implementation work.
```

