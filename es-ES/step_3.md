## Crear un rango de trazado

En este paso controlaremos el sentido en el que se mueven los motores (en sentido horario o antihorario) para establecer un punto máximo de recorrido en cada sentido.

--- collapse ---
---
title: Por qué necesitas cambiar la forma en que se mueven los motores
---

Tu motor siempre tomará el camino más corto hacia la nueva posición.

Por ejemplo, si el motor está a 170 grados y la siguiente posición es -170 grados, viajará en el sentido de las agujas del reloj, pasando por la posición de 180 grados para llegar a su destino lo más rápido posible.

![Un video que muestra un motor LEGO® Technic ™ con una columna negra ensamblada. El motor está girando y la columna gira como una manecilla de reloj en respuesta a los datos. El motor gira 360 grados completos, viajando en el sentido de las agujas del reloj y en sentido antihorario y, a veces, pasa por la posición cero en cualquier dirección.](images/motor_through_zero.gif)

Esto está bien para nuestra simulación, pero nuestro trazador no tendrá esta libertad de movimiento. Una vez que el bolígrafo ha llegado a la parte superior o inferior del papel (eje y), no puede seguir subiendo para emerger por la parte inferior; se romperá. Por lo tanto, será necesario evitar que tu trazador se desplace en el sentido de las agujas del reloj más allá de la marca de 180 grados.

Esto se puede lograr alterando el comportamiento del motor cuando se mueve a una posición. Puedes hacerlo pasando un parámetro `direction =` a la función `run_to_position()`. Puedes establecer este valor en `"clockwise"`(horario), `"anticlockwise"`(antihorario) o `"shortest'` (el más corto), que es el comportamiento predeterminado de la 'ruta más corta'.

![Un video que muestra un motor LEGO® Technic ™ con una columna negra ensamblada. El motor está girando y la columna gira como una manecilla de reloj en respuesta a los datos. El motor gira entre 0 y 180 grados, pero nunca pasa por cero.](images/motor_not_zero.gif)

Entonces, por ejemplo, `motor_y.run_to_position (50, 100, direction = "anticlockwise")` moverá un motor a la posición de 50 grados, girando en sentido antihorario a la velocidad máxima.

Es posible agregar un **control condicional** a tu bucle para asegurarte de que el motor nunca pase 180 grados y siempre se mueva de un ángulo más alto a uno más bajo girando en sentido antihorario.

Puedes encontrar la última posición del motor usando `motor_y.get_aposition`.

--- /collapse ---

--- task ---

Verifica el ángulo actual del motor en la parte superior de tu bucle `while`.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 7
line_highlights: 8
---

while True: current_angle = motor_y.get_aposition() new_angle = randint(-180, 180) print(new_angle) motor_y.run_to_position(new_angle, 100) sleep(0.1)

--- /code ---

--- /task ---

--- task ---

Ahora, en el bucle `while`, puedes agregar una comprobación para ver si el valor actual de `nuevo_angulo` es mayor o menor que `angulo_actual`.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 7
line_highlights: 11-16
---

while True: current_angle = motor_y.get_aposition() new_angle = randint(-180, 180) print(new_angle) if new_angle > current_angle: motor_y.run_to_position(new_angle, 100, direction="clockwise") print('Turning CW') elif new_angle < current_angle: motor_y.run_to_position(new_angle, 100, direction="anticlockwise") print('Turning ACW') sleep(0.1)

--- /code ---

--- /task ---

--- task ---

Ejecuta tu código. These conditional tests will prevent the motor from changing from a negative value to a positive one by passing through 180 degrees (and vice versa).

--- /task ---

--- save ---

