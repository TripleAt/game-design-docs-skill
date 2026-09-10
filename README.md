# Game Design Docs Skill

ゲームのアイデアを、判断・実装・検証に使える企画書へ変換するための [Hermes Agent](https://hermes-agent.nousresearch.com/docs) スキル。

## できること

- 新規ゲームのワンページピッチ、企画書、GDDを構成する
- プレイヤーの約束、コアループ、選択、トレードオフを明確にする
- MVP、非目標、リスク、検証指標を切り出す
- 既存企画や新機能をフィーチャーブリーフへ整理する
- 事実・仮説・決定・未決定を分離し、企画の矛盾を見つける

## 構成

- `SKILL.md` — スキル本体。使う場面、作成手順、品質基準
- `templates/game-proposal.md` — ゲーム全体の企画書テンプレート
- `templates/one-page-pitch.md` — 会議向け一枚企画テンプレート
- `templates/feature-brief.md` — 既存ゲームの機能企画テンプレート
- `references/quality-checklist.md` — レビュー用チェックリスト
- `scripts/validate_game_proposal.py` — 企画書の必須セクション検証

## 使い方

1. Hermes Agentのスキルディレクトリにこのリポジトリを配置する。
2. `SKILL.md` を読み込む。
3. 作りたい資料の種類に応じて、テンプレートを選ぶ。
4. 企画の前提が不足していても、影響が小さいものは仮定として明記して進める。
5. 最後に品質チェックと検証計画を確認する。

短い依頼なら、最初から完全なGDDを書かず、次の5点を先に出すとよい。

- 一行のプレイヤー約束
- コアループ
- 企画の柱
- MVPと非目標
- 最大のリスクと最初の検証

## ローカル検証

依存パッケージなしで実行できる。

```bash
python scripts/validate_game_proposal.py templates/game-proposal.md
python -m unittest discover -s tests -v
```

## ライセンス

MIT License。詳細は [`LICENSE`](LICENSE) を参照。
