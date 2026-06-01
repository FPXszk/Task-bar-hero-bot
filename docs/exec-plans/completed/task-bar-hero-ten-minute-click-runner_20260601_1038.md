# Task Bar Hero Ten Minute Click Runner

## 目的
- 現在の宝箱左クリック連打処理を、10 分に 1 回動かす実行スクリプトを追加する。
- 既存どおり、クリック時の対象名・座標・時刻をターミナルへ出力し続ける。
- デバッグ用スクリプトは残したまま、本番寄りの実行入口を分ける。

## 変更・作成・移動するファイル
- 作成: `docs/exec-plans/active/task-bar-hero-ten-minute-click-runner_20260601_1038.md`
- 変更予定: `README.md`
- 変更予定: `src/task_bar_hero/debug_click_loop.py`
- 作成予定: `scripts/run_ten_minute_click_loop.py`
- 作成予定: `docs/exec-plans/completed/task-bar-hero-ten-minute-click-runner_20260601_1038.md`
- 変更予定: `docs/exec-plans/active/task-bar-hero-ten-minute-click-runner_20260601_1038.md` を完了時に `completed/` へ移動

## 実装内容
- 既存のクリック実装を再利用し、10 分ごとのサイクルで動く専用 CLI を追加する。
- クリック内容は現状維持とし、3 座標を順番に左クリック 5 回、クリック間 0.5 秒で処理する。
- 実行時ログはそのまま残し、どこをクリックしたかがターミナルで分かるようにする。
- デフォルトの待機時間は 600 秒にするが、必要なら CLI 引数で上書きできる最小構成にする。

## 影響範囲
- 変更対象はクリック実行の CLI と、その土台になる既存クリックモジュールのみ。
- 座標取得スクリプトや他の補助スクリプトには触れない。
- 合成処理や座標判定の高度化は今回の対象外。

## 実装ステップ
- [x] 10 分間隔実行用 CLI を追加する
- [x] 必要なら既存クリックモジュールを CLI 再利用しやすい形に整える
- [x] README の実行手順を追加・更新する
- [x] 構文チェックと `--help` 確認を行う
- [x] 計画ファイルを `completed/` に移動し、実装をコミット・push する

## テスト戦略
- GUI 自動操作のため、この Linux 環境では実クリック確認は行わない。
- 検証項目:
  - `python3 -m py_compile scripts/run_ten_minute_click_loop.py scripts/run_debug_right_click_loop.py src/task_bar_hero/debug_click_loop.py`
  - `python3 scripts/run_ten_minute_click_loop.py --help`
- 実際のクリック結果は、ユーザーの Windows 実行で確認してもらう。

## バリデーションコマンド
- `python3 -m py_compile scripts/run_ten_minute_click_loop.py scripts/run_debug_right_click_loop.py src/task_bar_hero/debug_click_loop.py`
- `python3 scripts/run_ten_minute_click_loop.py --help`
- `git status --short`

## リスク・注意点
- 10 分間隔でも、ゲームウィンドウ位置がずれると誤クリックする。
- スリープ復帰やフォーカス変化の影響は今回考慮しない。
- 長時間運用時の停止は `Ctrl+C` 前提のままとする。

## 明示的な除外
- Windows タスクスケジューラ連携
- 合成処理
- クリック対象の自動判定
- 停止ホットキーや監視機能の追加
