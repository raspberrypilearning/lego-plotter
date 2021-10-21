## Build the plotter

In this step, you will build an x/y plotter using LEGO®.

There are plenty of ways you could do this, but the build instructions for the LEGO® SPIKE™ Prime *Track Your Parcels* project are a great starting point. You can use the motor from the previous step for the y-axis motor (the one holding the pen) in the build.

![A drawing from the LEGO® instructions.](images/build1.png)

--- task --- You will need to adapt the build slightly so that the arm is able to hold a pen. Rubber bands are a great way to hold a pen snugly against LEGO.

![A photo of the partially assembled plotter model, with a pen attached to the LEGO® elements with a rubber band.](images/rubber_bands.jpg)

<embed src="https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book1of2-05883f81fed73ac3738781d084e0d4e2.pdf" width="600" height="500" alt="pdf" pluginspage="http://www.adobe.com/products/acrobat/readstep2.html">
  --- /task ---</p> 
  
  <p spaces-before="0">
    The second part of the build completes the mechanism that uses the two motors to drive the plotter.
  </p>
  
  <p spaces-before="0">
    <img src="images/build2.png" alt="A drawing from the second part of the LEGO® instructions." />
  </p>
  
  <p spaces-before="0">

<embed src="https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book2of2-80dc3c8c61ec2d2ffa785b688326ef74.pdf" width="600" height="500" alt="pdf" pluginspage="http://www.adobe.com/products/acrobat/readstep2.html">
      </p> 
      
      <p spaces-before="0">
        --- task ---
      </p>
      
      <p spaces-before="0">
        Connect the LEGO® Technic™ motor that drives the pen up and down to port A on the Build HAT.
      </p>
      
      <p spaces-before="0">
        --- /task ---
      </p>
      
      <p spaces-before="0">
        Now you can use your simulated data source to test your plotter. For now, keep the lid on your pen or remove it all together while you observe the motion caused by the data.
      </p>

<h3 spaces-before="0">
  Calibrate the plotter
</h3>

<p spaces-before="0">
  Your program currently allows the motor to move through its full range of motion (-180 to +180 degrees from the zero point). But the physical constraints of the plotter mean that if you tried to drive the toothed rail to its maximum and minimum positions, it would crash the pen arm into other parts of the build. In order to avoid this, you must centre the bar.
</p>

<p spaces-before="0">
  --- task ---
</p>

<p spaces-before="0">
  Click into the <strong x-id="1">Shell pane</strong> of Thonny (the window beneath the code) so that you can execute Python one line at a time.
</p>

<p spaces-before="0">
  Enter these lines into the <strong x-id="1">Shell</strong> (you can just copy and paste them from your program above) pressing <kbd>Enter</kbd> between each one:
</p>

<pre><code class="python">&gt;&gt;&gt; from buildhat import Motor
</code></pre>

<p spaces-before="0">
  Press <kbd>Enter</kbd>.
</p>

<p spaces-before="0">
  Type:
</p>

<pre><code class="python">&gt;&gt;&gt; motor_y = Motor('A')
</code></pre>

<p spaces-before="0">
  Press <kbd>Enter</kbd>.
</p>

<p spaces-before="0">
  Type:
</p>

<pre><code class="python">&gt;&gt;&gt; motor_y.run_to_position(0, 100)
</code></pre>

<p spaces-before="0">
  Press <kbd>Enter</kbd>.
</p>

<p spaces-before="0">
  This should centre or <strong x-id="1">zero</strong> your motor.
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- task --- Adjust the position of your pen arm by gently pushing the toothed bar to the middle of its path, so that the pencil or pen lines up with the other motor.
</p>

<p spaces-before="0">
  <img src="images/pencil_lined_up.jpg" alt="The pencil is central to the housing, in line with the motor used to drive the paper feeder." />
</p>

<p spaces-before="0">
  --- /task ---
</p>

<p spaces-before="0">
  --- save ---
</p>

