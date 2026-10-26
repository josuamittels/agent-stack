from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[3]


class AuthoringPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.create_skill = (ROOT / "skills/create-skill/SKILL.md").read_text(encoding="utf-8")
        cls.template = (ROOT / "templates/SKILL.md").read_text(encoding="utf-8")
        cls.package_setup = (
            ROOT / "disciplines/spawn-evals/references/package-setup.md"
        ).read_text(encoding="utf-8")

    def test_qualitative_only_skill_omits_evaluator_and_package(self):
        self.assertIn("If no meaningful objective check is possible, do not invoke Spawn Evals, create a package", self.create_skill)
        self.assertIn("omit this entire section and all Spawn Evals references from the target skill", self.create_skill)
        self.assertIn("create no package", self.package_setup)

    def test_mixed_skill_packages_only_measurable_criteria(self):
        self.assertIn("For skills with both qualitative goals and measurable requirements, package only the measurable requirements", self.create_skill)
        self.assertIn("Map each meaningful objective criterion to an input field and a reproducible script condition", self.package_setup)

    def test_runtime_template_is_removed_when_no_objective_check_applies(self):
        self.assertIn("If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill", self.template)


if __name__ == "__main__":
    unittest.main()
