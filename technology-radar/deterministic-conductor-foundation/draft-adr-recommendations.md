# WP-007 Draft ADR Recommendations

## Metadata

| Field | Value |
| --- | --- |
| ID | DCF-006 |
| Title | WP-007 Draft ADR Recommendations |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | DCF-001, DCF-002, DCF-003, DCF-004 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-007 |
| Tags | adr-recommendations, deterministic-mvp, project-conductor |
| Review Date | 2026-07-02 |

## Purpose

This artifact recommends how ADR-DRAFT-013 through ADR-DRAFT-016 should be updated. It does not approve ADRs.

## ADR-DRAFT-013 Recommendation

Decision:

Adopt Python with uv as the deterministic Project Conductor runtime and project management foundation.

Decision detail:

- Core deterministic behavior should be standard-library-first.
- Pydantic should be approved for schema validation once the metadata and registry schema are defined.
- Typer should be approved for CLI ergonomics if the first implementation work package needs a multi-command local interface.
- Rich should be approved only for non-authoritative console presentation.
- JSON and Markdown outputs should remain authoritative over console rendering.

Explicit deferrals:

- FastAPI.
- AI Gateway.
- LangGraph.
- MCP.
- Browser automation.
- Agent frameworks.

## ADR-DRAFT-014 Recommendation

Decision:

Use current Markdown metadata tables as the MVP authoring source and generated JSON as the normalized machine-readable artifact registry.

Decision detail:

- Enforce the DOC-001 metadata field set.
- Require stable artifact IDs and review dates for durable artifacts.
- Normalize source metadata into a generated registry.
- Mark generated registry outputs as derived state.

Explicit deferrals:

- YAML front matter migration.
- TOML front matter migration.
- Sidecar metadata manifests.
- SQLite as the registry source of truth.

## ADR-DRAFT-015 Recommendation

Decision:

Use a deterministic filesystem-first repository state engine with content hashing, optional Git state enrichment, generated JSON indexes, and generated Markdown summaries.

Decision detail:

- Filesystem scan is the source of artifact discovery.
- Git state enriches local changed/untracked/history views but is not the only source.
- Content hashes identify stale generated outputs.
- Generated JSON supports dashboards and downstream automation.
- Generated Markdown supports human review.

Explicit deferrals:

- SQLite state store.
- Graph database or graph export as canonical state.
- Incremental indexing.
- Agentic checkpoint state.

## ADR-DRAFT-016 Recommendation

Decision:

Use local-first staged deterministic quality gates with Markdown and JSON report outputs.

Decision detail:

- Use severity levels: Info, Warning, Error, Blocker.
- Implement P0 gates for metadata, registry coverage, local links, dependency order, work package traceability, platform/application boundaries, evidence expectations, review freshness, and generated state freshness.
- Produce Markdown reports for human review.
- Produce JSON reports for dashboards and future automation.

Explicit deferrals:

- GitHub Actions enforcement.
- Pre-commit enforcement.
- Automated remediation.
- Agentic review routing.

## ADR Review Sequencing

```text
ADR-DRAFT-013 -> ADR-DRAFT-014 -> ADR-DRAFT-015 -> ADR-DRAFT-016
```

Rationale:

- Runtime decision constrains available validation and reporting tools.
- Metadata format constrains registry shape.
- Registry shape constrains state engine output.
- State engine output constrains quality gate inputs and reports.

## Approval Boundary

These recommendations are ready for human review. They should not be treated as approved decisions until the ADR drafts are updated and accepted through the programme governance process.

