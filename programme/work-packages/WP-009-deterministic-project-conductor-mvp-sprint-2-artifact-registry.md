# WP-009 Deterministic Project Conductor MVP Sprint 2 Artifact Registry Model

## Metadata

| Field | Value |
| --- | --- |
| ID | WP-009 |
| Title | Deterministic Project Conductor MVP Sprint 2 Artifact Registry Model |
| Version | 0.1.0 |
| Status | Sprint 2 Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008, PC-S1-REPORT, ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008, WP-009 |
| Tags | project-conductor, implementation, deterministic-mvp, sprint-002, artifact-registry |
| Review Date | 2026-07-02 |

## Objective

Implement Sprint 2 only: the Artifact Registry Model that converts Repository Discovery Capability, Filesystem Provider output into a deterministic registry representation future Project Conductor capabilities can consume.

## Sprint 1 Review Conditions Applied

| Condition | Status |
| --- | --- |
| Remove `.venv/`, `__MACOSX/`, `.DS_Store`, and `__pycache__/` noise. | Complete |
| Do not remove actual working `.git/` repository metadata. | Complete |
| Update `.gitignore` to prevent recurring packaged/cache noise. | Complete |
| Update Sprint 1 documentation language to Repository Discovery Capability, Filesystem Provider. | Complete |
| Avoid changing Sprint 1 runtime behavior except for hygiene. | Complete |

## Scope

In scope:

- `ArtifactRegistry` data model.
- `RegistryArtifact` data model.
- Conversion from `RepositoryScan` to registry entries.
- Deterministic ordering.
- Stable artifact IDs.
- Path, type, title, hash, metadata status, problems, and source provider.
- Deterministic JSON export.
- Registry structure validation.
- Validation report.
- Unit tests.
- Integration tests using the existing fixture repository.
- Golden expected JSON output.
- Sprint 2 documentation, evidence, and review package.

Out of scope:

- Database.
- Registry persistence beyond deterministic JSON export and test golden output.
- Git enrichment.
- Quality gates.
- AI, LangGraph, MCP, AI Gateway, Prompt Platform, Context Platform, Knowledge Platform, Browser Automation, or agents.
- Sprint 3 work.

## Deliverables

| Deliverable | Artifact | Status |
| --- | --- | --- |
| Sprint design | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/sprint-design.md` | Complete for Review |
| Technical design | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/technical-design.md` | Complete for Review |
| Implementation | `src/project_conductor/registry.py` | Complete for Review |
| Tests | `tests/project_conductor_tests/test_registry.py` | Complete for Review |
| Fixture updates | `tests/fixtures/repository-scanner/expected-artifact-registry.json` | Complete for Review |
| Evidence package | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/evidence/` | Complete for Review |
| Architecture review package | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/review/architecture-review-package.md` | Complete for Review |
| Code review package | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/review/code-review-package.md` | Complete for Review |
| Sprint report | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/sprint-report.md` | Complete for Review |
| Architecture checklist | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/review/architecture-review-checklist.md` | Complete for Review |
| Suggested commit message | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/review/suggested-git-commit-message.md` | Complete for Review |
| Suggested PR description | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/review/suggested-pull-request-description.md` | Complete for Review |
| Chief Architect questions | `programme/work-packages/project-conductor-sprints/sprint-002-artifact-registry/review/chief-architect-questions.md` | Complete for Review |

## Acceptance Status

| Criterion | Status |
| --- | --- |
| Registry model converts `RepositoryScan` into deterministic registry entries. | Passed |
| Registry entries preserve required fields. | Passed |
| Stable artifact IDs are generated. | Passed |
| Registry JSON is deterministic and compared to golden output. | Passed |
| Registry structure validation report exists. | Passed |
| Unit and integration tests pass locally. | Passed |
| No forbidden capabilities were implemented. | Passed |

## Stop Point

Sprint 2 is complete for review.

Do not continue to Sprint 3 until Chief Architect review accepts this slice.

