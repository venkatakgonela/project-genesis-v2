# Technology Discovery Programme

## Metadata

| Field | Value |
| --- | --- |
| ID | TD-001 |
| Title | Technology Discovery Programme |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-003, PRG-006, ARCH-004, TR-001, TR-002 |
| Related ADRs | ADR-003, ADR-004, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-010, ADR-012 |
| Related Work Packages | WP-003 |
| Tags | technology-discovery, programme, governance |
| Review Date | 2026-07-02 |

## Purpose

The Technology Discovery Programme governs how Project Genesis V2 identifies, evaluates, compares, recommends, approves, and periodically revisits technologies before implementation begins.

It does not select technologies. It creates the repeatable operating model future work packages will use to evaluate technologies.

## Programme Principles

- Evaluate capability fit before tool preference.
- Keep technology choices reversible until evidence supports adoption.
- Treat the Technology Radar as a discovery input, not an approval mechanism.
- Require ADRs for architecture-shaping technology decisions.
- Separate discovery, evaluation, recommendation, approval, and implementation.
- Prefer deterministic evidence over opinions or demos.
- Preserve platform optionality and model agnosticism.

## Relationship to WP-001 and WP-002

| Source | Contribution to WP-003 |
| --- | --- |
| WP-001 | Created the initial Technology Radar and Technology Evaluation Framework. |
| WP-002 | Defined capability sequencing, canonical capability names, and critical dependency path. |
| WP-003 | Defines the programme that will execute future technology discovery and evaluation. |

## Technology Discovery Lifecycle

```text
Technology Discovery
-> Evaluation
-> Comparison Matrix
-> Recommendation
-> ADR
-> Architecture Approval
-> Implementation
```

Implementation is explicitly outside WP-003. A technology cannot move from recommendation to implementation without ADR approval and an implementation work package.

## Capability Area Coverage

| Capability Area | Source Capability | Discovery Priority | Future Work Package |
| --- | --- | --- | --- |
| Evaluation Platform | Evaluation Platform, Golden Asset Lifecycle | P0 | WP-003A |
| Observability and Evidence | Observability, Evidence Storage Standard | P0 | WP-003B |
| Knowledge Platform and Storage/Retrieval | Knowledge Platform, Data Architecture | P1 | WP-003C |
| Prompt and Context Engineering | Prompt Platform, Context Engineering Platform | P1 | WP-003D |
| Model Providers and Local AI Runtime | Model Providers, AI Gateway, Model Routing | P1 | WP-003E |
| AI Gateway | AI Gateway, Model Routing, Model Providers | P1 | WP-003F |
| Tool and Browser Platform | Tool Platform, Browser Platform | P2 | WP-003G |
| Memory Platform | Memory Platform, Knowledge Platform, Context Engineering Platform | P2 | WP-003H |
| Agent Frameworks | Agent Platform | P2 | WP-003I |
| Deployment Platform | Deployment Architecture, Security and Data Governance | P2 | WP-003J |
| Security and Governance | Security and Data Governance, Project Conductor | P0 | WP-003K |

## Candidate Technology Sources

The initial candidate list comes from the existing Technology Radar:

- LangGraph.
- Microsoft Agent Framework.
- MCP.
- ToolHive.
- Playwright.
- FastAPI.
- PostgreSQL.
- pgvector.
- Langfuse.
- DeepEval.
- Promptfoo.
- Ragas.
- OpenTelemetry.
- Harness.
- Docker Compose.
- Terraform.
- Helm.
- Azure AI Foundry.
- OpenAI.
- Claude.
- Gemini.
- Ollama.
- LM Studio.

This programme does not score or select those technologies. Future discovery work packages will validate whether each belongs in the evaluation scope.

## Governance Model

| Role | Responsibility |
| --- | --- |
| Chief Architect | Owns final architecture approval and ADR acceptance. |
| Technology Discovery Owner | Coordinates discovery work packages and evidence quality. |
| Capability Owner | Defines capability-specific requirements and acceptance criteria. |
| Reviewer | Reviews evaluation evidence, comparison matrices, and ADR readiness. |
| Implementation Engineer | Does not implement until technology decisions are approved. |

## Output Artifacts

Future technology discovery work packages should produce:

- Discovery brief.
- Evaluation plan.
- Candidate technology list.
- Evidence collection plan.
- Comparison matrix.
- Evaluation report.
- Recommendation.
- ADR draft when architecture impact exists.
- Technology Radar update proposal.

## Non-Goals

- Choosing winners in WP-003.
- Implementing proof-of-concept code in WP-003.
- Replacing the Master Capability Roadmap.
- Redesigning platform capabilities.
- Treating popularity as evidence.

