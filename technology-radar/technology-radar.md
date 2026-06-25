# Technology Radar

## Metadata

| Field | Value |
| --- | --- |
| ID | TR-001 |
| Title | Initial Technology Radar |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | TR-002 |
| Related ADRs | ADR-012 |
| Related Work Packages | WP-001 |
| Tags | technology-radar, evaluation |
| Review Date | 2026-07-09 |

## Radar Policy

The radar records current interest, not final approval. Uncertain technologies are marked Assess until evaluated. Adopt requires evidence and an ADR.

## Rings

| Ring | Meaning |
| --- | --- |
| Adopt | Approved default for relevant use cases. Requires evidence and ADR. |
| Trial | Worth using in controlled work packages. Requires evaluation plan. |
| Assess | Worth researching. Not yet approved for implementation. |
| Hold | Avoid for now or use only with explicit exception. |

## Initial Entries

| Technology | Category | Ring | Rationale | Next Step |
| --- | --- | --- | --- | --- |
| LangGraph | Agent orchestration | Assess | Potential fit for agent workflows, but not yet evaluated for this platform. | Evaluate after Agent Platform ADR. |
| Microsoft Agent Framework | Agent orchestration | Assess | Potential enterprise relevance, needs maturity and fit assessment. | Research. |
| MCP | Tooling protocol | Assess | Promising tool and context integration protocol; needs architecture decision. | Evaluate with Tool Platform. |
| ToolHive | Tooling | Assess | Potential tool management option; uncertain fit. | Research. |
| Playwright | Browser automation | Trial | Strong candidate for browser workflows and evidence capture. | Evaluate with Browser Platform. |
| FastAPI | API framework | Assess | Familiar candidate for services, but no implementation code in WP-001. | Evaluate during runtime architecture. |
| PostgreSQL | Data platform | Assess | Likely enterprise-grade relational foundation, but data architecture is deferred. | Evaluate with data architecture. |
| pgvector | Vector storage | Assess | Potential retrieval substrate, needs retrieval evaluation and migration analysis. | Evaluate with Knowledge Platform. |
| Langfuse | LLM observability | Assess | Candidate for traces and evaluation evidence; needs cost and integration review. | Evaluate with Observability. |
| DeepEval | Evaluation | Assess | Candidate LLM evaluation framework; requires benchmark comparison. | Evaluate with Evaluation Platform. |
| Promptfoo | Prompt evaluation | Assess | Candidate prompt regression tool; needs workflow fit review. | Evaluate with Prompt Platform. |
| Ragas | Retrieval evaluation | Assess | Candidate retrieval evaluation framework; depends on retrieval architecture. | Evaluate with Knowledge Platform. |
| OpenTelemetry | Observability | Assess | Enterprise-standard observability candidate; needs architecture scope. | Evaluate with Observability. |
| Harness | Delivery platform | Assess | Potential CI/CD governance option; uncertain need at bootstrap. | Research later. |
| Docker Compose | Local orchestration | Trial | Useful for future deterministic local environments; no runtime services yet. | Revisit during first implementation WP. |
| Terraform | Infrastructure | Assess | Potential IaC standard; deployment architecture deferred. | Evaluate during infrastructure planning. |
| Helm | Kubernetes packaging | Assess | Relevant only if Kubernetes becomes target runtime. | Hold decision until deployment architecture. |
| Azure AI Foundry | Enterprise AI platform | Assess | Enterprise relevance; provider/platform fit not yet proven. | Evaluate during provider strategy. |
| OpenAI | Model provider | Assess | Candidate model provider; platform must remain provider agnostic. | Evaluate via AI Gateway. |
| Claude | Model provider | Assess | Candidate model provider; platform must remain provider agnostic. | Evaluate via AI Gateway. |
| Gemini | Model provider | Assess | Candidate model provider; platform must remain provider agnostic. | Evaluate via AI Gateway. |
| Ollama | Local model runtime | Assess | Candidate local runtime for offline experiments; needs quality and operations review. | Evaluate via Model Providers. |
| LM Studio | Local model runtime | Assess | Candidate local runtime; needs governance and repeatability assessment. | Evaluate via Model Providers. |

