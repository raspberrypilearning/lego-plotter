## Hinzufügen einer Echtzeit-Datenquelle

Es gibt eine Vielzahl von Sensoren, die du deinem Raspberry Pi hinzufügen kannst, um einen Datenstrom für deinen Plotter bereitzustellen.

Beginnen wir mit einer eingebauten Datenquelle: der Temperatur der CPU auf dem Raspberry Pi selbst. Wenn Sie die `vcgencmd` Bibliothek nicht installiert haben, sollten Sie dies jetzt tun.

--- collapse ---
---
title: Installation der Vcgencmd Python-Bibliothek
---

Stelle sicher, dass du mit dem Internet verbunden bist.

Öffne ein Terminal, indem du <kbd>Strg</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> auf deiner Tastatur drückst.

Gib an der Eingabeaufforderung `pip3 install vcgencmd` ein und drücke <kbd>Enter</kbd>.

Warte auf die Bestätigungsnachricht (es dauert nicht lange) und schließe dann das Terminalfenster.

--- /collapse ---

--- task ---

Gib folgende Zeilen in die Thonny-**Shell** ein, um die CPU-Temperatur zu messen und auszulesen.

```python
>>> from vcgencmd import Vcgencmd
```
Drücke <kbd>Enter</kbd>.

Tippe:
```python
>>> vcgm = Vcgencmd()
```
Drücke <kbd>Enter</kbd>.

Tippe:
```python
>>> vcgm.measure_temp()
```
Drücke <kbd>Enter</kbd>.

Du solltest sehen, dass die **Shell** einen Zahlenwert zurückgibt (er sollte ungefähr 50 sein) – so heiß läuft deine CPU.

--- /task ---

Jetzt heizen wir die Dinge auf, indem wir die CPU dazu bringen, etwas Arbeit zu machen!

--- task ---

Öffne den Webbrowser und sieh dir ein YouTube-Video an. Gehe nach ein paar Sekunden zurück zu Thonny und führe die letzte Zeile von Python erneut aus. Du solltest sehen, dass die Temperatur gestiegen ist.

--- /task ---

Nachdem du nun gesehen hast, wie du mit Python die Temperatur der CPU auslesen kannst, kannst du dein Programm `plotter.py` so ändern, dass es dies als Datenquelle verwendet.

--- task ---

Füge zunächst unter den vorhandenen Importzeilen am Anfang der Datei die Zeile hinzu, um die Vcgencmd-Bibliothek zu importieren:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 4
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor from vcgencmd import Vcgencmd

--- /code ---

--- /task ---

--- Aufgabe --- Erstelle ein vcgencmd-Objekt:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 9
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor from vcgencmd import Vcgencmd

motor_y = Motor('A') motor_x = Motor('B') taster = ForceSensor('C') vcgm = Vcgencmd()

motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

Ändere das Programm so, dass es Echtzeit-Temperaturwerte anstelle von zufällig generierten Zahlen verwendet. Dazu musst du `randint(-180, 180)` durch `vcgm.measure_temp()`ersetzen.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 15
line_highlights: 16
---

while not taster.is_pressed(): temp = vcgm.measure_temp() sensor_daten = motor_y.get_aposition()

--- /code ---

--- /task ---

Bevor du die Temperatur der CPU des Raspberry Pi als Datenquelle für deinen Plotter verwenden kannst, musst du sicherstellen, dass der maximal mögliche Wert der Datenquelle mathematisch so umgerechnet wird, dass er auf eine Skala zwischen -180 und 180. passt.

Die Temperaturwerte, die von `vcgencmd` geliefert werden liegen zwischen ca 50°C (wenn der Raspberry Pi eingeschaltet ist, aber nicht viel tut) bis knapp unter 90°C wenn er hart arbeitet (bei 85°C beginnt der Raspberry Pi seine Leistung zu drosseln, um die Temperatur unter diesem Wert zu halten). Angenommen, du möchtest einen Bereich von 40 °C bis 90 °C darstellen – dann musst du dies deinen verfügbaren Werten zuordnen: -180 bis 180.

Du kannst eine Funktion erstellen, um einen Wertebereich einem anderen Wertebereich zuzuordnen.

--- task ---

Füge diese Funktion über deiner `while` Schleife hinzu. Sie nimmt einen Temperaturbereich und einen Winkelbereich an und ordnet die Temperatur dann in einem Winkel zu.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 12
line_highlights: 13
---

def umwandlung(min_temp, max_temp, min_winkel, max_winkel, temp): temp_bereich = (max_temp - min_temp) motor_bereich = (max_winkel - min_winkel) gewandelt = (((temp - min_temp) * motor_bereich) / temp_bereich) + min_winkel return int(gewandelt)

--- /code ---

Jetzt kannst du in der `while` Schleife diese Funktion verwenden, um einen neuen Drehwinkel für den Motor zu berechnen.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 21
line_highlights: 24
---

while not taster.is_pressed(): temp = vcgm.measure_temp() winkel_jetzt = motor_y.get_aposition() sensor_daten = umwandlung(50, 90, -170, 170, temp)

--- /code ---

--- /task ---

Jetzt kannst du dein Programm ausführen. Lass die Raspberry Pi-CPU wie zuvor wärmer werden und du solltest sehen, wie sich der Stift allmählich nach oben bewegt. Wenn sich dein Stift nicht zu sehr bewegt, kannst du die `min_temp` und `max_temp` ändern, um mehr Bewegung zu sehen.

![Animation, die zeigt, wie das Papier durch den Plotter geführt wird, während sich der Bleistift zufällig entlang der y-Achse bewegt.](images/plotter_demo_2.gif)


--- save ---
