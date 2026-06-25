# Evaluation Platform

## Metadata

| Field | Value |
| --- | --- |
| ID | EVAL-000 |
| Title | Evaluation Platform Index |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | ARCH-002, ADR-005 |
| Related ADRs | ADR-005, ADR-012 |
| Related Work Packages | WP-001 |
| Tags | evaluation, platform |
| Review Date | 2026-07-16 |

## Purpose

The Evaluation Platform defines how Project Genesis V2 measures prompts, agents, tools, context, retrieval, models, workflows, and regressions before and after implementation.

## Evaluation Areas

| Area | Folder |
| --- | --- |
| Golden Prompts | `golden-prompts/` |
| Golden Datasets | `golden-datasets/` |
| Golden Workflows | `golden-workflows/` |
| Prompt Evaluation | `prompt-evaluation/` |
| Agent Evaluation | `agent-evaluation/` |
| Tool Evaluation | `tool-evaluation/` |
| Context Evaluation | `context-evaluation/` |
| Retrieval Evaluation | `retrieval-evaluation/` |
| Model Evaluation | `model-evaluation/` |
| Regression Testing | `regression-testing/` |
| Benchmark Results | `benchmark-results/` |
| Evaluation Reports | `evaluation-reports/` |
| Evaluation Metrics | `evaluation-metrics/` |
| Acceptance Criteria | `acceptance-criteria/` |

## Rule

Evaluation assets should be defined before implementation begins and promoted to `golden/` only after review.

