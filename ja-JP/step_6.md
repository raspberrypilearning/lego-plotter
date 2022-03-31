## ボタンコントロールを追加する

プロッターの実行を停止したり開始したりするために、作品にボタンを追加しましょう。

--- task ---

LEGO® SPIKE™ Prime フォースセンサーは、シンプルなボタンとして機能します。 これを Build HAT のポート C に接続します。

![LEGO® プロッターにフォースセンサーが追加された部分をクローズアップした写真。](images/force.jpg)

--- /task ---

--- task ---

`plotter.py` プログラムを編集して、ボタンコントロールを含めます。 `from buildhat import Motor` と書かれた行の最後に、コンマと、そのあとに `ForceSensor` (大文字と小文字**両方**を含めてください) を追加します:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 3
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor

--- /code ---

--- /task ---

--- task ---

モーター向けの似たような行の後に、ボタン向けのオブジェクトを作成する行を追加します。

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 7
---

motor_y = Motor('A') motor_x = Motor('B') button = ForceSensor('C') motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

メインループを `while True` から次のように変更します:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 13
line_highlights:
---

while not button.is_pressed(): current_angle = motor_y.get_aposition() new_angle = randint(-180, 180)

--- /code ---

--- /task ---

--- task ---

これで、ボタンを押すことでプロッターの動作を停止できます。 すべての片付けをしてから両方のモーターを停止するために、プログラムの最後に次の行を追加します。

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 19
line_highlights: 24-26
---

    elif new_angle < current_angle:
        motor_y.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)

motor_x.stop() motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

プロッターをテストする準備が整いました。 最終的なコードは以下のようになります:

--- code ---
---
language: python filename: plotter.py line_numbers: true
line_number_start: 1
---

# !/usr/bin/python3
from random import randint from time import sleep from buildhat import Motor, ForceSensor

button = ForceSensor('C') motor_y = Motor('A') motor_x = Motor('B')

motor_y.run_to_position(0, 100) motor_x.start(speed=-25)

while not button.is_pressed(): current_angle = motor_y.get_aposition() new_angle = randint(-180, 180) if new_angle > current_angle: motor_y.run_to_position(new_angle, 100, direction="clockwise") print('Turning CW') elif new_angle < current_angle: motor_y.run_to_position(new_angle, 100, direction="anticlockwise") print('Turning ACW') sleep(0.1)

motor_x.stop() motor_y.run_to_position(0, 100)

--- /code ---

--- task ---

プロッターの背面から紙を1枚、紙の前側の短辺がちょうどペンを越すあたりまで送ります。

--- /task ---

--- task ---

Thonny でプログラムを開始し、ペンがランダムなデータを紙にプロットするのを見てみましょう！

--- /task ---

--- task ---

紙を使用し終えたら、フォースセンサーのボタンを押してすべてを停止します。

--- /task ---

![プロッターが緑色のトレースを描いた紙の写真。](images/paper.JPG)

次のステップでは、入力データにリアルタイムデータソースを使用してみましょう！

--- save ---
