# Bounded Contexts

Use this when a domain has multiple teams, subdomains, integrations, conflicting terms, duplicated data, or workflows with different rule owners.

A Subdomain describes part of the business problem space. A Bounded Context is a boundary within which a model and Ubiquitous Language apply. They may align, but do not presume a one-to-one mapping. Read `strategic-modeling.md` when Subdomain discovery or Core, Supporting, or Generic classification affects the decision.

## Context Signals

Consider a separate bounded context when:

- The same term has different meanings in different workflows.
- Different teams own rules or releases.
- Data is copied because another area needs a different shape or lifecycle.
- One workflow treats a concept as a core decision while another treats it as reference data.
- Consistency requirements differ sharply.
- Integrations require translation or anti-corruption logic.

Do not split contexts only because tables or packages are numerous. Split around language, model, decision ownership, and rule boundaries. A candidate does not automatically define a service, module, team, database, or deployment boundary.

## Context Relationships

Analyze these dimensions separately and only record what the evidence supports:

- Direction and ownership: upstream, downstream, or mutually coordinated; identify who owns the relevant meaning and decisions.
- Collaboration or governance: Partnership, Customer/Supplier, Separate Ways, or an explicit project-local relationship.
- Model integration or protection: Shared Kernel, Conformist, Anti-Corruption Layer, Open Host Service, Published Language, or an explicit translation need.
- Exchanged business meaning: a capability, decision, reference fact, or historical fact needed across the boundary.

Use a named pattern only when its semantics fit. Record observed current and desired target intent
with separate item-level evidence and `confirmed | inferred | proposed` status when both are
material. Current-state evidence does not confirm a target proposal. Do not preselect APIs,
events, messaging, schemas, ports, adapters, reliability mechanisms, or topology.

## Checks

- Does each context have its own ubiquitous language?
- Who owns the rules, decisions, and vocabulary?
- What business meaning or fact crosses the boundary, and why is it needed?
- Where is translation needed?
- What must not leak across the boundary?
- Is this an observed current relationship or a proposed target relationship?
- What evidence supports the boundary and each relationship dimension?

## Output

- Bounded context candidates:
  - Name:
  - Current key language/model:
  - Current decision and rule owners:
  - Current intent:
  - Current status: confirmed | inferred | proposed
  - Current evidence:
  - Target key language/model:
  - Target decision and rule owners:
  - Target intent:
  - Target status: confirmed | inferred | proposed
  - Target evidence:
- Context relationships:
  - Contexts:
  - Current direction and ownership:
  - Current collaboration or governance:
  - Current model integration or protection:
  - Current exchanged business meaning/facts:
  - Current intent:
  - Current status: confirmed | inferred | proposed
  - Current evidence:
  - Target direction and ownership:
  - Target collaboration or governance:
  - Target model integration or protection:
  - Target exchanged business meaning/facts:
  - Target intent:
  - Target status: confirmed | inferred | proposed
  - Target evidence:
- Open questions:
