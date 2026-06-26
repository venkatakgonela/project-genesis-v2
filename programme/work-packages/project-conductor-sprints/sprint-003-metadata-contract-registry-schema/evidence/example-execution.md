# Sprint 3 Example Execution

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S3-EVD-EXAMPLE |
| Title | Sprint 3 Example Execution |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-010 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-010 |
| Tags | evidence, example-execution, registry-schema |
| Review Date | 2026-07-02 |

## Command

```bash
PYTHONPATH=src python3 -m project_conductor.cli --root tests/fixtures/repository-scanner/basic-repo --registry-json
```

## Result Excerpt

```json
{
  "registry_version": "0.2.0",
  "registry_schema_version": "1.0.0",
  "metadata_contract_version": "1.0.0",
  "artifact_count": 2,
  "artifacts": [
    {
      "artifact_id": "metadata:FIXTURE-001",
      "metadata_id": "FIXTURE-001",
      "durable": true
    },
    {
      "artifact_id": "path:ce3a89079780",
      "metadata_id": null,
      "durable": false
    }
  ]
}
```

