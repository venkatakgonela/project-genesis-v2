# Programme Impact Assessment

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-006 |
| Title | Programme Impact Assessment |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-001, FTD-002, FTD-003, FTD-004, FTD-005 |
| Related ADRs | ADR-002, ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, programme-impact |
| Review Date | 2026-07-02 |

## Purpose

This assessment describes how WP-005 changes programme readiness.

## Impact Summary

| Area | Impact |
| --- | --- |
| Scope control | Narrows technology discovery to Project Conductor blockers only. |
| Implementation readiness | Improves readiness by identifying the minimum decisions required before first implementation planning. |
| Technology discovery | Defers broad discovery until after Project Conductor foundation decisions. |
| ADR backlog | Adds four draft ADRs that support ADR-002 Project Conductor. |
| Architecture | No architecture changes. |
| Runtime code | No runtime code introduced. |

## Readiness Change

Before WP-005:

- The programme had a technology discovery process but no minimum decision set for the first platform capability.

After WP-005:

- The programme knows which four technology decisions must be evaluated before Project Conductor implementation planning.
- The programme knows which technology areas are explicitly unnecessary for Project Conductor.
- Future work can avoid broad research and stay focused on deterministic repository automation.

## Remaining Blockers Before Implementation

| Blocker | Resolution Path |
| --- | --- |
| ADR-002 Project Conductor is not approved. | Review and approve or revise ADR-002. |
| Runtime/tooling strategy not decided. | Complete WP-005A and promote ADR-DRAFT-013. |
| Metadata/registry format not decided. | Complete WP-005B and promote ADR-DRAFT-014. |
| Artifact state/index strategy not decided. | Complete WP-005C and promote ADR-DRAFT-015. |
| Quality gate/reporting strategy not decided. | Complete WP-005D and promote ADR-DRAFT-016. |
| Evidence and repository quality expectations not fully approved. | Align WP-005D with baseline readiness requirements. |

## Programme Recommendation

Run WP-005A through WP-005D before any Project Conductor implementation work package.

Do not run Agent Framework, AI Gateway, Model Provider, Prompt Platform, Context Engineering, Browser Platform, or Deployment Platform evaluations as part of Project Conductor foundation work.

