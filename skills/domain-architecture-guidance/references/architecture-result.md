# Architecture Guidance Result Protocol

Use this protocol for architecture decisions, reviews, and boundary-affecting implementation recommendations. Consume an applicable `Domain Modeling Result` when one exists; otherwise use explicit project evidence. Only confirmed domain decisions or explicitly accepted assumptions may drive architecture decisions. Do not presume that domain modeling is complete. Keep domain assumptions and decisions distinct from architecture choices, framework conventions, heuristics, and project policies.

## Required Shape

Return the architecture result with this shared envelope:

- **Phase**: `Architecture Guidance`
- **Status**: `completed`, `needs-input`, or `not-applicable`
- **Inputs**
- **Summary**
- **Assumptions**
- **Decisions**
- **Constraints**
- **Evidence**
- **Open Questions**
- **Artifacts**
- **Recommended Next Step**
- **Handoff Notes**

The shared envelope fields are required. Include only applicable Architecture Analysis fields; for a narrow review, omit irrelevant candidate styles, CQRS, integration/read-model, and framework sections rather than filling them speculatively.

**Architecture Analysis:**

- **Task and system context**
- **Consumed Domain Decisions**
  - **Modeling scope/depth**
  - **Subdomains / Bounded Contexts**
  - **Context relationships**
  - **Rules / lifecycle / consistency needs**
  - **Evidence state or accepted assumption**
    - **Acceptance source/evidence** (required for an accepted assumption)
- **Domain model complexity**
- **Architecture complexity**
- **Existing or claimed architecture**
- **Candidate styles or simpler alternatives**
- **Selected, preserved, and rejected choices**
- **Decision rationale**
- **Rule source levels**
- **Dependency direction**
- **Responsibility boundaries**
- **Command/query implications**
- **Transaction/consistency implications**
- **Integration/read-model implications**
- **Ecosystem mapping**
- **Application runtime integration policy**
- **Validation rules**
- **Documented exceptions/risks**
- **Readiness for framework landing or implementation planning**

The architecture specialist owns the `Architecture Analysis` payload. The coordinator may combine the result with other phase results but should not reinterpret its decisions. Record only the domain decisions needed for this architecture result, preserving their meaning and specialist ownership rather than rewriting the Domain Modeling payload. Trace each affected architecture choice and practical consequence back to a consumed domain decision or explicit project constraint.

An accepted assumption must record its acceptance source/evidence. The architecture agent must not accept an assumption itself or promote its own inference or proposal. Without explicit acceptance, preserve an `inferred` or `proposed` item only as uncertainty in **Open Questions** or **Handoff Notes**.

If a dependent architecture decision cannot responsibly be completed without that item, set only the dependent Architecture Guidance result to `needs-input`, preserve unaffected architecture conclusions, and route the smallest blocking business question to Domain Modeling. Do not change the Domain Modeling result or treat unrelated work as blocked.

If an architecture proposal would change business meaning or ownership, including Subdomain scope, Bounded Context meaning, context relationships, invariant ownership, lifecycle, Aggregate boundaries, or Domain Events, return that issue to Domain Modeling. Preserve architecture conclusions that do not depend on the unresolved modeling issue.

When an application runtime is selected, the **Application runtime integration policy** records only
the decisions needed by the increment: composition-root ownership or its deliberate absence,
global cross-cutting concerns, adapter-local protocol mappings, allowed dependency direction, and
documented exceptions. Treat package names such as `boot`, `bootstrap`, and `runtime` as project
conventions, not as architecture rules.

Tie evidence to project artifacts, confirmed domain results, and applicable sources. Record affected boundaries and the practical consequence of each decision.

## Decision Discipline

Classify every strong rule by its source level: **DDD core discipline**, **architecture constraint from the selected architecture**, **framework convention**, **heuristic**, or **project policy**. Read `architecture-constraints.md` for the rules supplied by each architecture and `source-policy.md` for authority and citation guidance; do not duplicate those catalogs here.

- Preserve the selected project architecture unless the task explicitly reconsiders it.
- Record when no strict architecture style is justified and existing or simpler conventions are sufficient.
- Do not force ports, CQRS, Event Sourcing, repositories, or rich DDD where the context does not justify them.
- Keep CQRS separate from Event Sourcing.
- Keep DDD modeling discipline distinct from structural rules introduced by a selected architecture.
- Label framework and ecosystem translations as implementation guidance rather than universal architecture rules.

## Phase-Local Status

Use `needs-input` only for the dependent Architecture Guidance result when unresolved architecture-owned facts or required business facts prevent a responsible result. This includes an unaccepted `inferred` or `proposed` domain item on which a required architecture decision depends. Route the smallest blocking question to Domain Modeling when it concerns business meaning or ownership, including Subdomain scope, Bounded Context meaning, context relationships, invariants, lifecycle, Aggregate boundaries, or Domain Events. Preserve unaffected architecture conclusions and nonblocking uncertainty in **Open Questions** or **Handoff Notes**.

Use `not-applicable` when no new architecture decision is needed beyond established conventions. Still record the evidence, the affected boundary, and why those conventions are sufficient.

Use `completed` when the architecture result is usable for its recommended next step, including any documented nonblocking risks or questions.
