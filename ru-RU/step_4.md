## Строим плоттер

На этом этапе ты построишь координатно-указательный плоттер с помощью LEGO®.

Есть много способов сделать это, но инструкции по сборке для проекта LEGO® SPIKE™ Prime *Отследи свои посылки* — отличная отправная точка. Ты можешь использовать двигатель из предыдущего шага для двигателя оси Y (тот, который держит перо) в этой сборке.

![Рисунок из инструкций LEGO®.](images/build1.png)

--- task ---

Тебе нужно будет немного адаптировать конструкцию, чтобы рука могла держать ручку. Резиновые ленты — отличный способ плотно прижать ручку к LEGO.

![Фотография частично собранной модели плоттера с ручкой, прикрепленной к элементам LEGO® резинкой.](images/rubber_bands.jpg)

<embed src="https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book1of2-05883f81fed73ac3738781d084e0d4e2.pdf" width="600" height="500" alt="pdf" pluginspage="http://www.adobe.com/products/acrobat/readstep2.html">
  </p> 
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    Вторая часть сборки завершает механизм, который использует два двигателя для привода плоттера.
  </p>
  
  <p spaces-before="0">
    <img src="images/build2.png" alt="Рисунок из второй части инструкции LEGO®." />
  </p>
  
  <p spaces-before="0">

<embed src="https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book2of2-80dc3c8c61ec2d2ffa785b688326ef74.pdf" width="600" height="500" alt="pdf" pluginspage="http://www.adobe.com/products/acrobat/readstep2.html">
      </p> 
      
      <p spaces-before="0">
        --- task ---
      </p>
      
      <p spaces-before="0">
        Подсоедини двигатель LEGO® Technic™, который двигает ручку вверх и вниз, к порту A на Build HAT.
      </p>
      
      <p spaces-before="0">
        --- /task ---
      </p>
      
      <p spaces-before="0">
        Теперь ты можешь использовать смоделированный источник данных для тестирования плоттера. А пока держи крышку на своей ручке или сними ее целиком, наблюдая за движением, вызванным данными.
      </p>

<h3 spaces-before="0">
  Калибровка плоттера
</h3>

<p spaces-before="0">
  В настоящее время твоя программа позволяет двигателю совершать полный диапазон движения (от -180 до +180 градусов от нулевой точки). Но физические ограничения плоттера подразумевают, что если ты попытаешься установить зубчатую рейку в ее максимальное и минимальное положения, она врежет ручку пера в другие части сборки. Для того, чтобы этого избежать, необходимо центрировать планку.
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Нажми на панель <strong x-id="1">Оболочка</strong> Thonny (окно под кодом), чтобы ты мог выполнять код Python по одной строке за раз.
</p>

<p spaces-before="0">
  Введи эти строки в оболочку <strong x-id="1">Оболочке</strong> (ты можешь просто скопировать и вставить их из своей программы выше), нажав <kbd>Ввод</kbd> между каждой из них:
</p>

<pre><code class="python">&gt;&gt;&gt; from buildhat import Motor
</code></pre>

<p spaces-before="0">
  Нажми <kbd>Ввод</kbd>.
</p>

<p spaces-before="0">
  Введи:
</p>

<pre><code class="python">&gt;&gt;&gt; motor_y = Motor('A')
</code></pre>

<p spaces-before="0">
  Нажми <kbd>Ввод</kbd>.
</p>

<p spaces-before="0">
  Введи:
</p>

<pre><code class="python">&gt;&gt;&gt; motor_y.run_to_position(0, 100)
</code></pre>

<p spaces-before="0">
  Нажми <kbd>Ввод</kbd>.
</p>

<p spaces-before="0">
  Это должно центрировать или <strong x-id="1">обнулить</strong> твой двигатель.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Отрегулируй положение рычага пера, осторожно надавив на зубчатый стержень до середины его пути, чтобы карандаш или ручка выровнялись с другим мотором.
</p>

<p spaces-before="0">
  <img src="images/pencil_lined_up.jpg" alt="Карандаш находится в центре корпуса, на одной линии с двигателем, используемым для привода устройства подачи бумаги." />
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- save ---
</p>

