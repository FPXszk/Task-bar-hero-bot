# Task Bar Hero Bot

Task Bar Hero の操作を段階的に自動化するためのリポジトリです。

まずは、ゲーム内の宝箱やボタンをクリックするために必要な座標を取得する最小デモを用意しています。

## 今回できること
- マウスクリックした位置のスクリーン座標を取得する
- 複数回クリックして、あとで座標を共有できる
- 宝箱座標をデバッグ用に定期左クリック連打する
- 宝箱座標を 10 分に 1 回の間隔で定期左クリック連打する

## セットアップ
Windows で仮想環境を作る例:

```bash
py -3 -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## 座標取得デモの使い方

```bash
py -3 scripts\capture_click_position.py
```

オプション確認:

```bash
py -3 scripts\capture_click_position.py --help
```

起動すると以下のように動きます。

1. コンソールに案内が表示される
2. Task Bar Hero の宝箱など、知りたい位置をマウスでクリックする
3. クリックごとに `x` と `y` が表示される
4. 終了したいときは `Esc` キー、または `Ctrl+C`

## 返してほしい情報
次の形式で、そのまま貼ってください。

```text
target: chest
x: 1234
y: 567
```

必要なら複数個まとめて大丈夫です。

```text
target: chest
x: 1234
y: 567

target: merge_button
x: 1400
y: 590
```

## 注意
- 取得されるのは画面全体の絶対座標です。
- 今回は座標取得だけです。5 分ごとの自動クリックや合成ロジックはまだ入れていません。

## デバッグ左クリック連打ループ
共有済みの次の座標を使って、順番に左クリックします。

- `normal_chest_double`: `x=812`, `y=942`
- `boss_chest_double`: `x=781`, `y=944`
- `single_chest`: `x=777`, `y=943`

デフォルトでは 3 秒待機してから開始し、10 秒ごとに 3 箇所を順番に処理します。各対象では 5 回ずつ左クリックし、クリック間は 0.5 秒待機します。

```bash
py -3 scripts\run_debug_right_click_loop.py
```

待機秒数やループ間隔、連打間隔を変える場合:

```bash
py -3 scripts\run_debug_right_click_loop.py --startup-delay-seconds 5 --interval-seconds 10 --click-delay-seconds 0.5
```

実行中は各クリックの対象名、座標、時刻、何回目のクリックかがターミナルに表示されます。停止したいときは `Ctrl+C` です。

## 10 分間隔クリックループ
同じ 3 つの座標に対して、10 分ごとに左クリック連打を行う本番寄りの実行スクリプトです。

```bash
py -3 scripts\run_ten_minute_click_loop.py
```

デフォルトでは 600 秒ごとにサイクルを回します。待機秒数や間隔を変えたい場合:

```bash
py -3 scripts\run_ten_minute_click_loop.py --startup-delay-seconds 5 --interval-seconds 600 --click-delay-seconds 0.5
```

このスクリプトでも、クリックごとの対象名、座標、時刻、何回目のクリックかをターミナルに表示します。停止したいときは `Ctrl+C` です。
