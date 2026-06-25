# WP-006 Project Conductor Product Definition and Operating Model

## Metadata

| Field | Value |
| --- | --- |
| ID | WP-006 |
| Title | Project Conductor Product Definition and Operating Model |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-001, WP-002, WP-003, WP-004, WP-005, WP-005E |
| Related ADRs | ADR-001, ADR-002, ADR-004, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-010, ADR-012, ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016, ADR-DRAFT-017, ADR-DRAFT-018, ADR-DRAFT-019, ADR-DRAFT-020, ADR-DRAFT-021, ADR-DRAFT-022 |
| Related Work Packages | WP-001, WP-002, WP-003, WP-004, WP-005 |
| Tags | project-conductor, product-definition, operating-model, planning |
| Review Date | 2026-07-02 |

## Objective

Create the definitive product definition and operating model for Project Conductor without selecting technologies, modifying architecture, writing ADRs, or implementing runtime code.

## Source Inputs

- `architecture/architecture-baseline.md`
- `architecture/capabilities/capability-map.md`
- `architecture/dependencies/capability-dependency-graph.md`
- `programme/planning/master-capability-roadmap.md`
- `programme/planning/programme-roadmap.md`
- `programme/baseline/authoritative-artifact-register.md`
- `technology-radar/discovery/technology-discovery-programme.md`
- `technology-radar/foundation-decision-sprint/agentic-scope-alignment-report.md`
- `technology-radar/foundation-decision-sprint/project-conductor-layered-capability-model.md`
- `technology-radar/foundation-decision-sprint/updated-wp-005-decision-map.md`
- `technology-radar/foundation-decision-sprint/updated-wp-005-execution-sequence.md`
- `platform/project-conductor/specs/architecture-specification.md`
- `platform/knowledge-platform/specs/architecture-specification.md`
- `platform/prompt-platform/specs/architecture-specification.md`
- `platform/context-engineering-platform/specs/architecture-specification.md`
- `platform/ai-gateway/specs/architecture-specification.md`
- `platform/evaluation-platform/specs/architecture-specification.md`
- `programme/work-packages/foundation-technology/WP-005A-deterministic-runtime-tooling-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005B-artifact-metadata-registry-format-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005C-artifact-state-index-strategy-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005D-quality-gate-reporting-strategy-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005E-agent-framework-orchestration-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005F-ai-gateway-model-routing-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005G-prompt-context-package-strategy-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005H-llm-observability-agent-evaluation-strategy.md`
- `programme/work-packages/foundation-technology/WP-005I-human-approval-checkpoint-workflow-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005J-mcp-tool-runtime-assessment.md`

## Deliverables

| Deliverable | Artifact | Status |
| --- | --- | --- |
| Product vision | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| User personas | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| User problems | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Core capability model | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Operating model | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Context package model | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Prompt package model | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Knowledge interaction model | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Review and governance model | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Future agent model | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| User experience model | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Success metrics | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| MVP definition | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |
| Product roadmap | `platform/project-conductor/product/product-definition-and-operating-model.md` | Complete for Review |

## Scope

In scope:

- Product definition.
- Product operating model.
- Product capability staging.
- User and workflow definition.
- Product success metrics.
- MVP, assisted, agentic, and multi-agent product horizons.

Out of scope:

- Runtime code.
- Python, FastAPI, LangGraph, AI Gateway, or Project Conductor implementation.
- Technology selection.
- ADR authoring or approval.
- Platform architecture redesign.
- Career Intelligence application design.

## Capability Links

- Project Conductor
- Programme Management
- Knowledge Platform
- Prompt Platform
- Context Engineering Platform
- Evaluation Platform
- AI Gateway
- Tool Platform
- Agent Platform
- Observability
- Technology Radar

## Definition of Done

| Criterion | Status |
| --- | --- |
| Project Conductor is defined as a product, not only an architecture capability. | Complete |
| Product definition aligns with the platform-first architecture baseline. | Complete |
| Product definition remains reusable beyond Career Intelligence. | Complete |
| Future technology evaluations can use the product definition as input. | Complete |
| No runtime implementation assumptions are introduced. | Complete |
| No new platform capability names are invented. | Complete |
| Prompt is archived in `prompts/`. | Complete |

