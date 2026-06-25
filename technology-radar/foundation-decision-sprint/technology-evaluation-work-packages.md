# Technology Evaluation Work Packages

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-003 |
| Title | Technology Evaluation Work Packages |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-001, FTD-002 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015, ADR-DRAFT-016 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, evaluation-work-packages |
| Review Date | 2026-07-02 |

## Purpose

This artifact defines one evaluation work package per blocking Project Conductor technology decision.

## WP-005A Deterministic Runtime and Tooling Evaluation

| Field | Value |
| --- | --- |
| Objective | Evaluate runtime and tooling options for deterministic repository scanning, validation, indexing, and report generation. |
| Scope | Local execution, package/tool management, testability, maintainability, cross-platform behavior, CI readiness. |
| Candidate Technologies | Python with uv, Node.js/TypeScript with pnpm, Go single-binary tooling, POSIX shell with Make. |
| Evaluation Criteria | Capability fit, deterministic behavior, maintainability, repository fit, testability, operational complexity, migration risk, learning value. |
| Expected Evidence | Candidate comparison matrix, small design analysis, maintenance analysis, dependency implications, migration risk notes. |
| Expected Deliverables | Evaluation report, recommendation, draft ADR-DRAFT-013 update. |
| Definition of Done | A runtime/tooling strategy is recommended with evidence and implementation remains unstarted. |

## WP-005B Artifact Metadata and Registry Format Evaluation

| Field | Value |
| --- | --- |
| Objective | Evaluate how Project Conductor should read and validate artifact metadata across existing Markdown artifacts and future templates. |
| Scope | Metadata representation, parseability, compatibility with current artifacts, migration effort, schema validation, author ergonomics. |
| Candidate Technologies | Existing Markdown metadata tables, YAML front matter, TOML front matter, sidecar YAML/TOML manifests, generated JSON schema-compatible metadata. |
| Evaluation Criteria | Capability fit, authoring simplicity, machine readability, migration risk, validation quality, future extensibility, consistency with templates. |
| Expected Evidence | Current artifact sample analysis, metadata extraction strategy, migration impact assessment, schema validation approach. |
| Expected Deliverables | Evaluation report, recommendation, draft ADR-DRAFT-014 update. |
| Definition of Done | A metadata and registry format strategy is recommended with evidence and no artifact migration is performed. |

## WP-005C Artifact State and Index Strategy Evaluation

| Field | Value |
| --- | --- |
| Objective | Evaluate how Project Conductor should represent artifact registry, work package registry, review queue, and evidence index state. |
| Scope | Generated index format, queryability, diffability, artifact graph representation, checkpoint strategy, local-first operation. |
| Candidate Technologies | Generated JSON index, generated YAML index, SQLite database, Markdown summary reports backed by structured index, graph export formats. |
| Evaluation Criteria | Determinism, version-control friendliness, query needs, implementation simplicity, migration risk, reviewability, integration with future dashboards. |
| Expected Evidence | Interface-to-state mapping, index shape proposal, trade-off matrix, review queue and evidence index examples. |
| Expected Deliverables | Evaluation report, recommendation, draft ADR-DRAFT-015 update. |
| Definition of Done | A state/index strategy is recommended with evidence and no registry implementation is created. |

## WP-005D Quality Gate and Reporting Strategy Evaluation

| Field | Value |
| --- | --- |
| Objective | Evaluate how Project Conductor should run quality gates and produce repository health reports and dashboard inputs. |
| Scope | Local CLI/task execution, report output format, failure levels, future CI integration, dashboard data output, review queue reporting. |
| Candidate Technologies | Local CLI output, generated Markdown reports, JSON report output, GitHub Actions integration, pre-commit integration, Make/task runner integration. |
| Evaluation Criteria | Capability fit, ease of review, CI readiness, local developer ergonomics, deterministic output, failure clarity, implementation simplicity. |
| Expected Evidence | Gate taxonomy proposal, report examples, failure severity model, future CI integration analysis. |
| Expected Deliverables | Evaluation report, recommendation, draft ADR-DRAFT-016 update. |
| Definition of Done | A quality gate/reporting strategy is recommended with evidence and no quality gate implementation is created. |

## Exclusion Guardrail

If an evaluation cannot explain how it directly enables Project Conductor implementation, it does not belong in WP-005.

