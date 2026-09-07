# Domain Architecture Plugin

English ｜ [中文](README_ZH.md)

---

A plugin-first architecture guidance package for business-domain software systems. It helps AI coding agents turn business requirements into domain models, architecture decisions, and, when applicable, framework-specific implementation guidance. It does not treat DDD, Hexagonal Architecture, Onion Architecture, CQRS, or a framework convention as one mandatory combined model.

## Quick Start

### Codex

```bash
codex plugin marketplace add huahill/domain-architecture-skills
codex plugin add domain-architecture@huahill
```

Confirm the plugin appears in `codex plugin list`, then start with this prompt:

```text
Use $domain-architecture-workflow for this business project.

Business goal and known rules:
Existing project or artifacts:
Technology constraints:
JFoundry: yes | no | undecided
Desired next activity:
```

The workflow uses the evidence provided, asks only for facts that block a responsible decision, and returns the applicable specialist results plus a `Domain Architecture Handoff` for planning, implementation, or review.

For local development from this checkout, use the local source instead:

```bash
codex plugin marketplace add .
codex plugin add domain-architecture@huahill
```

Use one source for the `huahill` marketplace name. To switch between a local checkout and the Git source, remove the existing marketplace first:

```bash
codex plugin marketplace remove huahill
```

When upgrading an installation that still uses the former `xfoundries` marketplace, migrate it once:

```bash
codex plugin marketplace remove xfoundries
codex plugin marketplace add huahill/domain-architecture-skills
codex plugin add domain-architecture@huahill
```

### Claude Code And Compatible Agents

Claude Code can validate and install the same plugin source through its plugin system:

```bash
claude plugin validate .
claude plugin marketplace add huahill/domain-architecture-skills
claude plugin install domain-architecture@huahill
```

Existing Claude Code installations should add the `huahill` marketplace and install
`domain-architecture@huahill`; the former marketplace entry can then be removed through Claude
Code's marketplace management.

The repository also includes an [`.agents/plugins` marketplace manifest](.agents/plugins/marketplace.json) for compatible agents. Its `skills/` directory is plugin-internal; install the `domain-architecture` plugin rather than copying individual skills.

## What It Does

For end-to-end work, start with `domain-architecture-workflow`:

```text
requirements
-> domain modeling
-> architecture guidance
-> optional jfoundry landing
-> Domain Architecture Handoff
-> detailed planning or the selected process companion
```

The handoff preserves specialist results, decisions, constraints, open questions, and blockers. It identifies the smallest planning-ready increment and its next owner; it is planning input, not a detailed implementation plan. The workflow supports a versioned machine-readable handoff contract with stable identity, revisions, dependency-scoped blockers, artifact references, accepted-assumption evidence, and planning-readiness metadata. Markdown remains the human-readable projection, and existing text-only consumers remain compatible. Persisted workflow artifacts use `docs/domain-architecture/`, and standalone detailed plans use its `plans/` child directory.

| Need | Entry point |
|---|---|
| End-to-end business-domain analysis and handoff | `domain-architecture-workflow` |
| Scoped strategic and tactical modeling: business capabilities, Subdomains, Bounded Contexts, Context Maps, current/target semantic conflicts, rules, lifecycle, and tactical patterns | `domain-modeling` |
| Architecture decision or boundary review | `domain-architecture-guidance` |
| Confirmed jfoundry implementation landing | `using-jfoundry` |

`domain-modeling` invokes strategic work only when the requested decision requires it, such as system decomposition, multi-team ownership, or cross-context semantic conflict. An established-context increment can remain tactical or return a lightweight `not-applicable` result. Strategic modeling describes the business problem space; it does not derive teams, modules, microservices, databases, deployment boundaries, or architecture styles.

## Scope And Limits

- The core modeling and architecture methods are language and framework neutral, but implementation guidance is deepest for Java/Kotlin. C#/.NET, Go, and Python receive ecosystem mapping rather than code templates; `using-jfoundry` is Java-only.
- The primary target is business backend software. Client applications are a conditional fit when they own substantial domain behavior, offline workflows, synchronization conflicts, or local persistence boundaries; this plugin does not provide platform-specific mobile or frontend implementation templates.
- Domain modeling can distinguish business capabilities, Subdomains, Bounded Contexts, and Context Maps, including current and target meaning in brownfield systems. It records business rules, lifecycle transitions, invariants, aggregates, and other tactical patterns only to the depth needed by the selected decision.
- Do not force DDD, Ports and Adapters, CQRS, repositories, or layered structures into simple CRUD applications, thin clients, or small scripts.

## Advanced Use

- `using-jfoundry` applies only after jfoundry is confirmed or explicitly requested. An undecided framework does not block framework-neutral modeling and architecture guidance. Its [architecture landing](skills/using-jfoundry/references/architecture.md) preserves the selected style rather than choosing one.
- A process companion such as Superpowers, SpecKit, or OpenSpec is optional and user-selected. It owns its own specifications, plans, tasks, implementation, review, files, and commands; this plugin owns the specialist results and handoff. The [first-use guide](skills/domain-architecture-workflow/references/first-use.md) defines the input, ownership, status, and return rules.
- The structured handoff contract is additive: it does not replace specialist result ownership or require a workflow engine. The repository includes standard-library tools to validate a handoff, create a blocker-resolution revision, and render summary/full Markdown views; database persistence and distributed recovery remain outside this phase. The contract is documented in [handoff-contract.md](skills/domain-architecture-workflow/references/handoff-contract.md) and defined by [its JSON Schema](schemas/domain-architecture-handoff.schema.json).
- Handoff consumers can request a summary or full projection. Persisted artifacts may declare a sensitivity classification and redaction requirement; process companions consume the contract and references but retain ownership of their own plans and execution state.
- Selected architecture styles retain their own constraints. Aggregate repositories, adapter vocabulary, integration contracts, and reliable messaging are governed by the [architecture constraints](skills/domain-architecture-guidance/references/architecture-constraints.md) and the applicable specialist references; the plugin does not infer those choices from package names or available framework features.

## Source Policy

The architecture guidance separates sources into three levels:

- Foundational sources: Eric Evans for DDD, Alistair Cockburn for Hexagonal Architecture, Martin Fowler for enterprise patterns and CQRS discussion, Greg Young for CQRS, Jeffrey Palermo for Onion Architecture, and Clean Architecture only as a cautious dependency-direction synthesis.
- Widely used implementation guidance: jMolecules, Microsoft .NET architecture guidance, Spring Modulith, ArchUnit, ArchUnitNET, and microservices.io.
- Opinionated synthesis and examples: useful for inspiration, but not canonical authority.

The plugin distinguishes DDD modeling concepts from architecture style constraints and framework conventions. It does not present DDD, Layered, Onion, Hexagonal, CQRS, and Event Sourcing as one canonical architecture.

## Repository Layout

```text
.codex-plugin/
  plugin.json
.claude-plugin/
  marketplace.json
  plugin.json
.agents/plugins/
  marketplace.json
skills/
  domain-architecture-workflow/
  domain-modeling/
  domain-architecture-guidance/
  using-jfoundry/
```

## Updating

For local development, keep the marketplace source pointed at this repository. After changing plugin metadata, reinstall or update the plugin in the target agent so it refreshes cached metadata.

The plugin uses one SemVer release version across the Codex and Claude manifests. Backward-compatible capabilities increment `MINOR`, compatible fixes increment `PATCH`, and incompatible public contracts increment `MAJOR` after `1.0.0` (or the next `MINOR` before `1.0.0`). Release tags use `domain-architecture--v<version>`.

Version `0.3.0` moves the repository and marketplace identity from `xfoundries` to `huahill`.
Existing installations must apply the marketplace migration described in Quick Start.

For Codex, `.codex-plugin/plugin.json` appends `+codex.<cachebuster>` to that release version. Refresh this suffix when changed plugin content or metadata must invalidate the Codex cache; do not increment the release version only for cache refresh. Then reinstall from `domain-architecture@huahill`.

## Design Principle

Use architecture patterns to protect business meaning and change boundaries. Do not use them as decorative structure.
