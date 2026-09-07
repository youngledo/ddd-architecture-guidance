import unittest

from scripts.render_handoff import render_handoff
from tests.handoff.test_validate_handoff import valid_interim


class RenderHandoffTests(unittest.TestCase):
    def test_summary_projection_contains_routing_information(self):
        rendered = render_handoff(valid_interim(), mode="summary")
        self.assertIn("Domain Architecture Handoff", rendered)
        self.assertIn("da-handoff-example-001-r1", rendered)
        self.assertIn("blocked", rendered)
        self.assertIn("B-001", rendered)
        self.assertNotIn("docs/domain-architecture/01-domain-modeling.md", rendered)

    def test_full_projection_contains_artifact_references(self):
        rendered = render_handoff(valid_interim(), mode="full")
        self.assertIn("docs/domain-architecture/01-domain-modeling.md", rendered)
        self.assertIn("domain-modeling-result", rendered)

    def test_full_projection_redacts_sensitive_artifact(self):
        document = valid_interim()
        document["artifacts"][0]["classification"] = "restricted"
        document["artifacts"][0]["redaction_required"] = True
        rendered = render_handoff(document, mode="full")
        self.assertIn("[redacted]", rendered)
        self.assertNotIn("docs/domain-architecture/01-domain-modeling.md", rendered)


if __name__ == "__main__":
    unittest.main()
