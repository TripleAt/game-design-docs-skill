#!/usr/bin/env python3
"""Validate that a full game proposal contains its decision-critical sections."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS: dict[str, tuple[str, ...]] = {
    "overview": ("企画概要", "概要", "summary"),
    "intent": ("企画意図", "intent"),
    "reader": ("読者", "判断", "reader"),
    "player": ("プレイヤー", "体験", "player"),
    "concept": ("コンセプト", "concept"),
    "pillars": ("企画の柱", "非目標", "pillars"),
    "setting": ("世界観", "設定", "setting"),
    "controls": ("ゲーム画面", "操作方法", "controls"),
    "cycle": ("ゲームサイクル", "game cycle"),
    "motivation": ("動機", "モチベーション", "motivation"),
    "loop": ("コアループ", "core loop"),
    "systems": ("システム", "system"),
    "gameplay": ("ゲーム性", "gameplay"),
    "progression": ("進行", "資源", "経済", "progression"),
    "content": ("コンテンツ", "レベル", "content", "level"),
    "ux": ("ux", "チュートリアル", "アクセシビリティ"),
    "production": ("技術", "制作条件", "production"),
    "validation": ("mvp", "検証", "validation"),
    "risks": ("リスク", "未決定事項", "risk"),
    "presentation": ("プレゼン", "presentation"),
    "next": ("次の行動", "next action"),
}


def heading_texts(markdown: str) -> list[str]:
    """Return normalized ATX heading text, excluding fenced code blocks."""
    in_fence = False
    headings: list[str] = []
    for line in markdown.splitlines():
        if line.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            headings.append(match.group(1).casefold())
    return headings


def validate(path: Path) -> list[str]:
    """Return human-readable validation errors."""
    if not path.is_file():
        return [f"file not found: {path}"]

    headings = heading_texts(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for label, candidates in REQUIRED_SECTIONS.items():
        if not any(
            candidate.casefold() in heading
            for heading in headings
            for candidate in candidates
        ):
            errors.append(f"missing required section: {label}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Markdown proposal to validate")
    args = parser.parse_args(argv)

    errors = validate(args.path)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"OK: {args.path} contains all decision-critical sections")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
