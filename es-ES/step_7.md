## Agrega una fuente de datos en tiempo real

Hay una gran variedad de sensores que puedes agregar a tu Raspberry Pi para proporcionar una alimentación de datos para tu trazador.

Comencemos con una fuente de datos incorporada: la temperatura de la CPU en la propia Raspberry Pi. Si no has instalado la `vcgencmd`, deberías hacerlo ahora.

--- collapse ---
---
title: Instala la biblioteca Vcgencmd de Python
---

Asegúrate de estar conectado a Internet.

Abre la terminal en tu Raspberry Pi presionando <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>en tu teclado.

En la ventana escribe `pip3 install vcgencmd` y presiona <kbd>Enter</kbd>.

Espera el mensaje de confirmación (no tardará mucho) y luego cierra la ventana de la terminal.

--- /collapse --- 

--- task ---

Usando la **Consola/REPL** en Thonny, ingresa las siguientes líneas de Python para probar y leer la temperatura de la CPU.

```python
>>> from vcgencmd import Vcgencmd
```
Presiona <kbd>Entrar</kbd>.

Escribe:
```python
>>> vcgm = Vcgencmd()
```
Presiona <kbd>Entrar</kbd>.

Escribe:
```python
>>> vcgm.measure_temp()
```
Presiona <kbd>Entrar</kbd>.

Deberías ver que la **Consola** devuelve un valor numérico (debería estar en algún lugar alrededor de 50); esa es la temperatura de tu CPU.

--- /task ---

¡Ahora vamos a calentarla haciéndola trabajar un poco!

--- task ---

Abre el navegador web y mira un video de YouTube. Después de unos segundos, vuelve a Thonny y vuelve a ejecutar la última línea de Python y debería ver que la temperatura ha aumentado.

--- /task ---

Ahora que has visto cómo leer la temperatura de la CPU con Python, puedes modificar tu programa `plotter.py` para que lo utilice como fuente de datos.

--- task ---

Primero, debajo de las líneas de importación existentes en la parte superior del archivo, agrega las líneas para importar la biblioteca Vcgencmd:

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 1
line_highlights: 4
---

from random import randint 
from time import sleep 
from buildhat import Motor, ForceSensor 
from vcgencmd import Vcgencmd

--- /code ---

--- /task ---

--- task ---
Crea un objeto vcgencmd:

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 1
line_highlights: 9
---

from random import randint 
from time import sleep 
from buildhat import Motor, ForceSensor 
from vcgencmd import Vcgencmd

motor_y = Motor('A') 
motor_x = Motor('B') 
boton = ForceSensor('C') 
vcgm = Vcgencmd()

motor_y.run_to_position(0, 100) 
motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

Cambia el programa para que utilice valores de temperatura en tiempo real en lugar de números generados aleatoriamente. Para hacer esto, necesitas reemplazar `randint(-180, 180)` con `vcgm.measure_temp()`.

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 15
line_highlights: 16
---

while not boton.is_pressed(): 
    temp = vcgm.measure_temp() 
    angulo_actual = motor_y.get_aposition()

--- /code ---

--- /task ---

Antes de poder usar la temperatura de la CPU de la Raspberry Pi como fuente de datos para tu trazador, debes asegurarte de que el valor máximo posible producido por la fuente de datos se convierta matemáticamente para que se ajuste a una escala entre -180 y 180.

El rango de valores de temperatura producidos por `vcgencmd` debe ser de alrededor de 50° C (cuando la Raspberry Pi está encendida, pero no hace mucho) a menos de 90° C cuando se trabaja duro (a 85° C, la Raspberry Pi regulará su rendimiento para mantener la temperatura por debajo de este valor). Supongamos que deseas trazar un rango de 40° C a 90° C; debes asignar esto a los valores disponibles: -180 a 180.

Puedes crear una función para reasignar un rango de valores a otro rango de valores.

--- task ---

Agrega esta función por encima de tu bucle `while`. Tomará un rango de temperatura y un rango de ángulo, y luego reasignará la temperatura a un ángulo.

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 12
line_highlights: 13
---

def remap(min_temp, max_temp, min_angulo, max_angulo, temp): 
    temp_rango = (max_temp - min_temp) 
    motor_rango = (max_angulo - min_angulo) 
    mapeado = (((temp - min_temp) * motor_rango) / temp_rango) + min_angle 
    return int(mapeado)

--- /code ---

Ahora, en el bucle `while`, puedes usar esta función para calcular un nuevo ángulo al que debe girar el motor.

--- code ---
---
language: python 
filename: plotter.py 
line_numbers: true 
line_number_start: 21
line_highlights: 24
---

while not boton.is_pressed(): 
    temp = vcgm.measure_temp() 
    angulo_actual = motor_y.get_aposition() 
    nuevo_angulo = remap(50, 90, -170, 170, temp)

--- /code ---

--- /task ---

Ahora puedes ejecutar tu programa. Haz que la CPU de la Raspberry Pi se caliente como hiciste antes y deberías ver que el lápiz se mueve gradualmente hacia arriba. No dudes en cambiar los parámetros `min_temp` y `max_temp`, si tu lápiz no se mueve demasiado.

![Animación que muestra el papel entrando al trazador mientras el lápiz se mueve y dibuja una línea fluctuante.](images/plotter_demo_2.gif)


--- save ---
