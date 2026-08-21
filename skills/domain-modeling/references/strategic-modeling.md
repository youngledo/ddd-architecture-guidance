# Strategic Modeling

Use this for a new business domain, system decomposition or modernization, multi-team ownership, cross-domain semantic conflict, or a decision about Subdomains, Bounded Contexts, or their relationships. Do not require it for a local increment whose relevant context and relationships are already established.

## Problem Space And Solution Space

- Domain and Subdomain describe the business problem space.
- A business capability describes what the business must be able to do; it is evidence for discovery, not automatically a Subdomain or Bounded Context.
- A Bounded Context is a boundary within which a particular model and Ubiquitous Language apply.
- Subdomain, Bounded Context, capability, team, module, system, database, and deployable service are not presumed to map one-to-one.

## Subdomain Classification

- Core: materially differentiates the business or is central to its strategy.
- Supporting: necessary and business-specific but not differentiating.
- Generic: solves a broadly shared problem for which a standard capability may exist.

Classify only when it informs an investment, sourcing, ownership, or modeling decision. Record the rationale, evidence, and `confirmed | inferred | proposed` status. Classification does not select rich DDD, custom implementation, outsourcing, a microservice, CQRS, or an architecture style.

## Bounded Context Discovery

Discover candidates from changes in language, model, rules, decision ownership, and consistency rather than from package, table, service, database, deployment, or organization-chart boundaries. For brownfield work, record observed current and desired target intent separately and expose semantic conflicts.

## Context Relationships

Keep these dimensions separate:

- Direction and ownership: upstream, downstream, or mutually coordinated.
- Collaboration or governance, when known: Partnership, Customer/Supplier, Separate Ways, or a clearly described project-local relationship.
- Model integration or protection, when known: Shared Kernel, Conformist, Anti-Corruption Layer, Open Host Service, Published Language, or an explicit translation need.
- Exchanged business meaning: capabilities, decisions, reference facts, or historical facts.

Use a named relationship pattern only when its semantics fit the evidence. Describe the business meaning exchanged; do not choose HTTP, messaging, schemas, ports, adapters, topology, reliability mechanisms, or other architecture and implementation mappings.

## Output

Return only the applicable `Domain Landscape`, `Subdomains`, `Bounded Contexts`, `Context Relationships`, and `Semantic Conflicts` sections inside the Domain Modeling Result. Record item-level evidence and `confirmed | inferred | proposed` status, and distinguish current from target intent where relevant.

Include covered and deferred areas. Unfinished landscape work blocks only decisions that depend on it; do not print empty sections or invent conclusions for deferred areas.
