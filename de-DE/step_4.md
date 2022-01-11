## Baue den Plotter

In diesem Schritt baust du einen x/y-Plotter mit LEGO®.

Dafür gibt es viele Möglichkeiten, aber die Bauanleitung für das Projekt LEGO® SPIKE™ Prime *Track Your Parcels* ist ein guter Ausgangspunkt. Du kannst den Motor aus dem vorherigen Schritt für den Y-Achsen-Motor (denjenigen, der den Stift hält) zum Bau verwenden.

![Eine Zeichnung aus der LEGO® Anleitung.](images/build1.png)

--- task ---

Du musst den Aufbau leicht anpassen, damit der Arm einen Stift halten kann. Gummibänder sind eine großartige Möglichkeit, einen Stift fest an LEGO zu halten.

![Ein Foto des teilweise zusammengebauten Plottermodells mit einem Stift, der mit einem Gummiband an den LEGO® Elementen befestigt ist.](images/rubber_bands.jpg)

<embed src="https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book1of2-05883f81fed73ac3738781d084e0d4e2.pdf" width="600" height="500" alt="pdf" pluginspage="http://www.adobe.com/products/acrobat/readstep2.html">
  </p> 
  
  <p spaces-before="0">
    --- /task ---
  </p>
  
  <p spaces-before="0">
    Nach dem zweiten Teil der Anleitung vervollständigst du den Mechanismus, der die beiden Motoren verwendet, um den Plotter anzutreiben.
  </p>
  
  <p spaces-before="0">
    <img src="images/build2.png" alt="Eine Zeichnung aus dem zweiten Teil der LEGO® Anleitung." />
  </p>
  
  <p spaces-before="0">

<embed src="https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book2of2-80dc3c8c61ec2d2ffa785b688326ef74.pdf" width="600" height="500" alt="pdf" pluginspage="http://www.adobe.com/products/acrobat/readstep2.html">
      </p> 
      
      <p spaces-before="0">
        --- task ---
      </p>
      
      <p spaces-before="0">
        Schließe den LEGO® Technic™-Motor, der den Stift nach oben und unten treibt, an Anschluss A am Build HAT an.
      </p>
      
      <p spaces-before="0">
        --- /task ---
      </p>
      
      <p spaces-before="0">
        Jetzt kannst du deine simulierte Datenquelle verwenden, um deinen Plotter zu testen. Lass vorerst den Deckel auf deinem Stift oder entferne ihn ganz, während du die durch die Daten verursachte Bewegung beobachtest.
      </p>

<h3 spaces-before="0">
  Kalibriere den Plotter
</h3>

<p spaces-before="0">
  Dein Programm ermöglicht es dem Motor derzeit, sich über seinen gesamten Bewegungsbereich zu drehen (-180 bis +180 Grad vom Nullpunkt). Die physischen Einschränkungen des Plotters bedeuten aber, dass der Stiftarm gegen andere Teile des Aufbaus prallte, wenn du versuchtest, die Zahnstange in ihre maximale und minimale Position zu bringen. Um dies zu vermeiden, musst du den Balken zentrieren.
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Klicke in den <strong x-id="1">Shell-Bereich</strong> von Thonny (das Fenster unter dem Code), damit du Python zeilenweise ausführen kannst.
</p>

<p spaces-before="0">
  Gib Sie diese Zeilen einzeln in die <strong x-id="1">Shell</strong> ein (du kannst sie einfach aus deinem Programm oben kopieren und einfügen) und drücken nach jeder Zeile <kbd>Enter</kbd>:
</p>

<pre><code class="python">&gt;&gt;&gt; from buildhat import Motor
</code></pre>

<p spaces-before="0">
  Drücke <kbd>Enter</kbd>.
</p>

<p spaces-before="0">
  Tippe:
</p>

<pre><code class="python">&gt;&gt;&gt; motor_y = Motor('A')
</code></pre>

<p spaces-before="0">
  Drücke <kbd>Enter</kbd>.
</p>

<p spaces-before="0">
  Tippe:
</p>

<pre><code class="python">&gt;&gt;&gt; motor_y.run_to_position(0, 100)
</code></pre>

<p spaces-before="0">
  Drücke <kbd>Enter</kbd>.
</p>

<p spaces-before="0">
  Dies sollte deinen Motor <strong x-id="1">nullen</strong> oder zentrieren.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Passe die Position deines Stiftarms an, indem du die Zahnstange vorsichtig in die Mitte ihres Weges schiebst, sodass der Filz- oder Bleistift mit dem anderen Motor ausgerichtet ist.
</p>

<p spaces-before="0">
  <img src="images/pencil_lined_up.jpg" alt="Der Stift befindet sich in der Mitte des Zeichenbereichs, gleich wie der Motor, der zum Antrieb des Papiereinzugs verwendet wird." />
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- save ---
</p>

