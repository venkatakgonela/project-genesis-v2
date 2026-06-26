# Sprint 4 Decision Log

## Architectural Decisions Made

- Repository State is a pure domain object built only from ArtifactRegistry.
- Repository State uses frozen dataclasses for immutability.
- Repository State includes version, generator, repository, statistics, metadata, validation, registry validation, and artifacts.
- Repository State serialization uses sorted JSON keys and a trailing newline.
- Default generated timestamp is deterministic: `1970-01-01T00:00:00Z`.

## Alternatives Considered

| Alternative | Decision |
| --- | --- |
| Persist Repository State now | Deferred. Persistence is Sprint 5 or later. |
| Add Git branch or commit metadata | Rejected for Sprint 4. Git integration is forbidden. |
| Use wall-clock generated timestamp | Rejected because it breaks deterministic output. |
| Add external JSON Schema validation dependency | Deferred pending Chief Architect schema decision. |

## Trade-Offs

- Deterministic timestamp improves reproducibility but does not record execution time.
- Keeping validation structural avoids scope drift but defers quality interpretation.
- Including artifacts in state makes the snapshot self-contained but duplicates registry artifact content.

## ADRs Created Or Updated

None.

## Deferred Decisions

- Machine-readable Repository State JSON Schema.
- Repository Persistence envelope.
- Repository History event format.
- Separation of execution timestamp from deterministic state payload.

## Outstanding Architectural Risks

- Persistence may require a wrapper envelope to preserve deterministic state while recording operational metadata.
- Future schema validation should not introduce nondeterministic ordering or external network dependency.
