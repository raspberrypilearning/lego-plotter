## Schaltflächen-Steuerelement hinzufügen

Um den Plotter zu stoppen und zu starten, kannst du deinem Gerät einen Schalter hinzufügen.

--- task ---

Der LEGO® SPIKE™ Prime Kraft-Sensor kann als einfacher Knopf benutzt werden. Schließe einen an Port C deines Build HAT an.

![Eine Nahaufnahme eines Teils des LEGO® Plotters, an dem der Kraftsensor hinzugefügt wurde.](images/force.jpg)

--- /task ---

--- task ---

Bearbeite dein Programm `plotter.py`, dass es eine Steuerung mittels eines Schalters enthält. Füge am Ende der Zeile `from buildhat import Motor ` ein Komma gefolgt von `ForceSensor` (Achte auf die **beiden** Großbuchstaben!) ein:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 3
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor

--- /code ---

--- /task ---

--- task ---

Um ein Objekt für den Schalter zu erstellen, füge diese Zeile nach den ähnlichen Zeilen für die Motoren hinzu,:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 7
---

motor_y = Motor('A') motor_x = Motor('B') taster = ForceSensor('C') motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

Ändere deine Hauptschleife von `while True` zu:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 13
line_highlights:
---

while not button.is_pressed(): current_angle = motor_y.get_aposition() new_angle = randint(-180, 180)

--- /code ---

--- /task ---

--- task ---

Jetzt kannst du den Plotterbetrieb durch Drücken der Taste stoppen. Um alles aufzuräumen und beide Motoren zu stoppen, füge die folgenden Zeilen am Ende deines Programms hinzu.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 19
line_highlights: 24-26
---

    elif sensor_daten < winkel_jetzt:
        motor_y.run_to_position(sensor_daten, 100, direction="anticlockwise")
        print('gegen Uhrzeigersinn')
    sleep(0.1)

motor_x.stop() motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

Jetzt kannst du deinen Plotter testen. Dein fertiger Code sollte so aussehen:

--- code ---
---
language: python filename: plotter.py line_numbers: true
line_number_start: 1
---

# !/usr/bin/python3
from random import randint from time import sleep from buildhat import Motor, ForceSensor

taster = ForceSensor('C') motor_y = Motor('A') motor_x = Motor('B')

motor_y.run_to_position(0, 100) motor_x.start(speed=-25)

while not button.is_pressed(): current_angle = motor_y.get_aposition() new_angle = randint(-180, 180) if new_angle > current_angle: motor_y.run_to_position(new_angle, 100, direction="clockwise") print('Turning CW') elif new_angle < current_angle: motor_y.run_to_position(new_angle, 100, direction="anticlockwise") print('Turning ACW') sleep(0.1)

motor_x.stop() motor_y.run_to_position(0, 100)

--- /code ---

--- task ---

Feed a piece of paper from the back of the plotter so that the front short edge is just beyond the pen.

--- /task ---

--- task ---

Start the program in Thonny, and watch as the pen plots your random data on your paper!

--- /task ---

--- task ---

Sobald das Papier aufgebraucht ist, drückst du die Kraftsensor-Taste, um alles zu stoppen.

--- /task ---

![Ein Foto von einem Blatt Papier, auf das der Plotter eine grüne Spur gezeichnet hat.](images/paper.JPG)

Im nächsten Schritt verwendest du eine Echtzeit-Datenquelle für deine Eingabedaten!

--- save ---
