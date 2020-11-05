## Adding a data source

There are are a huge variety of sensors you could add to your Raspberry Pi to provide a data feed for your plotter.

Let's start with an inbuilt data source: the temperature of the CPU on the Raspberry Pi itself. If you haven't installed the `vcgencmd` library, you should do that now. 

--- task ---

Using the Shell/REPL in Thonny, enter the following lines of Python to test reading the CPU temperature.

```python
>>> from vcgencmd import Vcgencmd
>>> vcgm = Vcgencmd()
>>> vcgm.measure_temp()
```

54.0

--- /task ---

--- task ---
Now let's warm things up by getting the CPU to do some work.  You could try opening the Chromium web browser and wathcing a YouTube movie. After a few seconds re-run the last line of Python and you should see that the temperature has increased. 

--- /task ---


Now that you've seen how to read the temperature of the CPU with Python, modify your plotter.py program so that it uses this as its data source. 

--- task ---
First, underneath the existing import lines at the top of the file, add the lines to import the Vcgencmd library and create a vcgencmd instance:

```python
from vcgencmd import Vcgencmd
vcgm = Vcgencmd()
```

--- /task ---

--- task ---

Then change the program so that is uses  actual temperature values rather than random generated ones. Because the `move_to_position()` function takes only integer values for the desired angular position, you need to convert the real values returned by `measure_temp()` accordingly.

```python
sensor_data = int(vcgm.measure_temp())
```
--- /task ---

Before you can use the temperature of the Raspberry Pi's CPU as a data source for you plotter, you need to map the range of possible temperatures onto the range of motion of the plotter. In other words, you want to make sure that the maximum possible value that will be produced by the data source will be mathematically converted so that it corresponds to a movemnet of the motor that takes it just below the furthest positive y position identified in the calibration step. Similarly the minimum value produced by the source should not cause the plotter arm to travel too far down (neagtive y). 

The range of temperrtaure values prooduced by `vcgencmd` should be from around 50 degrees C (when the Raspberry Pi is on but not doing very much) to less than 90 dgrees C when working hard (at 85 degrees C the Raspberry Pi will throttle its performance to keep the temperature below this value). 

So you'll probably need to map a range of 40 degrees of temperature onto a range of movement of 520 degrees (-170 + 350). So every degree by which the temperature changes can be represented by 13 degrees of rotation (520 / 40).

--- task ---
Add a scaling factor variable to your plotter.py program so that every change in temperature of 1 degree C causes 1 degree of movement of the motor.

```python
scaling_factor = 13
```

And the two lines that move the motor either clockwise or anticlockwise should become:

```python
motor_y.run_to_position(sensor_data*scaling_factor, 100, direction=1)
```

--- /task ---
There's ome more thing to do. 

Currnetly the plotter is configured to start drawing with the line in the center of the paper and then be able to record positive and negative values. You know that your data values will never be negtaive in this case, im fcat they are unlikley to go muc below 40 degrees even with a fan cooling the CPU. So you can movev the starting position of the pen to be much closer to the bottom of its range of motion. 

--- task ---
Change the line that currently moves the plotter to the zero position so that it instead sets it to just above the minimum value that you obtained from the calibrationstep.


```python
motor_y.run_to_position(-150, 100)

```

--- /task ---

--- task ---
Now you can run your program. Make the Raspberry Pi CPU get warmer liek you did before and you should see the pen gradually move upwards.

--- /task ---

Onec you're happy that this is working as you'd expect, add a sheet of paper underneat the small wheels and then modify you program to slowly turn these wheels as measurements are recorded.

--- task ---
Plug the large Technic motor (which drives these wheels) into port B on the BuildHAT. 
--- /task ---

--- task ---
Create a shortcut variable for this motor below the similar line for `motor_y`:
```python
motor_x = bh.port.B.motor

```
--- /task ---

--- task ---
Then add a line to start this motor turning imediatly before the `while True` loop:

```python
motor_x.run_at_speed(10, 100)

```

--- /task ---

--- save ---