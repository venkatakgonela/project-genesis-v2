# Foundation Decision 1: Repository Runtime

## Metadata

| Field | Value |
| --- | --- |
| ID | DCF-001 |
| Title | Repository Runtime Decision Report |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-007, WP-005A, ARCH-SPEC-001, PC-PROD-001 |
| Related ADRs | ADR-DRAFT-013 |
| Related Work Packages | WP-007, WP-005A |
| Tags | project-conductor, runtime, deterministic-mvp |
| Review Date | 2026-07-02 |

## Decision Question

What runtime and tooling strategy should be used for deterministic Project Conductor repository automation?

## Deterministic MVP Need

The runtime must support local-first repository scanning, metadata parsing, validation, generated reports, testable quality gates, and future CI use without requiring agent orchestration, model access, or application runtime services.

## Comparison Matrix

| Option | Purpose | Architectural Fit | Product Fit | Simplicity | Extensibility | Operational Complexity | Community Maturity | Sustainability | Learning Value | Interview Value | Migration Risk | Cost | Dependencies | Risks | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Python with uv | General deterministic tooling runtime and project manager. | High | High | High | High | Low | High | High | High | High | Low | Low | Python, uv | Requires dependency discipline. | Python official docs, uv docs, WP-005A. |
| Python standard library only | Minimal runtime with no external CLI/schema dependencies. | High | Medium | High | Medium | Low | High | High | Medium | Medium | Low | Low | Python only | CLI ergonomics and schema validation require more custom code. | Python official docs. |
| Python with Typer, Rich, Pydantic, uv | Developer-friendly CLI, readable console output, schema validation, managed project workflow. | High | High | Medium | High | Medium | High | High | High | High | Medium | Low | Python, uv, Typer, Rich, Pydantic | More dependencies than the deterministic core strictly requires. | Typer, Rich, Pydantic, uv docs. |
| Node.js/TypeScript with pnpm | Alternative typed CLI/tooling runtime. | Medium | Medium | Medium | High | Medium | High | High | Medium | Medium | Medium | Low | Node.js, pnpm, libraries | Less aligned with existing Python-oriented evaluation examples and future AI tooling. | WP-005A candidate only. |
| Go single-binary tooling | Portable compiled deterministic tooling. | Medium | Medium | Medium | Medium | Medium | High | High | Medium | Medium | High | Low | Go toolchain | Faster distribution later, but slower schema/report iteration now. | WP-005A candidate only. |
| POSIX shell with Make | Thin task orchestration and simple checks. | Low | Low | High for tiny tasks | Low | Low | High | Medium | Medium | Medium | High | Low | Shell, make | Poor cross-platform behavior and weak structured validation. | WP-005A candidate only. |

## Strengths

- Python has broad standard-library coverage for filesystem access, JSON handling, hashing, subprocess integration, SQLite access, and command-line parsing.
- uv provides a single project and package management workflow, which supports repeatable local execution and future CI readiness.
- Pydantic fits the deterministic need for structured metadata validation once the registry contract becomes explicit.
- Typer can improve command discoverability and help text for local users without changing the underlying product behavior.
- Rich can make local summaries easier to read, provided JSON and Markdown remain authoritative outputs.

## Weaknesses

- A dependency-heavy CLI can obscure the deterministic core if introduced too early.
- Typer and Rich improve experience but are not required to prove repository state logic.
- Pydantic introduces schema decisions that must align with the artifact metadata and registry decision.
- Go and TypeScript are credible alternatives but add migration cost and reduce alignment with Python-heavy AI engineering tooling.
- Shell scripting is too weak for the validation and registry behavior expected by the MVP.

## Risks

| Risk | Mitigation |
| --- | --- |
| Dependency sprawl before MVP behavior is stable. | Adopt standard-library-first implementation boundaries and require ADR approval for dependencies. |
| Console presentation becomes confused with canonical output. | Treat Rich output as non-authoritative; keep JSON and Markdown reports canonical. |
| Schema validation becomes coupled to future metadata migration. | Validate the current metadata table contract first; allow future registry format evolution. |
| uv adoption creates local onboarding friction. | Document fallback prerequisites and keep execution commands simple. |

## Recommendation

Use Python with uv as the deterministic runtime and project management foundation.

Adopt a standard-library-first design for core repository scanning, hashing, JSON output, filesystem traversal, and deterministic validation. Use Pydantic for explicit schema validation once the artifact registry contract is defined. Use Typer for CLI ergonomics if ADR-DRAFT-013 approves it. Use Rich only for non-authoritative console presentation.

Do not evaluate or introduce agent frameworks, model gateways, browser automation, or tool runtimes for the deterministic MVP.

## Rationale

Python with uv gives Project Conductor the best balance of maintainability, testability, packaging simplicity, developer experience, and future evolution. It supports the deterministic MVP without committing the project to web services, AI orchestration, or application runtime patterns.

The recommended boundary keeps the core deterministic logic independent of optional presentation dependencies. This protects future migration and allows CI adapters, richer reports, and dashboards to evolve without changing repository state semantics.

## Supporting Evidence

| Evidence Type | Evidence |
| --- | --- |
| Repository evidence | WP-005A identifies Python with uv as a candidate for deterministic repository automation. |
| Product evidence | PC-PROD-001 requires repository state awareness, review queues, evidence gaps, drift reports, and deterministic quality gates for MVP. |
| Architecture evidence | ARCH-SPEC-001 directs Project Conductor to start deterministic with repository scans, metadata validation, dependency checks, and dashboard generation. |
| External evidence | Python official documentation confirms broad standard-library support; uv documentation describes project and package management; Typer, Rich, and Pydantic documentation support CLI, terminal presentation, and validation use cases. |

## Draft ADR Recommendation

Update ADR-DRAFT-013 to recommend Python with uv for the deterministic Project Conductor runtime, with Pydantic approved for schema validation, Typer conditionally approved for CLI ergonomics, and Rich conditionally approved for non-authoritative console output.

ADR-DRAFT-013 should explicitly state that this decision does not authorize FastAPI, AI Gateway, LangGraph, MCP, browser automation, or agent framework implementation.

