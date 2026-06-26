# Sprint 3 Example Execution

## Command

```text
PYTHONPATH=src python3 -m project_conductor.cli --root tests/fixtures/repository-scanner/basic-repo --registry-json
```

## Output

```json
{
  "artifact_count": 2,
  "artifacts": [
    {
      "artifact_id": "metadata:FIXTURE-001",
      "durable": true,
      "hash": "ce66feadc5372b565dfd32e002ae98c7788c5ec223d02b1a000af444cf998242",
      "metadata_id": "FIXTURE-001",
      "metadata_status": "complete",
      "path": "README.md",
      "problems": [],
      "source_provider": "filesystem",
      "title": "Fixture Repository",
      "type": "repository"
    },
    {
      "artifact_id": "path:ce3a89079780",
      "durable": false,
      "hash": "b47ab94694f21363850d9da2c618e9798f7562b9c2bb00b3ba5d8430d852cccf",
      "metadata_id": null,
      "metadata_status": "missing",
      "path": "docs/no-metadata.md",
      "problems": [
        "metadata section not found"
      ],
      "source_provider": "filesystem",
      "title": "No Metadata",
      "type": "documentation"
    }
  ],
  "metadata_contract_version": "1.0.0",
  "registry_schema_version": "1.0.0",
  "registry_version": "0.2.0",
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
