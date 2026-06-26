# Sprint 4 Architecture Notes

## Architecture Position

Repository State sits after Artifact Registry and before future Repository Persistence, History, Diff, Quality Gates, Project Conductor workflows, and applications.

## Dependency Rule

Repository State is a pure domain object. It depends on ArtifactRegistry and the standard library only.

## Deterministic Timestamp

The default `generated_at` value is fixed at `1970-01-01T00:00:00Z` so repeated generation is reproducible. A caller may provide a timestamp later if an approved persistence or execution context requires it.

## Architectural Drift

No architectural drift identified. No persistence, history, diff, Git, quality gates, AI, agents, or application capability was introduced.
