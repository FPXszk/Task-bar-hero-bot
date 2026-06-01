# Task Bar Hero Debug Right Click Loop

## 目的
- 共有済み座標を使って、通常宝箱とボス宝箱を定期的に右クリックするデバッグスクリプトを追加する。
- デバッグしやすいように、各クリック実行時に対象名と座標をターミナルへ出力する。
- 本番前の確認用として、まずは 10 秒間隔で動かせるようにする。

## 変更・作成・移動するファイル
- 作成: `docs/exec-plans/active/task-bar-hero-debug-right-click-loop_20260601_1013.md`
- 変更予定: `README.md`
- 変更予定: `requirements.txt`
- 変更予定: `src/task_bar_hero/click_probe.py`
- 作成予定: `src/task_bar_hero/debug_click_loop.py`
- 作成予定: `scripts/run_debug_right_click_loop.py`
- 作成予定: `docs/exec-plans/completed/task-bar-hero-debug-right-click-loop_20260601_1013.md`
- 変更予定: `docs/exec-plans/active/task-bar-hero-debug-right-click-loop_20260601_1013.md` を完了時に `completed/` へ移動

## 実装内容
- 右クリック対象 2 点を固定座標で順番に処理するデバッグループを追加する。
- デフォルト間隔は 10 秒にし、各実行時に対象名・座標・時刻を標準出力へ表示する。
- 実行開始前に数秒の猶予を設け、ユーザーがゲーム画面へ戻る時間を確保する。
- 将来の 5 分間隔運用へ繋げやすいよう、間隔だけは CLI 引数で変更できる最小設計にする。

## 影響範囲
- 追加するのはデバッグ用途のクリック自動化のみ。
- 既存の座標取得スクリプトは壊さず、そのまま残す。
- 合成ロジック、画像認識、メニュー操作、キューブ操作は今回は実装しない。

## 実装ステップ
- [x] デバッグ右クリックループの本体を `src/` に実装する
- [x] 実行用 CLI を `scripts/` に追加する
- [x] 必要な依存関係と README の実行手順を更新する
- [x] 構文チェックと `--help` 確認を行う
- [x] 計画ファイルを `completed/` に移動し、実装をコミット・push する

## テスト戦略
- GUI 自動操作のため、この Linux 環境では実クリック確認は行わない。
- 検証項目:
  - `python3 -m py_compile scripts/run_debug_right_click_loop.py src/task_bar_hero/debug_click_loop.py src/task_bar_hero/click_probe.py`
  - `python3 scripts/run_debug_right_click_loop.py --help`
- 実際の右クリック結果は、ユーザーの Windows 実行で確認してもらう。

## バリデーションコマンド
- `python3 -m py_compile scripts/run_debug_right_click_loop.py src/task_bar_hero/debug_click_loop.py src/task_bar_hero/click_probe.py`
- `python3 scripts/run_debug_right_click_loop.py --help`
- `git status --short`

## リスク・注意点
- `pynput` による右クリックは、Windows の権限やフォーカス状態で期待どおり動かない場合がある。
- 画面基準の絶対座標を使うため、ゲームウィンドウ位置がずれると誤クリックする。
- 10 秒ループはデバッグ優先であり、長時間運用前提ではない。

## 明示的な除外
- 5 分間隔での本番運用ロジック
- 通常宝箱とボス宝箱以外のクリック自動化
- 合成処理
- 停止用ホットキーや高度な安全機構
