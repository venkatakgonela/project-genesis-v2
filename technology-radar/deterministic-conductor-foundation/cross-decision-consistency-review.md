# WP-007 Cross-Decision Consistency Review

## Metadata

| Field | Value |
| --- | --- |
| ID | DCF-007 |
| Title | WP-007 Cross-Decision Consistency Review |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | DCF-001, DCF-002, DCF-003, DCF-004 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-007 |
| Tags | consistency-review, deterministic-mvp, project-conductor |
| Review Date | 2026-07-02 |

## Purpose

Verify that the WP-007 recommendations work together coherently and remain aligned with Project Conductor Deterministic MVP scope.

## Recommendation Stack

```text
Python with uv runtime
  -> Markdown metadata table contract
  -> Generated JSON artifact registry
  -> Filesystem-first repository state engine
  -> Content hashing and optional Git enrichment
  -> Generated JSON indexes and Markdown summaries
  -> Local-first quality gates with JSON and Markdown reports
```

## Coherence Review

| Area | Assessment | Result |
| --- | --- | --- |
| Runtime to Registry | Python supports Markdown extraction, JSON generation, hashing, CLI workflows, and schema validation. | Compatible |
| Registry to State Engine | Markdown metadata tables can be normalized into generated JSON indexes. | Compatible |
| State Engine to Quality Gates | Quality gates can consume the generated registry, indexes, content hashes, and dependency data. | Compatible |
| Quality Gates to Product Definition | Gate taxonomy maps to deterministic MVP requirements: repository state, review support, evidence tracking, and drift detection. | Compatible |
| Human Review | Markdown summaries keep outputs reviewable without requiring dashboard implementation. | Compatible |
| Future Automation | JSON outputs create a path for dashboards, CI, and later assisted behavior. | Compatible |

## Conflict Review

| Potential Conflict | Assessment | Recommendation |
| --- | --- | --- |
| Markdown metadata vs machine readability | Markdown tables are less structured than front matter. | Use strict metadata table contract and generated JSON normalization. |
| Rich console output vs authoritative reports | Console output could be mistaken for evidence. | Treat Rich output as presentation only; Markdown and JSON are authoritative. |
| Git state vs filesystem state | Git state may be unavailable or incomplete in dirty local repositories. | Use filesystem scan as source and Git as enrichment. |
| SQLite vs generated JSON | SQLite is more queryable but less reviewable and adds migration overhead. | Defer SQLite until query scale requires it. |
| Quality gate strictness vs programme velocity | Too many blockers could slow planning. | Use severity model and reserve Blocker for architecture boundary violations. |

## Architectural Consistency

| Rule | Assessment |
| --- | --- |
| Platform capabilities must not depend on business applications. | Recommendations are application-agnostic and do not depend on Career Intelligence. |
| Every implementation must trace to architecture. | Recommendations trace to ARCH-SPEC-001 and PC-PROD-001. |
| Every architecture decision must trace to an ADR. | Recommendations map to ADR-DRAFT-013 through ADR-DRAFT-016. |
| Runtime technology choices remain reversible until supported by evaluation. | Recommendations remain draft and implementation is blocked pending review. |
| Deterministic MVP must not depend on assisted or agentic capabilities. | Recommendations exclude AI Gateway, MCP, agent frameworks, browser automation, and multi-agent technologies. |

## Required Adjustments

| Adjustment | Reason |
| --- | --- |
| ADR-DRAFT-014 and ADR-DRAFT-015 should define one shared normalized registry schema boundary. | Prevent divergence between metadata parsing and state output. |
| ADR-DRAFT-016 should consume the same generated state model used by dashboards. | Prevent duplicate reporting logic. |
| ADR-DRAFT-013 should distinguish core logic dependencies from presentation dependencies. | Prevent Typer/Rich from shaping domain behavior. |
| Generated outputs should be clearly marked as derived artifacts. | Prevent generated state from becoming a competing source of truth. |

## Verdict

The four WP-007 recommendations are coherent and suitable for ADR review.

They provide the minimum deterministic foundation required for Project Conductor MVP implementation planning while preserving future extension paths for assisted, agentic, and multi-agent horizons.

