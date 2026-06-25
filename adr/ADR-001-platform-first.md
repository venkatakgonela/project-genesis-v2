# ADR-001: Platform First

## Metadata

| Field | Value |
| --- | --- |
| ID | ADR-001 |
| Title | Platform First |
| Version | 0.1.0 |
| Status | Proposed |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | PRG-001, ARCH-001 |
| Related ADRs | ADR-011 |
| Related Work Packages | WP-001 |
| Tags | adr, platform |
| Review Date | 2026-07-09 |

## Context

Project Genesis V2 must remain a generic enterprise AI engineering operating system while supporting future business applications such as Career Intelligence.

## Proposed Decision

Platform capabilities will be designed and governed before business application implementation begins. Business applications may depend on platform capabilities; platform capabilities must not depend on business applications.

## Evidence Required

- Capability dependency reviews.
- Architecture reviews confirming dependency direction.
- Work packages linked to platform capability artifacts.

