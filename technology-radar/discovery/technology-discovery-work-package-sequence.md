# Technology Discovery Work Package Sequence

## Metadata

| Field | Value |
| --- | --- |
| ID | TD-008 |
| Title | Technology Discovery Work Package Sequence |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | TD-001, TD-007, PRG-006, ARCH-004 |
| Related ADRs | ADR-003, ADR-004, ADR-005, ADR-006, ADR-007, ADR-008, ADR-009, ADR-010, ADR-012 |
| Related Work Packages | WP-003 |
| Tags | technology-discovery, work-package-sequence |
| Review Date | 2026-07-02 |

## Purpose

This sequence defines future technology discovery work packages. It follows the Master Capability Roadmap and the Capability Dependency Graph. It does not authorize implementation.

## Work Package Sequence

| ID | Name | Purpose | Dependencies | Expected Deliverables | Definition of Done |
| --- | --- | --- | --- | --- | --- |
| WP-003A | Evaluation Platform Discovery | Establish how evaluation technologies will be evaluated for prompts, retrieval, models, agents, tools, and workflows. | WP-003, ADR-005, ADR-012 | Discovery brief, candidate list, evaluation plan, evidence standard, comparison matrix template. | Evaluation technology discovery is ready to execute without selecting tools. |
| WP-003B | Observability and Evidence Discovery | Define discovery path for trace, metric, log, model interaction, and evidence tooling. | WP-003A, Evidence Storage Standard planning | Discovery brief, observability evidence needs, candidate categories, ADR impact map. | Observability technology evaluation can begin with clear evidence needs. |
| WP-003C | Knowledge Platform, Storage, and Retrieval Discovery | Define discovery path for knowledge storage, retrieval, indexing, and data architecture technologies. | WP-003A, WP-003B, ADR-004 | Discovery brief, storage/retrieval decision questions, candidate categories, retrieval evaluation plan. | Knowledge technology evaluation is scoped without selecting storage. |
| WP-003D | Prompt and Context Engineering Discovery | Define discovery path for prompt asset management, context packaging, and context evaluation technologies. | WP-003A, WP-003C, ADR-006, ADR-007 | Discovery brief, prompt/context criteria, candidate categories, comparison matrix outline. | Prompt and context technology evaluation can proceed after capability architecture review. |
| WP-003E | Model Providers and Local AI Runtime Discovery | Define discovery path for cloud and local model providers and runtime environments. | WP-003A, WP-003B, ADR-010 | Provider evaluation plan, model evaluation criteria, local runtime criteria, cost and lock-in evidence requirements. | Provider and local runtime evaluations are ready without choosing models. |
| WP-003F | AI Gateway and Model Routing Discovery | Define discovery path for gateway patterns, provider abstraction, routing, and API boundary technologies. | WP-003E, WP-003B, ADR-003, ADR-010 | Gateway discovery brief, routing criteria, integration evidence plan, ADR readiness checklist. | AI Gateway technology decisions can be evaluated without implementation. |
| WP-003G | Tool and Browser Platform Discovery | Define discovery path for tool protocols, tool registries, browser automation, safety, and evaluation. | WP-003A, WP-003B, WP-003F, ADR-009 | Tool/browser discovery brief, candidate categories, safety criteria, browser workflow evidence plan. | Tool and browser technology evaluation is scoped. |
| WP-003H | Memory Platform Discovery | Define discovery path for durable memory, memory governance, storage patterns, and evaluation. | WP-003C, WP-003D, ADR-008 | Memory discovery brief, governance criteria, evidence requirements, consolidation recommendation path. | Memory technology evaluation can begin only after memory scope is decided. |
| WP-003I | Agent Framework Discovery | Define discovery path for agent orchestration frameworks after platform boundaries are clear. | WP-003F, WP-003G, WP-003H, ADR-005 | Agent framework discovery brief, orchestration criteria, safety and evaluation requirements, candidate categories. | Agent framework evaluation can proceed without selecting LangGraph or any alternative. |
| WP-003J | Deployment Platform Discovery | Define discovery path for local, CI/CD, infrastructure, and packaging technologies. | WP-003B, WP-003F, Security and Governance discovery | Deployment discovery brief, candidate categories, operational criteria, migration and cost criteria. | Deployment technology evaluation is scoped without production implementation. |
| WP-003K | Security and Governance Discovery | Define discovery path for secrets, permissions, policy, compliance, data governance, and technology risk controls. | WP-003, Architecture Baseline | Security/governance discovery brief, candidate categories, gate criteria, cross-cutting ADR triggers. | Security and governance discovery requirements are available for all later technology evaluations. |

## Dependency Order

```text
WP-003
  -> WP-003A
  -> WP-003B
  -> WP-003C
  -> WP-003D
  -> WP-003E
  -> WP-003F
  -> WP-003G
  -> WP-003H
  -> WP-003I
  -> WP-003J

WP-003K
  -> applies across WP-003A through WP-003J
```

WP-003K should start early because security and governance criteria affect every later technology evaluation.

## Sequencing Notes

- Evaluation Platform discovery comes first because later technology decisions need evaluation methods.
- Observability and evidence discovery comes early because runtime decisions require traceability.
- Knowledge, prompt, context, and memory discovery precede agent framework discovery.
- Model provider and AI Gateway discovery precede agent framework discovery.
- Tool and Browser Platform discovery precede agent framework discovery.
- Deployment discovery remains late because production readiness follows architecture maturity.

## Implementation Guardrail

None of these work packages authorizes implementation. Each produces discovery and evaluation artifacts only.

