# Project Conductor Dependency Analysis

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-001 |
| Title | Project Conductor Dependency Analysis |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | ARCH-SPEC-001, PRG-006, ARCH-004, BASE-002, BASE-004 |
| Related ADRs | ADR-002, ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, dependency-analysis, foundation-technology |
| Review Date | 2026-07-02 |

## Purpose

This analysis determines which dependencies and technology decisions block Project Conductor implementation planning.

## Source Evidence

| Source | Relevant Evidence |
| --- | --- |
| Project Conductor Specification | Project Conductor coordinates artifact lifecycle, work package sequencing, review cadence, evidence expectations, repository health checks, traceability, and dashboard generation. |
| Architecture Baseline | Every implementation must trace to architecture, ADR, evaluation, and evidence. |
| Master Capability Roadmap | Project Conductor is Phase 1, P0, and precedes most platform work. |
| Capability Dependency Graph | Project Conductor is foundational; later capabilities depend on it. |
| Authoritative Artifact Register | Architecture baseline, master roadmap, dependency graph, and technology discovery programme are authoritative. |
| Readiness Assessment | Runtime implementation remains blocked until ADRs, evidence standards, repository quality gates, and technology decisions mature. |

## Responsibilities

Project Conductor is responsible for:

- Maintaining relationships between capabilities, ADRs, work packages, evaluation plans, evidence, reviews, and lessons learned.
- Providing a consistent view of programme state.
- Enforcing lifecycle expectations before implementation begins.
- Supporting repository health checks.
- Supporting artifact traceability.
- Supporting future dashboard generation.

## Non-Responsibilities

Project Conductor is not responsible for:

- AI workflows.
- Model provider selection.
- Agent orchestration.
- Prompt execution.
- Context assembly.
- Business application logic.
- Browser automation.
- Production deployment.

## Inputs

| Input | Source | Notes |
| --- | --- | --- |
| Artifact metadata | Markdown artifacts across repository | Current metadata is represented as Markdown tables. |
| Artifact lifecycle states | `docs/artifact-lifecycle.md` | Defines lifecycle gates and states. |
| Capability map | `architecture/capabilities/capability-map.md` | Compact capability inventory. |
| Dependency graph | `architecture/dependencies/capability-dependency-graph.md` | Authoritative sequencing model. |
| Work packages | `programme/work-packages/` | WP records and future planned work packages. |
| ADRs | `adr/` and future draft ADRs | Decision status and traceability. |
| Registers | `programme/registers/` | Decisions, risks, assumptions. |
| Evaluation assets | `evaluation/` and `golden/` | Future evidence and acceptance criteria links. |
| Baseline artifacts | `programme/baseline/` | Authoritative artifact register and readiness gates. |

## Outputs

| Output | Purpose |
| --- | --- |
| Artifact registry | Index artifacts, metadata, status, owner, dependencies, and review dates. |
| Work package registry | Index work package status, dependencies, deliverables, and definition of done. |
| Review queue | Identify artifacts requiring review or stale review dates. |
| Evidence index | Link claims, work packages, evaluations, and evidence artifacts. |
| Repository health report | Report missing metadata, broken references, stale reviews, and lifecycle gaps. |
| Programme dashboard data | Future input for dashboard generation. |

## Interfaces

| Interface | Type | Blocking Technology Decision |
| --- | --- | --- |
| Artifact Registry | Generated index or queryable store | Artifact state and index strategy. |
| Work Package Registry | Generated index or queryable store | Artifact state and index strategy. |
| Review Queue | Generated report | Quality gate and reporting strategy. |
| Evidence Index | Generated index or report | Artifact metadata and state strategy. |
| Repository Health Checks | CLI, script, or task runner | Deterministic runtime and tooling strategy. |
| Dashboard Generation | Markdown, static output, or future UI feed | Quality gate and reporting strategy. |

## Dependency Decision Review

| Dependency or Integration | Can implementation begin without decision? | Explanation | Technology Decision Needed Now |
| --- | --- | --- | --- |
| Architecture Baseline | Yes | Authoritative baseline already exists. | No |
| Master Capability Roadmap | Yes | Authoritative capability hierarchy already exists. | No |
| Capability Map | Yes | Current map can be read as source artifact. | No |
| Capability Dependency Graph | Yes | Authoritative dependency model already exists. | No |
| Artifact Metadata Standard | Partially | Standard exists, but Project Conductor needs a machine-readable parsing strategy. | Yes |
| Artifact Registry | No | Core interface; implementation needs storage/index format. | Yes |
| Work Package Registry | No | Core interface; can share artifact registry strategy. | Yes |
| Review Queue | No | Requires validation/reporting strategy and review-date handling. | Yes |
| Evidence Index | Partially | A minimal version can index links; full evidence governance can evolve later. | Yes, only for index format |
| Repository Health Checks | No | Core responsibility; requires deterministic runtime/tooling. | Yes |
| Dashboard Generation | No | Core responsibility; requires output/reporting strategy. | Yes |
| Evidence Storage Standard | Yes for first implementation | Project Conductor can initially report missing evidence links; storage standard can mature separately. | No |
| Repository Quality Gates | No | Core implementation purpose; requires quality gate strategy. | Yes |
| Technology Discovery Programme | Yes | It governs evaluation but does not dictate conductor runtime. | No |
| Evaluation Platform | Yes | Project Conductor can be tested with focused acceptance checks before Evaluation Platform implementation. | No |
| Observability | Yes | Runtime observability is not needed for first deterministic repository tooling. | No |
| Knowledge Platform | Yes | Project Conductor indexes knowledge artifacts but does not require Knowledge Platform implementation. | No |
| Prompt Platform | Yes | Not a Project Conductor responsibility. | No |
| Context Engineering Platform | Yes | Not a Project Conductor responsibility. | No |
| Memory Platform | Yes | Not a Project Conductor responsibility. | No |
| AI Gateway | Yes | Explicitly not required; Project Conductor should begin deterministic. | No |
| Model Providers | Yes | Not required. | No |
| Tool Platform | Yes | Not required for first implementation; Project Conductor itself is not an agent tool yet. | No |
| Browser Platform | Yes | Not required. | No |
| Agent Platform | Yes | Explicitly out of scope; avoid agentic orchestration until lifecycle rules are stable. | No |
| Deployment Platform | Yes | Local deterministic tooling can precede deployment decisions. | No |

## Blocking Decision Summary

Only four technology decisions block useful Project Conductor implementation planning:

1. Deterministic runtime and tooling strategy.
2. Artifact metadata and registry format strategy.
3. Artifact state and index strategy.
4. Quality gate and reporting strategy.

All AI, agent, model, gateway, prompt, context, browser, and deployment technology evaluations are unnecessary for Project Conductor foundation work.

