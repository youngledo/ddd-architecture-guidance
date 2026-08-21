# Implementation Planning Handoff

## Purpose

The workflow supplies domain and architecture decisions to planning. When artifacts are persisted,
it owns their default location; a selected process companion owns its own detailed plans, tasks,
and execution state. Apply the same disciplined flow to every project, while scaling the
architecture work to the requested increment's risk.

## Default Artifact Location

For a new project that persists workflow artifacts, use:

```text
docs/domain-architecture/
  00-source-and-assumptions.md
  01-domain-modeling.md
  02-context-map.md
  03-architecture-guidance.md
  04-jfoundry-implementation-guidance.md
  05-implementation-roadmap.md
  adr/
  plans/
```

Create only artifacts that the request produces; the tree is a default organization, not a demand
to create empty files. `02-context-map.md` is an optional specialist-owned artifact; the
coordinator does not reconstruct the Context Map or create a parallel version. `plans/` holds
detailed plans only when no process companion owns them.

Existing documents outside this tree may be used as input evidence, but they do not change the
plugin output location. Do not create a second plugin artifact tree.

## Select The Required Depth

| Increment evidence | Required workflow depth |
|---|---|
| New business landscape, system decomposition or modernization, multi-team boundary, Subdomain/Bounded Context decision, or cross-context semantic conflict | Strategic Domain Modeling first, followed only by the tactical modeling and Architecture Guidance needed for the first planning-ready context or increment. |
| New domain behavior, invariants, bounded-context ownership, or external collaboration | Domain Modeling, Architecture Guidance, then optional framework landing before detailed planning. |
| Existing architecture with a business increment | Reuse confirmed results; revisit only the affected modeling, architecture, or landing phase. |
| Simple CRUD under established conventions | Record why richer modeling or an architecture decision is unnecessary; then plan the change. |
| Localized fix with no business or boundary change | Diagnose and plan the fix directly; return to a specialist only when the investigation exposes changed meaning or architecture drift. |

Do not make full DDD, Hexagonal, CQRS, or framework landing mandatory for every increment. Do
not bypass the applicable decision phase merely because a detailed plan would be quicker to write.

## Planning-Ready Handoff

Before detailed planning, the handoff must identify:

- the smallest independently verifiable increment and explicit non-goals;
- the confirmed domain, architecture, and framework decisions the increment consumes;
- every explicitly accepted assumption the increment consumes, preserving its original item
  status and acceptance source/evidence rather than relabeling it as `confirmed`;
- the exact Subdomain scope, Bounded Context meaning and ownership, context relationships, and
  current/target decisions consumed by the increment when they are relevant;
- relevant constraints and affected boundaries;
- open questions, distinguishing blockers for this increment from nonblocking future work;
- the next planning owner: plugin-managed planning or a named process companion.

All phases consumed by the selected increment must be usable: `completed` for their declared scope
and recommended next step, or responsibly `not-applicable`. A `needs-input` result pauses only the
increments that depend on the missing fact. Deferred strategic work that the increment does not
consume remains visible but does not block planning. Do not guess an external protocol, invariant,
transaction boundary, or runtime choice to make a plan appear complete.

Planning readiness uses the same domain evidence gate as Architecture Guidance. A consumed domain
item must be `confirmed` or an explicitly accepted assumption with acceptance source/evidence. An
`inferred` or `proposed` item without that acceptance remains uncertainty and blocks only a plan
that depends on it. Acceptance does not change the item's original status to `confirmed`.

## Planning Owners

### Plugin-Managed Planning

When no process companion is selected, the agent produces a detailed implementation plan under
`docs/domain-architecture/plans/`. The plan should state the increment goal, non-goals, affected files or modules,
model/API/persistence changes where applicable, tests, architecture checks, verification commands,
and blockers.

### Process Companion Planning

When the user selects Superpowers, OpenSpec, SpecKit, or another companion, that companion owns
its specification, detailed plan, tasks, approval gates, files, directories, commands, and
execution state. Feed the handoff into its next planning activity. The plugin continues to persist
its own results in `docs/domain-architecture/`, but does not create a
parallel detailed plan using the plugin's own format.

A companion may help gather requirements or create an initial proposal before this workflow runs.
It must consume the resulting handoff before finalizing a detailed plan or dependent tasks.

### Later Companion Adoption

An existing project can adopt a companion after an independent domain/architecture pass. The
companion reads the persisted specialist results and handoff, preserves confirmed decisions and
open questions, and creates only its own planning artifacts. Re-run a specialist only when the
evidence is stale, a business meaning changed, or a proposed implementation conflicts with an
existing constraint.

## Return Path

Implementation discoveries that alter Subdomain scope, Bounded Context meaning, team or rule
ownership, a context relationship, current/target intent, or other business meaning return to
Domain Modeling. Discoveries that alter architecture boundaries or dependency direction without
changing those domain decisions return to Architecture Guidance. Framework conflicts return to
JFoundry Implementation Guidance when applicable. Preserve unaffected completed results. The
planning owner updates its own artifacts after the revised handoff is available.
