# WP-010 Prompt: Deterministic Project Conductor MVP Implementation, Sprint 3

## Metadata

| Field | Value |
| --- | --- |
| ID | PROMPT-012 |
| Title | WP-010 Deterministic Project Conductor MVP Implementation, Sprint 3 Prompt |
| Created Date | 2026-06-25 |
| Related Work Packages | WP-010 |

## Prompt

WP-010 Prompt: Deterministic Project Conductor MVP Implementation, Sprint 3

Context:
WP-009 Sprint 2 has been reviewed and approved.

Sprint 2 implemented:
- ArtifactRegistry
- RegistryArtifact
- RegistryValidationReport
- deterministic JSON export
- stable IDs
- fixture tests
- golden output

Chief Architect decision:
Do not persist the registry yet.

Sprint 3 Scope:
Implement Metadata Contract and Registry Schema Hardening.

Purpose:
Before persisting generated registry output, define and enforce the deterministic metadata contract and explicit versioned registry schema.

Allowed scope:
- Define a versioned metadata contract for Markdown artifacts.
- Define required metadata fields.
- Define optional metadata fields.
- Define allowed metadata status values.
- Define artifact ID rules:
  - metadata-backed artifacts use artifact_id = metadata:<ID>
  - metadata-free artifacts use artifact_id = path:<sha1>
  - metadata_id remains the raw metadata ID value.
- Define which artifact classes are durable registry authorities.
- Keep metadata-free artifacts discoverable.
- Mark metadata-free artifacts as non-durable unless explicitly allowed.
- Define explicit registry schema document.
- Add schema validation logic using standard library only unless already approved otherwise.
- Update registry model if needed.
- Update tests and golden output.
- Add negative tests for invalid metadata.
- Add compatibility note for Sprint 2 registry output.
- Generate Sprint 3 review bundle.

Forbidden scope:
- No database.
- No generated registry persistence.
- No Git enrichment.
- No quality gates workflow.
- No AI.
- No LangGraph.
- No MCP.
- No AI Gateway.
- No Prompt Platform.
- No Context Platform.
- No Knowledge Platform.
- No Browser Automation.
- No agents.

Required deliverables:
- Sprint design
- Technical design
- Metadata contract document
- Registry schema document
- Implementation updates
- Unit tests
- Integration tests
- Golden output update
- Evidence package
- Architecture review package
- Code review package
- Sprint report
- Architecture checklist
- Suggested git commit message
- Suggested pull request description
- Questions requiring Chief Architect review

Stop after Sprint 3.

Do not continue to Sprint 4.

