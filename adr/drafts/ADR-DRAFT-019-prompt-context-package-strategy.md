# ADR-DRAFT-019: Prompt and Context Package Strategy

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-019 |
| Title | Prompt and Context Package Strategy |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005G, ARCH-SPEC-005, ARCH-SPEC-006 |
| Related ADRs | ADR-006, ADR-007 |
| Related Work Packages | WP-005, WP-005G |
| Tags | adr-draft, project-conductor, prompts, context |
| Review Date | 2026-07-16 |

## Context

Assisted Project Conductor needs to generate prompt packages and context packages for Codex, Claude, Gemini, and future model-assisted workflows.

## Decision Question

What prompt and context package format should Project Conductor generate and maintain?

## Candidate Options

- Markdown prompt packages.
- YAML prompt/context manifests.
- JSON context packages.
- Hybrid Markdown plus structured metadata.
- Prompt Platform asset format.
- Context Engineering Platform package format.

## Evidence Required

- Example package structures.
- Source manifest and provenance analysis.
- Model portability analysis.
- Token budget and context quality considerations.
- Migration impact from current artifacts.

## Draft Recommendation

No final package format selection yet.

Complete WP-005G before promoting this ADR.

