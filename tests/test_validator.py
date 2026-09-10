import tempfile
import unittest
from pathlib import Path

from scripts.validate_game_proposal import validate


VALID = """# Proposal
## 1. 企画概要
## 2. プレイヤーと体験の約束
## 3. 企画の柱と非目標
## 4. コアループ
## 5. ゲームシステム
## 6. 進行・資源・経済
## 7. コンテンツとレベル構造
## 8. UX・チュートリアル・アクセシビリティ
## 9. 技術・制作条件
## 10. MVP・検証計画
## 11. リスクと未決定事項
## 12. 次の行動
"""


class ValidatorTests(unittest.TestCase):
    def test_accepts_decision_critical_sections(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "proposal.md"
            path.write_text(VALID, encoding="utf-8")
            self.assertEqual(validate(path), [])

    def test_ignores_headings_inside_code_fences(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "proposal.md"
            path.write_text("```\n## 企画概要\n```\n", encoding="utf-8")
            self.assertIn("missing required section: overview", validate(path))

    def test_reports_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.md"
            self.assertEqual(validate(path), [f"file not found: {path}"])


if __name__ == "__main__":
    unittest.main()
