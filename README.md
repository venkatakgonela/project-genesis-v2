# Project Genesis V2

Project Genesis V2 is an enterprise AI engineering operating system. It is not an application. It is the version-controlled system of record for planning, architecture, implementation governance, evaluation, evidence, learning, and publishing across future AI applications.

The first planned business application is Career Intelligence. The platform remains generic: business applications depend on platform capabilities, and platform capabilities do not depend on business applications.

## Vision

Project Genesis V2 exists to make enterprise AI engineering repeatable, inspectable, and evidence-led. Every meaningful capability should leave a trail of artifacts: vision, requirements, architecture, ADRs, work packages, evaluation plans, evidence, review, and lessons learned.

The repository should compound knowledge over months. It should prefer deterministic engineering, clear interfaces, and reusable capabilities before introducing LLM-driven behavior.

## Repository Layout

| Path | Purpose |
| --- | --- |
| `programme/` | Charter, roadmap, scope, work packages, registers, sprint tracking, and programme dashboard. |
| `architecture/` | Baseline architecture, capability map, dependency map, and future architecture specifications. |
| `adr/` | Architecture decision records and decision placeholders. |
| `knowledge/` | Raw, synthesized, and approved knowledge captured from discussions, research, and reviews. |
| `evaluation/` | Evaluation platform structure, plans, metrics, benchmark results, and reports. |
| `golden/` | Golden prompts, datasets, and workflows promoted from evaluation assets. |
| `platform/` | Capability specifications for reusable platform services and engineering systems. |
| `applications/` | Business application placeholders that depend on platform capabilities. |
| `technology-radar/` | Technology radar and technology evaluation framework. |
| `docs/` | Cross-cutting standards, reports, reviews, and publication-ready documentation. |
| `templates/` | Reusable artifact templates. |
| `tests/` | Future repository quality checks and evaluation harness tests. No implementation code exists in this sprint. |

## How Decisions Are Made

Architecture decisions are made through ADRs. A decision is not considered durable until it has an ADR with context, options considered, decision, consequences, evidence needs, and review date.

Technology choices should flow through the Technology Evaluation Framework before becoming ADRs. The Technology Radar is an input to decisions, not a replacement for decisions.

## How Work Progresses

Work progresses through work packages. Each work package must connect to one or more capabilities, architecture artifacts, ADRs, evaluation plans, and evidence expectations.

The lifecycle is:

`Idea -> Research -> Architecture -> Approved -> Implementation -> Evaluation -> Review -> Published`

No implementation should begin until the relevant architecture artifact and ADR path exist.

## How Knowledge Is Captured

Raw discussion notes and research notes are stored in `knowledge/00-raw/`. Important insights are synthesized in `knowledge/01-synthesized/` and promoted to `knowledge/02-approved/` only after review.

Approved knowledge should reference related ADRs, capabilities, work packages, and evidence.

## How Evaluations Work

Evaluation starts before implementation. Evaluation artifacts define acceptance criteria, golden prompts, golden datasets, golden workflows, metrics, and regression expectations.

The evaluation platform is model-agnostic and should evaluate prompts, agents, tools, context handling, retrieval, models, and end-to-end workflows.

## How Evidence Is Collected

Evidence is collected per work package and capability. Evidence can include evaluation results, benchmark outputs, review notes, screenshots, traces, logs, runbooks, decision records, and lessons learned.

Capabilities are not complete without evidence and review.

