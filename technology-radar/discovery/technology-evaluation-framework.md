# Technology Evaluation Framework

## Metadata

| Field | Value |
| --- | --- |
| ID | TD-003 |
| Title | Technology Evaluation Framework |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | TD-001, TD-002, TR-002 |
| Related ADRs | ADR-012 |
| Related Work Packages | WP-003 |
| Tags | technology-discovery, evaluation-framework |
| Review Date | 2026-07-02 |

## Purpose

This framework defines the reusable criteria future technology discovery work packages will use. It expands the initial WP-001 framework without scoring any technology in WP-003.

## Evaluation Record Template

| Field | Description |
| --- | --- |
| Evaluation ID | Stable identifier for the evaluation. |
| Capability Area | Capability or future extension being served. |
| Decision Question | Question the evaluation must answer. |
| Candidate Technology | Technology being evaluated. |
| Evaluation Scope | Included scenarios and boundaries. |
| Non-Goals | Explicitly excluded questions. |
| Evidence Sources | Documentation, trials, benchmarks, reviews, architecture analysis, cost data, or operational evidence. |
| Related ADRs | Existing or proposed ADRs affected by the evaluation. |
| Related Work Packages | Work packages that requested or depend on the evaluation. |
| Recommendation | Adopt, Trial, Assess, Hold, or No Decision. |
| Supporting Evidence | Links to evidence artifacts and comparison matrices. |

## Evaluation Criteria

| Criterion | Evaluation Questions | Evidence Type |
| --- | --- | --- |
| Capability Fit | Does the technology solve a real capability need from the roadmap? | Capability mapping, scenario fit, gap analysis. |
| Enterprise Adoption | Is the technology credible in enterprise environments? | Adoption signals, case studies, ecosystem evidence. |
| Community Maturity | Is the community active, documented, and resilient? | Release activity, documentation quality, community support. |
| Long-term Sustainability | Is the project likely to remain viable over the programme horizon? | Governance model, maintainers, roadmap, funding model. |
| Extensibility | Can it support future platform needs without brittle workarounds? | Plugin points, APIs, integration patterns. |
| Operational Complexity | What operational burden does it introduce? | Deployment model, observability needs, failure modes. |
| Learning Value | What durable engineering knowledge does evaluation create? | Architecture learning, reusable patterns, portfolio value. |
| Vendor Lock-in | How hard would it be to leave or replace? | Data portability, API abstraction, contractual constraints. |
| Cost | What are usage, licensing, infrastructure, and maintenance costs? | Pricing, estimated usage, support costs. |
| Migration Risk | What risk exists if the technology must be replaced later? | Migration paths, data formats, abstraction options. |
| Integration Effort | How hard is integration with current and planned platform capabilities? | Interface analysis, dependency mapping. |
| Interview and Portfolio Value | Does it demonstrate credible enterprise AI engineering judgment? | Explanation value, relevance to enterprise architecture. |
| Recommendation | What radar ring or next action is justified? | Evidence-backed decision summary. |
| Supporting Evidence | What proof supports the recommendation? | Linked evidence pack and comparison matrix. |

## Recommendation Values

| Value | Meaning |
| --- | --- |
| Adopt | Approved default for a defined use case. Requires ADR approval. |
| Trial | Worth controlled evaluation or limited use under a work package. |
| Assess | Worth tracking or researching; not approved for implementation. |
| Hold | Do not use unless a future ADR grants an exception. |
| No Decision | Evidence is insufficient or the capability is not mature enough. |

## Scoring Policy

WP-003 does not score technologies.

Future work packages may use qualitative ratings or numeric scores only after defining:

- Evaluation scenario.
- Weighting rationale.
- Evidence standard.
- Reviewer.
- Decision threshold.

## Required Evidence Standard

Every recommendation must include:

- Direct capability trace.
- Comparison against alternatives where alternatives exist.
- Known limitations.
- Migration and lock-in analysis.
- Cost and operational implications.
- ADR impact statement.

