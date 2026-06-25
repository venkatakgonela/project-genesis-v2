# Technology Discovery Backlog

## Metadata

| Field | Value |
| --- | --- |
| ID | TD-007 |
| Title | Technology Discovery Backlog |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | TD-001, PRG-006, ARCH-004, TR-001 |
| Related ADRs | ADR-003, ADR-004, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-010, ADR-012 |
| Related Work Packages | WP-003 |
| Tags | technology-discovery, backlog |
| Review Date | 2026-07-02 |

## Purpose

This backlog lists future technology discovery areas. It is not a technology selection list and does not score candidates.

## Backlog Items

| ID | Capability Area | Capability Dependencies | Candidate Technologies or Categories | Priority | Future WP | Status |
| --- | --- | --- | --- | --- | --- | --- |
| TD-BL-001 | Evaluation Platform | Project Conductor, Technology Radar | DeepEval, Promptfoo, Ragas, evaluation harness categories | P0 | WP-003A | Ready for discovery |
| TD-BL-002 | Observability and Evidence | Project Conductor, Evidence Storage Standard | Langfuse, OpenTelemetry, trace/evidence storage categories | P0 | WP-003B | Ready for discovery |
| TD-BL-003 | Knowledge Platform and Storage/Retrieval | Project Conductor, Evaluation Platform | PostgreSQL, pgvector, retrieval framework categories | P1 | WP-003C | Pending Phase 3 architecture |
| TD-BL-004 | Prompt Platform | Evaluation Platform, Knowledge Platform | Promptfoo, prompt registry categories, prompt asset formats | P1 | WP-003D | Pending Evaluation Platform governance |
| TD-BL-005 | Context Engineering | Knowledge Platform, Evaluation Platform | Context packaging patterns, retrieval/context evaluation categories | P1 | WP-003D | Pending Knowledge Platform architecture |
| TD-BL-006 | Model Providers | Evaluation Platform, Observability | OpenAI, Claude, Gemini, provider abstraction categories | P1 | WP-003E | Pending model evaluation plan |
| TD-BL-007 | Local AI Runtime | Model Providers, Evaluation Platform | Ollama, LM Studio, local runtime categories | P2 | WP-003E | Watch |
| TD-BL-008 | AI Gateway | Model Providers, Model Routing, Observability | Gateway abstraction patterns, API framework categories, FastAPI as radar candidate | P1 | WP-003F | Pending ADR-003 and ADR-010 |
| TD-BL-009 | Tool Platform | Evaluation Platform, Observability | MCP, ToolHive, tool registry categories | P2 | WP-003G | Pending Tool Platform architecture |
| TD-BL-010 | Browser Platform | Tool Platform, Evaluation Platform, Observability | Playwright, browser automation categories | P2 | WP-003G | Pending Tool Platform architecture |
| TD-BL-011 | Memory Platform | Knowledge Platform, Context Engineering, Evaluation Platform | Memory architecture categories, storage patterns | P2 | WP-003H | Pending ADR-008 |
| TD-BL-012 | Agent Frameworks | AI Gateway, Tool Platform, Context Engineering, Memory, Evaluation, Observability | LangGraph, Microsoft Agent Framework, orchestration categories | P2 | WP-003I | Blocked until prerequisites mature |
| TD-BL-013 | Deployment Platform | Observability, Security and Data Governance, AI Gateway | Docker Compose, Terraform, Helm, Harness, deployment categories | P2 | WP-003J | Future extension |
| TD-BL-014 | Security and Governance | Project Conductor, Architecture Baseline | Policy, secrets, permissioning, compliance, governance categories | P0 | WP-003K | Ready for discovery framing |
| TD-BL-015 | Enterprise AI Platform | AI Gateway, Model Providers, Security and Governance | Azure AI Foundry, enterprise platform categories | P2 | WP-003E or WP-003J | Watch |

## Backlog Rules

- Backlog priority reflects discovery sequencing, not technology value.
- Candidate lists are starting points, not approved evaluation scope.
- Any new candidate must map to a capability area before evaluation.
- Agent framework discovery remains blocked until gateway, tool, context, memory, evaluation, and observability decisions are mature enough.

## Missing Capability Review

Every platform capability from the Master Capability Roadmap has a corresponding discovery path:

- Project Conductor and Programme Management are covered by governance tooling and repository quality discovery through WP-003K and future WP-004.
- Technology Radar is covered by WP-003 itself.
- Evaluation Platform is covered by WP-003A.
- Observability is covered by WP-003B.
- Knowledge Platform is covered by WP-003C.
- Prompt Platform is covered by WP-003D.
- Context Engineering Platform is covered by WP-003D.
- Memory Platform is covered by WP-003H.
- Model Providers, Local AI Runtime, AI Gateway, and Model Routing are covered by WP-003E and WP-003F.
- Tool Platform and Browser Platform are covered by WP-003G.
- Agent Platform is covered by WP-003I.
- Artifact Publisher is covered through Observability and Evidence, Knowledge Platform, and future publishing work packages.
- Career Intelligence depends on platform discovery outcomes and does not require a separate technology discovery programme yet.

