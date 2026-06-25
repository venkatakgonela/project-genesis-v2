# Sprint 2 Example Execution

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S2-EVD-EXAMPLE |
| Title | Sprint 2 Example Execution |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-009 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-009 |
| Tags | evidence, example-execution, artifact-registry |
| Review Date | 2026-07-02 |

## Registry JSON Execution

Command:

```bash
PYTHONPATH=src python3 -m project_conductor.cli --root tests/fixtures/repository-scanner/basic-repo --registry-json
```

Result excerpt:

```json
{
  "artifact_count": 2,
  "registry_version": "0.1.0",
  "source_provider": "filesystem",
  "validation": {
    "errors": [],
    "valid": true,
    "warnings": [
      "artifact 'docs/no-metadata.md' metadata_status is missing"
    ]
  }
}
```

## Golden Output

The full expected output is stored at:

`tests/fixtures/repository-scanner/expected-artifact-registry.json`

