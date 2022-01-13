## Feed in paper

Du programmierst nun den zweiten Motor so, dass er das Papier mit einer konstanten Geschwindigkeit durch den Plotter transportiert.

--- task ---

Führe ein Blatt A5-Papier (oder schneide etwas Schmierpapier auf ungefähr diese Größe) von hinten unter die kleinen Räder.

![Papier wurde von der Rückseite des Plotters eingezogen, so dass die Bleistiftspitze auf der Vorderkante aufliegt.](images/paper_in.jpg)

--- /task ---

--- task ---

Stecke den hinteren LEGO® Technic™-Motor (der diese Räder antreibt) in Port B am Build HAT.

--- /task ---

--- task ---

Erstelle ein Objekt mit dem Namen `motor_x` für diesen Motor unter der ähnlichen Zeile für den `motor_y`:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 6
---

motor_y = Motor('A') motor_x = Motor('B') motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

--- task ---

Add a line to start this motor turning immediately before the `while True` loop:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 8
---

motor_y = Motor('A') motor_x = Motor('B') motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

Nach dem Programmstart läuft dadurch der Einzugsmotor mit einer konstanten Geschwindigkeit von -25 Umdrehungen pro Minute. Ändere die Zahl in den Klammern, um mit der Geschwindigkeit zu experimentieren.

--- task ---

Führe deinen Code aus und beobachte, wie das Papier durch den Plotter geführt wird, während sich der Bleistift in der `y` Richtung zufällig bewegt.

![Animation, die zeigt, wie das Papier durch den Plotter geführt wird, während sich der Bleistift zufällig entlang der y-Achse bewegt.](images/feeding_paper.gif)

--- /task ---

Um den Papiervorschub durch den Motor zu stoppen, kannst du Folgendes in die **Shell**eingeben.

```python
>>> from buildhat import Motor
>>> motor_x = Motor('B')
>>> motor_x.stop()
```

--- save ---


