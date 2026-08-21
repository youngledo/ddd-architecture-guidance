# Event Storming

Use this when a workflow has multiple steps, policies, external systems, asynchronous reactions, retries, compensations, or unclear ownership.

## Modeling Elements

- Command: an intent to do something, usually imperative, e.g. `Submit Order`.
- Candidate Business Fact/Event: something that happened in business time, stated in past tense,
  e.g. `Order Submitted`; discovery does not yet make it a formal Domain Event.
- Domain Event: a promoted candidate whose occurrence matters to domain history, a later business
  decision, a policy, or collaboration.
- Policy: a rule or process that reacts to an event and may issue a command.
- Aggregate: the consistency boundary that handles commands and emits events.
- External System: something outside the domain model that sends commands or receives facts.
- Read Model: information shaped for a query, screen, report, notification, or decision support.

## Flow

1. List candidate business facts/events first in business time order.
2. Add commands that cause each candidate.
3. Add the actor or external system that issues each command.
4. Add policies that react to events and trigger later commands.
5. Mark rules that can reject commands.
6. Mark read models needed by users or policies.
7. Group related commands and candidate facts/events around aggregate candidates.
8. Split the flow when vocabulary or ownership changes.
9. Promote only the candidates with relevant business meaning to formal Domain Events.

## Heuristics

- Commands are requests and can fail; facts that already occurred should not be rejected after the
  fact.
- If a rule must reject a command, it belongs near the aggregate or domain service making that decision.
- If a reaction can happen later, it may be a policy/process rather than part of the aggregate transaction.
- If a read model combines multiple aggregates, keep it out of the write aggregate.
- A state change alone is insufficient reason to create a Domain Event. Promote a candidate only
  when its occurrence matters to domain history, later business decisions, a policy, or
  collaboration.
- Keep event meaning and business facts in the domain model. Transport schemas, Integration Events,
  publication, versioning, delivery guarantees, retries, and reliability mechanisms belong to
  downstream architecture or implementation guidance.

## Output Shape

Use a compact list:

```text
Actor/System -> Command -> Aggregate -> Candidate Fact/Event -> Policy/Reaction -> Read Model
```

Then record:

- Candidates promoted to Domain Events and their business relevance:
- Candidates retained only as discovery facts:
- Rejection rules:
- Immediate consistency needs:
- Eventually consistent reactions:
- External systems:
- Open questions:
