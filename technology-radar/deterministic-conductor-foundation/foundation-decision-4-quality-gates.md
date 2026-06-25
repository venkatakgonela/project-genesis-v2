# Foundation Decision 4: Quality Gates

## Metadata

| Field | Value |
| --- | --- |
| ID | DCF-004 |
| Title | Quality Gates Decision Report |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-007, WP-005D, DCF-001, DCF-002, DCF-003, PC-PROD-001 |
| Related ADRs | ADR-DRAFT-016 |
| Related Work Packages | WP-007, WP-005D |
| Tags | project-conductor, quality-gates, reporting |
| Review Date | 2026-07-02 |

## Decision Question

How should deterministic Project Conductor execute repository quality gates and produce reports?

## Deterministic MVP Need

Quality gates must validate repository health, artifact metadata, traceability, dependency order, evidence coverage, review readiness, and platform/application boundaries before implementation proceeds.

## Comparison Matrix

| Option | Purpose | Architectural Fit | Product Fit | Simplicity | Extensibility | Operational Complexity | Community Maturity | Sustainability | Learning Value | Interview Value | Migration Risk | Cost | Dependencies | Risks | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Local CLI output | Fast feedback for local users. | High | High | High | Medium | Low | High | High | Medium | Medium | Low | Low | Runtime CLI | Not sufficient as durable evidence. | WP-005D. |
| Generated Markdown reports | Human-readable review evidence. | High | High | High | Medium | Low | High | High | High | High | Low | Low | Markdown | Harder for dashboards to consume directly. | PC-PROD-001. |
| JSON report output | Machine-readable gate evidence and dashboard input. | High | High | High | High | Low | High | High | High | High | Low | Low | JSON | Less readable for humans without summaries. | WP-005D. |
| GitHub Actions integration | Future CI enforcement. | Medium | Medium | Medium | High | Medium | High | High | Medium | High | Medium | Low | CI platform | Premature before local gates are stable. | WP-005D. |
| Pre-commit integration | Developer feedback before commits. | Medium | Medium | Medium | Medium | Medium | High | Medium | Medium | Medium | Medium | Low | Pre-commit tooling | Can be noisy before gate severity is calibrated. | WP-005D. |
| Make or task runner integration | Simple command wrapper. | Medium | Medium | High | Medium | Low | High | Medium | Medium | Medium | Medium | Low | Make/task runner | Wrapper is not the gate strategy. | WP-005D. |
| Staged gates with Markdown and JSON outputs | Gate taxonomy plus durable human and machine outputs. | High | High | High | High | Low | High | High | High | High | Low | Low | Runtime, registry, state engine | Requires severity policy and stable output contract. | PC-PROD-001, WP-005D. |

## Gate Taxonomy

| Gate | Purpose | MVP Severity Default |
| --- | --- | --- |
| Metadata Gate | Required metadata exists and follows the metadata table contract. | Error |
| Artifact Registry Gate | Artifacts appear in the generated registry with stable identifiers and paths. | Error |
| Link and Path Gate | Referenced local artifacts exist. | Warning or Error depending on reference type |
| ADR Traceability Gate | Work packages and specifications link to expected ADRs or ADR drafts. | Warning |
| Work Package Traceability Gate | Deliverables link to source work packages and definition of done. | Error |
| Dependency Gate | Capability and work package ordering follows dependency graph constraints. | Error |
| Platform/Application Boundary Gate | Platform artifacts do not depend on application-specific artifacts. | Blocker |
| Capability Naming Gate | New or duplicate capability names are flagged. | Warning |
| Evidence Gate | Required evidence is declared and produced or explicitly deferred. | Warning or Error depending on phase |
| Review Freshness Gate | Review dates and status are present and stale reviews are flagged. | Warning |
| Generated State Freshness Gate | Generated registry and reports match current source content hashes. | Error |

## Severity Model

| Severity | Meaning | Expected Action |
| --- | --- | --- |
| Info | Useful observation. | Review when convenient. |
| Warning | Potential drift or incomplete evidence. | Address before phase transition or implementation readiness. |
| Error | Violates repository quality expectations. | Fix before implementation work proceeds. |
| Blocker | Violates architecture boundary or safety-critical governance. | Stop and require human review. |

## Strengths

- Staged gates map directly to the deterministic MVP success criteria.
- Markdown reports support human review and portfolio-quality evidence.
- JSON reports support dashboards and future CI integration.
- Severity levels prevent every issue from becoming an implementation blocker.
- Local-first gates can be adapted into CI later.

## Weaknesses

- Gate taxonomy needs calibration during first implementation.
- Without ADR approval, gate failure rules remain recommendations.
- Markdown and JSON dual output requires consistent generation logic.
- Some gates, such as architecture drift, may initially be conservative.

## Risks

| Risk | Mitigation |
| --- | --- |
| Quality gates become too noisy. | Start with a small P0 gate set and use warning severity for exploratory checks. |
| Reports become disconnected from generated JSON. | Generate both outputs from the same state model. |
| CI integration is added before local behavior stabilizes. | Treat CI and pre-commit as adapters after local gates are trusted. |
| Architecture rule checks overreach. | Keep MVP rules limited to explicit baseline rules, dependency graph, and platform/application boundary. |

## Recommendation

Use staged deterministic quality gates with:

- Local CLI execution for fast feedback.
- Generated Markdown reports for human review and durable evidence.
- Generated JSON reports for dashboards, automation, and future CI.
- A severity model of Info, Warning, Error, and Blocker.
- MVP gates focused on metadata, registry coverage, local links, traceability, dependency order, evidence expectations, review freshness, generated state freshness, and platform/application boundary rules.

Defer GitHub Actions and pre-commit enforcement until the local gate taxonomy and severity model are reviewed.

## Rationale

The product definition requires review support, evidence tracking, drift detection, architecture compliance, and repository health reporting. A staged gate model provides those outcomes without prematurely binding the project to CI, pre-commit tools, or external services.

## Supporting Evidence

| Evidence Type | Evidence |
| --- | --- |
| Repository evidence | WP-005D identifies local CLI output, Markdown reports, JSON outputs, CI, pre-commit, and task runner integration as candidates. |
| Product evidence | PC-PROD-001 requires deterministic quality gates, review queues, evidence gap reports, and architecture compliance checks. |
| Architecture evidence | ARCH-001 requires implementation traceability, ADR traceability, evidence expectations, and platform/application boundaries. |
| Baseline evidence | BASE-002 identifies authoritative sources that gates should validate against. |

## Draft ADR Recommendation

Update ADR-DRAFT-016 to recommend local-first staged quality gates with Markdown and JSON outputs.

ADR-DRAFT-016 should defer CI enforcement and pre-commit enforcement until local deterministic gates are stable and reviewed.

