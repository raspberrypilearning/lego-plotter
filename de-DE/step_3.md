## Erstelle einen Plotbereich

In diesem Schritt steuern wir die Bewegungsrichtung der Motoren (im oder gegen den Uhrzeigersinn), um die maximalen Bewegungen in jede Richtung einzustellen.

--- collapse ---
---
title: Warum du die Bewegungsabläufe der Motoren ändern musst
---

Dein Motor nimmt immer den kürzesten Weg zur neuen Position.

Wenn sich der Motor beispielsweise auf 170 Grad befindet und die nächste Position -170 Grad beträgt, fährt er im Uhrzeigersinn durch die 180-Grad-Position, um so schnell wie möglich an sein Ziel zu gelangen.

![Ein Filmclip, der einen LEGO® Technic™ Motor mit einem daran befestigten schwarzen Balkenelement zeigt. Der Motor dreht sich und der daran befestigte Balken dreht sich wie ein Uhrzeiger als Reaktion auf die Daten. Der Motor dreht sich um volle 360 Grad, im Uhrzeigersinn und gegen den Uhrzeigersinn, und durchläuft manchmal die Nullposition in beide Richtungen.](images/motor_through_zero.gif)

Für unsere Simulation ist das in Ordnung, aber unser Plotter wird diese Bewegungsfreiheit nicht haben. Sobald der Stift den oberen oder unteren Rand des Papiers (y-Achse) erreicht hat, kann er nicht weiter nach oben fahren, um unten herauszukommen – er wird brechen. Es muss also verhindert werden, dass Ihr Plotter im Uhrzeigersinn über die 180-Grad-Marke hinaus fährt.

Dies kann erreicht werden, indem das Verhalten des Motors beim Anfahren einer Position geändert wird. Du kannst dies tun, indem du einen zusätzlichen `direction=` Parameter an die Funktion `run_to_position()` übergibst. Du kannst diesen Wert auf `"im Uhrzeigersinn"`, `"gegen den Uhrzeigersinn"`oder `"kürzeste"` setzen, wobei das Standardverhalten "kürzester Weg" ist.

![Ein Filmclip, der einen LEGO® Technic™ Motor mit einem daran befestigten schwarzen Balkenelement zeigt. Der Motor dreht sich und der daran befestigte Balken dreht sich wie ein Uhrzeiger als Reaktion auf die Daten. Der Motor dreht zwischen 0 und 180 Grad, geht aber nie durch Null.](images/motor_not_zero.gif)

So wird beispielsweise `motor_y.run_to_position(50, 100, direction="anticlockwise")` einen Motor in die 50-Grad-Position fahren und zwar maximaler Geschwindigkeit gegen den Uhrzeigersinn.

Es ist möglich eine, **Bedingungs-Prüfung** zu deiner Schleife hinzuzufügen, um sicherzustellen, dass der Motor niemals 180 Grad durchläuft und sich von einem höheren Winkel zu einem niedrigeren immer gegen den Uhrzeigersinn bewegt.

Die letzte Position des Motors findest du mit `motor_y.get_aposition`.

--- /collapse ---

--- task ---

Überprüfe den aktuellen Winkel des Motors an der Spitze deiner `while` Schleife.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 7
line_highlights: 8
---

while True: winkel_jetzt = motor_y.get_aposition() winkel_neu = randint(-180, 180) print(winkel_neu) motor_y.run_to_position(winkel_neu, 100) sleep(0.1)

--- /code ---

--- /task ---

--- task ---

Jetzt können Sie in der `while` Schleife eine Prüfung hinzufügen, um zu sehen, ob der aktuelle Wert von `winkel_neu` größer oder kleiner als der `winkel_jetzt` ist.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 7
line_highlights: 11-16
---

while True: winkel_jetzt = motor_y.get_aposition() winkel_neu = randint(-180, 180) print(winkel_neu) if winkel_neu > winkel_jetzt: motor_y.run_to_position(winkel_neu, 100, direction="clockwise") print('Turning CW') elif winkel_neu < winkel_jetzt: motor_y.run_to_position(winkel_neu, 100, direction="anticlockwise") print('Turning ACW') sleep(0.1)

--- /code ---

--- /task ---

--- task ---

Führen deinen Code aus. These conditional tests will prevent the motor from changing from a negative value to a positive one by passing through 180 degrees (and vice versa).

--- /task ---

--- save ---

