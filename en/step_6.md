## Button control

To stop and start the plotter running, you can add a button to your build.

--- task ---

The LEGO Force sensor can act as a simple button. Connect one to port C on your BuildHAT.

![A close-up photo of part of the LEGO plotter that a LEGO force sensor has been added.](images/force.jpg)

--- /task ---

--- task ---
Edit your `plotter.py` program to include button control. To the end of the line which says `from buildhat import Motor` add a comma followed by `ForceSensor` (making sure you get **both** capital letters!):

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
line_highlights: 3
---
from random import randint
from time import sleep
from buildhat import Motor, ForceSensor
--- /code ---

--- /task ---

--- task ---

Add this line to set up a shortcut variable for the button after the similar lines for the motors:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 7
---
motor_y = Motor('A')
motor_x = Motor('B')
button = ForceSensor('C')
motor_y.run_to_position(0, 100)
motor_x.start(-20)

--- /code ---

--- /task ---

--- task ---

Change your main loop from `while True` to:

```python
while not button.is_pressed():
```
--- /task ---

--- task ---

Now you can stop the plotter operating by pressing the button. To tidy everything up and stop both motors, add the following lines after - and outside of -  the main loop

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 24
---

motor_y.run_to_position(0,100)
motor_y.stop()
motor_x.stop()

--- /code ---

--- /task ---

Now you are ready to test your plotter. Your final script should look like this:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
---
from random import randint
from time import sleep
from buildhat import Motor, ForceSensor

motor_y = Motor('A')
motor_x = Motor('B')
button = ForceSensor('C')
motor_y.run_to_position(0,100)
motor_x.start(-20)
last_value=0

while not button.is_pressed():
    sensor_data = int(vcgm.measure_temp()-40)
    print(sensor_data)
    if sensor_data < last_value:
        motor_y.run_to_position(sensor_data*5, 100, direction="anticlockwise")
        last_value = sensor_data
    else:
        motor_y.run_to_position(sensor_data*5, 100, direction="clockwise")
        last_value = sensor_data
    sleep(0.1)
    
motor_y.run_to_position(0,100)
motor_y.stop()
motor_x.stop()

--- /code ---


--- task ---

Feed a piece of paper from the back of the plotter so that one short edge is just beyond the pen.

--- /task ---

--- task ---

Start the program in Thonny, and watch as the pen plots your random data on your paper!

--- /task ---

--- task ---

Once the paper has been used, press the Force sensor button to stop everything. 

--- /task ---

![A photo of a piece of paper which on which the plotter has draw a green trace](images/paper.JPG)

In the next step you will use a real-time data source for your input data! 