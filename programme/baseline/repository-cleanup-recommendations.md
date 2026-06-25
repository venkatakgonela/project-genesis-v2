# Repository Cleanup Recommendations

## Metadata

| Field | Value |
| --- | --- |
| ID | BASE-003 |
| Title | Repository Cleanup Recommendations |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | BASE-001, BASE-002 |
| Related ADRs | ADR-001, ADR-002, ADR-012 |
| Related Work Packages | WP-004 |
| Tags | cleanup, recommendations, baseline |
| Review Date | 2026-07-02 |

## Purpose

This artifact recommends cleanup actions. It does not perform cleanup.

## Recommended Actions

| ID | Artifact or Area | Action | Rationale | Priority |
| --- | --- | --- | --- | --- |
| CLEAN-001 | `.DS_Store` | Remove | Local system file is not an engineering artifact. | P0 |
| CLEAN-002 | `programme/roadmap.md` | Archive or mark superseded | WP-002 programme roadmap and master capability roadmap are now more authoritative. | P1 |
| CLEAN-003 | `technology-radar/technology-evaluation-framework.md` | Mark superseded by WP-003 framework | WP-003 framework has expanded criteria, evidence rules, and recommendation policy. | P1 |
| CLEAN-004 | `programme/planning/future-work-package-sequence.md` | Revise | It describes WP-003 as governance ADR approval, but actual WP-003 is Technology Discovery Programme. | P0 |
| CLEAN-005 | `programme/planning/programme-readiness-report.md` | Mark as WP-002 historical readiness | It recommends a next milestone that has since changed. | P1 |
| CLEAN-006 | `web-review/` | Keep as review evidence or move under `docs/reviews/web-review/` | Useful external review evidence, but not canonical governance. | P2 |
| CLEAN-007 | `docs/reviews/engineering-self-review.md` | Keep as WP-001 review evidence | Historical but valuable. | P3 |
| CLEAN-008 | `architecture/dependencies/capability-dependency-map.md` | Keep as initial dependency map | Do not delete; dependency graph is authoritative for sequencing. | P2 |
| CLEAN-009 | ADR placeholders | Keep and prioritize review | They are needed, but cannot authorize implementation until approved. | P0 |
| CLEAN-010 | `prompts/` | Keep | Prompts provide source traceability but are not architecture. | P3 |

## Merge Recommendations

| Source | Target | Recommendation |
| --- | --- | --- |
| WP-001 roadmap insights | `programme/planning/programme-roadmap.md` | Merge any still-useful horizon language, then mark original as historical. |
| WP-001 technology evaluation criteria | `technology-radar/discovery/technology-evaluation-framework.md` | Confirm all useful criteria are represented, then mark original as superseded. |
| Web-review architecture findings | `programme/baseline/consolidation-report.md` or future baseline review | Preserve findings but do not keep web-review as active governance. |

## Archive Recommendations

| Artifact | Archive Path Suggestion | Reason |
| --- | --- | --- |
| `programme/roadmap.md` | `docs/archive/wp-001/programme-roadmap.md` | Superseded by WP-002 planning artifacts. |
| `web-review/*.md` | `docs/archive/web-review/` or `docs/reviews/web-review/` | Review evidence, not active governance. |

## Rename Recommendations

| Current Name | Suggested Name | Reason |
| --- | --- | --- |
| `technology-radar/technology-evaluation-framework.md` | `technology-radar/initial-technology-evaluation-framework.md` | Clarifies it is the WP-001 seed framework. |
| `programme/planning/future-work-package-sequence.md` | Keep name after revision | The name is useful; content needs alignment. |

## Deprecation Recommendations

| Artifact | Deprecation Reason | Replacement |
| --- | --- | --- |
| `programme/roadmap.md` | Superseded by more complete WP-002 roadmap. | `programme/planning/programme-roadmap.md` |
| WP-002 readiness recommendation that WP-003 should approve governance ADRs | Actual WP-003 has become Technology Discovery Programme. | New post-WP-004 governance ADR work package should be created. |

## Keep Recommendations

| Artifact Area | Reason |
| --- | --- |
| `architecture/architecture-baseline.md` | Authoritative architecture baseline. |
| `programme/planning/master-capability-roadmap.md` | Authoritative capability hierarchy and planning roadmap. |
| `architecture/dependencies/capability-dependency-graph.md` | Authoritative dependency model. |
| `technology-radar/discovery/` | Authoritative technology discovery programme. |
| `platform/*/specs/` | Capability specifications are still needed before implementation. |
| `evaluation/` and `golden/` | Evaluation and golden asset lifecycle structure is valid. |
| `knowledge/` | Knowledge lifecycle structure is valid. |
| `templates/` | Reusable artifact templates are valid. |

## Cleanup Sequencing

Recommended future cleanup work package:

WP-005 Baseline Cleanup Execution.

Definition of done:

- Remove non-artifact files.
- Add supersession notes.
- Update future work package sequence.
- Move or tag historical review artifacts.
- Update programme dashboard and registers.
- Confirm authoritative artifact register still matches repository state.

