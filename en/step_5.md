## Paper feeding

These are the final touches need to make a usable, controllable paper plotter. We will now program the second motor to feed paper through the plotter at a constant rate.

--- task ---
Feed a sheet of A5 paper (or cut up some scrap to about this size) underneath the small wheels from behind.
--- /task --

--- task ---
Plug the rear Technic motor (which drives these wheels) into port B on the BuildHAT. 
--- /task ---

--- task ---
Create a shortcut variable called `motor_x` for this motor, below the similar line for `motor_y`:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 6
---
motor_y = Motor('A')
motor_x = Motor('B')
motor_y.run_to_position(0, 100)

--- /code ---
--- /task ---

--- task ---
Add a line to start this motor turning immediately before the `while True` loop:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 8
---
motor_y = Motor('A')
motor_x = Motor('B')
motor_y.run_to_position(0, 100)
motor_x.start(-20)

--- /code ---

--- /task ---

This will make the feeder motor run at a constant rate of -20 turns per minute when the program starts. Change the number in the brackets to experiment with the speed. 

In the next step, we will make a button that can turn the plotter off. 

--- save ---


