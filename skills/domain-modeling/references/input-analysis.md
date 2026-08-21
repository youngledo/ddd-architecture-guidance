# Input Analysis

Use this when the input is a requirements document, user story, support ticket, database schema, API contract, existing code, or a verbal workflow description.

## Extract From Text

Identify:

- Actors: people, systems, organizations, roles.
- Business capabilities: what the business must be able to do, without assuming a system or team boundary.
- Commands: user or system intents, usually verbs.
- Candidate business facts/events: facts that already happened, usually past tense. Promote a
  candidate to a Domain Event only when its occurrence has business significance for history,
  later decisions, policies, or collaboration; a state change alone is not sufficient.
- Policies: rules that react to events or decide whether commands are allowed.
- State: statuses, lifecycle stages, counters, balances, reservations, allocations.
- Invariants: rules that must always hold.
- Decision and rule ownership: who has authority to define or change a business decision.
- Organizational ownership: current team or organizational responsibility, treated as evidence rather than a target boundary.
- Conflicting meanings: terms, rules, or models that vary across workflows or owners.
- Current and target intent: observed current meaning versus the desired business model.
- Cross-context dependencies: business facts, decisions, or capabilities required from another context.
- External systems: payment providers, identity services, brokers, search, ERP, files.
- Read needs: screens, reports, dashboards, exports, notifications.
- Exceptions: cancellation, timeout, retry, compensation, partial failure, manual override.

Prefer exact business words when they appear. If two words look similar, keep both until the domain confirms whether they are synonyms.

## Extract From Existing Structures

Tables, APIs, packages, services, and organization charts are evidence of the current system, not the target domain model.

Look for:

- IDs that indicate entity or aggregate identity.
- Status fields that imply lifecycle commands.
- Audit fields that imply events or policies.
- Foreign keys that may be references across aggregates or contexts.
- Wide tables that may hide value objects.
- Join tables that may represent membership, assignment, allocation, or permission concepts.
- Endpoints named `create`, `update`, or `save` that may hide business commands.
- Packages or services that combine terms with conflicting rules or split one coherent decision across technical boundaries.
- Team or organization boundaries that reveal current ownership without proving a Subdomain or Bounded Context boundary.

Do not mirror every table as an aggregate or every package, service, or team as a Bounded Context. Ask what business decision and meaning the model must protect.

## Questions To Ask

- What action is the user or system trying to complete?
- What business rule can reject this action?
- What must be consistent immediately after the action?
- What can be eventually consistent?
- Who owns this concept and its vocabulary?
- Who owns the business decision or rule, and is that different from current system or team ownership?
- Where does the same term or fact have a conflicting meaning?
- Which current boundaries are observations, and which target boundaries are supported by business evidence?
- Which business fact, decision, or capability must cross a context boundary?
- What downstream process reacts after this fact happens?
- What historical edge cases caused bugs or manual corrections?

## Output

Produce a compact extraction list:

- Candidate terms:
- Candidate business capabilities/subdomains:
- Candidate commands:
- Candidate business facts/events:
- Candidate rules/invariants:
- Candidate states:
- External actors/systems:
- Ownership and cross-context signals:
- Observed current / desired target differences:
- Read/reporting needs:
- Open questions:
