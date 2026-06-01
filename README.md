# Task Bar Hero Bot

Task Bar Hero の操作を段階的に自動化するためのリポジトリです。

まずは、ゲーム内の宝箱やボタンをクリックするために必要な座標を取得する最小デモを用意しています。

## 今回できること
- マウスクリックした位置のスクリーン座標を取得する
- 複数回クリックして、あとで座標を共有できる

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
