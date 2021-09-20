## Introduction

Use LEGO and the Raspberry Pi Build HAT to create a data plotter. 

### What you will make

--- no-print ---

![A movie showing the LEGO plotter in action. A piece of paper is being fed out of the machine with a green signal being traced out by a pen.](images/plotter_demo.gif)

--- /no-print ---

--- print-only ---
![A photo of the completed plotter project](images/completed.jpg)
--- /print-only ---

--- collapse ---
---
title: What you will need
---
### Hardware

+ A Raspberry Pi computer
+ A Raspberry Pi Build HAT
+ Two LEGO Technic motors
+ A LEGO Technic Force sensor 
OR
+ A push button, breadboard and jumper wires
+ Assortment of LEGO, including two small wheels. We used a selection from the [LEGO Spike Prime kit](https://education.lego.com/en-gb/product/spike-prime)
+ A 9v power supply with a barrel jack. This can be a battery pack, but make sure that all cells are fully charged. 

### Software


+ Python 3
+ The Vcgencmd Python3 library

### Downloads

+ [LEGO Spike Prime Building instructions: Track your parcels 1/2](https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book1of2-05883f81fed73ac3738781d084e0d4e2.pdf)
+ [LEGO Spike Prime Building instructions: Track your parcels 2/2](https://le-www-live-s.legocdn.com/sc/media/lessons/prime/pdf/building-instructions/track-your-packages-bi-pdf-book2of2-80dc3c8c61ec2d2ffa785b688326ef74.pdf)

--- /collapse ---

--- collapse ---
---
title: Installing the Vcgencmd python library
---
Make sure you are connected to the internet.

Open the terminal on your Raspberry Pi by pressing `Ctrl + Alt + T` on your keyboard.

At the prompt type: `sudo pip3 install vcgencmd` and press Enter.
 
Wait for the confirmation message (it won't take long) then close the terminal window.

--- /collapse --- 


--- collapse ---
---
title: What you will learn
---

+ Calculating angles of rotation
+ Mapping data ranges onto appropriate scales for visualisation
+ Using conditional statements  (if/else)

--- /collapse ---

--- collapse ---
---
title: Additional information for educators
---

You can download the completed project [here](http://rpf.io/p/en/projectName-get){:target="_blank"}.

If you need to print this project, please use the [printer-friendly version](https://projects.raspberrypi.org/en/projects/projectName/print){:target="_blank"}.

--- /collapse ---
