# Capability Dependency Graph

## Metadata

| Field | Value |
| --- | --- |
| ID | ARCH-004 |
| Title | Capability Dependency Graph |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | ARCH-002, ARCH-003, PRG-006 |
| Related ADRs | ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-010, ADR-011, ADR-012 |
| Related Work Packages | WP-002 |
| Tags | dependencies, graph, critical-path |
| Review Date | 2026-07-02 |

## Purpose

This artifact refines the WP-001 capability dependency map into an explicit dependency graph for planning and sequencing.

## Graph Rules

- Edges point from a capability to the capability it depends on.
- Business applications may depend on platform capabilities.
- Platform capabilities must not depend on business applications.
- Golden prompts, datasets, and workflows are evaluation assets, not independent platform pillars.
- Context Engineering Platform is the canonical name for the WP-001 Context Platform capability family.

## Dependency Graph

```text
Career Intelligence
  -> AI Gateway
  -> Knowledge Platform
  -> Browser Platform
  -> Project Conductor
  -> Evaluation Platform
  -> Prompt Platform
  -> Context Engineering Platform

Agent Platform
  -> AI Gateway
  -> Tool Platform
  -> Context Engineering Platform
  -> Memory Platform
  -> Evaluation Platform
  -> Observability

Browser Platform
  -> Tool Platform
  -> Evaluation Platform
  -> Observability

Tool Platform
  -> Evaluation Platform
  -> Observability
  -> Project Conductor

AI Gateway
  -> Model Providers
  -> Observability
  -> Evaluation Platform
  -> Project Conductor

Model Providers
  -> Evaluation Platform
  -> Technology Radar
  -> Observability

Context Engineering Platform
  -> Knowledge Platform
  -> Memory Platform
  -> Evaluation Platform
  -> Project Conductor

Memory Platform
  -> Knowledge Platform
  -> Evaluation Platform
  -> Observability

Prompt Platform
  -> Evaluation Platform
  -> Knowledge Platform
  -> Project Conductor

Knowledge Platform
  -> Project Conductor
  -> Evaluation Platform

Artifact Publisher
  -> Knowledge Platform
  -> Project Conductor

Evaluation Platform
  -> Project Conductor
  -> Technology Radar

Golden Asset Lifecycle
  -> Evaluation Platform
  -> Project Conductor

Observability
  -> Project Conductor
  -> Evidence Storage Standard

Programme Management
  -> Project Conductor

Technology Radar
  -> Project Conductor
```

## Dependency Refinements

| Refinement | Reason |
| --- | --- |
| Context Platform renamed to Context Engineering Platform for roadmap planning. | Aligns with the platform specification and architecture review recommendation. |
| Golden prompts, datasets, and workflows grouped as Golden Asset Lifecycle. | Avoids treating evaluation asset folders as separate platform capabilities. |
| Observability placed before AI Gateway, Tool Platform, Browser Platform, and Agent Platform. | Runtime capabilities need evidence, traces, and model interaction visibility. |
| Artifact Publisher kept after Knowledge Platform for implementation but before published evidence workflows. | Publishing depends on approved knowledge and artifact governance. |
| Security, data, and deployment treated as future extensions. | They were deferred in WP-001 and should not be silently promoted into platform core. |

## Critical Path

```text
Project Conductor
  -> Programme Management
  -> Repository Quality Gates
  -> Evidence Storage Standard
  -> Evaluation Platform
  -> Golden Asset Lifecycle
  -> Observability
  -> Knowledge Platform
  -> Prompt Platform
  -> Context Engineering Platform
  -> Model Providers
  -> AI Gateway
  -> Tool Platform
  -> Browser Platform
  -> Agent Platform
  -> Career Intelligence
```

## Circular Dependency Review

No circular dependencies are approved for implementation.

Potential conceptual tensions from WP-001 have been resolved for planning:

- Knowledge Platform is planned before Artifact Publisher. Artifact Publisher may publish knowledge outputs later, but Knowledge Platform does not require Artifact Publisher to begin architecture work.
- Evaluation Platform is planned before Golden Asset Lifecycle. Golden prompts, datasets, and workflows are promoted after evaluation governance exists.
- Context Engineering Platform is planned before durable Memory Platform implementation. Memory can later provide inputs to context packages, but initial context architecture must not require implemented memory.

## Sequencing Verdict

The refined graph is suitable for programme planning. Implementation work should begin only after the Phase 1 governance controls and Phase 2 evaluation and observability foundations are approved.
