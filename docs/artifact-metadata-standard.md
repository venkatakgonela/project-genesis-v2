# Artifact Metadata Standard

## Metadata

| Field | Value |
| --- | --- |
| ID | DOC-001 |
| Title | Artifact Metadata Standard |
| Version | 0.1.0 |
| Status | Approved for Bootstrap |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | None |
| Related ADRs | ADR-000 |
| Related Work Packages | WP-001 |
| Tags | governance, metadata, artifacts |
| Review Date | 2026-07-09 |

## Purpose

This standard defines the common metadata block used by Project Genesis V2 engineering artifacts where metadata adds value.

## Required Fields

Use this metadata format for artifacts that carry decisions, plans, specifications, evidence, reviews, or reusable knowledge.

| Field | Meaning |
| --- | --- |
| ID | Stable identifier, unique within artifact type. |
| Title | Human-readable artifact name. |
| Version | Semantic document version. |
| Status | Lifecycle state. |
| Owner | Accountable role or person. |
| Created Date | Date first created. |
| Updated Date | Date last materially changed. |
| Dependencies | Artifact, capability, or decision dependencies. |
| Related ADRs | ADRs that justify or constrain the artifact. |
| Related Work Packages | Work packages that create or modify the artifact. |
| Tags | Searchable labels. |
| Review Date | Next scheduled review date. |

## Status Values

Recommended status values:

- Idea
- Research
- Draft
- Proposed
- Approved for Bootstrap
- Approved
- Implementation Ready
- In Implementation
- Evaluation
- In Review
- Published
- Superseded
- Deprecated

## Usage Guidance

Do not force metadata onto tiny index files, generated outputs, or short notes where it adds no value. When in doubt, include metadata for artifacts that will be referenced by future work packages or ADRs.

