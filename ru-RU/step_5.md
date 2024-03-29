## Подача бумаги

Теперь ты запрограммируешь второй двигатель для подачи бумаги через плоттер с постоянной скоростью.

--- task ---

Подложи лист бумаги формата A5 (или нарежь обрезки примерно такого же размера) под маленькие колеса сзади.

![Бумага подается с задней стороны плоттера, так что кончик карандаша упирается в переднюю кромку.](images/paper_in.jpg)

--- /task ---

--- task ---

Подключи задний двигатель LEGO® Technic™ (который приводит в движение эти колеса) к порту B на Build HAT.

--- /task ---

--- task ---

Создай объект с именем `motor_x` для этого двигателя, ниже аналогичной строки для `motor_y`:

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

Добавь строку, чтобы двигатель начал вращаться непосредственно перед циклом `while True`:

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

Это заставит двигатель подачи работать с постоянной скоростью 25 оборотов в минуту при запуске программы. Измени число в скобках, чтобы поэкспериментировать со скоростью.

--- task ---

Запусти свой код и посмотри, как бумага проходит через плоттер, а карандаш беспорядочно перемещается в направлении `y`.

![Анимация, показывающая, как бумага проходит через плоттер, а карандаш случайно перемещается по оси y.](images/feeding_paper.gif)

--- /task ---

Чтобы остановить двигатель, подающий бумагу, ты можешь ввести следующее в **Оболочке**.

```python
>>> from buildhat import Motor
>>> motor_x = Motor('B')
>>> motor_x.stop()
```

--- save ---


