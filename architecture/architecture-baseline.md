# Architecture Baseline

## Metadata

| Field | Value |
| --- | --- |
| ID | ARCH-001 |
| Title | Architecture Baseline |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | PRG-001 |
| Related ADRs | ADR-001 |
| Related Work Packages | WP-001 |
| Tags | architecture, baseline |
| Review Date | 2026-07-09 |

## Architectural Intent

Project Genesis V2 is organized as a platform of reusable AI engineering capabilities. Business applications consume those platform capabilities through stable interfaces.

## Core Boundaries

| Boundary | Responsibility |
| --- | --- |
| Programme | Work sequencing, governance, scope, risks, assumptions, reviews. |
| Architecture | Capability model, dependency model, specifications, ADR alignment. |
| Evaluation | Golden assets, metrics, evaluation reports, regression expectations. |
| Platform | Reusable capabilities such as AI Gateway, Knowledge Platform, Prompt Platform, and Context Engineering. |
| Applications | Business-specific products such as Career Intelligence. |
| Knowledge | Raw, synthesized, and approved knowledge artifacts. |
| Evidence | Proof that a capability or work package met its acceptance criteria. |

## Architecture Rules

- Platform capabilities must not depend on business applications.
- Business applications may depend on platform capabilities.
- Every implementation must trace to an architecture artifact.
- Every architecture decision must trace to an ADR.
- Every capability must define evaluation and evidence expectations.
- Runtime technology choices remain reversible until supported by evaluation.

## Deferred Architecture Work

- Runtime deployment architecture.
- Data architecture.
- Security architecture.
- Observability architecture.
- Evidence storage architecture.
- Repository quality gate architecture.

