---
name: domain-modeling
description: Use when modeling business domains from requirements, workflows, existing systems, tables, or APIs; identifying business capabilities, subdomains, bounded contexts, context maps, ubiquitous language, rules, commands, aggregates, value objects, domain events, services, lifecycle or read needs; or reviewing whether a proposed model is behavior-rich rather than table-driven.
---

# Domain Modeling

## Purpose

Use this skill to turn business requirements into an explicit domain model before implementation. It is framework-neutral and should not assume jfoundry, Spring, .NET, Go, Python, or any specific architecture style.

Do not treat domain modeling notes as ceremony for simple CRUD changes. Use them when a change introduces business rules, lifecycle state, invariants, domain events, cross-aggregate coordination, or ambiguous domain language.

## Core Workflow

1. Declare the decision scope (`landscape`, `bounded-context`, or `increment`) and required depth (`strategic`, `tactical`, or `both`).
2. Start from business workflows, not tables or controllers.
3. Extract language, commands, events, rules, states, exceptions, and external actors.
4. When strategic depth applies, identify capabilities, Subdomains, Bounded Contexts, and relevant context relationships.
5. When tactical depth applies, design aggregates around invariants and consistency boundaries.
6. Produce the modeling output protocol before coding.
7. Review for table-driven modeling, anemic behavior, oversized aggregates, and misplaced orchestration.

## Reference Routing

- Read `references/input-analysis.md` when starting from requirements, user stories, tickets, existing tables, APIs, or code.
- Read `references/strategic-modeling.md` for new business domains, system decomposition or modernization, multi-team ownership, Subdomain classification, Bounded Context discovery, Context Maps, or cross-context semantic conflicts.
- Read `references/event-storming.md` when workflows are complex, event-heavy, or involve policies and external systems.
- Read `references/bounded-contexts.md` when terms, ownership, data, or rules may differ across teams or subdomains.
- Read `references/aggregate-design.md` when choosing aggregate roots, entities, value objects, invariants, repositories, or domain services.
- Read `references/modeling-output.md` before producing the modeling note or asking for domain review.
- Read `references/review-and-antipatterns.md` when reviewing a proposed model or checking for table-driven/anemic designs.

## Ground Rules

- Prefer domain terms from the business language. Avoid technical names such as manager, handler, data, record, wrapper, or config unless they are real domain terms.
- Keep open domain questions visible. Do not silently hard-code guesses as business rules.
- Do not force DDD patterns into low-complexity CRUD areas.
- Use strategic modeling only when the requested decision needs it. Do not derive teams, modules, services, databases, deployment boundaries, or architecture styles from capabilities, Subdomains, Bounded Contexts, or Context Maps.
- Treat architecture and framework mapping as a later step. First make the domain assumptions explicit.
