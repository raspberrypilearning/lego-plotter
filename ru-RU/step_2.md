## Перемещаем моторы с помощью данных

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Возможно, ты видел в фильмах-катастрофах о землетрясениях сцену, где используется <span style="color: #0faeb0">[seismometer](https://en.wikipedia.org/wiki/Seismometer) </span> для отображения толчков. 

Конструкция таких устройств довольно проста: один двигатель используется для перемещения бумаги мимо пера (ось x), а другой, перпендикулярный первому, перемещает перо в ответ на изменение данных (y-ось). 

В этом проекте ты создашь плоттер из LEGO® и подключишь его к Raspberry Pi, чтобы он мог отображать данные в реальном времени.

--- task ---

Подключи к компьютеру Raspberry Pi монитор, клавиатуру и мышь. Если ты никогда раньше не использовал Raspberry Pi, ты можешь начать с [этого проекта](https://projects.raspberrypi.org/ru-RU/projects/raspberry-pi-getting-started).

Прикрепи Build HAT к Raspberry Pi (убедись, что ты видишь логотип Raspberry Pi сверху) и подключи источник питания 7,5 В к циллиндрическому разъему Build HAT. Это приведёт к запуску твоей Raspberry Pi.

--- /task ---

--- task ---

Открой Thonny из меню программирования и добавь следующие строки, чтобы начать свою программу с импорта библиотек, которые ты будешь использовать:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
line_highlights: 1,2,3
---

from random import randint
from time import sleep
from buildhat import Motor

--- /code ---

Сохрани эту программу как `plotter.py`, нажав <kbd>Ctrl</kbd>+<kbd>s</kbd>.

--- /task ---

--- task ---

Теперь используй `randint` для создания случайного значения в диапазоне (в данном случае от -180 до 180) и сохрани его в переменной с именем `new_angle`:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 5,6
---

new_angle = randint(-180,180)
print(new_angle)

--- /code ---

--- /task ---

--- task ---

Запусти программу несколько раз, нажав кнопку **Run** в верхней части окна. Ты должен увидеть, что каждый раз в консоли под твоим кодом появляются разные значения.

--- /task ---

Вместо того, чтобы запускать этот скрипт вручную, создай **цикл** для повторного запуска скрипта. Чтобы непрерывно запускать одни и те же строки, ты можешь использовать цикл `while True:`.

--- task ---

Добавь пустую строку над кодом, который ты только что добавил, нажав <kbd>Ввод</kbd>.

В этой новой строке введи `while True:`; убедись, что ты использовал заглавную букву «Т».

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 5
---

while True:
new_angle = randint(-180,180)
print(new_angle)

--- /code ---

--- /task ---

--- task ---

Добавь четыре пробела в начале каждой строки ниже, чтобы создать **блок кода с отступом**. Это сообщает компьютеру, какие строчки включены в твой цикл.


--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 6,7
---

while True:
    new_angle = randint(-180,180)
    print(new_angle)

--- /code ---

--- /task ---

--- task ---

В конце кода нажми <kbd>Ввод</kbd>, чтобы добавить еще одну строку с отступом. В этой строке введи `sleep(0.1)`.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 8
---

while True:
    new_angle = randint(-180,180)
    print(new_angle)
    sleep(0.1)

--- /code ---

--- /task ---

--- task ---

Запусти свой код, чтобы увидеть значения, напечатанные в консоли. Если ты получишь какие-либо ошибки, убедись, что твой код выглядит так:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
---

from random import randint
from time import sleep
from buildhat import Motor

while True:
    new_angle = randint(-180,180)
    print(new_angle)
    sleep(0.1)

--- /code ---

--- /task ---

Теперь, когда у тебя есть некоторые данные, ты можешь использовать их для управления положением мотора.

--- task ---

Подключи двигатель LEGO® Technic™ к порту A на плате Build HAT. Добавь несколько дополнительных элементов LEGO к моторной оси, чтобы можно было легко увидеть, как вращается мотор.

--- /task ---

--- task ---

Совмести элемент с меткой линии на двигателе, а затем установи двигатель в нулевое положение:

![Фотография мотора LEGO® Technic™, показывающая леденец и нулевую метку, используемые для установки энкодера на 0 градусов.](images/zero.JPG)

--- /task ---

Теперь измени основную часть твоей программы так, чтобы угол поворота двигателя совпал с последним значением, полученным твоим симулятором сенсора.

Для этого тебе нужно настроить двигатель так, чтобы программа могла получить к нему доступ.

--- task ---

Создай объект `motor_y` для порта `A` на Build HAT, а затем поверни двигатель в положение `0` со скоростью `100`.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 4
line_highlights: 5, 6
---

motor_y = Motor('A')
motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

--- task ---

Следующая строка заставляет мотор поворачиваться на угол, сохраненный в `new_angle`.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 7
line_highlights: 11
---

while True:
    new_angle = randint(-180,180)
    print(new_angle)
    motor_y.run_to_position(new_angle, 100)

--- /code ---

--- /task ---

--- task ---

Нажми **Run** и ты должен увидеть, как твой двигатель вращается по часовой стрелке в разных положениях в ответ на изменение данных. Если ты снова запустишь программу, она должна сбросить положение двигателя обратно на `0`, прежде, чем снова начать случайное движение.

Если ты получишь какие-либо ошибки, убедись, что твой код выглядит так.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
---

from random import randint
from time import sleep
from buildhat import Motor

motor_y = Motor('A')
motor_y.run_to_position(0, 100)

while True:
    new_angle = randint(-180,180)
    print(new_angle)
    motor_y.run_to_position(new_angle, 100)
    sleep(0.1)

--- /code ---

--- /task ---

![Видеоклип, показывающий двигатель LEGO® Technic™ с прикрепленным черным балочным элементом. Двигатель вращается, а прикрепленная балка вращается, как часовая стрелка, в ответ на данные. Двигатель вращается только между 0 и 180 градусами, двигаясь по часовой стрелке и против часовой стрелки.](images/motor_180.gif)

--- save ---
