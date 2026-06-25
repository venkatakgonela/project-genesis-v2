# Foundation Technology Decision List

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-002 |
| Title | Foundation Technology Decision List |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-001 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, technology-decisions |
| Review Date | 2026-07-02 |

## Purpose

This list includes only technology decisions that are genuinely required before Project Conductor implementation can begin.

## Decision List

| ID | Decision Question | Why It Matters | Dependencies | Priority | Suggested Future Work Package | Expected ADR |
| --- | --- | --- | --- | --- | --- | --- |
| FTD-DEC-001 | What deterministic runtime and tooling strategy should Project Conductor use? | Repository scanning, metadata validation, dependency checks, and dashboard generation require an executable environment and package/tooling strategy. | Project Conductor specification, repository structure, artifact metadata standard. | P0 | WP-005A | ADR-DRAFT-013 |
| FTD-DEC-002 | What artifact metadata and registry format should Project Conductor parse and validate? | Current metadata is represented in Markdown tables; implementation needs a reliable machine-readable strategy before validation can be credible. | Artifact metadata standard, templates, current Markdown artifacts. | P0 | WP-005B | ADR-DRAFT-014 |
| FTD-DEC-003 | What artifact state and index strategy should Project Conductor use? | Artifact Registry, Work Package Registry, Review Queue, and Evidence Index require an index or state model. | FTD-DEC-001, FTD-DEC-002. | P0 | WP-005C | ADR-DRAFT-015 |
| FTD-DEC-004 | What quality gate and reporting strategy should Project Conductor use for repository health and dashboard output? | Project Conductor must produce health checks, review queues, traceability gaps, and dashboard inputs before it can enforce lifecycle expectations. | FTD-DEC-001, FTD-DEC-002, FTD-DEC-003. | P0 | WP-005D | ADR-DRAFT-016 |

## Explicitly Excluded Decisions

| Excluded Area | Reason |
| --- | --- |
| Agent framework selection | Project Conductor begins deterministic and explicitly does not implement AI workflows. |
| AI Gateway implementation | Project Conductor does not require model access. |
| Model provider selection | Project Conductor should not depend on model providers. |
| Prompt platform tooling | Project Conductor does not manage prompt execution. |
| Context engineering tooling | Project Conductor does not assemble runtime context. |
| Browser automation | Project Conductor does not require browser workflows. |
| Deployment platform | Local deterministic tooling can be evaluated before deployment decisions. |
| Production observability stack | First Project Conductor implementation can generate repository evidence without runtime observability infrastructure. |

## Recommendation

Proceed with four focused evaluation work packages only:

1. WP-005A Deterministic Runtime and Tooling Evaluation.
2. WP-005B Artifact Metadata and Registry Format Evaluation.
3. WP-005C Artifact State and Index Strategy Evaluation.
4. WP-005D Quality Gate and Reporting Strategy Evaluation.

Do not start broader technology evaluations until these foundation decisions are resolved.

