#!/usr/bin/env python3
"""Render a structured handoff as a compact summary or full Markdown projection."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _line(value: Any) -> str:
    return str(value) if value is not None else "—"


def render_handoff(document: dict[str, Any], mode: str = "summary") -> str:
    if mode not in {"summary", "full"}:
        raise ValueError("mode must be summary or full")

    request = document.get("request", {})
    scope = document.get("scope", {})
    readiness = document.get("planning_readiness", {})
    lines = [
        "# Domain Architecture Handoff",
        "",
        f"- Lineage: `{_line(document.get('lineage_id'))}`",
        f"- Handoff: `{_line(document.get('handoff_id'))}`",
        f"- Revision: `{_line(document.get('revision'))}` ({_line(document.get('kind'))}; {_line(document.get('status'))})",
        f"- Outcome: {_line(request.get('outcome'))}",
        f"- Scope: {_line(scope.get('decision_scope'))} / {_line(scope.get('modeling_depth'))}",
        "",
        "## Planning Readiness",
        "",
        f"- Status: **{_line(readiness.get('status'))}**",
        f"- Next owner: {_line(readiness.get('next_owner'))}",
        f"- Next step: {_line(readiness.get('recommended_next_step'))}",
    ]

    if readiness.get("dependent_blockers"):
        lines.append(f"- Dependent blockers: {', '.join(readiness['dependent_blockers'])}")

    lines.extend(["", "## Phases", ""])
    for phase in document.get("phases", []):
        applicability = phase.get("applicability")
        suffix = f"; applicability={applicability}" if applicability else ""
        lines.append(f"- `{phase.get('phase')}`: **{phase.get('status')}**{suffix}")

    blockers = document.get("blockers", [])
    lines.extend(["", "## Blockers", ""])
    if blockers:
        for blocker in blockers:
            lines.append(
                f"- `{blocker.get('blocker_id')}` ({blocker.get('status')}): {blocker.get('question')}"
            )
    else:
        lines.append("- None")

    decisions = document.get("decisions", {})
    lines.extend(["", "## Decisions", ""])
    confirmed = decisions.get("confirmed", [])
    assumptions = decisions.get("accepted_assumptions", [])
    if not confirmed and not assumptions:
        lines.append("- None")
    for decision in confirmed:
        lines.append(f"- Confirmed `{decision.get('decision_ref')}`: {decision.get('statement')}")
    for decision in assumptions:
        lines.append(
            f"- Accepted assumption `{decision.get('decision_ref')}` "
            f"({decision.get('original_status')}): {decision.get('statement')}"
        )

    if mode == "full":
        lines.extend(["", "## Artifacts", ""])
        artifacts = document.get("artifacts", [])
        if artifacts:
            for artifact in artifacts:
                location = "[redacted]" if artifact.get("redaction_required") else (
                    artifact.get("path") or artifact.get("content_digest") or "embedded"
                )
                classification = artifact.get("classification")
                label = f"; classification={classification}" if classification else ""
                lines.append(f"- `{artifact.get('artifact_id')}` ({artifact.get('kind')}): `{location}`{label}")
        else:
            lines.append("- None")

        lines.extend(["", "## Open Questions", ""])
        questions = document.get("open_questions", [])
        lines.extend(f"- {question}" for question in questions) if questions else lines.append("- None")

        lines.extend(["", "## Invalidation", ""])
        invalidation = document.get("invalidation", [])
        if invalidation:
            for item in invalidation:
                lines.append(
                    f"- `{item.get('source_ref')}` invalidates "
                    f"{', '.join(item.get('invalidates', []))}: {item.get('reason')}"
                )
        else:
            lines.append("- None")

    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="handoff JSON")
    parser.add_argument("--mode", choices=["summary", "full"], default="summary")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    document = json.loads(args.input.read_text(encoding="utf-8"))
    rendered = render_handoff(document, args.mode)
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
