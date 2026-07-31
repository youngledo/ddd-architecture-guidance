# Maintaining `using-jfoundry`

These instructions apply only when changing this skill or its bundled references.

## Content Ownership

- Keep downstream project decisions, architecture boundaries, and version-aware documentation routing here.
- Do not duplicate JFoundry versioned implementation facts: Maven coordinates, configuration properties, compatibility matrices, verification results, or starter catalogues belong to the selected JFoundry release documentation.
- Stable JFoundry annotations, contracts, and base types may appear when they are necessary to express a template or a downstream implementation pattern. Route their exact semantics and version-specific mechanics to the selected release documentation.
- Do not record a temporary incident, issue investigation, or workaround unless it has become a stable downstream contract that every affected project must follow.

## Change Check

Before adding guidance, decide whether it is a stable project decision. If it is a version-sensitive framework fact, replace it with a route to the selected release documentation instead.
