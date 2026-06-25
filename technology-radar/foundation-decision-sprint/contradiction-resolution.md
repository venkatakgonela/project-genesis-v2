# Contradiction Resolution

## Metadata

| Field | Value |
| --- | --- |
| ID | FTD-013 |
| Title | Contradiction Resolution |
| Version | 0.1.0 |
| Status | Complete for Review |
| Owner | Chief Architect |
| Created Date | 2026-06-25 |
| Updated Date | 2026-06-25 |
| Dependencies | FTD-008, FTD-009, FTD-010, FTD-011 |
| Related ADRs | ADR-002, ADR-DRAFT-017, ADR-DRAFT-018, ADR-DRAFT-019, ADR-DRAFT-020, ADR-DRAFT-021, ADR-DRAFT-022 |
| Related Work Packages | WP-005 |
| Tags | project-conductor, contradiction-resolution, scope |
| Review Date | 2026-07-02 |

## Question

Was excluding Agent Framework, AI Gateway, and related agentic technologies from WP-005 correct?

## Correct for deterministic MVP?

Yes.

For the deterministic Project Conductor MVP, excluding Agent Framework, AI Gateway, model providers, prompt/context tooling, browser automation, and deployment platform was correct.

The deterministic MVP needs to parse artifacts, build indexes, validate metadata, generate quality reports, and produce review/dashboard outputs. None of that requires agent orchestration or model access.

## Correct for full Project Conductor vision?

No.

The full Project Conductor vision includes assisted and agentic coordination: prompt and context package generation, model-assisted reasoning, implementation handoff, review routing, ADR alignment support, human approval, checkpointed workflows, and future multi-agent coordination.

Those capabilities require technology decisions beyond WP-005A-D.

## Required correction?

Yes.

WP-005A-D should remain unchanged as deterministic substrate work packages.

WP-005 must be extended with agentic decision work packages, sequenced after the deterministic substrate.

## Recommended updated scope

WP-005 should cover:

- WP-005A-D for Layer 0 deterministic Project Conductor MVP.
- WP-005G, WP-005F, and WP-005H for Layer 1 assisted Project Conductor.
- WP-005I, WP-005E, and WP-005J for Layer 2 agentic Project Conductor.
- Layer 3 multi-agent coordination should remain deferred until Layer 2 is proven.

## Final Resolution

The earlier exclusion was not wrong; it was incomplete.

It was correct for the first implementation slice and incorrect as a statement about the full Project Conductor vision.

