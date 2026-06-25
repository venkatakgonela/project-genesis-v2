# ADR-DRAFT-022: MCP and Tool Runtime Strategy

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-DRAFT-022 |
| Title | MCP and Tool Runtime Strategy |
| Version | 0.1.0 |
| Status | Draft |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | WP-005J, ADR-009, ADR-DRAFT-017 |
| Related ADRs | ADR-009 |
| Related Work Packages | WP-005, WP-005J |
| Tags | adr-draft, project-conductor, mcp, tool-runtime |
| Review Date | 2026-07-30 |

## Context

Agentic Project Conductor may need governed tool access for repository inspection, evidence capture, review routing, and future multi-agent coordination.

## Decision Question

What MCP and tool runtime strategy should Project Conductor use for governed tool invocation?

## Candidate Options

- MCP.
- ToolHive or equivalent managed tool runtime.
- Direct local command tools.
- Repository-specific tool registry.
- Agent framework-native tool adapters.

## Evidence Required

- Tool invocation scenario analysis.
- Permission and security model.
- Evidence capture requirements.
- Integration with Project Conductor registry.
- Operational and migration risk analysis.

## Draft Recommendation

No final MCP or tool runtime selection yet.

Complete WP-005J before promoting this ADR.

