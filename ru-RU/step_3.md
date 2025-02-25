## Задаём диапазон рисования

На этом шаге мы будем контролировать направление, в котором вращаются двигатели (по часовой стрелке или против часовой стрелки), чтобы установить максимальную точку перемещения в каждом направлении.

--- collapse ---
---
title: Почему тебе нужно менять способ движения двигателей
---

Твой двигатель всегда будет выбирать кратчайший путь к новому положению.

Например, если двигатель находится в положении 170 градусов, а следующая позиция -170 градусов, он будет двигаться по часовой стрелке, проходя через положение 180 градусов, чтобы добраться до места назначения как можно быстрее.

![Видеоклип, показывающий двигатель LEGO® Technic™ с прикрепленным черным балочным элементом. Двигатель вращается, а прикрепленная балка вращается, как часовая стрелка, в ответ на данные. Двигатель поворачивается на полные 360 градусов, двигаясь по часовой стрелке и против часовой стрелки, а иногда проходя через нулевое положение в любом направлении.](images/motor_through_zero.gif)

Это нормально для нашей симуляции, но наш плоттер не будет иметь такой свободы передвижения. Как только ручка достигает верхней или нижней части бумаги (ось Y), она не может продолжать движение вверх, чтобы выйти из нижней части — она сломается. Таким образом, твой плоттер должен быть защищен от перемещения по часовой стрелке за отметку 180 градусов.

Этого можно добиться, изменив поведение двигателя при перемещении в нужную позицию. Ты можешь сделать это, передав дополнительный параметр `direction=` функции `run_to_position()`. Ты можетешь установить это значение на `«по часовой стрелке»`, `«против часовой стрелки»` или `«кратчайший путь»`, что является поведением «кратчайшего пути» по умолчанию.

![Видеоклип, показывающий двигатель LEGO® Technic™ с прикрепленным черным балочным элементом. Двигатель вращается, а прикрепленная балка вращается, как часовая стрелка, в ответ на данные. Двигатель поворачивается от 0 до 180 градусов, но никогда не проходит через ноль.](images/motor_not_zero.gif)

Так, например, `motor_y.run_to_position(50, 100, direction="anticlockwise")` приведет двигатель в положение 50 градусов, вращая его против часовой стрелки на максимальной скорости.

Можно добавить **условную проверку** в твой цикл, чтобы гарантировать, что двигатель никогда не проходит через 180 градусов и всегда перемещается от большего угла к меньшему, поворачиваясь против часовой стрелки.

Ты можешь найти последнее положение двигателя, используя `motor_y.get_aposition`.

--- /collapse ---

--- task ---

Проверь текущий угол двигателя в верхней части цикла `while`.

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

Теперь в цикле `while` ты можешь добавить проверку, чтобы увидеть, является ли текущее значение `new_angle` больше или меньше, чем `current_angle`.

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

Запусти свой код. Эти условные тесты предотвратят изменение мотором значения от отрицательного до положительного при прохождении через 180 градусов (и наоборот).

--- /task ---

--- save ---

