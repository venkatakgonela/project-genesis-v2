# Prompt: WP-003 Technology Discovery Programme

## Metadata

| Field | Value |
| --- | --- |
| ID | PROMPT-006 |
| Title | WP-003 Technology Discovery Programme |
| Created Date | 2026-06-25 |
| Source | User goal prompt |
| Related Work Packages | WP-003 |
| Status | Archived |

## Prompt

```text
# PROJECT GENESIS V2

## WP-003 – Technology Discovery Programme

### Context

WP-001 (Genesis Foundation Pack) and WP-002 (Architecture Baseline, Capability Mapping, Dependency Planning, and Programme Structure) have been completed and accepted.

The platform architecture, governance model, capability hierarchy, dependency graph, and implementation sequencing now exist.

The next step is **not implementation**.

The next step is to establish a **Technology Discovery Programme** that will govern all future technology evaluations before implementation begins.

### Objective

Design the Technology Discovery Programme for Project Genesis V2.

This work package must **not evaluate every technology** and must **not recommend final technology selections**.

Instead, create the programme that will perform those evaluations through future work packages.

### Scope

Create:

1. Technology Discovery Programme
2. Technology Discovery Process
3. Technology Evaluation Framework
4. ADR Lifecycle for technology decisions
5. Technology Decision Gates
6. Technology Watch process for continuously tracking new tools and frameworks
7. Technology Discovery Backlog
8. Sequenced work packages (WP-003A, WP-003B, WP-003C...) for each major capability area

### Candidate Capability Areas

Derive these from the repository, but expect areas such as:

* Agent Frameworks
* AI Gateway
* Knowledge Platform
* Context Engineering
* Prompt Platform
* Evaluation Platform
* Browser Platform
* Tool Platform
* Memory Platform
* Observability
* Model Providers
* Deployment Platform
* Local AI Runtime
* Storage & Retrieval
* Security & Governance

### Evaluation Framework

Define a reusable evaluation framework including criteria such as:

* Capability Fit
* Enterprise Adoption
* Community Maturity
* Long-term Sustainability
* Extensibility
* Operational Complexity
* Learning Value
* Vendor Lock-in
* Cost
* Migration Risk
* Integration Effort
* Interview & Portfolio Value
* Recommendation
* Supporting Evidence

Do not score technologies yet.

### ADR Strategy

Design how technology evaluations progress into ADRs.

Technology Discovery
-> Evaluation
-> Comparison Matrix
-> Recommendation
-> ADR
-> Architecture Approval
-> Implementation

### Technology Watch

Design a recurring process for identifying new technologies throughout the lifetime of Project Genesis V2.

Include sources, review cadence, promotion criteria, and retirement criteria.

### Constraints

* Do not implement any code.
* Do not compare technologies in depth.
* Do not select winners.
* Do not modify existing architecture.
* Build the programme that will execute technology discovery over the coming months.

### Final Review

Verify that:

* Every platform capability has a corresponding future technology evaluation.
* No implementation begins before technology decisions are approved.
* The programme complements WP-001 and WP-002 without duplicating them.
* Future work packages are sequenced according to the existing capability dependency graph.

The final deliverable should become the authoritative Technology Discovery Programme for Project Genesis V2.
```

