import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

path = Path(__file__).resolve().parents[1] / "skills/android-tutorial-creator/scripts/create_tutorial.py"
spec = importlib.util.spec_from_file_location("scaffold", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ScaffoldTests(unittest.TestCase):
    def test_creates_honest_outline(self):
        with tempfile.TemporaryDirectory() as directory:
            result = module.create_tutorial("Compose State", "compose-state", "beginner", directory)
            brief = json.loads((result / "lesson.json").read_text())
            self.assertEqual(brief["status"], "outline")
            self.assertFalse(brief["sample_generated"])
            self.assertEqual(brief["checks_run"], [])
            self.assertIn("# Compose State", (result / "README.md").read_text())
            self.assertNotIn("{{topic}}", (result / "README.md").read_text())

    def test_existing_lesson_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            result = module.create_tutorial("Original", "lesson", "beginner", directory)
            (result / "README.md").write_text("Learner edits")
            with self.assertRaises(FileExistsError):
                module.create_tutorial("Replacement", "lesson", "advanced", directory)
            self.assertEqual((result / "README.md").read_text(), "Learner edits")

    def test_rejects_traversal_and_absolute_slugs(self):
        with tempfile.TemporaryDirectory() as directory:
            for slug in ["../escape", "/tmp/escape", "a/b", "", "Bad Name", "a--b"]:
                with self.subTest(slug=slug), self.assertRaises(ValueError):
                    module.create_tutorial("Topic", slug, "beginner", directory)
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_rejects_invalid_brief(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                module.create_tutorial("   ", "lesson", "beginner", directory)
            with self.assertRaises(ValueError):
                module.create_tutorial("Topic", "lesson", "expert", directory)
