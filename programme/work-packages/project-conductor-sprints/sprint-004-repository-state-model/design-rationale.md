# Sprint 4 Design Rationale

## Decisions

- Use frozen dataclasses for immutable domain objects.
- Build state solely from ArtifactRegistry.
- Include artifacts in RepositoryState so downstream capabilities receive a canonical current-state snapshot.
- Keep validation structural and defer quality gate interpretation.
- Use deterministic generated timestamp by default.

## Alternatives Considered

| Alternative | Reason Deferred |
| --- | --- |
| Persist Repository State to disk | Sprint 4 explicitly forbids persistence. |
| Use current wall-clock time | Breaks byte-for-byte determinism. |
| Add JSON Schema library | Adds dependency and belongs after schema review. |
| Add Git branch or commit metadata | Sprint 4 forbids Git and branch awareness. |
