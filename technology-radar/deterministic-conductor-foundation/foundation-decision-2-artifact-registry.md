# Foundation Decision 2: Artifact Registry

## Metadata

| Field | Value |
| --- | --- |
| ID | DCF-002 |
| Title | Artifact Registry Decision Report |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-007, WP-005B, DOC-001, BASE-002, PC-PROD-001 |
| Related ADRs | ADR-DRAFT-014 |
| Related Work Packages | WP-007, WP-005B |
| Tags | project-conductor, artifact-registry, metadata |
| Review Date | 2026-07-02 |

## Decision Question

What artifact metadata and registry strategy should deterministic Project Conductor parse and validate?

## Deterministic MVP Need

The registry must identify repository artifacts, read their metadata state, connect artifacts to capabilities, ADRs, work packages, reviews, and evidence, and produce machine-readable outputs without forcing a broad migration of existing Markdown artifacts.

## Comparison Matrix

| Option | Purpose | Architectural Fit | Product Fit | Simplicity | Extensibility | Operational Complexity | Community Maturity | Sustainability | Learning Value | Interview Value | Migration Risk | Cost | Dependencies | Risks | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Existing Markdown metadata tables | Preserve current authoring model. | High | Medium | High | Medium | Low | Medium | Medium | Medium | Medium | Low | Low | Markdown parser or controlled parser | Table parsing can be brittle unless the contract is strict. | DOC-001 and current artifacts. |
| YAML front matter | Structured metadata embedded in Markdown. | High | High | Medium | High | Medium | High | High | High | High | High | Low | YAML parser | Requires artifact migration and author retraining. | YAML spec, WP-005B. |
| TOML front matter | Structured metadata with stricter syntax than YAML. | Medium | Medium | Medium | Medium | Medium | Medium | Medium | Medium | Medium | High | Low | TOML parser | Less common in Markdown content workflows. | WP-005B. |
| Sidecar YAML or TOML manifests | Separate metadata from Markdown body. | Medium | Medium | Medium | High | Medium | High | Medium | Medium | Medium | Medium | Low | YAML/TOML parser | Drift risk between artifact and sidecar manifest. | WP-005B. |
| Generated JSON registry | Machine-readable normalized registry output. | High | High | High | High | Low | High | High | High | High | Low | Low | JSON support | Must not become hand-edited source of truth. | Python JSON docs, WP-005C. |
| SQLite registry | Queryable local state store. | Medium | Medium | Medium | High | Medium | High | High | High | High | Medium | Low | SQLite | Overpowered for MVP registry authoring; binary state less reviewable. | SQLite docs, WP-005C. |
| Hybrid Markdown source plus generated JSON registry | Preserve current authoring and produce structured machine output. | High | High | High | High | Low | High | High | High | High | Low | Low | Markdown extraction, JSON, optional schema validation | Requires strict source contract and generation discipline. | Current repo, DOC-001, BASE-002, PC-PROD-001. |

## Strengths

- The current repository already uses consistent Markdown metadata tables.
- Preserving Markdown tables avoids migration churn before implementation.
- Generated JSON gives Project Conductor a deterministic machine-readable artifact registry.
- The hybrid model keeps human authoring and machine consumption separate.
- A strict metadata table contract can be validated incrementally.

## Weaknesses

- Markdown tables are less inherently structured than front matter.
- Without a strict contract, small formatting variations may break extraction.
- Generated JSON adds an output artifact that must be clearly marked generated.
- YAML front matter may be a better long-term authoring format but would cause migration before the MVP proves value.

## Risks

| Risk | Mitigation |
| --- | --- |
| Metadata table drift across artifacts. | Define a strict MVP metadata table contract based on DOC-001 required fields. |
| Generated registry becomes manually edited. | Mark generated outputs as derived and regenerate them deterministically. |
| Future front matter migration becomes harder. | Keep normalized registry schema independent of source authoring format. |
| Registry omits important non-metadata relationships. | Include source links, related ADRs, work packages, dependencies, tags, review dates, and artifact type. |

## Recommendation

Use a hybrid strategy:

- Keep the existing Markdown metadata table as the MVP authoring source.
- Define a stricter Project Genesis metadata table contract using DOC-001 fields.
- Generate a structured JSON artifact registry from Markdown artifacts.
- Treat generated JSON as machine-readable derived state, not hand-authored source truth.
- Defer YAML or TOML front matter migration until deterministic MVP behavior is proven.
- Defer SQLite as an artifact registry store until query scale or dashboard needs exceed generated JSON.

## Rationale

This recommendation respects the repository as the source of truth and avoids a broad migration before Project Conductor exists. It gives deterministic Project Conductor enough structure for registry generation, traceability, quality gates, and review queues while preserving human-readable Markdown artifacts.

The normalized JSON registry creates a future migration path. If YAML front matter becomes desirable later, the source format can change while the normalized registry contract remains stable.

## Supporting Evidence

| Evidence Type | Evidence |
| --- | --- |
| Repository evidence | Current durable artifacts use Markdown metadata tables shaped by DOC-001. |
| Product evidence | PC-PROD-001 requires artifact metadata state, work package mapping, evidence tracking, and review queues. |
| Architecture evidence | ARCH-SPEC-001 defines Artifact Registry, Work Package Registry, Review Queue, and Evidence Index as Project Conductor interfaces. |
| Baseline evidence | BASE-002 identifies authoritative artifacts and supports source-of-truth traceability. |
| External evidence | JSON is broadly supported by standard tooling; YAML and CommonMark have formal specifications, but front matter migration is not required for the deterministic MVP. |

## Draft ADR Recommendation

Update ADR-DRAFT-014 to recommend current Markdown metadata tables as the MVP authoring source and generated JSON as the normalized registry output.

ADR-DRAFT-014 should explicitly defer YAML front matter migration, sidecar manifests, and SQLite registry storage until the deterministic MVP proves its registry contract and query needs.

