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
- `templates/presentation-brief.md` — 企画プレゼンの話順・接続文・想定質問
- `references/quality-checklist.md` — レビュー用チェックリスト
- `references/beginner-structure.md` — 初心者向け8項目の最小構成と図解の使い方
- `references/boot-camp-series.md` — 連載5本の要点とスキルへの反映
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

## 参考にした構成

初心者向け8項目に加えて、読者起点、コンセプトを判断軸にする考え方、システムとUXの対応、動機の矢印によるゲームサイクル、コンセプトから始めるプレゼンの流れを取り入れている。詳細は [`references/boot-camp-series.md`](references/boot-camp-series.md) を参照。

参考:

- [【ゲーム企画 BOOT CAMP!!】Part1 企画書はなんのために書く？](https://note.com/shuei_camp/n/n245a7b8b5acd)
- [【ゲーム企画 BOOT CAMP!!】Part2 コンセプトは迷える開発者の指針！](https://note.com/shuei_camp/n/ncb43760f1d55)
- [【ゲーム企画 BOOT CAMP!!】Part3 ゲームシステムとゲーム性](https://note.com/shuei_camp/n/n51b2a2ee7156)
- [【ゲーム企画 BOOT CAMP!!】Part4 長く遊ばせるための「ゲームサイクル」](https://note.com/shuei_camp/n/n0d4a8e56361c)
- [【ゲーム企画 BOOT CAMP!!】Part5 頭に入ってくるプレゼン方法](https://note.com/shuei_camp/n/n72103d08edb8)

## ローカル検証

依存パッケージなしで実行できる。

```bash
python scripts/validate_game_proposal.py templates/game-proposal.md
python -m unittest discover -s tests -v
```

## ライセンス

MIT License。詳細は [`LICENSE`](LICENSE) を参照。
