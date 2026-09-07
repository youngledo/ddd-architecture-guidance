# Domain Architecture Handoff Contract

This reference defines the first-generation structured representation of the coordinator-owned
`Domain Architecture Handoff`. The canonical schema is
[`schemas/domain-architecture-handoff.schema.json`](../../../schemas/domain-architecture-handoff.schema.json).

## Purpose and Ownership

The handoff is planning and review input, not a detailed implementation plan. Specialist results
remain authoritative for their own payloads:

```text
Domain Modeling Result
        -> Architecture Guidance Result
        -> optional JFoundry Implementation Guidance Result
        -> Domain Architecture Handoff
```

The coordinator owns the composite handoff and its routing metadata. It references specialist
results instead of reconstructing a second domain model, architecture analysis, or framework
landing. A process companion may consume the handoff, but is not required by this plugin.

## Canonical and Human-Readable Forms

When a structured handoff is available, it is the canonical interoperability form. The coordinator
may also return a Markdown projection for human review. Existing text-only handoffs remain
compatible; consumers may migrate incrementally.

The contract has these top-level sections:

- identity and lifecycle: `contract_version`, `lineage_id`, `handoff_id`, `revision`, `kind`,
  `parent_handoff_id`, and `status`;
- request and scope: requested outcome, process companion, decision scope, modeling depth, selected
  increment, and non-goals;
- producer: workflow skill, plugin release, and generation timestamp;
- phases: specialist status, result reference, optional applicability, and dependency impact;
- decisions: confirmed decisions, accepted assumptions, and governing constraints;
- blockers and questions: dependency-scoped blockers and nonblocking open questions;
- artifacts: specialist-owned result or evidence references;
- presentation: optional `summary`/`full` mode, artifact selection, and redaction policy;
- planning readiness: readiness status, consumed increment, dependent blockers, next owner, and next
  activity;
- invalidation: changed evidence, affected result references, reason, and return phase.

## Identity and Revisions

- `lineage_id` identifies one logical requested outcome.
- `handoff_id` identifies one immutable handoff artifact within that lineage.
- `revision` increases monotonically for that handoff.
- `kind: interim` means a dependent blocker remains open.
- `kind: final` means the selected increment can be routed to planning or the selected companion.
- `kind: revision` records a later handoff after new evidence or implementation feedback; it must
  use a new `handoff_id` and link to its parent artifact through `parent_handoff_id`.
- Handoff lifecycle (`active`, `superseded`, `abandoned`) is separate from phase status.

Unchanged specialist results should keep their references across revisions. New revisions identify
downstream decisions made stale by changed evidence instead of silently deleting them.

## Phase Status and Dependency Scope

Phase statuses remain exactly:

- `completed`: usable for the declared scope and recommended next step;
- `needs-input`: missing information blocks this phase or a dependent activity;
- `not-applicable`: no responsible decision is required for this phase.

The `affects` field records which later phase or planning activity depends on the result. A
`needs-input` result therefore blocks only dependent work. An undecided optional jfoundry landing
does not block framework-neutral modeling or architecture guidance.

## Blockers

Each blocker has a stable `blocker_id`, an owning phase, affected work, the smallest blocking
question, a resolution requirement, and a lifecycle status. A later answer binds to the blocker
through `resolution_ref`; it does not overwrite the original question or evidence.

`planning_readiness.status` is `ready` only when every phase consumed by the selected increment is
`completed` or responsibly `not-applicable`, and no dependent blocker remains unresolved. Deferred
strategic work that the increment does not consume remains visible without blocking that increment.

## Evidence, Decisions, and Accepted Assumptions

The handoff preserves the original item-level status of every consumed domain decision:

```text
confirmed | inferred | proposed
```

An `inferred` or `proposed` item may drive downstream planning only as an explicitly accepted
assumption. The acceptance must identify its source evidence or decision record. Acceptance never
changes the original item status to `confirmed`.

Current-state evidence does not confirm a proposed target meaning. The handoff must keep these
statements and their evidence separate.

## Artifacts and Invalidation

Artifacts are referenced by stable IDs and repository-relative paths when persisted. A result may
be embedded for an ephemeral conversation, but it still receives an artifact ID in the handoff.
Artifacts may carry `classification` (`public`, `internal`, `confidential`, or `restricted`) and a
`redaction_required` flag. Summary projections should omit restricted content and point consumers
to the full artifact references only when the consumer is authorized to use them.

The coordinator must record conflicting or changed evidence explicitly. An invalidation entry names
the source item, the downstream result references it invalidates, the reason, and the phase to which
the question returns. Unaffected results remain active and reusable.

## Projection Order

The Markdown projection should present information in this order:

1. identity and lifecycle;
2. requested outcome and increment scope;
3. phase states and result references;
4. planning readiness and blockers;
5. confirmed decisions and accepted assumptions;
6. constraints, open questions, and deferred work;
7. artifacts and next owner;
8. invalidation or revision notes.

The Markdown projection is not an independently edited source of truth once a structured handoff is
available.

## Summary, Full Views, and Companion Consumption

The repository provides a small renderer for two views:

- `summary`: identity, scope, phase states, planning readiness, blockers, and decision summaries;
- `full`: the summary plus artifact references, open questions, and invalidation notes.

A process companion consumes the structured contract by checking `contract_version`, phase statuses,
`planning_readiness`, dependent blocker IDs, and artifact references. It owns its own proposal, plan,
tasks, approvals, and execution state; the plugin does not create companion-specific files or infer
their commands. A companion that cannot consume the declared contract version must stop at the
handoff boundary rather than guess.

## Operational Boundary and Future Phases

Semantic phase status must not be used to hide operational failures such as malformed output,
timeouts, or failed tool calls. The repository now includes executable semantic validation, a
blocker-resolution revision helper, and summary/full rendering tools. Explicit execution records,
database persistence, concurrency handling, and distributed recovery remain future work.

This first-generation contract deliberately does not introduce a database, workflow engine,
automatic resume, distributed locking, or process-companion-specific integration.
