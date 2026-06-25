# Recommended Execution Sequence

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-004 |
| Title | Recommended Execution Sequence |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-001, FTD-002, FTD-003 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, execution-sequence |
| Review Date | 2026-07-02 |

## Purpose

This sequence orders the WP-005 technology evaluations by architectural dependency.

## Recommended Order

| Order | Work Package | Why This Comes Next |
| --- | --- | --- |
| 1 | WP-005A Deterministic Runtime and Tooling Evaluation | All later decisions depend on knowing the execution environment and packaging/tooling constraints. |
| 2 | WP-005B Artifact Metadata and Registry Format Evaluation | Project Conductor cannot validate artifacts until it knows how metadata will be represented and parsed. |
| 3 | WP-005C Artifact State and Index Strategy Evaluation | Registry, review queue, and evidence index design depend on runtime/tooling and metadata format. |
| 4 | WP-005D Quality Gate and Reporting Strategy Evaluation | Quality gates and reports depend on runtime execution, metadata extraction, and index strategy. |

## Dependency Chain

```text
WP-005A Runtime and Tooling
  -> WP-005B Metadata and Registry Format
  -> WP-005C State and Index Strategy
  -> WP-005D Quality Gate and Reporting Strategy
  -> Project Conductor Implementation Planning
```

## Why Broader Technology Evaluation Is Excluded

| Technology Area | Reason Excluded From WP-005 |
| --- | --- |
| Agent Frameworks | Project Conductor begins deterministic and is not an agent workflow. |
| AI Gateway | Project Conductor does not need model access. |
| Model Providers | No model provider is required for repository validation. |
| Prompt Platform | Prompt lifecycle is not required for Project Conductor implementation. |
| Context Engineering | Context packaging is unrelated to repository artifact scanning. |
| Browser Platform | Browser automation is not required. |
| Deployment Platform | Local implementation planning can precede deployment evaluation. |

## Implementation Gate

Project Conductor implementation planning may begin only after:

- WP-005A through WP-005D complete.
- ADR-DRAFT-013 through ADR-DRAFT-016 are converted into reviewed ADRs.
- ADR-002 Project Conductor is approved or revised.
- Evidence expectations and repository quality gates are accepted.

