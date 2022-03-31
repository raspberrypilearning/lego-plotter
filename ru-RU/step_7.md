## Добавляем источник данных в реальном времени

Существует огромное количество датчиков, которые ты можешь добавить к Raspberry Pi, чтобы обеспечить поток данных для твоего плоттера.

Начнем со встроенного источника данных: температуры процессора на самой Raspberry Pi. Если ты еще не установил библиотеку `vcgencmd`, сделай это сейчас.

--- collapse ---
---
title: Установка библиотеки Python Vcgencmd
---

Убедись, что ты подключён к Интернету.

Открой окно терминала на Raspberry Pi, нажав <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> на своей клавиатуре.

В командной строке введи: `sudo pip3 install vcgencmd` и нажми <kbd>Ввод</kbd>.

Дождись подтверждающего сообщения (это не займет много времени), затем закрой окно терминала.

--- /collapse ---

--- task ---

Используя **Оболочку** в Thonny, введи следующие строки Python, чтобы проверить и считать температуру процессора.

```python
>>> from vcgencmd import Vcgencmd
```
Нажми <kbd>Ввод</kbd>.

Введи:
```python
>>> vcgm = Vcgencmd()
```
Нажми <kbd>Ввод</kbd>.

Введи:
```python
>>> vcgm.measure_temp()
```
Нажми <kbd>Ввод</kbd>.

Ты должен увидеть, что **Оболока** возвращает числовое значение (оно должно быть где-то около 50) — это то, насколько сильно работает твой процессор.

--- /task ---

Теперь давай разогреемся, заставив ЦП немного поработать!

--- task ---

Открой веб-браузер и посмотри видео на YouTube. Через несколько секунд вернись к Thonny и повторно запусти последнюю строку Python, и ты должен увидеть, что температура увеличилась.

--- /task ---

Теперь, когда ты узнал, как считывать температуру процессора с помощью Python, ты можешь изменить свою программу `plotter.py`, чтобы она использовала температуру в качестве источника данных.

--- task ---

Во-первых, под существующими строками импорта в верхней части файла добавь строки для импорта библиотеки Vcgencmd:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
line_highlights: 4
---

from random import randint
from time import sleep
from buildhat import Motor, ForceSensor
from vcgencmd import Vcgencmd

--- /code ---

--- /task ---

--- task --- Создай объект vcgencmd:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
line_highlights: 9
---

from random import randint
from time import sleep
from buildhat import Motor, ForceSensor
from vcgencmd import Vcgencmd

motor_y = Motor('A')
motor_x = Motor('B')
button = ForceSensor('C')
vcgm = Vcgencmd()

motor_y.run_to_position(0, 100)
motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

Измени программу так, чтобы она использовала значения температуры в реальном времени, а не случайно сгенерированные числа. Для этого тебе нужно заменить `randint(-180, 180)` на `vcgm.measure_temp()`.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 15
line_highlights: 16
---

while not button.is_pressed():
    temp = vcgm.measure_temp()
    current_angle = motor_y.get_aposition()

--- /code ---

--- /task ---

Прежде чем ты сможешь использовать температуру процессора Raspberry Pi в качестве источника данных для твоего плоттера, ты должен убедиться, что максимально возможное значение, полученное источником данных, будет математически преобразовано, чтобы оно соответствовало шкале от -180 до 180.

Диапазон значений температуры, создаваемых `vcgencmd`, должен быть примерно от 50°C (когда Raspberry Pi включен, но мало что делает) до менее 90°C при интенсивной работе (при 85°C Raspberry Pi будет уменьшать его производительность, чтобы поддерживать температуру ниже этого значения). Допустим, ты хочешь отрисовать диапазон от 40° C до 90° C — тебе нужно сопоставить его с доступными значениями: от -180 до 180.

Ты можешь создать функцию для повторного сопоставления одного диапазона значений с другим диапазоном значений.

--- task ---

Добавь эту функцию над циклом `while`. Она возьмет диапазон температур и диапазон углов, а затем переназначит температуру в угол.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 12
line_highlights: 13
---

def remap(min_temp, max_temp, min_angle, max_angle, temp):
    temp_range = (max_temp - min_temp)
    motor_range = (max_angle - min_angle)
    mapped = (((temp - min_temp) * motor_range) / temp_range) + min_angle
    return int(mapped)

--- /code ---

Теперь, в цикле `while`, ты можешь использовать эту функцию для вычисления нового угла поворота двигателя.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 21
line_highlights: 24
---

while not button.is_pressed():
    temp = vcgm.measure_temp()
    current_angle = motor_y.get_aposition()
    new_angle = remap(50, 90, -170, 170, temp)
    
--- /code ---

--- /task ---

Теперь ты можешь запустить свою программу. Сделай так, чтобы процессор Raspberry Pi стал теплее, как ты это делал раньше, и ты должен увидеть, как перо постепенно движется вверх. Не стесняйся изменять параметры `min_temp` и `max_temp`, если твое перо не слишком сильно двигается.

![Анимация, показывающая, как бумага проходит через плоттер, а перо движется и рисует колеблющуюся линию.](images/plotter_demo_2.gif)


--- save ---
