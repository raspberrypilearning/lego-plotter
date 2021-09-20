## Adding a real-time data source

There are are a huge variety of sensors you could add to your Raspberry Pi to provide a data feed for your plotter.

Let's start with an inbuilt data source: the temperature of the CPU on the Raspberry Pi itself. If you haven't installed the `vcgencmd` library, you should do that now. 

--- collapse ---
---
title: Installing the Vcgencmd python library
---
Make sure you are connected to the internet.

Open the terminal on your Raspberry Pi by pressing `Ctrl + Alt + T` on your keyboard.

At the prompt type: `sudo pip3 install vcgencmd` and press Enter.
 
Wait for the confirmation message (it won't take long) then close the terminal window.

--- /collapse --- 

--- task ---

Using the Shell/REPL in Thonny, enter the following lines of Python to test reading the CPU temperature.

```python
>>> from vcgencmd import Vcgencmd
```
Press Enter.

Type:
```python
>>> vcgm = Vcgencmd()
```
Press Enter.

Type:
```python
>>> vcgm.measure_temp()
```
Press Enter.

You should see the shell return a number value (it should be somewhere around 50) - this is how hot your CPU is running.

--- /task ---

Now let's warm things up by getting the CPU to do some work!

--- task ---
Open the web browser and watch a YouTube video. After a few seconds, go back to Thonny and re-run the last line of Python and you should see that the temperature has increased. 
--- /task ---

Now that you've seen how to read the temperature of the CPU with Python, we will modify your plotter.py program so that it uses this as its data source. 

--- task ---
First, underneath the existing import lines at the top of the file, add the lines to import the Vcgencmd library:

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
create a vcgencmd instance:
--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
line_highlights: 10
---
from random import randint
from time import sleep
from buildhat import Motor, ForceSensor

motor_y = Motor('A')
motor_x = Motor('B')
button = ForceSensor('C')
motor_y.run_to_position(0,100)
motor_x.start(-20)
vcgm = Vcgencmd()
--- /code ---

--- /task ---

--- task ---

Change the program so that it uses real-time temperature values rather than randomly generated numbers. To do this we need to replace `randint(-180, 180)` with `vcgm.measure_temp()`.

Because the `run_to_position()` function takes only integer values for the desired angular position, you need to convert the real values returned by `measure_temp()` accordingly:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 14
line_highlights: 15
---
while not button.is_pressed():
    sensor_data = int(vcgm.measure_temp())
    print(sensor_data)
--- /task ---

Before you can use the temperature of the Raspberry Pi's CPU as a data source for you plotter, you want to make sure that the maximum possible value that will be produced by the data source will be mathematically converted so that it fits on a scale between -180 and 180. 

The range of temperature values produced by `vcgencmd` should be from around 50 degrees C (when the Raspberry Pi is on but not doing very much) to less than 90 degrees C when working hard (at 85 degrees C the Raspberry Pi will throttle its performance to keep the temperature below this value).

--- task ---
Add a scaling factor variable to your plotter.py program so that every change in temperature of 1 degree C causes 1 degree of movement of the motor.

```python
scaling_factor = 7.2
```

And the two lines that move the motor either clockwise or anticlockwise should become:

```python
motor_y.run_to_position(sensor_data*scaling_factor, 100, direction="anticlockwise")
```

--- /task ---
There's ome more thing to do. 

Currently the plotter is configured to start drawing with the line in the center of the paper and then be able to record positive and negative values. You know that your data values will never be negative in this case, im fact they are unlikely to go muc below 40 degrees even with a fan cooling the CPU. So you can move the starting position of the pen to be much closer to the bottom of its range of motion. 

--- task ---
Change the line that currently moves the plotter to the zero position so that it instead sets it to just above the minimum value that you obtained from the calibration step.


```python
motor_y.run_to_position(-150, 100)

```

--- /task ---

--- task ---
Now you can run your program. Make the Raspberry Pi CPU get warmer like you did before and you should see the pen gradually move upwards.

--- /task ---




--- save ---