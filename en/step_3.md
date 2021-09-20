## Creating a plot range

By default your motor will always take the shortest path to the new position. 

For example; if the motor is at 170 degrees and the next position is -170 degrees, it will travel in a clockwise direction, passing through the 180 degree position in order to get to its destination as quickly as possible. 

This is fine for our simulation, but our plotter will not have this freedom of movement. Once the pen has reached the top or bottom of the paper (y-axis) it cannot continue to travel up to emerge at the bottom - it will break. So your plotter will always need to be prevented from travelling clockwise past the 180 degree mark.

![A movie clip showing a LEGO motor with a black beam element attached. The motor is turning and the attached beam rotating like a clock hand in response to the data. The motor  turns through a full 360 degrees, travelling clockwise and anti-clockwise and sometimes passing through the zero position in either direction.](images/motor_through_zero.gif)

This can be achieved by altering the behaviour of the motor when moving to a position. By passing an additional `direction=` parameter to the `run_to_position()` function. You can set this value to `"clockwise"`, `"anticlockwise"` or `"shortest"`, which is the default 'shortest path' behaviour).

![A movie clip showing a LEGO motor with a black beam element attached. The motor is turning and the attached beam rotating like a clock hand in response to the data. The motor only turns between 0 and 180 degrees, but never passes through zero.](images/motor_not_zero.gif)

So for example:
```python
motor_y.run_to_position(50,100,direction="anticlockwise")
```
will drive a motor to 50 degrees position, turning anti-clockwise at maximum speed.

It is possible to add a **conditional check** to your loop to ensure that the motor never passes through 180 degrees and always moves from a higher angle to a lower one by turning in an anti-clockwise direction. 

We will store the last position in a variable at the end of the loop and use that at the start of loop to see if the new position is greater or smaller than the preceding one, then choose the right direction to travel to avoid breaking the plotter arm.


```
--- task ---
Change your script so that you can carry out this check using an `if` conditional:
```python
if sensor_data < last value:
    # move anti-clockwise
else:
    # move clockwise
```
--- /task ---

Your modified loop should look like this (with the `import` lines and BuildHAT setup at the top). Note that `last_value` is set to be the start position (in this case, 0) **before** the `while` loop. 

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 7
line_highlights: 7
---

last_value = 0
while True:
    sensor_data = randint(-180,180)
    print(sensor_data)
    if sensor_data < last value:
        motor_y.run_to_position(sensor_data, 100, direction="anticlockwise") # move anti-clockwise
    else:
        motor_y.run_to_position(sensor_data, 100, direction="clockwise") # move clockwise
    sleep(0.1)
--- /code ---
--- /task ---


This conditional test will be preventing the motor from turning from a negative value to a positive one *without* passing through 180 degrees (and vice versa).

In the next step, you will follow the LEGO build instructions to make the plotter.

--- save ---

