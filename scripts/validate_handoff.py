#!/usr/bin/env python3
"""Validate semantic rules for a Domain Architecture Handoff document."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = {
    "contract_version",
    "lineage_id",
    "handoff_id",
    "revision",
    "kind",
    "parent_handoff_id",
    "status",
    "request",
    "scope",
    "producer",
    "phases",
    "decisions",
    "blockers",
    "open_questions",
    "artifacts",
    "planning_readiness",
    "invalidation",
}
PHASES = {
    "domain-modeling",
    "architecture-guidance",
    "jfoundry-implementation-guidance",
}
STATUSES = {"completed", "needs-input", "not-applicable"}
ID_PATTERN = re.compile(r"^da-handoff-[A-Za-z0-9][A-Za-z0-9._-]*$")
LINEAGE_PATTERN = re.compile(r"^da-lineage-[A-Za-z0-9][A-Za-z0-9._-]*$")


def _required(document: dict[str, Any], names: set[str], errors: list[str]) -> None:
    for name in sorted(names - document.keys()):
        errors.append(f"missing required field: {name}")


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_document(document: Any) -> list[str]:
    """Return semantic validation errors; an empty list means valid."""

    errors: list[str] = []
    if not isinstance(document, dict):
        return ["handoff must be a JSON object"]

    _required(document, REQUIRED_TOP_LEVEL, errors)
    if errors:
        return errors

    if document["contract_version"] != "1.0":
        errors.append("contract_version must be 1.0")
    if not _is_non_empty_string(document["lineage_id"]) or not LINEAGE_PATTERN.fullmatch(document["lineage_id"]):
        errors.append("lineage_id must match da-lineage-*")
    if not _is_non_empty_string(document["handoff_id"]) or not ID_PATTERN.fullmatch(document["handoff_id"]):
        errors.append("handoff_id must match da-handoff-*")
    if not isinstance(document["revision"], int) or isinstance(document["revision"], bool) or document["revision"] < 1:
        errors.append("revision must be a positive integer")
    if document["kind"] not in {"interim", "final", "revision"}:
        errors.append("kind must be interim, final, or revision")
    if document["status"] not in {"active", "superseded", "abandoned"}:
        errors.append("status must be active, superseded, or abandoned")
    if document["kind"] == "revision":
        if not _is_non_empty_string(document["parent_handoff_id"]):
            errors.append("revision requires parent_handoff_id")
        if document["revision"] < 2:
            errors.append("revision handoff must have revision >= 2")
        if document["parent_handoff_id"] == document["handoff_id"]:
            errors.append("revision parent_handoff_id must differ from handoff_id")

    request = document["request"]
    if not isinstance(request, dict) or not _is_non_empty_string(request.get("outcome")):
        errors.append("request.outcome must be a non-empty string")

    scope = document["scope"]
    if not isinstance(scope, dict):
        errors.append("scope must be an object")
    else:
        if scope.get("decision_scope") not in {"landscape", "bounded-context", "increment"}:
            errors.append("scope.decision_scope is invalid")
        if scope.get("modeling_depth") not in {"strategic", "tactical", "both"}:
            errors.append("scope.modeling_depth is invalid")
        if scope.get("decision_scope") == "increment" and not _is_non_empty_string(scope.get("increment_id")):
            errors.append("increment scope requires scope.increment_id")

    producer = document["producer"]
    if not isinstance(producer, dict) or producer.get("skill") != "domain-architecture-workflow":
        errors.append("producer.skill must be domain-architecture-workflow")

    artifacts = document["artifacts"]
    artifact_ids: set[str] = set()
    if not isinstance(artifacts, list):
        errors.append("artifacts must be an array")
        artifacts = []
    for artifact in artifacts:
        if not isinstance(artifact, dict):
            errors.append("artifact entries must be objects")
            continue
        artifact_id = artifact.get("artifact_id")
        if not _is_non_empty_string(artifact_id):
            errors.append("artifact_id must be a non-empty string")
        elif artifact_id in artifact_ids:
            errors.append(f"duplicate artifact_id: {artifact_id}")
        else:
            artifact_ids.add(artifact_id)
        if artifact.get("path") is None and artifact.get("content_digest") is None:
            errors.append(f"artifact {artifact_id or '<unknown>'} needs path or content_digest")
        if artifact.get("classification") is not None and artifact.get("classification") not in {
            "public", "internal", "confidential", "restricted"
        }:
            errors.append(f"artifact {artifact_id or '<unknown>'} has invalid classification")
        if artifact.get("redaction_required") is not None and not isinstance(artifact.get("redaction_required"), bool):
            errors.append(f"artifact {artifact_id or '<unknown>'} redaction_required must be boolean")

    presentation = document.get("presentation")
    if presentation is not None:
        if not isinstance(presentation, dict):
            errors.append("presentation must be an object")
        else:
            if presentation.get("mode") not in {"summary", "full"}:
                errors.append("presentation.mode is invalid")
            if presentation.get("redaction_policy") not in {"none", "standard", "required"}:
                errors.append("presentation.redaction_policy is invalid")
            references = set(presentation.get("full_artifact_refs", []))
            unknown = references - artifact_ids
            if unknown:
                errors.append(f"presentation references unknown artifact(s): {', '.join(sorted(unknown))}")

    phases = document["phases"]
    phase_names: set[str] = set()
    if not isinstance(phases, list):
        errors.append("phases must be an array")
        phases = []
    for phase in phases:
        if not isinstance(phase, dict):
            errors.append("phase entries must be objects")
            continue
        name = phase.get("phase")
        if name not in PHASES:
            errors.append(f"unknown phase: {name}")
        elif name in phase_names:
            errors.append(f"duplicate phase: {name}")
        else:
            phase_names.add(name)
        status = phase.get("status")
        if status not in STATUSES:
            errors.append(f"invalid status for phase {name}")
        result_ref = phase.get("result_ref")
        if status == "completed" and not _is_non_empty_string(result_ref):
            errors.append(f"completed phase {name} requires result_ref")
        if _is_non_empty_string(result_ref) and result_ref not in artifact_ids and not result_ref.startswith("embedded:"):
            errors.append(f"phase {name} result_ref does not resolve: {result_ref}")
        if name == "jfoundry-implementation-guidance":
            if phase.get("applicability") not in {"applicable", "not-applicable", "undecided"}:
                errors.append("jfoundry phase requires valid applicability")
            if phase.get("applicability") == "undecided" and (status != "not-applicable" or result_ref is not None):
                errors.append("undecided jfoundry phase must be not-applicable with null result_ref")

    decisions = document["decisions"]
    if not isinstance(decisions, dict):
        errors.append("decisions must be an object")
        decisions = {}
    for entry in decisions.get("confirmed", []):
        if not isinstance(entry, dict):
            errors.append("confirmed decision entries must be objects")
            continue
        if entry.get("original_status") != "confirmed":
            errors.append(f"confirmed decision {entry.get('decision_ref')} must retain original_status confirmed")
    for entry in decisions.get("accepted_assumptions", []):
        if not isinstance(entry, dict):
            errors.append("accepted assumption entries must be objects")
            continue
        acceptance = entry.get("acceptance") or {}
        if entry.get("original_status") not in {"inferred", "proposed"}:
            errors.append(f"accepted assumption {entry.get('decision_ref')} must be inferred or proposed")
        if acceptance.get("status") != "accepted" or not _is_non_empty_string(acceptance.get("source_ref")):
            errors.append(f"accepted assumption {entry.get('decision_ref')} requires acceptance source_ref")

    blockers = document["blockers"]
    blocker_ids: set[str] = set()
    unresolved: set[str] = set()
    if not isinstance(blockers, list):
        errors.append("blockers must be an array")
        blockers = []
    for blocker in blockers:
        if not isinstance(blocker, dict):
            errors.append("blocker entries must be objects")
            continue
        blocker_id = blocker.get("blocker_id")
        if blocker_id in blocker_ids:
            errors.append(f"duplicate blocker_id: {blocker_id}")
        blocker_ids.add(blocker_id)
        if blocker.get("status") == "resolved":
            if not _is_non_empty_string(blocker.get("resolution_ref")):
                errors.append(f"resolved blocker {blocker_id} requires resolution_ref")
        elif blocker.get("status") == "open":
            unresolved.add(blocker_id)

    readiness = document["planning_readiness"]
    if not isinstance(readiness, dict):
        errors.append("planning_readiness must be an object")
    else:
        readiness_status = readiness.get("status")
        dependent = readiness.get("dependent_blockers") or []
        unknown_dependent = set(dependent) - blocker_ids
        if unknown_dependent:
            errors.append(f"unknown dependent blocker(s): {', '.join(sorted(unknown_dependent))}")
        if readiness_status == "ready" and (dependent or unresolved.intersection(dependent)):
            errors.append("ready handoff cannot have a dependent blocker")
        if readiness_status == "blocked" and not dependent:
            errors.append("blocked handoff requires dependent blockers")
        if document["kind"] == "final" and readiness_status != "ready":
            errors.append("final handoff requires planning_readiness.status ready")

    if document["kind"] == "revision" and document["revision"] >= 2:
        expected_suffix = f"-r{document['revision']}"
        if not document["handoff_id"].endswith(expected_suffix):
            errors.append(f"revision handoff_id must end with {expected_suffix}")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("handoff", type=Path, help="path to a JSON handoff document")
    args = parser.parse_args(argv)
    try:
        document = json.loads(args.handoff.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: cannot read handoff: {exc}", file=sys.stderr)
        return 2
    errors = validate_document(document)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    print(f"valid handoff: {document['handoff_id']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
