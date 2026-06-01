# Task Bar Hero Debug Left Click Burst

## 目的
- デバッグスクリプトを右クリックから左クリックへ切り替える。
- 共有済みの 3 つの宝箱座標を対象に、それぞれ 5 回ずつクリックする。
- 各クリックの間に 0.5 秒ディレイを入れ、クリックごとに座標をターミナルへ出力する。

## 変更・作成・移動するファイル
- 作成: `docs/exec-plans/active/task-bar-hero-debug-left-click-burst_20260601_1025.md`
- 変更予定: `README.md`
- 変更予定: `src/task_bar_hero/debug_click_loop.py`
- 変更予定: `scripts/run_debug_right_click_loop.py`
- 作成予定: `docs/exec-plans/completed/task-bar-hero-debug-left-click-burst_20260601_1025.md`
- 変更予定: `docs/exec-plans/active/task-bar-hero-debug-left-click-burst_20260601_1025.md` を完了時に `completed/` へ移動

## 実装内容
- 対象座標を次の 3 点に更新する。
  - `normal_chest_double`: `x=812`, `y=942`
  - `boss_chest_double`: `x=781`, `y=944`
  - `single_chest`: `x=777`, `y=943`
- 10 秒ごとのサイクルは維持しつつ、各サイクルで各対象を左クリック 5 回ずつ行う。
- クリック間に 0.5 秒待機し、各クリックごとに対象名・座標・時刻・何回目かを標準出力へ表示する。
- 既存 CLI 名はそのまま残しつつ、README 上の説明を左クリック連打仕様に更新する。

## 影響範囲
- 変更対象は既存のデバッグクリックスクリプトのみ。
- 座標取得スクリプトや他のモジュールには触れない。
- 5 分運用、合成処理、座標自動判定は今回の対象外。

## 実装ステップ
- [x] デバッグクリック本体を左クリック 5 連打仕様へ更新する
- [x] CLI と README の説明を実装に合わせて更新する
- [x] 構文チェックと `--help` 確認を行う
- [x] 計画ファイルを `completed/` に移動し、実装をコミット・push する

## テスト戦略
- GUI 自動操作のため、この Linux 環境では実クリック確認は行わない。
- 検証項目:
  - `python3 -m py_compile scripts/run_debug_right_click_loop.py src/task_bar_hero/debug_click_loop.py`
  - `python3 scripts/run_debug_right_click_loop.py --help`
- 実際のクリック結果は、ユーザーの Windows 実行で確認してもらう。

## バリデーションコマンド
- `python3 -m py_compile scripts/run_debug_right_click_loop.py src/task_bar_hero/debug_click_loop.py`
- `python3 scripts/run_debug_right_click_loop.py --help`
- `git status --short`

## リスク・注意点
- 0.5 秒ディレイでも、ゲーム側の反応が遅い場合は取りこぼしが出る可能性がある。
- 絶対座標のため、ウィンドウ位置が変わると誤クリックする。
- 既存 CLI 名は `run_debug_right_click_loop.py` のままだが、実際の挙動は左クリックに変わる。

## 明示的な除外
- スクリプト名の大規模整理
- クリック対象の動的切り替え
- 5 分本番ループ
- 合成処理
