## リアルタイムデータソースの追加

プロッターにデータフィードを提供するために Raspberry Pi に追加できるセンサーはとてもたくさんあります。

Raspberry Pi 自体のCPUの温度という、組み込まれたデータソースから始めましょう。 もし `vcgencmd` ライブラリがインストールされていない場合は、ここでインストールしましょう。

--- collapse ---
---
title: Vcgencmd python ライブラリのインストール
---

インターネットに接続していることを確認してください。

キーボードの <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> を押して、Raspberry Pi上にターミナルウィンドウを開きます。

プロンプトで入力します: `sudo pip3 install vcgencmd` そして <kbd>Enter</kbd> キーを入力します。

確認のメッセージを待って(それほどかかりません)、ターミナルウィンドウを閉じます。

--- /collapse ---

--- task ---

Thonny の **Shell/REPL** を使用して、試しにCPUの温度を読み取るために、Pythonの次の行を入力します。

```python
>>> from vcgencmd import Vcgencmd
```
<kbd>Enter</kbd> を押します。

続けて入力します:
```python
>>> vcgm = Vcgencmd()
```
<kbd>Enter</kbd> を押します。

続けて入力します:
```python
>>> vcgm.measure_temp()
```
<kbd>Enter</kbd> を押します。

すると **Shell** が数値を返すでしょう(おそらく50前後のはずです)。これはCPUがどのくらいの熱さで動作しているかです。

--- /task ---

それでは、CPUに作業を行わせて、温めてみましょう。

--- task ---

Web ブラウザーを開いて、 YouTube でビデオを視聴します。 数秒したら Thonny に戻って、 Python の最後の行をもう一度実行すると、温度が上昇していることがわかります。

--- /task ---

Python で CPU の温度を読み取る方法を確認したので、 `plotter.py` を書き換えてこれをデータソースとして使用できます。

--- task ---

はじめに、ファイル上部にすでにある import 行の下に、 Vcgencmd ライブラリをインポートするための行を追加します:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 4
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor from vcgencmd import Vcgencmd

--- /code ---

--- /task ---

--- task --- vcgencmd オブジェクトを作成します:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 9
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor from vcgencmd import Vcgencmd

motor_y = Motor('A') motor_x = Motor('B') button = ForceSensor('C') vcgm = Vcgencmd()

motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

ランダムに生成された数値ではなく、リアルタイムな温度の値を使用するように、プログラムを変更します。 これをするには、 `randint(-180, 180)` を `vcgm.measure_temp()` に置き換える必要があります。

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 15
line_highlights: 16
---

while not button.is_pressed(): temp = vcgm.measure_temp() current_angle = motor_y.get_aposition()

--- /code ---

--- /task ---

Raspberry Pi の CPU の温度をプロッターのデータソースとして使用する前に、データソースによって生成される可能な最大値が、-180〜180のスケールに収まるように、数学的に変換する必要があります。

`vcgencmd` が返す温度の値の範囲は、約 50°C (Raspberry Pi がオンでもあまり使っていない時) から、高負荷時で 90°C 未満です (85°C になると、 Raspberry Pi はこの温度を維持するためにパフォーマンスを抑制しだします) 。 例えば、 40°C から 90°C の範囲をプロットしたいとすると、これをプロッターで利用可能な、 -180 から 180 の値にマップする必要があります。

ある範囲の値を別の範囲の値に再マップする関数を作成できます。

--- task ---

この関数を `while` ループの上に追加します。 温度の範囲と角度の範囲を取得して、温度を角度に再マッピングします。

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 12
line_highlights: 13
---

def remap(min_temp, max_temp, min_angle, max_angle, temp): temp_range = (max_temp - min_temp) motor_range = (max_angle - min_angle) mapped = (((temp - min_temp) * motor_range) / temp_range) + min_angle return int(mapped)

--- /code ---

これで、 `while` ループの中でこの関数を使用して、モーターが回転する新しい角度を計算できます。

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 21
line_highlights: 24
---

while not button.is_pressed(): temp = vcgm.measure_temp() current_angle = motor_y.get_aposition() new_angle = remap(50, 90, -170, 170, temp)

--- /code ---

--- /task ---

これでプログラムを実行できます。 前と同じように Raspberry Pi CPU を暖かくすると、ペンが徐々に上に移動するのがわかります。 ペンがあまり動かない場合は、 `min_free` と `max_temp` のパラメーターを自由に変更してください。

![ペンが移動して変動する線を描いている間に、紙がプロッターを移動する様子を示すアニメーション。](images/plotter_demo_2.gif)


--- save ---
