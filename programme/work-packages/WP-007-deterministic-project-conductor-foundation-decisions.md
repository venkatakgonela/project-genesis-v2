# WP-007 Deterministic Project Conductor Foundation Decisions

## Metadata

| Field | Value |
| --- | --- |
| ID | WP-007 |
| Title | Deterministic Project Conductor Foundation Decisions |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-001, WP-002, WP-003, WP-004, WP-005, WP-006, ARCH-SPEC-001, PC-PROD-001 |
| Related ADRs | ADR-002, ADR-012, ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-005A, WP-005B, WP-005C, WP-005D, WP-006 |
| Tags | project-conductor, deterministic-mvp, foundation-decisions |
| Review Date | 2026-07-02 |

## Objective

Produce evidence-based engineering recommendations for the minimum deterministic Project Conductor foundation decisions required before Deterministic MVP implementation can begin.

## Scope

In scope:

- Repository runtime recommendation.
- Artifact registry recommendation.
- Repository state engine recommendation.
- Quality gate recommendation.
- Cross-decision consistency review.
- Deterministic MVP readiness assessment.

Out of scope:

- Runtime implementation.
- Python code generation.
- Project Conductor implementation.
- FastAPI, LangGraph, Microsoft Agent Framework, AI Gateway, MCP, browser automation, or multi-agent evaluation.
- Assisted, agentic, or multi-agent capability decisions.
- ADR approval.

## Source Inputs

- `architecture/architecture-baseline.md`
- `architecture/capabilities/capability-map.md`
- `architecture/dependencies/capability-dependency-graph.md`
- `platform/project-conductor/specs/architecture-specification.md`
- `platform/project-conductor/product/product-definition-and-operating-model.md`
- `technology-radar/discovery/technology-discovery-programme.md`
- `programme/work-packages/foundation-technology/WP-005A-deterministic-runtime-tooling-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005B-artifact-metadata-registry-format-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005C-artifact-state-index-strategy-evaluation.md`
- `programme/work-packages/foundation-technology/WP-005D-quality-gate-reporting-strategy-evaluation.md`
- `programme/baseline/authoritative-artifact-register.md`

## Deliverables

| Deliverable | Artifact | Status |
| --- | --- | --- |
| Foundation Decision 1 | `technology-radar/deterministic-conductor-foundation/foundation-decision-1-repository-runtime.md` | Complete for Review |
| Foundation Decision 2 | `technology-radar/deterministic-conductor-foundation/foundation-decision-2-artifact-registry.md` | Complete for Review |
| Foundation Decision 3 | `technology-radar/deterministic-conductor-foundation/foundation-decision-3-repository-state-engine.md` | Complete for Review |
| Foundation Decision 4 | `technology-radar/deterministic-conductor-foundation/foundation-decision-4-quality-gates.md` | Complete for Review |
| Evidence summary | `technology-radar/deterministic-conductor-foundation/evidence-summary.md` | Complete for Review |
| Draft ADR recommendations | `technology-radar/deterministic-conductor-foundation/draft-adr-recommendations.md` | Complete for Review |
| Cross-decision consistency review | `technology-radar/deterministic-conductor-foundation/cross-decision-consistency-review.md` | Complete for Review |
| Deterministic MVP readiness report | `technology-radar/deterministic-conductor-foundation/deterministic-mvp-readiness-report.md` | Complete for Review |

## Recommendation Summary

| Decision | Recommendation | ADR Draft |
| --- | --- | --- |
| Repository Runtime | Use Python with uv as the deterministic runtime and project management foundation; use standard-library-first behavior, Pydantic for schema validation, Typer for CLI ergonomics, and Rich only for non-authoritative console presentation. | ADR-DRAFT-013 |
| Artifact Registry | Keep current Markdown metadata tables as the MVP authoring source, enforce a stricter metadata table contract, and generate structured JSON registry outputs. Defer YAML front matter migration. | ADR-DRAFT-014 |
| Repository State Engine | Use deterministic filesystem scanning, normalized metadata extraction, content hashing, optional Git state enrichment, and generated JSON indexes with Markdown summaries. Defer SQLite until query scale requires it. | ADR-DRAFT-015 |
| Quality Gates | Use staged deterministic gates with severity levels and dual output: human-readable Markdown reports plus machine-readable JSON. Keep CI and pre-commit integration as later adapters. | ADR-DRAFT-016 |

## Definition of Done

| Criterion | Status |
| --- | --- |
| Each foundation decision includes comparison matrix, strengths, weaknesses, risks, recommendation, rationale, evidence, and draft ADR recommendation. | Complete |
| Recommendations support only the Deterministic MVP. | Complete |
| Deferred assisted, agentic, and multi-agent technologies are not evaluated. | Complete |
| Recommendations trace to existing repository artifacts. | Complete |
| Implementation remains blocked pending review and ADR action. | Complete |
| Source prompt is archived in `prompts/`. | Complete |

