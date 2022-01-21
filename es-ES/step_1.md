## Introducción

Utiliza LEGO® y Raspberry Pi Build HAT para crear un trazador de datos.

### Lo que harás

--- no-print ---

![Una película que muestra el trazador LEGO® en acción. Un trozo de papel sale de la máquina con una señal verde que se traza con un bolígrafo.](images/plotter_demo.gif)

--- /no-print ---

--- print-only ---
![A photo of the completed plotter project.](images/completed.jpg)
--- /print-only ---

### Lo que aprenderás

+ Cómo calcular ángulos de rotación
+ Cómo mapear rangos de datos en escalas apropiadas para visualización
+ Cómo usar declaraciones condicionales (if / else)

### Hardware

+ Una computadora Raspberry Pi
+ Un Build HAT Raspberry Pi
+ Dos motores LEGO® Technic ™
+ Un sensor de fuerza LEGO® SPIKE ™ O un botón pulsador, una placa de pruebas y cables de puente
+ Variedad de LEGO®, incluidas dos ruedas pequeñas (utilizamos una selección del kit [LEGO® Education SPIKE ™ Prime](https://education.lego.com/en-gb/product/spike-prime))
+ Una fuente de alimentación de 7,5 V con un conector de barril (en su lugar, puedes usar un paquete de baterías, pero asegúrate de que todas las celdas estén completamente cargadas)

### Software

+ Python 3
+ La biblioteca Vcgencmd de Python3

### Descargas

+ [Instrucciones de construcción de LEGO® SPIKE ™ Prime: *Rastrea tus paquetes* (1/2)](https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book1of2-05883f81fed73ac3738781d084e0d4e2.pdf){:target="_blank"}
+ [Instrucciones de construcción de LEGO® SPIKE ™ Prime: *Rastrea tus paquetes* (2/2)](https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book2of2-80dc3c8c61ec2d2ffa785b688326ef74.pdf){:target="_blank"}
+ [Script terminado para Lego Plotter](http://rpf.io/p/es-ES/lego-plotter-go){:target="_blank"}

--- collapse ---
---
title: Instala la biblioteca Vcgencmd de Python
---

Asegúrate de estar conectado a Internet.

Abre la terminal en tu Raspberry Pi presionando <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>en tu teclado.

En la ventana escribe `pip3 install vcgencmd` y presiona <kbd>Enter</kbd>.

Espera el mensaje de confirmación (no tardará mucho) y luego cierra la ventana de la terminal.

--- /collapse --- 

--- collapse ---
---
title: Información adicional para educadores
---

Puedes descargar el proyecto completo [aquí](http://rpf.io/p/es-ES/projectName-get){:target="_blank"}.

Si necesitas imprimir este proyecto, usa la [versión para imprimir](https://projects.raspberrypi.org/es-ES/projects/projectName/print){:target="_blank"}.

--- /collapse ---

Antes de comenzar, deberás configurar tu computadora Raspberry Pi e instalar el Build HAT:

--- task ---

Monta tu Raspberry Pi en la placa de construcción LEGO usando pernos y tuercas M2, asegurándote de que la Raspberry Pi esté en el lado sin borde':

 ![Raspberry Pi atornillada a una placa de construcción LEGO magenta.](images/build_11.jpg)

--- /task ---

Montar la Raspberry Pi de esta manera permite un fácil acceso a los puertos, así como a la ranura de la tarjeta SD. La placa de construcción te permitirá conectar la Raspberry Pi a la estructura principal de tu tablero más fácilmente.

--- task ---

Alinea el Build HAT con la Raspberry Pi, asegurándote de que puedes ver la etiqueta `This way up`. Asegúrate de que todos los pines GPIO estén cubiertos por el HAT y presiona firmemente. (El ejemplo usa una [cabezera de apilamiento ](https://www.adafruit.com/product/2223){:target="_blank"}, lo que alarga los pines)

![Imagen de los pines GPIO asomandose por la parte superior del Build HAT.](images/build_15.jpg) ![Animación que muestra el ajuste de Buildhat a Raspberry Pi](images/haton.gif)

--- /task ---

Ahora debes encender tu Raspberry Pi utilizando el conector de barril de 7.5V en el Build HAT, lo cual te permitirá usar los motores.

--- task ---

Si aún no lo ha hecho, configura tu Raspberry Pi siguiendo estas instrucciones:

[Configurando tu Raspberry Pi](https://projects.raspberrypi.org/es-ES/projects/raspberry-pi-setting-up){:target="_blank"}

--- /task ---

--- task ---

Una vez que la Raspberry Pi se haya iniciado, abre la herramienta de configuración de Raspberry Pi haciendo clic en el botón Menú de Raspberry y luego seleccionando "Preferencias" y luego "Configuración de Raspberry Pi".

Haz clic en la pestaña "interfaces" y ajusta la configuración Serie como se muestra a continuación:

![Imagen que muestra la pantalla de configuración del sistema operativo Raspberry Pi con el puerto en serie habilitado y la consola en serie deshabilitada](images/configshot.jpg)

--- /task ---

--- task ---

También necesitarás instalar la biblioteca buildhat de python siguiendo estas instrucciones:

--- collapse ---
---
title: Instala la biblioteca buildhat de Python
---

Abre una ventana de terminal en tu Raspberry Pi presionando <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd>.

En el indicador, escribe: `sudo pip3 install buildhat`

Presiona <kbd>Entrar</kbd> y espera el mensaje "installation completed".

--- /collapse ---

--- /task ---
