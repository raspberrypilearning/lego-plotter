## Mueve los motores con datos

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Es posible que haya visto en las películas de desastres por terremotos una escena en la que utilizan un sismógrafo <span style="color: #0faeb0">[seismometer](https://es.wikipedia.org/wiki/Sism%C3%B3grafo) </span> para mostrar los temblores. 

El diseño de tales dispositivos es bastante simple: un motor se usa para mover el papel más allá del lápiz (el eje x), mientras que otro, en ángulo recto con el primero, mueve el lápiz en respuesta a los datos cambiantes (y -eje). </p>

En este proyecto, crearás un trazador con LEGO® y lo conectarás a tu Raspberry Pi para poder trazar datos en tiempo real.

--- task ---

Conecta un monitor, teclado y mouse a tu Raspberry Pi. Si nunca antes has usado una Raspberry Pi, es posible que desees comenzar con [este proyecto](https://projects.raspberrypi.org/es-ES/projects/raspberry-pi-getting-started).

Conecta el Build HAT a tu Raspberry Pi (asegúratse de que puedes ver el logotipo de Raspberry Pi en la parte superior) y conecta una fuente de alimentación de 7,5 V al conector de barril del Build HAT. Esto iniciará tu Raspberry Pi.

--- /task ---

--- task ---

Abre Thonny desde el menú de programación y agrega las siguientes líneas para comenzar su programa importando las bibliotecas que utilizarás:

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

Guarda este programa como `plotter.py` presionando <kbd>Ctrl</kbd>+<kbd>s</kbd>.

--- /task ---

--- task ---

Ahora usa la función `randint` para crear un valor aleatorio en un rango (en este caso, -180 a 180) y almacénalo en una variable llamada `nuevo_angulo`:

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 5
line_highlights: 5,6
---

nuevo_angulo = randint(-180,180) 
print(nuevo_angulo)

--- /code ---

--- /task ---

--- task ---

Ejecuta tu programa varias veces haciendo clic en el botón **Ejecutar** en la parte superior de la ventana. Cada vez deberías ver aparecer valores diferentes en la consola debajo de tu código.

--- /task ---

En lugar de ejecutar este script manualmente, crea un **bucle** para ejecutar el script repetidamente. Para ejecutar las mismas líneas continuamente, puedes usar un bucle `while True:`.

--- task ---

Agregue una línea en blanco sobre el código que acabas de agregar presionando <kbd>Entrar</kbd>.

En esta nueva línea, ingresa `while True:`; asegúrese de escribirlo con "T"' mayúscula.

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 5
line_highlights: 5
---

while True: 
nuevo_angulo = randint(-180,180) 
print(nuevo_angulo)

--- /code ---

--- /task ---

--- task ---

Agregue cuatro espacios al comienzo de cada una de las líneas debajo para crear un **bloque de código indentado**. Esto le dice a la computadora qué líneas están incluidas en tu bucle.


--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 5
line_highlights: 6,7
---

while True: 
    nuevo_angulo = randint(-180,180) 
    print(nuevo_angulo)

--- /code ---

--- /task ---

--- task ---

Al final de tu código, presione <kbd>Entrar</kbd> para agregar otra línea indentada. En esta línea, escribe `sleep (0.1)`.

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 5
line_highlights: 8
---

while True: 
    nuevo_angulo = randint(-180,180) 
    print(nuevo_angulo) 
    sleep(0.1)

--- /code ---

--- /task ---

--- task ---

Ejecuta tu código para ver los valores impresos en la consola. Si tienes algún error, verifica que tu código tenga este aspecto:

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
    nuevo_angulo = randint(-180,180) 
    print(nuevo_angulo) 
    sleep(0.1)

--- /code ---

--- /task ---

Ahora que tiene algunos datos, puede usarlos para controlar la posición de un motor.

--- task ---

Conecte un motor LEGO® Technic ™ al puerto A del Build HAT. Agrega algunos elementos LEGO adicionales al eje del motor para que sea fácil ver el motor girando.

--- /task ---

--- task ---

Alinea el elemento con la línea marcada en el motor y luego coloca el motor en la posición cero:

![Una foto de un motor LEGO® Technic ™ que muestra la paleta y las etiquetas de cero utilizadas para configurar el codificador en 0 grados.](images/zero.JPG)

--- /task ---

Ahora, modifica el cuerpo principal de tu programa para que el ángulo al que gira el motor sea el mismo que el último valor producido por tu sensor simulado.

Para hacer esto, necesitas configurar tu motor para que el programa pueda acceder a él.

--- task ---

Crear un objeto `motor_y` para el puerto `A` en el Build HAT y luego gira el motor a la posición `0` con una velocidad de `100`.

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

La siguiente línea hace que el motor gire al ángulo almacenado en `nuevo_angulo`.

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 7
line_highlights: 11
---

while True: 
    nuevo_angulo = randint(-180,180) 
    print(nuevo_angulo) 
    motor_y.run_to_position(nuevo_angulo, 100)

--- /code ---

--- /task ---

--- task ---

Haz clic en **Ejecutar** y deberías ver tu motor gira en el sentido de las agujas del reloj a diferentes posiciones en respuesta a los datos cambiantes. Si vuelves a ejecutar el programa, debería restablecer la posición del motor a `0` antes de volver a moverse aleatoriamente.

Si tienes errores, verifica que tu código tenga este aspecto.

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
    nuevo_angulo = randint(-180,180) 
    print(nuevo_angulo) 
    motor_y.run_to_position(nuevo_angulo, 100) 
sleep(0.1)

--- /code ---

--- /task ---

![Una película que muestra un motor LEGO® Technic ™ con una columna negra ensamblada. El motor está girando y la columna gira como una manecilla de reloj en respuesta a los datos. El motor solo gira entre 0 y 180 grados, viajando en sentido horario y antihorario.](images/motor_180.gif)

--- save ---
