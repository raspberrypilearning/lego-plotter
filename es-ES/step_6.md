## Add a button control

Para detener e iniciar la ejecución del trazador, puedes agregar un botón a su construcción.

--- task ---

El sensor de fuerza principal LEGO® SPIKE ™ puede actuar como un simple botón. Conecta uno al puerto C en tu Build HAT.

![Una foto en primer plano de parte del trazador LEGO® donde se ha agregado el sensor de fuerza.](images/force.jpg)

--- /task ---

--- task ---

Edita tu programa `plotter.py` para incluir un botón de control. Agrega una coma seguida de `ForceSensor` (¡asegurándote de incluir **ambas** letras mayúsculas!) Al final de la línea que dice `from buildhat import Motor`:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 3
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor

--- /code ---

--- /task ---

--- task ---

Agrega esta línea para crear un objeto para el botón después de las líneas similares para los motores:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 7
---

motor_y = Motor('A') motor_x = Motor('B') button = ForceSensor('C') motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

Cambie su bucle principal de `while True` a:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 13
line_highlights:
---

while not button.is_pressed(): current_angle = motor_y.get_aposition() new_angle = randint(-180, 180)

--- /code ---

--- /task ---

--- task ---

Ahora puedes detener el funcionamiento del plotter presionando el botón. Para finalizar todo y detener ambos motores, agrega las siguientes líneas al final de tu programa.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 19
line_highlights: 24-26
---

    elif new_angle < current_angle:
        motor_y.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)

motor_x.stop() motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

Now you are ready to test your plotter. Your final script should look like this:

--- code ---
---
language: python filename: plotter.py line_numbers: true
line_number_start: 1
---

# !/usr/bin/python3
from random import randint from time import sleep from buildhat import Motor, ForceSensor

button = ForceSensor('C') motor_y = Motor('A') motor_x = Motor('B')

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

Once the paper has been used, press the Force Sensor button to stop everything.

--- /task ---

![A photo of a piece of paper, on which the plotter has draw a green trace.](images/paper.JPG)

In the next step, you will use a real-time data source for your input data!

--- save ---
