# Suggested Pull Request Description

## Summary

Implements WP-010 Sprint 3 of the deterministic Project Conductor MVP: Metadata Contract and Registry Schema Hardening.

## Scope

- Adds versioned metadata contract.
- Adds explicit registry schema documentation.
- Updates registry model with schema and contract versions.
- Updates artifact ID rules to `metadata:<ID>` and `path:<sha1>`.
- Adds durable registry authority rules.
- Updates validation logic and golden output.
- Adds negative validation tests.
- Adds corrected minimal Chief Architect review bundle.

## Out Of Scope

- Registry persistence.
- Database.
- Git enrichment.
- Quality gates.
- AI, LangGraph, MCP, AI Gateway, Prompt Platform, Context Platform, Knowledge Platform, Browser Automation, or agents.

## Verification

```text
PYTHONPATH=src python3 -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=src python3 -m trace --count --summary --coverdir /private/tmp/pgv2-trace --module unittest discover -s tests -p 'test_*.py'
```
