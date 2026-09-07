# Workflow Results

For the structured coordinator-owned handoff contract, read
[handoff-contract.md](handoff-contract.md). The JSON Schema lives at
`schemas/domain-architecture-handoff.schema.json`. This document remains the authority for phase
result semantics; the handoff contract adds identity, revision, dependency, artifact, and planning
readiness metadata without changing specialist ownership.

## Common Result Envelope

Return each phase result with these fields:

- **Phase**
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

Treat this envelope as a shared interoperability and content contract, not a mandatory file format. Each specialist owns and returns its phase-specific payload inside the envelope. The coordinator checks status and combines results; it does not rewrite or replace specialist guidance. Use **Artifacts** to reference persisted specialist results when available, but do not treat it as the only payload carrier.

When a structured handoff is emitted, the Markdown response is its human-readable projection. The
structured handoff references specialist results and artifacts rather than copying them into a new
coordinator-owned source of truth. Existing text-only consumers remain supported.

Mark a phase `completed` when its result is usable for the declared phase scope and recommended next step. Completion outside that scope is not implied. Mark it `needs-input` rather than guess when missing information blocks a responsible decision. Pause only dependent phase progression, preserve completed results, emit an interim `Domain Architecture Handoff` containing the blockers, and ask the smallest blocking question. Mark a phase `not-applicable` and record why it is unnecessary.

The handoff contract distinguishes phase status from handoff lifecycle and revision. An interim
handoff may become a later revision after a blocker is resolved; unaffected phase result references
remain reusable, while invalidated downstream decisions are recorded explicitly.

## Phase Order And Transitions

Run phases in this order:

1. Establish business context.
2. Classify the required decision scope and strategic, tactical, or combined modeling depth; do not
   force landscape analysis, full DDD, or architecture work when existing evidence makes it
   unnecessary. The coordinator selects depth and consumes the specialist result; it does not
   perform or rewrite strategic modeling.
3. Produce and consume the `Domain Modeling Result` from `domain-modeling` when needed.
4. Produce and consume the `Architecture Guidance Result` from `domain-architecture-guidance` when needed.
5. Produce and consume the `using-jfoundry` result only when jfoundry applies.
6. Produce the `Domain Architecture Handoff` and route it to detailed planning.

Move backward when later work invalidates earlier assumptions:

- Return from architecture to modeling for ambiguous domain facts or a proposed change to
  Subdomain scope, Bounded Context meaning, team or rule ownership, context relationships, or
  current/target intent.
- Return from jfoundry guidance to architecture when framework conventions conflict with chosen boundaries.
- Return from implementation or review to architecture when code drifts from the chosen architecture.
- Return from implementation to modeling when business meaning changes.

Preserve prior confirmed results that are unaffected by the change. State what changed, why it
changed, and which downstream results need revision.

## Framework Landing Applicability

Classify jfoundry applicability without making it a prerequisite for framework-neutral work:

- When the project uses jfoundry or the user explicitly requests jfoundry-specific landing, invoke `using-jfoundry` after the required domain and architecture assumptions are clear.
- When the project does not use jfoundry, skip `using-jfoundry` and record why no framework landing applies. Do not invoke the specialist merely to return `not-applicable`.
- When jfoundry use is undecided, continue Domain Modeling and Architecture Guidance without invoking `using-jfoundry`. Record the pending optional landing in the handoff. Ask the smallest blocking question only when the recommended next activity is framework-specific and the unresolved choice materially changes that activity.

An undecided optional framework landing does not make Domain Modeling or Architecture Guidance `needs-input`.

## Blocking Rules

Use `needs-input` for each example below only when the unresolved information prevents a responsible current or downstream decision. Otherwise record it as an assumption or open question and let the responsible specialist classify the detail:

- conflicting meanings for the same domain term;
- an invariant that would otherwise be inferred rather than confirmed;
- an unresolved transaction spanning aggregates;
- unknown delivery, ordering, retry, or idempotency semantics at an external boundary;
- an unknown that could change the architecture choice or dependency direction;
- a framework convention that conflicts with the chosen architecture;
- an exact dependency or runtime version that cannot be recommended safely from verified evidence.

## Process Companion Selection

Honor an explicit process choice and cooperate with an already active workflow. Do not ask the user to select a process companion for standalone modeling, architecture guidance, review, or jfoundry guidance. For an end-to-end request, ask only when the execution choice materially affects the handoff. Never select a companion merely because it is installed.

Treat Superpowers, OpenSpec, and SpecKit only as optional examples of process companions. Do not depend on them or reproduce their procedures.

When no companion is selected, identify plugin-managed detailed planning under
`docs/domain-architecture/plans/` as the next owner. When a companion is selected later, it consumes the persisted handoff and
owns only its own planning artifacts; rerun a specialist only for stale or conflicting evidence.

## Domain Architecture Handoff

Produce one composite handoff containing:

- the requested outcome;
- the selected process companion, if any;
- each phase state;
- result summaries and artifacts;
- the Domain Modeling scope and depth, preserved directly or by specialist artifact reference;
- affected Subdomains and Bounded Contexts for the selected increment;
- relevant context relationships, including exchanged business meaning and ownership;
- current-versus-target distinctions and semantic conflicts;
- deferred strategic areas, distinguishing blockers on the selected increment from unrelated
  future work;
- confirmed decisions;
- explicitly accepted assumptions consumed by Architecture Guidance or planning, preserving each
  assumption's original item status and acceptance source/evidence rather than relabeling it as a
  confirmed decision;
- governing constraints;
- open questions, including blockers;
- the framework landing, or why none applies;
- the application runtime integration policy when a runtime decision makes it relevant;
- planning readiness for the selected increment, including its explicit non-goals and dependent blockers;
- the next planning owner: plugin-managed planning or the selected process companion;
- the recommended next activity.

Keep distinctions explicit among domain-modeling decisions, architecture-style constraints, framework conventions, heuristics, and project policies.

The coordinator may summarize or reference a specialist payload, but it must preserve the evidence
state of every consumed domain item. A proposed target cannot appear under confirmed decisions. It
may support a dependent handoff only as an explicitly accepted assumption with its acceptance
source/evidence, consistently with the Architecture Guidance Result.
