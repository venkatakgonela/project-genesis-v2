# Sprint 3 Test Results

## Metadata

| Field | Value |
| --- | --- |
| ID | PC-S3-EVD-TESTS |
| Title | Sprint 3 Test Results |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-010 |
| Related ADRs | ADR-DRAFT-014, ADR-DRAFT-015 |
| Related Work Packages | WP-010 |
| Tags | evidence, tests, metadata-contract, registry-schema |
| Review Date | 2026-07-02 |

## Test Command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'
```

## Result

```text
...............
----------------------------------------------------------------------
Ran 15 tests in 0.106s

OK
```

## Sprint 3 Test Additions

| Behavior | Test |
| --- | --- |
| Metadata contract exposes required and optional fields. | `ArtifactRegistryTests.test_metadata_contract_exposes_required_and_optional_fields` |
| Invalid metadata status fails validation. | `ArtifactRegistryTests.test_validation_detects_invalid_metadata_status` |
| Metadata-backed ID missing `metadata:` prefix fails validation. | `ArtifactRegistryTests.test_validation_detects_unprefixed_metadata_artifact_id` |
| Metadata-free durable artifact fails validation. | `ArtifactRegistryTests.test_validation_rejects_metadata_free_durable_artifact` |

