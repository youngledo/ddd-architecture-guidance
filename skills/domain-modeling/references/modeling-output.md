# Domain Modeling Result Protocol

Use this protocol before writing production code for a new bounded context, non-trivial use case,
aggregate, domain event, or cross-aggregate workflow. The result exposes business meaning,
assumptions, and readiness for architecture analysis; it is not a large design document.

Return the phase-specific **Domain Model** owned by `domain-modeling` inside the shared result
envelope. Keep the result concise enough for review and downstream architecture mapping.

## Result Shape

Keep the shared envelope unchanged:

```text
Phase: Domain Modeling
Status: completed | needs-input | not-applicable
Inputs:
Summary:
Assumptions:
Decisions:
Constraints:
Evidence:
Open Questions:
Artifacts:
Recommended Next Step:
Handoff Notes:

Domain Model:
  Modeling Scope:
    Decision scope: landscape | bounded-context | increment
    Depth: strategic | tactical | both
    Covered areas:
    Deferred areas:
    Current intent:
    Target intent:

  Domain Landscape:
  - Domain/area:
    Current business capabilities/intent:
    Current status: confirmed | inferred | proposed
    Current evidence:
    Target business capabilities/intent:
    Target status: confirmed | inferred | proposed
    Target evidence:

  Subdomains:
  - Subdomain:
    Current classification, when useful: Core | Supporting | Generic
    Current intent:
    Current status: confirmed | inferred | proposed
    Current evidence:
    Target classification, when useful: Core | Supporting | Generic
    Target intent:
    Target status: confirmed | inferred | proposed
    Target evidence:
    Classification/change rationale:

  Bounded Contexts:
  - Context:
    Current key language/model:
    Current decision and rule ownership:
    Current intent:
    Current status: confirmed | inferred | proposed
    Current evidence:
    Target key language/model:
    Target decision and rule ownership:
    Target intent:
    Target status: confirmed | inferred | proposed
    Target evidence:

  Context Relationships:
  - Contexts:
    Current direction and ownership:
    Current collaboration or governance:
    Current model integration or protection:
    Current exchanged business meaning/facts:
    Current intent:
    Current status: confirmed | inferred | proposed
    Current evidence:
    Target direction and ownership:
    Target collaboration or governance:
    Target model integration or protection:
    Target exchanged business meaning/facts:
    Target intent:
    Target status: confirmed | inferred | proposed
    Target evidence:

  Semantic Conflicts:
  - Conflict:
    Observed current meaning:
    Current status: confirmed | inferred | proposed
    Current evidence:
    Proposed target meaning:
    Target status: confirmed | inferred | proposed
    Target evidence:
    Affected decisions:

  Ubiquitous Language:
  - Term:
    Meaning:
    Context/source:
    Status: confirmed | inferred | proposed
    Evidence:

  Business Rules / Invariants:
  - ID, when referenced:
    Rule:
    Scope/subject:
    Trigger:
    Required condition:
    Rejection/outcome:
    Consistency need:
    Status: confirmed | inferred | proposed
    Evidence:

  Lifecycle / State Transitions:
  - Subject:
    From:
    Command/trigger:
    Preconditions:
    To/outcome:
    Invalid transitions:
    Resulting Domain Event, when justified:
    Status: confirmed | inferred | proposed
    Evidence:

  Commands:
  - Command:
    Actor:
    Preconditions:
    Rejection rules:
    Status: confirmed | inferred | proposed
    Evidence:

  Aggregates:
  - Aggregate:
    Identity:
    Commands handled:
    Invariant IDs protected:
    Status: confirmed | inferred | proposed
    Evidence:

  Entities:
  - Entity:
    Status: confirmed | inferred | proposed
    Evidence:

  Value Objects:
  - Value Object:
    Validation/meaning:
    Status: confirmed | inferred | proposed
    Evidence:

  Domain Events:
  - Event:
    Emitted by:
    Meaning/business relevance:
    Business facts:
    Status: confirmed | inferred | proposed
    Evidence:

  Domain Services:
  - Name:
    Business rule:
    Reason rule does not belong to one aggregate:
    Status: confirmed | inferred | proposed
    Evidence:

  Policies:
  - Name:
    Trigger:
    Decision/reaction:
    Resulting command or outcome:
    Status: confirmed | inferred | proposed
    Evidence:

  External Domain Facts / Capabilities Needed:
  - Fact/capability:
    Domain decision requiring it:
    Business meaning:
    Status: confirmed | inferred | proposed
    Evidence:

  Application Coordination Needs (later mapped to application services when justified):
  - Use case:
    Coordination needed:
    Business reason:
    Status: confirmed | inferred | proposed
    Evidence:

  Aggregate Lifecycle / Access Needs (later mapped to repositories when justified):
  - Aggregate:
    Load/save intent:
    Business reason:
    Status: confirmed | inferred | proposed
    Evidence:

  Read Needs / Read Models:
  - Read need:
    Shape/purpose:
    Status: confirmed | inferred | proposed
    Evidence:
```

The common envelope and `Modeling Scope` are required for every substantive result. Emit only the
payload sections that apply to the declared scope and depth. Do not print empty sections or invent
terms, classifications, rules, states, events, services, or relationships to complete the shape.
Use stable local IDs only when another item must reference an entry, such as an Aggregate referring
to the invariants it protects. Every reference must resolve to an ID present in the scoped result.

Use `Domain Landscape` and `Subdomains` only for applicable strategic decisions. Include
`Bounded Contexts` at the level needed by the declared scope, `Context Relationships` when
interacting contexts affect the decision, and `Semantic Conflicts` when current and target meanings
differ.

Item status means:

- `confirmed`: explicit business evidence or accepted project evidence supports the item;
- `inferred`: available evidence supports a responsible working assumption that remains visible
  for review;
- `proposed`: the model recommends a choice that has not yet been accepted.

Do not use numeric confidence scores. Envelope-level `Evidence` indexes the inputs; item-level
`Evidence` traces each material strategic or tactical decision to its support.

Current and target statements are separate modeling items. When both are material, give each its
own `confirmed | inferred | proposed` status and evidence; do not let observed current-state
evidence confirm a proposed target. A target item with `proposed` status may be handed downstream
only as uncertainty or as an explicitly accepted assumption whose acceptance source/evidence is
recorded. It must not cross the Architecture Guidance evidence gate as a confirmed domain
decision.

## Status Semantics

- Use `completed` when the result is usable for its declared scope, depth, and **Recommended Next
  Step**. It does not claim that deferred areas or the wider domain landscape are complete.
- Use `needs-input` only when missing or ambiguous business information about a material term,
  invariant, cross-aggregate interaction, external effect, or bounded-context boundary prevents a
  usable Domain Model for the dependent next activity. Ask the smallest question that resolves the
  blocker, preserve completed independent work, and do not block unrelated increments.
- Use `not-applicable` for simple CRUD or a pure read-model change that does not require richer
  domain modeling. Record the affected concept, governing constraints, and reason modeling is not
  applicable in a compact result; do not expand it into the substantive payload template.

List intentionally deferred areas in `Modeling Scope`. Deferral is not evidence of global
completion and blocks only decisions that depend on the deferred work.

Do not treat every inferred invariant or multi-aggregate command as automatically blocking. The
modeling specialist owns the readiness judgment and records non-blocking uncertainty in
**Assumptions** or **Open Questions**.

Record architecture, integration, or dependency uncertainty that does not block a usable Domain
Model in **Open Questions** or **Handoff Notes** for the downstream specialist. Do not use that
uncertainty alone to mark Domain Modeling `needs-input`.

## Boundary Between Modeling And Architecture Mapping

Commands in this note mean business intentions that can be accepted or rejected. They do not imply
that implementation must create command classes, command handlers, or CQRS.

Read needs and read models identify query, screen, report, notification, or decision-support
shapes that should not distort write aggregates. They do not imply an implementation term such as
`QueryPort`, `ReadModelPort`, `LookupPort`, repository, controller, or API endpoint.

Application coordination needs describe business use cases that require coordination. Aggregate
lifecycle and access needs describe business-required load/save intent. Neither selects service
classes, interfaces, repository abstractions, ports, or framework types.

External domain facts and capabilities describe information or decisions the domain needs from
outside the modeled boundary. They do not select a Repository, Port, client, adapter, transport, or
dependency direction.

Map commands, read needs, coordination needs, and lifecycle/access needs to architecture and
implementation constructs only after the domain assumptions and chosen architecture are clear.

## When To Ask For Review

Ask for review before coding when any of these conditions could affect business meaning. A review
need does not by itself require `needs-input`; apply the status semantics above.

- A term has multiple possible meanings.
- An invariant is inferred, not stated.
- A lifecycle transition or rejection rule is inferred or contradictory.
- A command appears to modify multiple aggregates.
- A domain event might trigger external effects.
- A table/API shape is driving the model.
- The model would introduce a new bounded context.
- A Subdomain classification or context relationship lacks evidence.

## When To Keep It Lightweight

For simple CRUD, small field additions, or pure read-model changes, summarize only the affected
concept, governing constraints, and reason no richer model is needed. Use `not-applicable` when the
phase adds no responsible modeling decision; otherwise return the smallest useful completed model.
