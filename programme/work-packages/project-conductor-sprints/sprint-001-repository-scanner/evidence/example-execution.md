# Sprint 1 Example Execution

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S1-EVD-EXAMPLE |
| Title | Sprint 1 Example Execution |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-008 |
| Related ADRs | ADR-DRAFT-013, ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-008 |
| Tags | evidence, example-execution, repository-scanner |
| Review Date | 2026-07-02 |

## Fixture JSON Execution

Command:

```bash
PYTHONPATH=src python3 -m project_conductor.cli --root tests/fixtures/repository-scanner/basic-repo --json
```

Result excerpt:

```json
{
  "artifact_count": 2,
  "metadata_count": 1,
  "problem_count": 1,
  "artifacts": [
    {
      "path": "README.md",
      "artifact_type": "repository",
      "title": "Fixture Repository",
      "has_metadata": true
    },
    {
      "path": "docs/no-metadata.md",
      "artifact_type": "documentation",
      "title": "No Metadata",
      "has_metadata": false
    }
  ]
}
```

## Repository Smoke Execution

Command:

```bash
PYTHONPATH=src python3 -m project_conductor.cli --root .
```

Result before documentation package finalization:

```text
Repository root: /Users/kirangonela/code/project-genesis-v2
Artifacts discovered: 178
Artifacts with metadata: 142
Scan problems: 45
```

The repository smoke count is not used as a stable acceptance value because adding review and evidence documentation changes the number of discovered Markdown artifacts.

