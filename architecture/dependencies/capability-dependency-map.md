# Capability Dependency Map

## Metadata

| Field | Value |
| --- | --- |
| ID | ARCH-003 |
| Title | Capability Dependency Map |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | ARCH-002 |
| Related ADRs | ADR-001, ADR-002, ADR-011 |
| Related Work Packages | WP-001 |
| Tags | dependencies, sequencing, architecture |
| Review Date | 2026-07-09 |

## Dependency Rules

- Applications depend on platform capabilities.
- Platform capabilities do not depend on applications.
- Shared governance capabilities should be implemented before runtime capabilities.
- Evaluation dependencies should be defined before implementation begins.

## Initial Dependency Map

| Capability | Depends On | Sequencing Notes |
| --- | --- | --- |
| Career Intelligence | AI Gateway, Knowledge Platform, Browser Platform, Project Conductor, Evaluation Platform, Prompt Platform, Context Platform | Business application should not begin until core platform contracts are approved. |
| AI Gateway | Model Providers, Observability, Evaluation Platform, Project Conductor | Needs provider abstraction and routing ADR before implementation. |
| Knowledge Platform | Project Conductor, Artifact Publisher, Evaluation Platform | Requires knowledge lifecycle and approval workflow. |
| Evaluation Platform | Golden Prompts, Golden Datasets, Golden Workflows, Observability, Project Conductor | Should be established before any agentic implementation. |
| Prompt Platform | Evaluation Platform, Knowledge Platform, Project Conductor | Prompts require versioning, review, and evaluation gates. |
| Context Platform | Knowledge Platform, Memory Platform, Evaluation Platform, Project Conductor | Context quality must be measurable. |
| Memory Platform | Knowledge Platform, Evaluation Platform, Observability | Future durable memory should be governed and auditable. |
| Agent Platform | AI Gateway, Tool Platform, Context Platform, Memory Platform, Evaluation Platform, Observability | Agent orchestration comes after gateway, tools, context, and evaluation basics. |
| Browser Platform | Tool Platform, Evaluation Platform, Observability | Browser automation needs evidence and regression tests. |
| Artifact Publisher | Knowledge Platform, Project Conductor | Publishing should only expose reviewed artifacts. |
| Programme Management | Project Conductor | Programme state feeds work sequencing and review. |

## Suggested Implementation Sequence

1. Project Conductor and Programme Management.
2. Evaluation Platform scaffold and golden asset lifecycle.
3. AI Gateway architecture and model routing ADRs.
4. Knowledge Platform and Artifact Publisher.
5. Prompt Platform and Context Platform.
6. Browser Platform and Tool Platform.
7. Career Intelligence application foundation.

