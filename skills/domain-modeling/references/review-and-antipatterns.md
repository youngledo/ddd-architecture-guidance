# Review And Anti-Patterns

Use this to review a proposed model or to check work before implementation.

## Review Checklist

- Is the decision scope, modeling depth, current/target intent, and deferred work explicit?
- Are Subdomains, Bounded Contexts, teams, systems, and deployable services kept conceptually
  distinct rather than forced into a one-to-one mapping?
- Does each material strategic classification or relationship have rationale, status, and evidence?
- Are business rules and invariants explicit, independently reviewable, and referenced by the
  Aggregates that protect them?
- Are lifecycle transitions complete and mutually consistent, including preconditions, invalid
  transitions, and rejection outcomes?
- Does each aggregate protect a real invariant?
- Are commands named as business tasks rather than CRUD operations?
- Are events meaningful business facts in past tense?
- Does each Domain Event matter to history, later decisions, a policy, or collaboration rather than
  merely recording every state change?
- Are value objects carrying validation and meaning, not just wrapping primitives mechanically?
- Are domain services reserved for domain decisions that do not belong to one aggregate?
- Are application services coordinating use cases instead of owning core business rules?
- Are repositories focused on aggregate lifecycle and command-side loading?
- Are read models separate from write aggregates when their shape differs?
- Are open questions visible before code hardens the model?
- Are observed technical structures treated as current evidence rather than automatic target
  domain boundaries?
- Does unfinished landscape work block only the decisions that depend on it?

## Anti-Patterns

### Table-Driven Aggregate

Symptom: one aggregate per table, mostly getters/setters.

Fix: start from commands and invariants. Keep CRUD simple when there is no domain behavior.

### Subdomain-Context-Service Collapse

Symptom: each Subdomain is assumed to be exactly one Bounded Context, team, and deployable service.

Fix: model problem-space Subdomains and model boundaries separately. Let architecture and project
constraints decide team, module, system, and deployment mappings.

### Unevidenced Strategic Classification

Symptom: a Subdomain is labeled Core, Supporting, or Generic, or a context boundary is proposed,
without a decision scope, rationale, evidence state, or source.

Fix: classify only when it informs the requested decision. Record scope, rationale,
`confirmed | inferred | proposed` status, and evidence for every material strategic item.

### Anemic Domain Model

Symptom: application services contain all rules, domain objects only store data.

Fix: move lifecycle decisions and invariant checks into aggregate methods or value objects.

### Oversized Aggregate

Symptom: one aggregate changes for many unrelated workflows or loads a large object graph.

Fix: split around invariants and immediate consistency. Use events or policies for eventual reactions.

### Rules Hidden In Aggregates

Symptom: rules appear only as prose under Aggregate entries, so lifecycle and cross-item conflicts
cannot be reviewed independently.

Fix: record business rules and invariants as first-class items. Assign a stable local ID only when
another item must refer to the rule; make every such reference resolve to an ID in the scoped
result.

### Missing Or Contradictory Lifecycle

Symptom: states are listed without legal transitions, preconditions, invalid transitions, or
rejection outcomes, or different flows imply contradictory transitions.

Fix: model lifecycle transitions explicitly and reconcile conflicts before aggregates or code make
them implicit.

### Fake Domain Service

Symptom: a service is called domain service but handles application workflow, transaction demarcation, concrete persistence APIs, HTTP calls, security, or logging.

Fix: move technical workflow to application services or adapters. Keep only domain decisions that
do not fit an entity, value object, or aggregate. When a decision needs aggregate access or an
external business fact, record that need; architecture guidance decides whether a Repository or
other interface is justified, where it belongs, and which dependency direction is allowed.

### Event As Command

Symptom: an event named in imperative form or used as something that can fail.

Fix: model the request as a command and the successful fact as a past-tense event.

### Event For Every State Change

Symptom: every persisted state change is promoted to a Domain Event even when it has no relevance
to domain history, later decisions, policies, or collaboration.

Fix: keep such observations as candidate discovery facts. Promote only facts with explicit business
meaning and evidence.

### Current Technology As Target Domain

Symptom: existing tables, APIs, packages, services, databases, or team boundaries are copied into
the target domain model without examining their business meaning.

Fix: record them as evidence of the current system, distinguish current from target intent, and
make semantic conflicts visible.

### Global Landscape Blocker

Symptom: unfinished enterprise or landscape analysis blocks a local increment whose context
meaning, rules, and relationships are already usable.

Fix: block only dependent work. Preserve scoped completed results and defer unrelated landscape
questions explicitly.

### Over-Modeled CRUD

Symptom: many aggregates, repositories, factories, and services for simple data maintenance.

Fix: use a simpler transaction script or CRUD model until real invariants appear.
