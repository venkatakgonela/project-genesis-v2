# Programme Roadmap

## Metadata

| Field | Value |
| --- | --- |
| ID | PRG-007 |
| Title | Programme Roadmap |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | PRG-006, ARCH-004 |
| Related ADRs | ADR-001, ADR-002, ADR-005, ADR-012 |
| Related Work Packages | WP-002 |
| Tags | roadmap, programme, phases |
| Review Date | 2026-07-02 |

## Purpose

This programme roadmap translates the Master Capability Roadmap into implementation phases for the next 6-12 months. It remains planning-only and does not authorize runtime implementation.

## Phase 0: Bootstrap Baseline

Goal:

Establish the repository as an enterprise AI engineering operating system.

Completed through WP-001:

- Repository structure.
- Architecture baseline.
- Capability map.
- Capability dependency map.
- ADR placeholders.
- Technology radar.
- Evaluation scaffold.
- Platform specifications.
- Bootstrap and review reports.

Exit criteria:

- WP-001 accepted.
- Repository committed and pushed.
- No runtime code introduced.

## Phase 1: Governance and Planning Control

Goal:

Turn the repository scaffold into a controlled programme system before implementation begins.

Capabilities:

- Project Conductor.
- Programme Management.
- Technology Radar.
- Repository Quality Gates.
- Evidence Storage Standard.

Primary ADRs:

- ADR-001 Platform First.
- ADR-002 Project Conductor.
- ADR-012 Technology Radar.
- Future Repository Quality Gates ADR.
- Future Evidence Storage ADR.

Exit criteria:

- Canonical capability names accepted.
- Artifact index approach defined.
- ADR approval workflow defined.
- Evidence naming and storage standard approved.
- Repository validation requirements defined.

## Phase 2: Evaluation and Evidence Foundation

Goal:

Make evaluation, golden assets, observability, and evidence production ready enough to govern later platform implementation.

Capabilities:

- Evaluation Platform.
- Golden Asset Lifecycle.
- Observability.
- Security and Data Governance baseline.

Primary ADRs:

- ADR-005 Evaluation Platform.
- ADR-012 Technology Radar.
- Future Observability ADR.
- Future Security and Data Governance ADR.

Exit criteria:

- Evaluation plan template accepted.
- Golden asset promotion rules accepted.
- Observability architecture approved.
- Security and data governance baseline approved.
- First non-runtime evaluation assets drafted.

## Phase 3: Knowledge, Prompt, and Context Foundations

Goal:

Prepare the platform capabilities that structure knowledge, prompts, context, and memory before model or agent runtime work.

Capabilities:

- Knowledge Platform.
- Prompt Platform.
- Context Engineering Platform.
- Memory Platform.
- Data Architecture.

Primary ADRs:

- ADR-004 Knowledge Platform.
- ADR-006 Prompt Platform.
- ADR-007 Context Engineering.
- ADR-008 Memory Platform.
- Future Data Architecture ADR.

Exit criteria:

- Knowledge lifecycle and approval gates reviewed.
- Prompt asset lifecycle reviewed.
- Context package architecture reviewed.
- Memory capability scope decided.
- Data architecture decisions identified.

## Phase 4: Model, Tool, and Runtime Boundary Architecture

Goal:

Define model, gateway, tool, and browser boundaries without coupling them to Career Intelligence.

Capabilities:

- Model Providers.
- AI Gateway.
- Model Routing.
- Tool Platform.
- Browser Platform.

Primary ADRs:

- ADR-003 AI Gateway.
- ADR-009 Tool Platform.
- ADR-010 Model Routing.
- Future Browser Platform ADR.

Exit criteria:

- Provider abstraction approach reviewed.
- Model routing policy inputs defined.
- Tool governance architecture reviewed.
- Browser Platform role reviewed.
- Technology evaluations identified for runtime candidates.

## Phase 5: Agent and Application Readiness

Goal:

Prepare agent orchestration and the first business application architecture only after platform contracts are mature.

Capabilities:

- Agent Platform.
- Business Applications.
- Career Intelligence.
- Application Onboarding Standard.

Primary ADRs:

- ADR-011 Business Applications.
- Future Agent Platform ADR.
- Future Application Onboarding ADR.

Exit criteria:

- Business application dependency rules approved.
- Agent Platform architecture scope approved.
- Career Intelligence product and architecture briefs drafted.
- Evaluation plan for Career Intelligence drafted.

## Phase 6: Production Readiness and Publishing

Goal:

Prepare production, operations, and publication pathways after capability architecture is stable.

Capabilities:

- Artifact Publisher.
- Deployment Architecture.
- Security and Data Governance.
- Observability.
- Evidence and Portfolio Publishing.

Primary ADRs:

- Future Deployment Architecture ADR.
- Future Artifact Publishing ADR.
- Future Security ADR.
- Future Observability ADR.

Exit criteria:

- Deployment path reviewed.
- Evidence publishing approach approved.
- Operational readiness checklist defined.
- Portfolio publication standards approved.

## Programme Gates

| Gate | Required Before Moving Forward |
| --- | --- |
| Phase 1 to Phase 2 | Platform-first ADR, Project Conductor ADR, Technology Radar ADR, evidence standard, and repository quality gate plan. |
| Phase 2 to Phase 3 | Evaluation Platform ADR, golden asset rules, observability architecture, and security baseline. |
| Phase 3 to Phase 4 | Knowledge, Prompt, Context Engineering, Memory, and data architecture decisions reviewed. |
| Phase 4 to Phase 5 | AI Gateway, Model Routing, Tool Platform, Browser Platform, and provider strategy reviewed. |
| Phase 5 to Phase 6 | Application onboarding rules, Agent Platform scope, and Career Intelligence architecture plan reviewed. |

