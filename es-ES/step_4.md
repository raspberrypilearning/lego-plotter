## Construye el trazador

En este paso, construirás un trazador x / y usando LEGO®.

Hay muchas formas de hacerlo, pero las instrucciones de construcción del proyecto LEGO® SPIKE ™ Prime *Sigue tus envíos* son un excelente punto de partida. Puedes usar el motor del paso anterior para el motor del eje y (el que sostiene el lápiz) en la construcción.

![Un dibujo de las instrucciones de LEGO®.](images/build1.png)

--- task ---

Deberás adaptar la estructura ligeramente para que el brazo pueda sostener un bolígrafo. Las bandas elásticas son una excelente manera de sujetar un bolígrafo cómodamente contra LEGO.

![A photo of the partially assembled plotter model, with a pen attached to the LEGO® elements with a rubber band.](images/rubber_bands.jpg)

<embed src="https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book1of2-05883f81fed73ac3738781d084e0d4e2.pdf" width="600" height="500" alt="pdf" pluginspage="http://www.adobe.com/products/acrobat/readstep2.html">
  </p> 
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    La segunda parte de la construcción completa el mecanismo que usa los dos motores para impulsar el trazador.
  </p>
  
  <p spaces-before="0">
    <img src="images/build2.png" alt="Un dibujo de la segunda parte de las instrucciones de LEGO®." />
  </p>
  
  <p spaces-before="0">

<embed src="https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book2of2-80dc3c8c61ec2d2ffa785b688326ef74.pdf" width="600" height="500" alt="pdf" pluginspage="http://www.adobe.com/products/acrobat/readstep2.html">
      </p> 
      
      <p spaces-before="0">
        --- task ---
      </p>
      
      <p spaces-before="0">
        Conecta el motor LEGO® Technic ™ que mueve el lápiz hacia arriba y hacia abajo al puerto A del Build HAT.
      </p>
      
      <p spaces-before="0">
        --- /task ---
      </p>
      
      <p spaces-before="0">
        Ahora puedes usar tu fuente de datos simulada para probar tu trazador. Por ahora, mantén el bolígrafo tapado o quítalo del brazo del trazador mientras observas el movimiento causado por los datos.
      </p>

<h3 spaces-before="0">
  Calibrar el trazador
</h3>

<p spaces-before="0">
  Tu programa actualmente permite que el motor se mueva a través de su rango completo de movimiento (-180 a +180 grados desde el punto cero). Pero las limitaciones físicas del trazador significan que si intentaras mover el riel dentado a sus posiciones máxima y mínima, el brazo de la pluma se estrellará contra otras partes de la construcción. Para evitar esto, debes centrar la barra.
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Haz clic en el <strong x-id="1">panel de consola</strong> de Thonny (la ventana debajo del código) para poder ejecutar Python una línea a la vez.
</p>

<p spaces-before="0">
  Ingresa estas líneas en la <strong x-id="1">Consola</strong> (puedes copiarlas y pegarlas desde tu programa anterior) presionando <kbd>Entrar</kbd> entre cada una:
</p>

<pre><code class="python">&gt;&gt;&gt; from buildhat import Motor
</code></pre>

<p spaces-before="0">
  Presiona <kbd>Entrar</kbd>.
</p>

<p spaces-before="0">
  Escribe:
</p>

<pre><code class="python">&gt;&gt;&gt; motor_y = Motor('A')
</code></pre>

<p spaces-before="0">
  Presiona <kbd>Entrar</kbd>.
</p>

<p spaces-before="0">
  Escribe:
</p>

<pre><code class="python">&gt;&gt;&gt; motor_y.run_to_position(0, 100)
</code></pre>

<p spaces-before="0">
  Presiona <kbd>Entrar</kbd>.
</p>

<p spaces-before="0">
  Esto debería centrar o <strong x-id="1">poner a cero</strong> tu motor.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Ajusta la posición del brazo del bolígrafo empujando suavemente la barra dentada hacia el centro de su recorrido, de modo que el lápiz o bolígrafo se alinee con el otro motor.
</p>

<p spaces-before="0">
  <img src="images/pencil_lined_up.jpg" alt="El lápiz está en el centro de la estructura, en línea con el motor utilizado para impulsar el alimentador de papel." />
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- save ---
</p>

