# Authoritative Artifact Register

## Metadata

| Field | Value |
| --- | --- |
| ID | BASE-002 |
| Title | Authoritative Artifact Register |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | BASE-001 |
| Related ADRs | ADR-001, ADR-002, ADR-012 |
| Related Work Packages | WP-004, WP-006, WP-007, WP-008, WP-009, WP-010 |
| Tags | artifact-register, baseline, authority |
| Review Date | 2026-07-02 |

## Purpose

This register identifies the authoritative source for each engineering concern after WP-001, WP-002, and WP-003.

## Authoritative Sources

| Engineering Concern | Authoritative Artifact | Supporting Artifacts | Notes |
| --- | --- | --- | --- |
| Repository purpose and vision | `README.md` | `programme/project-charter.md` | README is public entry point; charter is programme-level purpose. |
| Programme charter | `programme/project-charter.md` | `README.md` | Charter remains the programme mandate. |
| Artifact metadata standard | `docs/artifact-metadata-standard.md` | `docs/artifact-lifecycle.md` | Use for all durable engineering artifacts. |
| Artifact lifecycle | `docs/artifact-lifecycle.md` | Templates | Defines lifecycle states and gates. |
| Architecture baseline | `architecture/architecture-baseline.md` | Platform specifications | One authoritative architecture baseline exists. |
| Capability hierarchy and phase model | `programme/planning/master-capability-roadmap.md` | `architecture/capabilities/capability-map.md` | Master roadmap is authoritative for hierarchy, phases, and priority. |
| Capability inventory | `architecture/capabilities/capability-map.md` | `programme/planning/master-capability-roadmap.md` | Capability map remains the compact inventory. |
| Dependency model | `architecture/dependencies/capability-dependency-graph.md` | `architecture/dependencies/capability-dependency-map.md` | Dependency graph is authoritative for sequencing. |
| Programme roadmap | `programme/planning/programme-roadmap.md` | `programme/planning/master-capability-roadmap.md` | WP-001 `programme/roadmap.md` is historical. |
| Future work package sequence | `programme/planning/future-work-package-sequence.md` | WP package files | Needs future update to align with actual WP-003 and WP-004. |
| Scope control | `programme/scope-register.md` | `programme/planning/scope-validation-report.md` | Scope register remains authoritative; scope validation is review evidence. |
| Programme dashboard | `programme/programme-dashboard.md` | Work package files | Dashboard should be updated after cleanup. |
| ADRs | `adr/` | Decision register | ADR directory remains authoritative for decisions. Most ADRs are not yet approved. |
| Decision register | `programme/registers/decision-register.md` | `adr/` | Register summarizes decisions; ADRs contain detail. |
| Risk register | `programme/registers/risk-register.md` | Readiness reports | Register remains authoritative for active risks. |
| Assumption register | `programme/registers/assumption-register.md` | Readiness reports | Register remains authoritative for assumptions. |
| Technology radar inventory | `technology-radar/technology-radar.md` | Discovery backlog | Radar is authoritative for candidate technology ring state. |
| Technology discovery programme | `technology-radar/discovery/technology-discovery-programme.md` | All `technology-radar/discovery/*` documents | One authoritative technology discovery programme exists. |
| Technology evaluation framework | `technology-radar/discovery/technology-evaluation-framework.md` | `technology-radar/technology-evaluation-framework.md` | WP-003 framework supersedes WP-001 seed framework for future evaluations. |
| Technology ADR lifecycle | `technology-radar/discovery/technology-adr-lifecycle.md` | ADR template | Governs technology decision flow. |
| Technology decision gates | `technology-radar/discovery/technology-decision-gates.md` | Work package sequence | Blocks premature implementation. |
| Technology watch | `technology-radar/discovery/technology-watch-process.md` | Technology radar | Governs recurring signal review. |
| Technology discovery backlog | `technology-radar/discovery/technology-discovery-backlog.md` | WP-003A-K files | Authoritative backlog for discovery work. |
| Deterministic Project Conductor foundation decisions | `technology-radar/deterministic-conductor-foundation/` | `programme/work-packages/WP-007-deterministic-project-conductor-foundation-decisions.md`, ADR-DRAFT-013 through ADR-DRAFT-016 | Authoritative recommendation package for deterministic Project Conductor MVP foundation decisions until ADRs are reviewed. |
| Project Conductor Sprint 1 implementation | `programme/work-packages/project-conductor-sprints/sprint-001-repository-scanner/` | `src/project_conductor/`, `tests/project_conductor_tests/`, `programme/work-packages/WP-008-deterministic-project-conductor-mvp-implementation.md` | Authoritative Sprint 1 review, evidence, and documentation package for the repository scanner slice. |
| Project Conductor Sprint 2 implementation | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/` | `src/project_conductor/registry.py`, `tests/project_conductor_tests/test_registry.py`, `programme/work-packages/WP-009-deterministic-project-conductor-mvp-sprint-2-artifact-registry.md` | Authoritative Sprint 2 review, evidence, and documentation package for the Artifact Registry Model slice. |
| Project Conductor Sprint 3 implementation | `programme/work-packages/project-conductor-sprints/sprint-003-metadata-contract-registry-schema/` | `src/project_conductor/metadata_contract.py`, `src/project_conductor/registry.py`, `programme/work-packages/WP-010-deterministic-project-conductor-mvp-sprint-3-metadata-contract-registry-schema.md` | Authoritative Sprint 3 review, evidence, metadata contract, and registry schema package. |
| Platform specifications | `platform/*/specs/architecture-specification.md` | Architecture baseline, ADRs | Specifications are authoritative per capability until replaced by approved architecture revisions. |
| Project Conductor product definition | `platform/project-conductor/product/product-definition-and-operating-model.md` | `platform/project-conductor/specs/architecture-specification.md`, `programme/work-packages/WP-006-project-conductor-product-definition-operating-model.md` | Authoritative product definition and operating model for Project Conductor. Does not replace architecture specifications or ADRs. |
| Evaluation platform scaffold | `evaluation/README.md` | Evaluation subfolder READMEs | Authoritative for evaluation folder structure only, not evaluation execution. |
| Golden assets | `golden/README.md` | `evaluation/golden-*` | `evaluation/` holds candidates; `golden/` holds approved assets. |
| Knowledge lifecycle | `knowledge/README.md` | `knowledge/00-raw/`, `knowledge/01-synthesized/`, `knowledge/02-approved/` | Authoritative lifecycle exists. |
| Prompt archive | `prompts/README.md` | Prompt files | Source prompts are inputs, not approved architecture. |
| Baseline consolidation | `programme/baseline/` | WP-004 file | Authoritative review of baseline readiness. |

## Authority Rules

- When two documents conflict, prefer the newer WP-specific artifact only when this register names it authoritative.
- Historical artifacts should not be deleted without an archive decision.
- ADRs override roadmap assumptions only after approval.
- The Master Capability Roadmap governs planning, but does not authorize implementation.
- Technology Discovery governs evaluation process, but does not authorize technology adoption.

## Final Authority Verification

| Required Baseline Concern | Authoritative Artifact | Verification |
| --- | --- | --- |
| One architecture baseline | `architecture/architecture-baseline.md` | Present |
| One capability hierarchy | `programme/planning/master-capability-roadmap.md` | Present |
| One dependency model | `architecture/dependencies/capability-dependency-graph.md` | Present |
| One technology discovery programme | `technology-radar/discovery/technology-discovery-programme.md` | Present |
