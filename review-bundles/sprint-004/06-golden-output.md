# Sprint 4 Golden Output

Source file: `tests/fixtures/repository-scanner/expected-repository-state.json`

```json
{
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
  "generator": {
    "generated_at": "1970-01-01T00:00:00Z",
    "name": "project-conductor-repository-state-builder",
    "version": "0.1.0"
  },
  "metadata": {
    "complete_count": 1,
    "durable_artifact_count": 1,
    "incomplete_count": 0,
    "metadata_backed_artifact_count": 1,
    "metadata_free_artifact_count": 1,
    "missing_count": 1,
    "non_durable_artifact_count": 1
  },
  "registry_validation": {
    "errors": [],
    "valid": true,
    "warnings": [
      "artifact 'docs/no-metadata.md' metadata_status is missing"
    ]
  },
  "repository": {
    "artifact_count": 2,
    "durable_artifact_count": 1,
    "problem_count": 1,
    "source_provider": "filesystem"
  },
  "statistics": {
    "artifact_count": 2,
    "artifact_types": [
      {
        "count": 1,
        "key": "documentation"
      },
      {
        "count": 1,
        "key": "repository"
      }
    ],
    "durable_artifact_count": 1,
    "metadata_backed_artifact_count": 1,
    "metadata_free_artifact_count": 1,
    "metadata_statuses": [
      {
        "count": 1,
        "key": "complete"
      },
      {
        "count": 1,
        "key": "missing"
      }
    ]
  },
  "validation": {
    "errors": [],
    "valid": true,
    "warnings": [
      "repository state includes 1 artifact problem(s)",
      "artifact 'docs/no-metadata.md' metadata_status is missing"
    ]
  },
  "validation_summary": {
    "error_count": 0,
    "valid": true,
    "warning_count": 1
  },
  "version": {
    "metadata_contract_version": "1.0.0",
    "registry_schema_version": "1.0.0",
    "registry_version": "0.2.0",
    "repository_state_version": "0.1.0"
  }
}
```
