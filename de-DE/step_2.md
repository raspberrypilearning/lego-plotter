## Bewege die Motoren mit Daten

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Vielleicht hast du in Erdbeben-Katastrophenfilmen eine Szene gesehen, in der ein <span style="color: #0faeb0">[Seismograph](https://de.wikipedia.org/wiki/Seismograph) </span> verwendet wird, um die Erschütterungen anzuzeigen. 

Der Aufbau solcher Geräte ist recht einfach: Ein Motor wird verwendet, um das Papier am Stift vorbei (die x-Achse) zu bewegen, während ein anderer Motor, rechtwinklig zum ersten, den Stift als Reaktion auf die sich ändernden Daten (y -Achse) bewegt. </p>

In diesem Projekt erstellest du einen Plotter aus LEGO® und verbindest ihn mit deinem Raspberry Pi, damit er Echtzeitdaten zeichnen kann.

--- task ---

Schließe einen Monitor, eine Tastatur und eine Maus an deinen Raspberry Pi an. Wenn du noch nie einen Raspberry Pi verwendet hast, solltest du mit [diesem Projekt](https://projects.raspberrypi.org/en/projects/raspberry-pi-getting-started) beginnen.

Befestige den Build HAT an deinem Raspberry Pi (stelle sicher, dass das Raspberry Pi-Logo auf der Oberseite zu sehen ist) und schließe ein 7,5-V-Netzteil an die Hohlstecker-Buchse des Build HAT an. Dadurch wird dein Raspberry Pi gestartet.

--- /task ---

--- task ---

Öffne Thonny aus dem Programmiermenü und beginne dein Programm mit den folgenden Zeilen, die die Bibliotheken importieren, die du verwenden wirst:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 1,2,3
---

from random import randint from time import sleep from buildhat import Motor

--- /code ---

Speichere dieses Programm als `plotter.py` indem du <kbd>Strg</kbd>+<kbd>s</kbd>drückst.

--- /task ---

--- task ---

Now use the `randint` function to create a random value between a range (in this case, -180 to 180) and store it in a variable called `new_angle`:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 5,6
---

new_angle = randint(-180,180) print(new_angle)

--- /code ---

--- /task ---

--- task ---

Führe dein Programm einige Male aus, indem du oben im Fenster auf die Schaltfläche **Run** klickst. In der Shell unter Ihrem Code sollten jedes Mal unterschiedliche Werte angezeigt werden.

--- /task ---

Anstatt dieses Skript manuell zu starten, schreib eine **Schleife**, um das Skript wiederholt auszuführen. Um die gleichen Zeilen kontinuierlich auszuführen, kannst du eine `while True:` Schleife verwenden.

--- task ---

Füge über dem soeben hinzugefügten Code eine Leerzeile ein, indem du <kbd>Enter</kbd> drückst.

Gib in dieser neuen Zeile `while True:` ein; Stelle sicher, dass du ein großes 'T' verwendest.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 5
---

while True: new_angle = randint(-180,180) print(new_angle)

--- /code ---

--- /task ---

--- task ---

Füge am Anfang jeder der darunter liegenden Zeilen vier Leerzeichen hinzu, um einen um **eingerückten Codeblock**zu erstellen. Dies teilt dem Computer mit, welche Zeilen in deiner Schleife enthalten sind.


--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 6,7
---

while True: new_angle = randint(-180,180) print(new_angle)

--- /code ---

--- /task ---

--- task ---

Drücke am Ende deines Codes <kbd>Enter</kbd>, um eine weitere eingerückte Zeile hinzuzufügen. Schreib `sleep(0.1)` in diese Zeile.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 8
---

while True: new_angle = randint(-180,180) print(new_angle) sleep(0.1)

--- /code ---

--- /task ---

--- task ---

Führe deinen Code aus, und sieh dir in der Shell die Reihe von Werten an. Wenn du Fehler erhältst, überprüfe, ob dein Code wie folgt aussieht:

--- code ---
---
language: python filename: plotter.py line_numbers: true
line_number_start: 1
---

from random import randint from time import sleep from buildhat import Motor

while True: new_angle = randint(-180,180) print(new_angle) sleep(0.1)

--- /code ---

--- /task ---

Nachdem du nun einige Daten hast, kannst du diese verwenden, um die Position eines Motors zu steuern.

--- task ---

Schließe einen LEGO® Technic™ Motor an Port A des Build HAT an. Füge der Motorachse einige zusätzliche LEGO-Elemente hinzu, damit der Motor leicht zu sehen ist.

--- /task ---

--- task ---

Richte das Element mit der Strichmarkierung am Motor aus und stelle den Motor dann in die Nullposition:

![Ein Foto eines LEGO® Technic™-Motors mit den Lollipop- und Null-Symbolen, die verwendet werden, um den Encoder auf 0 Grad einzustellen.](images/zero.JPG)

--- /task ---

Änder nun den Hauptteil deines Programms so, dass der vom Motor gedrehte Winkel dem neuesten Wert deines simulierten Sensors entspricht.

Dazu musst du deinen Motor so einrichten, dass das Programm darauf zugreifen kann.

--- task ---

Erstellen Sie ein Objekt `motor_y` am Anschluss `A` auf dem Build HAT. Drehe dann den Motor zur `0` Position mit einer Geschwindigkeit von `100`.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 4
line_highlights: 5, 6
---

motor_y = Motor('A') motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

--- task ---

The next line makes the motor turn to the angle stored in `new_angle`.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 7
line_highlights: 11
---

while True: new_angle = randint(-180,180) print(new_angle) motor_y.run_to_position(new_angle, 100)

--- /code ---

--- /task ---

--- task ---

Klicke auf **Run** und du solltest sehen, wie sich dein Motor als Reaktion auf die sich ändernden Daten wie ein Uhrzeiger in verschiedene Positionen dreht. Wenn du das Programm erneut ausführst, sollte es die Motorposition auf `0` zurücksetzen, bevor er sich erneut zufällig bewegt.

Wenn du Fehler erhältst, überprüfe, ob dein Code wie folgt aussieht.

--- code ---
---
language: python filename: plotter.py line_numbers: true
line_number_start: 1
---

from random import randint from time import sleep from buildhat import Motor

motor_y = Motor('A') motor_y.run_to_position(0, 100)

while True: new_angle = randint(-180,180) print(new_angle) motor_y.run_to_position(new_angle, 100) sleep(0.1)

--- /code ---

--- /task ---

![Ein Filmclip, der einen LEGO® Technic™ Motor mit einem daran befestigten schwarzen Balkenelement zeigt. Der Motor dreht sich und der daran befestigte Balken dreht sich wie ein Uhrzeiger als Reaktion auf die Daten. Der Motor dreht sich nur zwischen 0 und 180 Grad im Uhrzeigersinn und gegen den Uhrzeigersinn.](images/motor_180.gif)

--- save ---
