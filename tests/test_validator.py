import tempfile
import unittest
from pathlib import Path

from scripts.validate_game_proposal import validate


VALID = """# Proposal
## 1. 企画概要
## 1.5 企画意図
## 1.6 読者と判断
## 2. プレイヤーと体験の約束
### コンセプト
## 3. 企画の柱と非目標
## 4. 世界観・設定
## 5. ゲーム画面・操作方法
## 6. ゲームサイクルとコアループ
### 動機の矢印
## 7. ゲームシステム
### ゲーム性の仕組み
## 8. 進行・資源・経済
## 9. コンテンツとレベル構造
## 10. UX・チュートリアル・アクセシビリティ
## 11. 技術・制作条件
## 12. MVP・検証計画
## 13. リスクと未決定事項
## 14. 次の行動
## 15. プレゼン要約と想定質問
"""


class ValidatorTests(unittest.TestCase):
    def test_accepts_decision_critical_sections(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "proposal.md"
            path.write_text(VALID, encoding="utf-8")
            self.assertEqual(validate(path), [])

    def test_requires_reader_concept_gameplay_and_presentation_sections(self):
        legacy = (
            VALID.replace("## 1.6 読者と判断\n", "")
            .replace("### コンセプト\n", "")
            .replace("### 動機の矢印\n", "")
            .replace("### ゲーム性の仕組み\n", "")
            .replace("## 15. プレゼン要約と想定質問\n", "")
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "legacy.md"
            path.write_text(legacy, encoding="utf-8")
            errors = validate(path)
            for section in ("reader", "concept", "motivation", "gameplay", "presentation"):
                self.assertIn(f"missing required section: {section}", errors)

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
