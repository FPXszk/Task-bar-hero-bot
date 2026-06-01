# Task Bar Hero Bootstrap And Click Demo

## 目的
- Git 未管理の本プロジェクトを GitHub に push できる状態へ整える。
- Task Bar Hero のクリック位置を取得するための最小 Python デモを作る。
- 次段階の自動クリック実装に使える座標取得結果をユーザーが返せる形にする。

## 変更・作成・移動するファイル
- 作成: `docs/exec-plans/active/task-bar-hero-bootstrap-and-click-demo_20260601_0951.md`
- 作成予定: `.gitignore`
- 作成予定: `README.md`
- 作成予定: `requirements.txt`
- 作成予定: `scripts/capture_click_position.py`
- 作成予定: `src/task_bar_hero/__init__.py`
- 作成予定: `src/task_bar_hero/click_probe.py`
- 作成予定: `docs/exec-plans/completed/task-bar-hero-bootstrap-and-click-demo_20260601_0951.md`
- 変更予定: `docs/exec-plans/active/task-bar-hero-bootstrap-and-click-demo_20260601_0951.md` を完了時に `completed/` へ移動

## 実装内容
- Git リポジトリを初期化し、GitHub に `Task-bar-hero-bot` を public で作成して push する。
- Windows 上でマウスクリック位置を取得できる最小 Python スクリプトを追加する。
- 実行方法と、ユーザーが返すべき座標情報を README に記載する。

## 影響範囲
- 新規プロジェクトの初期ファイル追加のみ。
- 既存 workflow や既存ドキュメントは原則変更しない。
- クリック取得はデモ用途に限定し、自動操作ループや合成ロジックは今回は実装しない。

## 実装ステップ
- [x] Git 管理を初期化し、初回 push の前提を整える
- [x] Windows で使う Python 依存と `.gitignore` を追加する
- [x] クリック座標取得デモを `scripts/` と `src/` に実装する
- [x] 実行手順と返却フォーマットを README に記載する
- [x] 最低限の動作確認を行う
- [x] 計画ファイルを `completed/` に移動し、実装をコミット・push する

## テスト戦略
- RED/GREEN が必要な複雑なロジックではないため、今回は手動検証を主とする。
- 検証項目:
  - `python3 -m py_compile scripts/capture_click_position.py src/task_bar_hero/click_probe.py`
  - `python3 scripts/capture_click_position.py --help`
- Windows 実機でのクリック取得は、ユーザー実行で確認してもらう前提にする。

## バリデーションコマンド
- `python3 -m py_compile scripts/capture_click_position.py src/task_bar_hero/click_probe.py`
- `python3 scripts/capture_click_position.py --help`
- `git status --short`

## リスク・注意点
- この Linux 環境では Windows GUI クリック取得の実動作までは確認できない。
- `pyautogui` は実行環境によって追加依存が必要になる可能性があるため、最初は座標取得に必要な最小依存に限定する。
- GitHub 初回 push では、既存の `.github/workflows/` も含めて公開されるため、その点は前提として扱う。

## 明示的な除外
- 宝箱の自動クリックループ
- 5 分ごとの定期実行
- アイテム合成ロジック
- 画像認識やウィンドウ検出の高度化
