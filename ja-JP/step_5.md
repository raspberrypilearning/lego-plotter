## 紙を送る

次に、2つ目のモーター用にプログラムを作成して、一定の速度でプロッターに紙を送ります。

--- task ---

後ろにある小さなホイールの下にA5サイズの紙 (または適当な紙からこのサイズに切り出します) を1枚送ります。

![紙がプロッターの裏側から送られてくるので、鉛筆の先が紙の縁に載っています。](images/paper_in.jpg)

--- /task ---

--- task ---

後部の (これらのホイールを駆動するための) LEGO® Technic™ モーターを Build HAT のポート B に接続します。

--- /task ---

--- task ---

前に作成した `motor_y` と同じように、このモーターに `motor_x` というオブジェクトを作成します:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 6
---

motor_y = Motor('A')
motor_x = Motor('B')
motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

--- task ---

`while True` ループの直前に、このモーターの回転を開始するための行を追加します:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 8
---

motor_y = Motor('A')
motor_x = Motor('B')
motor_y.run_to_position(0, 100)
motor_x.start(-25)

--- /code ---

--- /task ---

これで、プログラムが開始するとフィーダー用のモーターが毎分 -25 回転の一定した速度で動くようになります。 かっこ内の数字を変更して、速度を試してください。

--- task ---

コードを実行して、鉛筆が `y` 方向にランダムに移動しながら、用紙がプロッターによって送られることを確認します。

![鉛筆が y 軸に沿ってランダムに移動している間に、紙がプロッターを通過する様子を示すアニメーション。](images/feeding_paper.gif)

--- /task ---

モーターが用紙を送るのを止めるには、 **シェル** に次のように入力します。

```python
>>> from buildhat import Motor
>>> motor_x = Motor('B')
>>> motor_x.stop()
```

--- save ---


