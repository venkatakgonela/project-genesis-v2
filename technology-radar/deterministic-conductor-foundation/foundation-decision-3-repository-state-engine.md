# Foundation Decision 3: Repository State Engine

## Metadata

| Field | Value |
| --- | --- |
| ID | DCF-003 |
| Title | Repository State Engine Decision Report |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-007, WP-005C, DCF-001, DCF-002, ARCH-SPEC-001, PC-PROD-001 |
| Related ADRs | ADR-DRAFT-015 |
| Related Work Packages | WP-007, WP-005C |
| Tags | project-conductor, repository-state, artifact-index |
| Review Date | 2026-07-02 |

## Decision Question

How should deterministic Project Conductor determine repository state?

## Deterministic MVP Need

The state engine must identify artifacts, extract metadata, compute state, detect changes, generate indexes, and produce review and evidence views in a deterministic local workflow.

## Comparison Matrix

| Option | Purpose | Architectural Fit | Product Fit | Simplicity | Extensibility | Operational Complexity | Community Maturity | Sustainability | Learning Value | Interview Value | Migration Risk | Cost | Dependencies | Risks | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full filesystem scan | Discover all repository artifacts deterministically. | High | High | High | Medium | Low | High | High | Medium | Medium | Low | Low | Filesystem APIs | May become slower as repository grows. | PC-PROD-001, ARCH-SPEC-001. |
| Git status enrichment | Add changed, untracked, and modified state. | Medium | High | Medium | High | Medium | High | High | Medium | High | Low | Low | Git CLI or library | Git status can be slower in large worktrees and should not be the only source. | Git docs. |
| Git history analysis | Understand artifact evolution and review history. | Medium | Medium | Medium | High | Medium | High | High | Medium | High | Medium | Low | Git | More than MVP needs unless history-based reports are required. | Git docs. |
| Content hashing | Detect deterministic content changes and stale indexes. | High | High | High | High | Low | High | High | High | High | Low | Low | Hashing support | Hashes do not explain semantic meaning of change. | Python standard library docs. |
| Incremental indexing | Avoid scanning unchanged content. | Medium | Medium | Medium | High | Medium | High | Medium | Medium | Medium | Medium | Low | Prior index, hashes | Premature until repository size justifies complexity. | WP-005C. |
| SQLite state store | Queryable state cache. | Medium | Medium | Medium | High | Medium | High | High | High | High | Medium | Low | SQLite | Binary state and migrations add complexity before query needs are proven. | SQLite docs. |
| Generated JSON indexes plus Markdown summaries | Machine-readable and human-reviewable state output. | High | High | High | High | Low | High | High | High | High | Low | Low | JSON, Markdown | Requires clear generated-output policy. | WP-005C, PC-PROD-001. |

## Strengths

- Full filesystem scanning is deterministic, transparent, and easy to test.
- Content hashing provides a stable basis for change detection and stale-output detection.
- Git state can enrich reports without replacing filesystem truth.
- Generated JSON indexes serve dashboards, quality gates, and future adapters.
- Markdown summaries keep review outputs readable for humans.

## Weaknesses

- A full scan is less efficient than incremental indexing at large scale.
- Git history analysis can distract from MVP state needs.
- Generated indexes need stable naming and regeneration rules.
- SQLite may become useful later but creates schema migration decisions too early.

## Risks

| Risk | Mitigation |
| --- | --- |
| Repository state becomes nondeterministic due to environment differences. | Normalize paths, timestamps, sorting, and generated output ordering. |
| Git state is unavailable or dirty in local workflows. | Treat Git data as optional enrichment and always support filesystem-only state. |
| Generated state becomes stale. | Use content hashes and quality gates to detect stale generated outputs. |
| State model grows into future agent checkpointing too early. | Limit WP-007 state to deterministic artifact, work package, review, evidence, and dependency views. |

## Recommendation

Use a deterministic repository state engine based on:

- Full filesystem scanning for supported artifact paths.
- Metadata extraction from the current Markdown metadata contract.
- Content hashing for change detection and stale-output checks.
- Optional Git state enrichment for modified, untracked, and history-aware views.
- Generated JSON indexes for machine consumption.
- Generated Markdown summaries for human review.

Defer incremental indexing, SQLite state storage, graph database storage, and checkpoint workflow state until deterministic MVP needs prove they are necessary.

## Rationale

The Deterministic MVP needs correctness, transparency, and reviewability more than storage sophistication. A filesystem-first state engine with hashes and generated indexes satisfies repository awareness, review queue generation, evidence tracking, and drift detection without taking on database migrations or agentic checkpoint semantics.

## Supporting Evidence

| Evidence Type | Evidence |
| --- | --- |
| Repository evidence | WP-005C identifies generated indexes, Markdown reports, SQLite, and graph exports as candidate strategies. |
| Product evidence | PC-PROD-001 requires repository state awareness, progress tracking, review support, and evidence tracking as MVP capabilities. |
| Architecture evidence | ARCH-SPEC-001 requires future artifact registry, work package registry, review queue, and evidence index interfaces. |
| External evidence | Git documentation supports changed/untracked state and history inspection; SQLite is viable later but not necessary for MVP query scale. |

## Draft ADR Recommendation

Update ADR-DRAFT-015 to recommend a filesystem-first deterministic state engine with generated JSON indexes and Markdown summaries.

ADR-DRAFT-015 should defer SQLite, graph stores, incremental indexing, and checkpoint workflow state until after the MVP demonstrates scale or query needs.

