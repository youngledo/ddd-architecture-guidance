#!/usr/bin/env python3
"""Create immutable handoff revisions while resolving dependency blockers."""

from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any

try:
    from scripts.validate_handoff import validate_document
except ModuleNotFoundError:  # pragma: no cover - direct script execution
    from validate_handoff import validate_document


REVISION_SUFFIX = re.compile(r"-r[0-9]+$")


def resolve_blocker(document: dict[str, Any], blocker_id: str, resolution_ref: str) -> dict[str, Any]:
    """Return a new revision with one open blocker resolved; never mutate *document*."""

    if not isinstance(document, dict):
        raise ValueError("handoff must be an object")
    original_errors = validate_document(document)
    if original_errors:
        raise ValueError("cannot revise invalid handoff: " + "; ".join(original_errors))
    if not isinstance(resolution_ref, str) or not resolution_ref.strip():
        raise ValueError("resolution_ref must be a non-empty string")

    blocker = next((item for item in document["blockers"] if item.get("blocker_id") == blocker_id), None)
    if blocker is None:
        raise ValueError(f"unknown blocker: {blocker_id}")
    if blocker.get("status") != "open":
        raise ValueError(f"blocker is not open: {blocker_id}")

    revised = copy.deepcopy(document)
    revision = document["revision"] + 1
    revised["revision"] = revision
    revised["kind"] = "revision"
    revised["parent_handoff_id"] = document["handoff_id"]
    base_id = REVISION_SUFFIX.sub("", document["handoff_id"])
    revised["handoff_id"] = f"{base_id}-r{revision}"

    for item in revised["blockers"]:
        if item.get("blocker_id") == blocker_id:
            item["status"] = "resolved"
            item["resolution_ref"] = resolution_ref
            break

    dependent = revised["planning_readiness"].get("dependent_blockers", [])
    revised["planning_readiness"]["dependent_blockers"] = [
        current for current in dependent if current != blocker_id
    ]
    if not revised["planning_readiness"]["dependent_blockers"] and revised["planning_readiness"].get("status") == "blocked":
        revised["planning_readiness"]["status"] = "deferred"

    revised_errors = validate_document(revised)
    if revised_errors:
        raise ValueError("revision would be invalid: " + "; ".join(revised_errors))
    return revised


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="parent handoff JSON")
    parser.add_argument("output", type=Path, help="new revision JSON")
    parser.add_argument("--blocker", required=True, help="blocker ID to resolve")
    parser.add_argument("--resolution-ref", required=True, help="evidence or decision reference")
    args = parser.parse_args(argv)

    document = json.loads(args.input.read_text(encoding="utf-8"))
    revised = resolve_blocker(document, args.blocker, args.resolution_ref)
    args.output.write_text(json.dumps(revised, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"created revision: {revised['handoff_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
