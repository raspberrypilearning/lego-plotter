## Creating a plot range

You need to be able to control the direction the motors move in — clockwise or anti-clockwise.

--- collapse ---
---
title: Why you need to change the way the motors move
---

Your motor will always take the shortest path to the new position. 

For example, if the motor is at 170 degrees and the next position is -170 degrees, it will travel in a clockwise direction, passing through the 180 degree position in order to get to its destination as quickly as possible. 

![A movie clip showing a LEGO® Technic™ motor with a black beam element attached. The motor is turning and the attached beam is rotating like a clock hand in response to the data. The motor turns through a full 360 degrees, travelling clockwise and anti-clockwise, and sometimes passing through the zero position in either direction.](images/motor_through_zero.gif)

This is fine for our simulation, but our plotter will not have this freedom of movement. Once the pen has reached the top or bottom of the paper (y-axis), it cannot continue to travel up to emerge at the bottom — it will break. So your plotter will need to be prevented from travelling clockwise past the 180 degree mark.

This can be achieved by altering the behaviour of the motor when moving to a position. You can do this by passing an additional `direction=` parameter to the `run_to_position()` function. You can set this value to `"clockwise"`, `"anticlockwise"`, or `"shortest"`, which is the default 'shortest path' behaviour.

![A movie clip showing a LEGO® Technic™ motor with a black beam element attached. The motor is turning and the attached beam rotating like a clock hand in response to the data. The motor turns between 0 and 180 degrees, but never passes through zero.](images/motor_not_zero.gif)

So, for example, `motor_y.run_to_position(50, 100, direction="anticlockwise")` will drive a motor to the 50 degrees position, turning anti-clockwise at maximum speed.

It is possible to add a **conditional check** to your loop to ensure that the motor never passes through 180 degrees and always moves from a higher angle to a lower one by turning in an anti-clockwise direction.

You can find the last position of the motor by using `motor_y.get_aposition`.

--- /collapse ---

--- task ---

Check for the motor's current angle at the top of your `while` loop.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 7
line_highlights: 8
---
while True:
    current_angle = motor_y.get_aposition()
    sensor_data = randint(-180, 180)
    print(sensor_data)
    motor_y.run_to_position(sensor_data, 100)
    sleep(0.1)
--- /code ---

--- /task ---

--- task ---

Now, in the `while` loop, you can add a check to see if the current value of `sensor_data` is greater or less than the `current_angle`.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 7
line_highlights: 11-16
---
while True:
    current_angle = motor_y.get_aposition()
    sensor_data = randint(-180, 180)
    print(sensor_data)
    if sensor_data > current_angle:
        motor_y.run_to_position(new_angle, 100, direction="clockwise")
        print('Turning CW')
    elif new_angle < current_angle:
        motor_y.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)
--- /code ---

--- /task ---

--- task ---

Run your code. This conditional test will be preventing the motor from turning from a negative value to a positive one **without** passing through 180 degrees (and vice versa).

--- /task ---

--- save ---

