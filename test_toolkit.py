import tempfile
import unittest
from pathlib import Path

from src.oss_maintainer_toolkit import inspect_repository


class InspectRepositoryTests(unittest.TestCase):
    def test_detects_present_files_and_directories(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("hello", encoding="utf-8")
            (root / "LICENSE").write_text("MIT", encoding="utf-8")
            (root / "tests").mkdir()
            (root / ".github" / "workflows").mkdir(parents=True)
            report = inspect_repository(root)
            self.assertTrue(report["checks"]["readme"]["present"])
            self.assertTrue(report["checks"]["licence"]["present"])
            self.assertTrue(report["checks"]["tests"]["present"])
            self.assertTrue(report["checks"]["github_actions"]["present"])
            self.assertFalse(report["checks"]["security_policy"]["present"])

    def test_reports_missing_files(self):
        with tempfile.TemporaryDirectory() as temp:
            report = inspect_repository(Path(temp))
            self.assertEqual(report["summary"]["present"], 0)
            self.assertIn("readme", report["summary"]["missing"])

    def test_rejects_non_directory(self):
        with tempfile.TemporaryDirectory() as temp:
            file_path = Path(temp) / "not-a-directory"
            file_path.write_text("x", encoding="utf-8")
            with self.assertRaises(ValueError):
                inspect_repository(file_path)


if __name__ == "__main__":
    unittest.main()
