# WP-009 Prompt: Deterministic Project Conductor MVP Implementation, Sprint 2

## Metadata

| Field | Value |
| --- | --- |
| ID | PROMPT-011 |
| Title | WP-009 Deterministic Project Conductor MVP Implementation, Sprint 2 Prompt |
| Created Date | 2026-06-25 |
| Related Work Packages | WP-009 |

## Prompt

WP-009 Prompt: Deterministic Project Conductor MVP Implementation, Sprint 2

Context:
WP-008 Sprint 1 has been reviewed and approved with conditions.

Sprint 1 implemented the Repository Discovery Capability, Filesystem Provider.

Before beginning Sprint 2, first apply Sprint 1 review conditions:

1. Remove packaged noise from the repository:

   * .venv/
   * .git/ if accidentally included in delivery archive
   * __MACOSX/
   * .DS_Store
   * **pycache**/

2. Update .gitignore to prevent these from recurring.

3. Update Sprint 1 documentation language so the capability is described as:
   Repository Discovery Capability, Filesystem Provider.

Do not change Sprint 1 runtime behavior unless required for hygiene.

Sprint 2 Scope:
Implement the Artifact Registry Model.

Purpose:
Convert the in-memory RepositoryScan output from Sprint 1 into a deterministic Artifact Registry representation that future Project Conductor capabilities can consume.

Allowed scope:

* Define ArtifactRegistry data model.
* Define RegistryArtifact data model.
* Convert RepositoryScan artifacts into registry entries.
* Preserve deterministic ordering.
* Generate stable artifact IDs.
* Include path, type, title, hash, metadata status, problems, and source provider.
* Export registry to deterministic JSON.
* Validate registry structure.
* Produce validation report.
* Add unit tests.
* Add integration tests using the existing fixture repository.
* Add golden expected JSON output.
* Generate Sprint 2 documentation, evidence, and review packages.

Forbidden scope:

* No database.
* No registry persistence beyond deterministic JSON export.
* No Git enrichment.
* No quality gates.
* No AI.
* No LangGraph.
* No MCP.
* No AI Gateway.
* No Prompt Platform.
* No Context Platform.
* No Knowledge Platform.
* No Browser Automation.
* No agents.

Required deliverables:

* Sprint design
* Technical design
* Implementation
* Tests
* Fixture updates
* Golden output
* Evidence package
* Architecture review package
* Code review package
* Sprint report
* Architecture checklist
* Suggested git commit message
* Suggested pull request description
* Questions requiring Chief Architect review

Stop after Sprint 2.

Do not continue to Sprint 3.

