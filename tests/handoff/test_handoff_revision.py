import copy
import unittest

from scripts.handoff_revision import resolve_blocker
from tests.handoff.test_validate_handoff import valid_interim


class HandoffRevisionTests(unittest.TestCase):
    def test_resolving_blocker_creates_new_immutable_revision(self):
        original = valid_interim()
        revised = resolve_blocker(original, "B-001", "decision-record:ADR-014")

        self.assertIsNot(revised, original)
        self.assertEqual(revised["lineage_id"], original["lineage_id"])
        self.assertEqual(revised["revision"], 2)
        self.assertEqual(revised["kind"], "revision")
        self.assertEqual(revised["parent_handoff_id"], original["handoff_id"])
        self.assertNotEqual(revised["handoff_id"], original["handoff_id"])
        self.assertEqual(revised["blockers"][0]["status"], "resolved")
        self.assertEqual(revised["blockers"][0]["resolution_ref"], "decision-record:ADR-014")
        self.assertEqual(original["blockers"][0]["status"], "open")

    def test_resolving_unknown_blocker_fails(self):
        with self.assertRaises(ValueError):
            resolve_blocker(valid_interim(), "B-404", "E-404")


if __name__ == "__main__":
    unittest.main()
