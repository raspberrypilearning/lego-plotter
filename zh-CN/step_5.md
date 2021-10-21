## Paper feeding

You will now program the second motor to feed paper through the plotter at a constant rate.

--- task ---

Feed a sheet of A5 paper (or cut up some scrap to about this size) underneath the small wheels from behind.

![Paper has been fed in from the back of the plotter, so that the pencil tip rests on the leading edge.](images/paper_in.jpg)

--- /task ---

--- task ---

Plug the rear LEGO® Technic™ motor (which drives these wheels) into port B on the Build HAT.

--- /task ---

--- task ---

Create an object called `motor_x` for this motor, below the similar line for `motor_y`:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 6
---

motor_y = Motor('A') motor_x = Motor('B') motor_y.run_to_position(0, 100)

--- /code ---

--- /task ---

--- task ---

Add a line to start this motor turning immediately before the `while True` loop:

--- code ---
---
language: python filename: plotter.py line_numbers: true line_number_start: 5
line_highlights: 8
---

motor_y = Motor('A') motor_x = Motor('B') motor_y.run_to_position(0, 100) motor_x.start(-25)

--- /code ---

--- /task ---

This will make the feeder motor run at a constant rate of -25 turns per minute when the program starts. Change the number in the brackets to experiment with the speed.

--- task ---

Run your code and watch the paper being fed through the plotter, as the pencil moves randomly in the `y` direction.

![Animation showing the paper being fed through the plotter while the pencil moves randomly along the y axis.](images/feeding_paper.gif)

--- /task ---

To stop the motor feeding the paper, you can type the following into the **Shell**.

```python
>>> from buildhat import Motor
>>> motor_x = Motor('B')
>>> motor_x.stop()
```

--- save ---


