## プロット範囲を作る

このステップでは、各方向の最大の移動地点を決めるために、モーターが移動する方向 (時計回りか反時計回り) を制御します。

--- collapse ---
---
title: モーターの動き方を変える必要がある理由
---

モーターは常に最短の経路で新しい位置に向かいます。

例えば、モーターが170度にあって次の位置が-170度の時、モーターは目的の角度に早く到着することを優先して時計回りに回転し180度を通過します。

![黒い梁の要素が取り付けられた LEGO® Technic™ モーターを示す動画。 データに応じて、モーターに取り付けられた梁が時計の針のように回転します。 モーターは時計回りや反時計回りに移動して完全に360度回転し、場合によっていずれかの方向でゼロ位置を通過します。](images/motor_through_zero.gif)

シミュレーションなら問題ありませんが、プロッターはそれほど自由に動くことはできません。 ペンが紙の上または下 (y軸) に到達すると、それ以上は動くことができなくなり、いずれ壊れてしまいます。 よって、プロッターが時計回りに180度を超えて移動しないようにする必要があります。

これは、指定の位置に移動するときのモーターの動作を変更することで実現できます。 `direction=` パラメーターを `run_to_position()` 関数に渡しましょう。 値には `"clockwise"` 、 `"anticlockwise"` 、 `"shortest"` を設定でき、デフォルトでは「最短経路("shortest")」で動作します。

![黒い梁の要素が取り付けられた LEGO® Technic™ モーターを示す動画。 データに応じて、モーターに取り付けられた梁が時計の針のように回転します。 モーターが0度から180度の間で回転しますが、0度は通過しません。](images/motor_not_zero.gif)

つまり、たとえば `motor_y.run_to_position(50, 100, direction="anticlockwise")` は、モーターを50度の位置に、最大速度で反時計回りに回転します。

ループに**条件チェック**を追加することで、モーターが180度を通過せず反時計回りに回転して、常に高い角度から低い角度に移動できるようになります。

モーターの最新の位置は、 `motor_y.get_aposition` で見つけることができます。

--- /collapse ---

--- task ---

`while` ループの冒頭でモーターの現在の角度を確認します。

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 7
line_highlights: 8
---

while True:
    current_angle = motor_y.get_aposition()
    new_angle = randint(-180, 180)
    print(new_angle)
    motor_y.run_to_position(new_angle, 100)
    sleep(0.1)

--- /code ---

--- /task ---

--- task ---

これで、 `while` ループの中で、現在の `new_angle` の値が `current_angle` より大きいか小さいかのチェックを追加することができます。

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 7
line_highlights: 11-16
---

while True:
    current_angle = motor_y.get_aposition()
    new_angle = randint(-180, 180)
    print(new_angle)
    if new_angle > current_angle:
        motor_y.run_to_position(new_angle, 100, direction="clockwise")
        print('Turning CW')
    elif new_angle < current_angle:
        motor_y.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)
    
--- /code ---

--- /task ---

--- task ---

コードを実行しましょう。 これらの条件テストによって、モーターが180度を通過して負の値から正の値 (あるいはその逆) に変化するのを防げます。

--- /task ---

--- save ---

