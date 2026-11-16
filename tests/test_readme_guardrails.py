"""Regression checks for public claims and safety caveats in the profile README."""

from pathlib import Path
import unittest


README = Path(__file__).resolve().parents[1] / "README.md"


class ProfileReadmeGuardrails(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = README.read_text(encoding="utf-8")

    def test_each_selected_evidence_row_links_to_a_project_repository(self):
        section = self.text.split("## Selected Evidence", 1)[1].split("## Selected Projects", 1)[0]
        rows = [line for line in section.splitlines() if line.startswith("| [")]
        self.assertTrue(rows, "Selected Evidence must contain linked evidence rows")
        for row in rows:
            self.assertRegex(row, r"\[[^\]]+\]\(https://github\.com/[^/\s)]+/[^/\s)]+\)")

    def test_reported_metrics_are_not_presented_as_independently_validated(self):
        section = self.text.split("## Selected Evidence", 1)[1].split("## Selected Projects", 1)[0]
        self.assertIn("not be interpreted as production performance", section)
        self.assertIn("not independent validation", section)
        self.assertIn("not been independently reproduced", section)

    def test_healthcare_project_is_explicitly_non_clinical(self):
        section = self.text.split("### Healthcare Recommendation System", 1)[1].split("### Urban Scene Semantic Segmentation", 1)[0]
        self.assertIn("synthetic data", section)
        self.assertIn("not a clinical product", section)
        self.assertIn("not a clinical product or medical decision-support system", section)
        self.assertIn("not intended for use in patient care", section)


if __name__ == "__main__":
    unittest.main()
