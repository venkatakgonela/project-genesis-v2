# Project Genesis V2 Master Capability Roadmap

## Metadata

| Field | Value |
| --- | --- |
| ID | PRG-006 |
| Title | Project Genesis V2 Master Capability Roadmap |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | PRG-001, ARCH-001, ARCH-002, ARCH-003, WP-001 |
| Related ADRs | ADR-001, ADR-002, ADR-003, ADR-004, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-010, ADR-011, ADR-012 |
| Related Work Packages | WP-001, WP-002 |
| Tags | roadmap, capabilities, programme-planning |
| Review Date | 2026-07-02 |

## Purpose

This roadmap is the primary planning artifact for Project Genesis V2. Every future capability, work package, sprint, ADR, and implementation should trace back to this roadmap.

The roadmap consolidates the WP-001 architecture baseline, capability map, dependency map, platform specifications, ADR placeholders, technology radar, bootstrap reports, and web-review reports into a sequenced 6-12 month planning view.

## Planning Rules

- Platform capabilities remain reusable.
- Business applications depend on platform capabilities.
- Platform capabilities do not depend on business applications.
- No implementation begins without architecture, ADR path, evaluation plan, and evidence plan.
- Technology adoption follows the Technology Evaluation Framework.
- Capability names in this roadmap are canonical for planning unless superseded by a reviewed ADR.

## Canonical Capability Names

| Canonical Name | Notes |
| --- | --- |
| Context Engineering Platform | Consolidates the WP-001 shorthand "Context Platform" and the platform specification name "Context Engineering Platform". |
| Golden Asset Lifecycle | Represents the existing golden prompts, golden datasets, and golden workflows evaluation assets. It is an evaluation sub-capability, not a separate platform pillar. |
| Tool Platform | Retained from ADR-009 and dependency map as a future platform capability. |

## Capability Phase Model

| Phase | Name | Goal | Exit Criteria |
| --- | --- | --- | --- |
| Phase 0 | Bootstrap Complete | Establish repository operating system scaffold. | WP-001 accepted and repository baseline committed. |
| Phase 1 | Governance and Architecture Control | Stabilize planning, ADR, evidence, and repository quality controls. | ADR-001, ADR-002, and ADR-012 reviewed; artifact index and evidence policy defined. |
| Phase 2 | Evaluation and Observability Foundation | Make evaluation and evidence collection implementation-ready before runtime capabilities. | Evaluation architecture, golden asset lifecycle, observability architecture, and evidence conventions approved. |
| Phase 3 | Knowledge, Prompt, and Context Foundations | Prepare reusable knowledge, prompt, and context capability contracts. | Knowledge, Prompt, Context Engineering, and Memory ADRs reviewed with evaluation plans. |
| Phase 4 | Model, Tool, and Runtime Boundary Design | Prepare provider, tool, browser, and gateway boundaries without application coupling. | AI Gateway, Model Routing, Tool Platform, Browser Platform, and Model Providers decisions reviewed. |
| Phase 5 | Agent and Application Readiness | Prepare Agent Platform and Career Intelligence application architecture. | Agent Platform and Business Applications ADRs reviewed; Career Intelligence work package ready. |
| Phase 6 | Production Readiness and Publishing | Prepare deployment, security, operations, and publication pathways. | Deployment, security, observability, and artifact publishing standards approved. |

## Platform Capabilities

| Capability | Purpose | Dependencies | Priority | Estimated Phase | Status | Future Work Packages | Related ADRs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project Conductor | Coordinate artifact lifecycle, work package sequencing, review cadence, and evidence expectations. | Architecture Baseline, Capability Map, Capability Dependency Map | P0 | Phase 1 | Specification created; implementation deferred | WP-003, WP-004 | ADR-002 |
| Programme Management | Maintain roadmap, sprint tracking, registers, dashboard, and governance cadence. | Project Conductor | P0 | Phase 1 | Bootstrap artifacts created | WP-003, WP-004 | ADR-002 |
| Technology Radar | Govern technology interest, evaluation, and adoption status. | Technology Evaluation Framework | P0 | Phase 1 | Radar created; entries unevaluated | WP-003, WP-005 | ADR-012 |
| Evaluation Platform | Define evaluation plans, metrics, reports, golden assets, regression expectations, and acceptance criteria. | Project Conductor, Technology Radar | P0 | Phase 2 | Specification and scaffold created | WP-005, WP-006 | ADR-005, ADR-012 |
| Golden Asset Lifecycle | Govern candidate and approved prompts, datasets, and workflows. | Evaluation Platform, Project Conductor | P0 | Phase 2 | Folder scaffold created | WP-005, WP-006 | ADR-005 |
| Observability | Define tracing, metrics, logs, model interaction visibility, and run evidence. | Project Conductor, Evidence Storage Standard | P0 | Phase 2 | Capability placeholder | WP-006 | Future Observability ADR |
| Artifact Publisher | Publish reviewed artifacts, evidence summaries, and portfolio-ready outputs. | Project Conductor, Knowledge Platform, Evidence Storage Standard | P1 | Phase 6 | Capability placeholder; evidence template exists | WP-014, WP-018 | Future Artifact Publishing ADR |
| Knowledge Platform | Capture, synthesize, approve, and serve knowledge artifacts. | Project Conductor, Evaluation Platform | P1 | Phase 3 | Specification created | WP-007 | ADR-004 |
| Prompt Platform | Manage prompt assets, versioning, review, evaluation, and promotion. | Evaluation Platform, Knowledge Platform, Project Conductor | P1 | Phase 3 | Specification created | WP-008 | ADR-006, ADR-005 |
| Context Engineering Platform | Package task context, provenance, budget, retrieval outputs, memory inputs, and application state. | Knowledge Platform, Evaluation Platform, Project Conductor | P1 | Phase 3 | Specification created; canonical name needs review acceptance | WP-009 | ADR-007, ADR-008 |
| Memory Platform | Provide future durable memory with governance, provenance, and evaluation. | Knowledge Platform, Evaluation Platform, Observability | P2 | Phase 3 | ADR placeholder | WP-010 | ADR-008 |
| Model Providers | Define provider integration strategy for OpenAI, Claude, Gemini, Ollama, LM Studio, and future providers. | Evaluation Platform, Technology Radar, Observability | P1 | Phase 4 | Capability placeholder; radar entries exist | WP-011 | ADR-003, ADR-010, ADR-012 |
| AI Gateway | Provide model-agnostic access, routing, policy, observability, and provider abstraction. | Model Providers, Observability, Evaluation Platform, Project Conductor | P1 | Phase 4 | Specification created; implementation deferred | WP-011, WP-012 | ADR-003, ADR-010 |
| Tool Platform | Govern tool registry, tool invocation boundaries, safety, observability, and evaluation. | Evaluation Platform, Observability, Project Conductor | P2 | Phase 4 | ADR placeholder | WP-012 | ADR-009 |
| Browser Platform | Provide future browser automation and observation capability. | Tool Platform, Evaluation Platform, Observability | P2 | Phase 4 | Roadmap placeholder | WP-013 | ADR-009, Future Browser Platform ADR |
| Agent Platform | Provide future orchestration substrate for deterministic and agentic workflows. | AI Gateway, Tool Platform, Context Engineering Platform, Memory Platform, Evaluation Platform, Observability | P2 | Phase 5 | Roadmap placeholder | WP-014 | Future Agent Platform ADR |

## Business Applications

| Capability | Purpose | Dependencies | Priority | Estimated Phase | Status | Future Work Packages | Related ADRs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Career Intelligence | First planned business application built on platform capabilities. | AI Gateway, Knowledge Platform, Browser Platform, Project Conductor, Evaluation Platform, Prompt Platform, Context Engineering Platform | P1 | Phase 5 | Placeholder only | WP-015, WP-016 | ADR-001, ADR-011 |

## Future Extensions

Future extensions are recognized because they were identified in WP-001 review artifacts or deferred architecture lists. They should not become implementation work until explicitly approved.

| Extension | Purpose | Dependencies | Priority | Estimated Phase | Status | Future Work Packages | Related ADRs |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Repository Quality Gates | Deterministic checks for metadata, traceability, required links, and stale reviews. | Project Conductor, Artifact Metadata Standard | P0 | Phase 1 | Deferred architecture work | WP-004 | Future Repository Quality Gates ADR |
| Evidence Storage Standard | Standardize evidence naming, storage, retention, and publication readiness. | Project Conductor, Artifact Metadata Standard | P0 | Phase 1 | Deferred architecture work | WP-004 | Future Evidence Storage ADR |
| Security and Data Governance | Define security, privacy, data boundaries, and approval gates before runtime work. | Architecture Baseline, Knowledge Platform, AI Gateway | P0 | Phase 2 and Phase 6 | Deferred architecture work | WP-006, WP-017 | Future Security ADR |
| Data Architecture | Define data ownership, storage, retrieval, and migration boundaries. | Knowledge Platform, Evaluation Platform | P1 | Phase 3 | Deferred architecture work | WP-007 | Future Data Architecture ADR |
| Deployment Architecture | Define production deployment path after platform boundaries are approved. | Observability, Security and Data Governance, AI Gateway | P2 | Phase 6 | Deferred architecture work | WP-017 | Future Deployment ADR |
| Application Onboarding Standard | Define how future applications depend on platform capabilities. | Business Applications ADR, Project Conductor | P1 | Phase 5 | Deferred review item | WP-015 | ADR-011 |

## Critical Implementation Path

The critical path is:

1. Project Conductor and Programme Management governance.
2. ADR approval workflow, artifact index, evidence storage standard, and repository quality gates.
3. Evaluation Platform, Golden Asset Lifecycle, and Observability architecture.
4. Knowledge Platform, Prompt Platform, and Context Engineering Platform.
5. Model Providers, AI Gateway, Model Routing, and Tool Platform.
6. Browser Platform and Agent Platform.
7. Career Intelligence application architecture.
8. Production readiness and artifact publishing.

## Scope Drift Controls

- New capability proposals must identify the existing capability they extend or explain why consolidation is impossible.
- Runtime implementation work must trace to this roadmap, a work package, an architecture specification, related ADRs, an evaluation plan, and evidence expectations.
- Technology additions must enter the Technology Radar as Assess unless supported by evaluation evidence.
- Application-specific needs must remain under `applications/` until they are proven reusable platform concerns.
