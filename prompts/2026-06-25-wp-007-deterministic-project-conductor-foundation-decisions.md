# PROJECT GENESIS V2

## WP-007 – Deterministic Project Conductor Foundation Decisions

### Context

WP-001 through WP-006 have been completed.

The Engineering Operating System, architecture baseline, capability model, dependency graph, technology discovery programme, product definition, and operating model now exist.

Project Conductor has been formally defined as a product.

The Product Definition clearly establishes four maturity horizons:

* Deterministic MVP
* Assisted Conductor
* Agentic Conductor
* Multi-Agent Conductor

The Deterministic MVP is the first implementation target.

The purpose of WP-007 is to make the minimum set of engineering decisions required to implement the Deterministic MVP.

This work package does **not** evaluate technologies required only for the Assisted, Agentic, or Multi-Agent horizons.

---

# Objective

Produce evidence-based engineering recommendations for the deterministic Project Conductor foundation.

These recommendations should directly support implementation of the Deterministic MVP defined in the Project Conductor Product Definition.

Implementation remains blocked until these recommendations have been reviewed.

---

# Source of Truth

Treat the following artifacts as authoritative:

* Architecture Baseline
* Capability Map
* Capability Dependency Graph
* Project Conductor Architecture Specification
* Project Conductor Product Definition and Operating Model
* Technology Discovery Programme
* WP-005A through WP-005D
* Authoritative Artifact Register

Do not recreate these artifacts.

Do not redesign the architecture.

---

# Scope

Evaluate only technologies required for the Deterministic MVP.

Do not evaluate technologies that support only:

* Assisted Conductor
* Agentic Conductor
* Multi-Agent Conductor

Those remain deferred.

---

# Foundation Decision 1 – Repository Runtime

Evaluate approaches for implementing the deterministic Project Conductor runtime.

Examples may include:

* Python
* Typer
* Rich
* Pydantic
* uv

Focus on maintainability, portability, testing, packaging, developer experience, and long-term sustainability.

---

# Foundation Decision 2 – Artifact Registry

Evaluate strategies for storing and indexing repository artifacts.

Examples may include:

* Markdown front matter
* YAML metadata
* JSON manifests
* SQLite
* Hybrid approaches

Determine which approach best supports repository awareness, traceability, and future evolution.

---

# Foundation Decision 3 – Repository State Engine

Evaluate strategies for determining repository state.

Consider:

* File system scanning
* Git history
* Incremental indexing
* Content hashing
* Change detection

Recommend an architecture suitable for deterministic operation.

---

# Foundation Decision 4 – Quality Gates

Evaluate approaches for repository quality validation.

Examples:

* Markdown validation
* Metadata validation
* Link validation
* Repository consistency
* Architecture rule validation
* Naming validation
* Dependency validation

Recommend a quality gate strategy appropriate for Project Genesis.

---

# Evaluation Framework

For every candidate technology or approach evaluate:

* Purpose
* Architectural Fit
* Product Fit
* Simplicity
* Extensibility
* Operational Complexity
* Community Maturity
* Long-term Sustainability
* Learning Value
* Interview Value
* Migration Risk
* Cost
* Dependencies
* Risks
* Supporting Evidence

Avoid popularity-based recommendations.

Ground recommendations in the Project Conductor product definition.

---

# Decision Output

For each Foundation Decision produce:

* Comparison Matrix
* Strengths
* Weaknesses
* Risks
* Recommendation
* Rationale
* Supporting Evidence
* Draft ADR Recommendation

Do not approve ADRs.

---

# Cross-Decision Review

After completing all evaluations:

Verify that the selected approaches work together coherently.

Identify any conflicts between recommendations.

Recommend any adjustments required to maintain architectural consistency.

---

# Readiness Assessment

Determine whether sufficient engineering evidence now exists to begin implementation of the Deterministic Project Conductor MVP.

If not, identify precisely what evidence is still missing.

---

# Constraints

Do not implement code.

Do not generate Python.

Do not generate FastAPI.

Do not implement Project Conductor.

Do not evaluate LangGraph, Microsoft Agent Framework, AI Gateway, MCP, Browser Automation, or Multi-Agent technologies in this work package unless they are proven to be direct dependencies of the Deterministic MVP.

Remain aligned with the Product Definition and Operating Model.

---

# Deliverables

Produce:

1. Foundation Decision Reports (1–4)
2. Comparison Matrices
3. Evidence Summaries
4. Draft ADR Recommendations
5. Cross-Decision Consistency Review
6. Deterministic MVP Readiness Report

---

# Final Self Review

Before completing:

* Verify every recommendation directly supports the Deterministic MVP.
* Verify no deferred agentic technologies have been evaluated unnecessarily.
* Verify recommendations remain architecture-first and evidence-based.
* Verify all outputs are traceable to existing repository artifacts.

The goal is to produce the minimum set of engineering decisions required to confidently begin implementation of the Deterministic Project Conductor MVP.
