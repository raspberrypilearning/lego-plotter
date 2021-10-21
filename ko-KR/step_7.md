## Add a real-time data source

There are are a huge variety of sensors you could add to your Raspberry Pi to provide a data feed for your plotter.

Let's start with an in-built data source: the temperature of the CPU on the Raspberry Pi itself. If you haven't installed the `vcgencmd` library, you should do that now.

--- collapse ---
---
title: Install the Vcgencmd python library
---

Make sure you are connected to the internet.

Open the terminal on your Raspberry Pi by pressing <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>T</kbd> on your keyboard.

At the prompt type: `sudo pip3 install vcgencmd` and press <kbd>Enter</kbd>.

Wait for the confirmation message (it won't take long), then close the terminal window.

--- /collapse ---

--- task ---

Using the **Shell/REPL** in Thonny, enter the following lines of Python to test and read the CPU temperature.

```python
>>> from vcgencmd import Vcgencmd
```
Press <kbd>Enter</kbd>.

Type:
```python
>>> vcgm = Vcgencmd()
```
Press <kbd>Enter</kbd>.

Type:
```python
>>> vcgm.measure_temp()
```
Press <kbd>Enter</kbd>.

You should see the **Shell** return a number value (it should be somewhere around 50) — this is how hot your CPU is running.

--- /task ---

Now let's warm things up by getting the CPU to do some work!

--- task ---

Open the web browser and watch a YouTube video. After a few seconds, go back to Thonny and re-run the last line of Python and you should see that the temperature has increased.

--- /task ---

Now that you've seen how to read the temperature of the CPU with Python, you can modify your `plotter.py` program so that it uses this as its data source.

--- task ---

First, underneath the existing import lines at the top of the file, add the lines to import the Vcgencmd library:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 4
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor from vcgencmd import Vcgencmd

--- /code ---

--- /task ---

--- task --- Create a vcgencmd object:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 1
line_highlights: 9
---

from random import randint from time import sleep from buildhat import Motor, ForceSensor from vcgencmd import Vcgencmd

motor_y = Motor('A') motor_x = Motor('B') button = ForceSensor('C') vcgm = Vcgencmd()

motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

--- task ---

Change the program so that it uses real-time temperature values rather than randomly generated numbers. To do this, you need to replace `randint(-180, 180)` with `vcgm.measure_temp()`.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 15
line_highlights: 16
---

while not button.is_pressed(): temp = vcgm.measure_temp() current_angle = motor_y.get_aposition()

--- /code ---

--- /task ---

Before you can use the temperature of the Raspberry Pi's CPU as a data source for your plotter, you want to make sure that the maximum possible value produced by the data source will be mathematically converted so that it fits on a scale between -180 and 180.

The range of temperature values produced by `vcgencmd` should be from around 50°C (when the Raspberry Pi is on, but not doing very much) to less than 90°C when working hard (at 85°C, the Raspberry Pi will throttle its performance to keep the temperature below this value). Let's say you want to plot a range from 40°C to 90°C — you need to map this to your available values: -180 to 180.

You can create a function to remap one range of values to another range of values.

--- task ---

Add this function above your `while` loop. It will take a temperature range and an angle range, and then remap the temperature into an angle.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 12
line_highlights: 13
---

def remap(min_temp, max_temp, min_angle, max_angle, temp): temp_range = (max_temp - min_temp) motor_range = (max_angle - min_angle) mapped = (((temp - min_temp) * motor_range) / temp_range) + min_angle return int(mapped)

--- /code ---

Now, in the `while` loop, you can use this function to calculate a new angle for the motor to turn to.

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 21
line_highlights: 24
---

while not button.is_pressed(): temp = vcgm.measure_temp() current_angle = motor_y.get_aposition() new_angle = remap(50, 90, -170, 170, temp)

--- /code ---

--- /task ---

Now you can run your program. Make the Raspberry Pi CPU get warmer like you did before and you should see the pen gradually move upwards. Feel free to change the `min_temp` and `max_temp` parameters, if your pen isn't moving too much.

![Animation showing the paper moving through the plotter while the pen moves and draws a fluctuating line.](images/plotter_demo_2.gif)


--- save ---
