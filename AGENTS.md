# Agent Instructions

This repository contains the `domain-architecture` plugin for business-domain software architecture.

The plugin exposes these internal skills:

- `domain-architecture-workflow`: entry-point workflow and routing.
- `domain-modeling`: framework-neutral domain modeling.
- `domain-architecture-guidance`: source-aware architecture guidance.
- `using-jfoundry`: jfoundry-specific application guidance.

## Scope

The repository helps agents and developers move from business requirements to domain models, architecture decisions, and optional framework-specific implementation guidance.

The plugin covers:

- Domain-Driven Design concepts and modeling workflow.
- Layered Architecture.
- Onion Architecture.
- Hexagonal Architecture / Ports and Adapters.
- CQRS, without assuming Event Sourcing.
- Architecture unit tests such as ArchUnit and ArchUnitNET.
- jMolecules-style expression for Java/Kotlin.
- jfoundry-specific business project guidance.

Do not collapse DDD, Layered, Onion, Hexagonal / Ports and Adapters, CQRS, Event Sourcing, jMolecules, or jfoundry into one canonical model. Attribute every recommendation to the right level: domain modeling, architecture style, implementation guidance, framework convention, or project-local decision.

## Skill Boundaries

- Treat the plugin as the installation and distribution unit. The `skills/` directories are plugin-internal capabilities and compatibility assets, not independent products.
- Keep `.agents/plugins/marketplace.json` as the repo-owned marketplace entry for Codex and other compatible agents. It should point at the repository root plugin with `source.url: "./"`.
- Keep `.claude-plugin/marketplace.json` as the repo-owned marketplace entry for Claude Code. Do not force Claude Code to consume the Codex marketplace schema.
- Keep `domain-architecture-workflow` as a coordinator. It should route to other skills and define phase order, not duplicate their detailed references.
- Keep phase payload ownership with the specialist: `domain-modeling` returns the Domain Modeling Result, `domain-architecture-guidance` returns the Architecture Guidance Result, and `using-jfoundry` returns the JFoundry Implementation Guidance Result when jfoundry applies. The coordinator combines them into the Domain Architecture Handoff.
- Use the shared result envelope and phase statuses for substantive decisions, reviews, and implementation guidance. Do not force the full envelope onto simple conceptual explanations.
- A `needs-input` result blocks only dependent phases. Preserve completed results, emit an interim handoff, and ask the smallest blocking question.
- Keep `domain-modeling` framework-neutral. It should not assume jfoundry, Spring, .NET, Go, Python, or a specific architecture style.
- Keep Subdomains and Bounded Contexts distinct. A Subdomain describes the problem space; a Bounded Context defines where a model and Ubiquitous Language apply. Neither implies a one-to-one mapping to a business capability, team, module, system, database, microservice, or deployment boundary.
- Invoke strategic modeling only when the requested decision needs it. Do not require enterprise-wide landscape work for an independent increment whose relevant context meaning, rules, and relationships are already usable.
- Keep problem-space modeling separate from architecture and deployment mapping. Domain Modeling may describe exchanged business meaning and model-protection needs, but Architecture Guidance owns interface placement, integration mechanisms, dependency direction, and deployment consequences.
- For material modeling items, preserve item-level `confirmed | inferred | proposed` status and evidence. Distinguish observed current meaning from proposed target meaning, especially when technical artifacts are the evidence.
- Treat `completed` as complete only for the declared modeling scope, depth, and recommended next activity. Deferred work blocks only decisions that depend on it and must not be presented as globally modeled or confirmed.
- Keep optional context-map artifacts owned by `domain-modeling`. The coordinator may preserve or reference `02-context-map.md`, but should not reconstruct the specialist payload or create a parallel context map.
- Keep `domain-architecture-guidance` source-aware. `references/source-policy.md` remains authoritative for source hierarchy.
- Keep `using-jfoundry` jfoundry-specific. Do not move general DDD methodology into it.
- Skip `using-jfoundry` for non-jfoundry projects and record why no framework landing applies in the composite handoff; do not invoke the specialist merely to produce a `not-applicable` result. When jfoundry use is undecided, do not invoke the specialist or block framework-neutral Domain Modeling and Architecture Guidance. Defer the choice until a framework-specific next activity materially requires it, and record the pending optional landing in the handoff.
- Do not make this repository depend on Superpowers, OpenSpec, SpecKit, or any other external process framework. They may be described only as optional companions selected by the user or already active in the project.
- Keep remote protocol translation in the business project's infrastructure adapter. Expected remote absence, conflict, and business rejection belong in the Port result; only known technical failures at an application-owned secondary Port are candidates for `ExternalAccessException` translation.

## Source Policy

Prefer foundational and broadly recognized sources for architecture claims:

- Eric Evans for DDD concepts.
- Alistair Cockburn for Hexagonal Architecture / Ports and Adapters.
- Martin Fowler for enterprise application patterns and CQRS discussion.
- Greg Young for CQRS-specific material.
- Jeffrey Palermo for Onion Architecture.
- Robert C. Martin's Clean Architecture article only for dependency direction and independence principles.
- jMolecules as the main practical Java/Kotlin reference.
- Microsoft architecture guidance for pragmatic .NET/backend implementation.
- ArchUnit and ArchUnitNET as architecture validation tools.

Do not treat Herberto Graca's "Explicit Architecture" as an authoritative model. It may be mentioned only as an opinionated synthesis.

Do not treat Clean Architecture as a wholly new, standalone architecture. Use it cautiously as a synthesis and terminology bridge for dependency direction and independence principles.

## Editing Rules

- Keep each skill's `SKILL.md` concise. Put detailed guidance in that skill's `references/`.
- Keep references one level below the skill directory and link them directly from `SKILL.md`.
- Keep examples short and labeled as sketches. They should demonstrate translation choices, not prescribe a universal project template.
- Preserve the distinction between foundational sources, implementation guidance, opinionated synthesis, and framework conventions.
- Preserve architecture constraints when a project explicitly chooses Layered, Onion, Hexagonal / Ports and Adapters, or CQRS.
- Do not introduce universal rules such as mandatory CQRS, mandatory Event Sourcing, mandatory repository abstractions, mandatory folder structures, or mandatory jfoundry adoption.
- Distinguish DDD core discipline from optional implementation preferences. Once a project chooses DDD, ubiquitous language, bounded-context meaning, invariant protection, identity/value distinction, and domain behavior placement should be treated as real design constraints.
- Use "usually", "when justified", or "in this architecture" for context-dependent guidance.
- Keep guidance language-neutral where possible, then translate into ecosystem-specific advice.
- Do not make jMolecules a cross-language implementation mandate.
- Do not make ArchUnit or ArchUnitNET sources of architecture rules; they validate rules chosen from architecture and codebase context.

## Documentation Rules

- Update both `README.md` and `README_ZH.md` for user-facing changes.
- Keep English and Chinese READMEs aligned in meaning, even if not line-by-line translations.
- Treat `README_ZH.md` as a Chinese document: write explanatory prose, headings, labels, and
  descriptions in Chinese. Retain English only for proper nouns, product and project names,
  commands, file paths, code identifiers, protocol field values, standard technical abbreviations,
  and formal source or library names when translating them would reduce precision. For example,
  keep `Codex`, `Claude Code`, `DDD`, `CQRS`, `jfoundry`, `JSON Schema`, shell commands, and
  repository paths; translate ordinary words such as `marketplace`, `skill`, `contract`,
  `summary/full`, `consumer`, and `reference` into Chinese. Review `README_ZH.md` for accidental
  English prose whenever it is updated.
- Do not commit files under `docs/superpowers/`. They are local process artifacts and are
  intentionally ignored. Never force-add them; unstage any accidentally added files before commit.
- In this plugin repository, treat generated handoff, design, and plan documents under
  `docs/domain-architecture/` as local workflow artifacts by default. Do not commit them unless the
  user explicitly requests that the artifact itself be versioned. The documented runtime output
  location for business projects does not make those generated outputs part of this plugin's source
  distribution.
- Keep installation instructions plugin-first and compatible with Codex `.agents/plugins` and Claude Code plugin workflows.
- Prefer the repo-local marketplace workflow over loose user-level skill copying.
- Mention raw `skills/` installation only as a fallback for agents without plugin support.
- Avoid marketing claims. State scope and limits clearly.

## Versioning

- Use one canonical SemVer release version for the plugin. Keep it synchronized across
  `.claude-plugin/plugin.json`, both version fields in `.claude-plugin/marketplace.json`, and the
  base version before `+` in `.codex-plugin/plugin.json`.
- Increment `MAJOR` for incompatible public plugin or result-contract changes, `MINOR` for
  backward-compatible capabilities, skills, or result sections, and `PATCH` for compatible fixes
  and clarifications. While the plugin is below `1.0.0`, use the next `MINOR` for incompatible
  public contract changes and document the migration.
- Keep the Codex version in the form `<release-version>+codex.<cachebuster>`. The suffix is build
  metadata used to invalidate Codex caches; it is not an independent release version and must not
  be used instead of a SemVer increment.
- Refresh the Codex cachebuster whenever changed plugin content or metadata is prepared for Codex
  installation. Do not change the canonical release version solely to refresh a local cache.
- Tag releases as `domain-architecture--v<release-version>` after manifests validate and the
  release commit is finalized. Do not include the Codex cachebuster in the tag.

## Validation

After editing skill metadata or `SKILL.md`, validate every checked-in skill:

```bash
for skill in skills/*; do
  python3 /Users/huangxiao/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
```

Before publishing, check:

- `.codex-plugin/plugin.json` validates with the Codex plugin validator.
- `.claude-plugin/plugin.json` validates with `claude plugin validate`.
- `.agents/plugins/marketplace.json` remains present and points at the repository root plugin.
- `.claude-plugin/marketplace.json` remains present and validates with `claude plugin validate --strict`.
- All release-version fields agree, excluding the Codex `+codex.<cachebuster>` suffix.
- Every `skills/*/SKILL.md` has valid YAML frontmatter with `name` and `description`.
- `domain-architecture-workflow` does not hard-depend on superpowers or any other external workflow skill.
- `domain-modeling` contains modeling workflow and output protocol guidance without framework assumptions.
- `domain-architecture-guidance/references/source-policy.md` explains source hierarchy and cautions around Explicit Architecture and Clean Architecture.
- `domain-architecture-guidance/references/architecture-constraints.md` separates DDD modeling concepts from Layered, Onion, Hexagonal / Ports and Adapters, and CQRS structural rules.
- `using-jfoundry` remains a downstream business project skill, not a framework-maintenance skill.
- `using-jfoundry/references/exception-handling.md` distinguishes expected remote outcomes from technical access failures and keeps business protocol interpretation out of jfoundry core.
- `README.md` and `README_ZH.md` mention all shipped skills.
