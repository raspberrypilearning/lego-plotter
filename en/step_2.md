## Moving the motors with data

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
You may have seen in earthquake disaster movies where a <span style="color: #0faeb0">[seismometer](https://en.wikipedia.org/wiki/Seismometer) </span> is used to show the impending tremors. 

The design of such devices is quite simple: one motor is used to move the paper across the pen (the x-axis) while another at right angles to the first, moves the pen up and down in response to the changing data (y-axis). </p>

In this project you will create a plotter from LEGO, and connect it to your Raspberry Pi so it can plot real-time data.

--- task ---

Connect a monitor, keyboard and mouse to your Raspberry Pi. If you've never used a Raspberry Pi before, you might want to start with [this project](https://learning-admin.raspberrypi.org/en/projects/raspberry-pi-getting-started).

Attach the Build HAT to your Raspberry Pi (making sure you can see the Raspberry Pi logo on top) and connect a 7.5v power supply to the barrel jack of the BuildHAT. This will boot your Raspberry Pi.

--- /task ---

--- task ---

Open Thonny from the programming menu and add the following lines to begin your program by importing the libraries you will be using:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
line_highlights: 1,2,3
---
from random import randint
from time import sleep
from buildhat import Motor

--- /code ---

Save this program as `plotter.py` by pressing `Ctrl + s`.

--- /task ---

--- task ---

Now use the `randint` function to create a random value between a pre-defined range (in this case -180 to 180) and store it in a variable:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 5,6
---
sensor_data = randint(-180,180)
print(sensor_data)

--- /code ---

--- /task ---

--- task ---

Run your program a few times by clicking the **Run** button at the top of the window. You should see different values appear in the shell beneath your code each time.

--- /task ---

Instead of running this script manually, creating a **loop** will have the script run itself repeatedly. To run the same lines continuously you can use a `while True:` loop.

--- task ---

Add a blank line above the code you just added by pressing Enter.

On this new line, enter `while True:`, making sure you have a capital 'T'.

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 5
---
while True:
sensor_data = randint(-180,180)
print(sensor_data)

--- /code ---

--- /task ---

--- task ---

Add four spaces to the start of each of the lines beneath to create an **indented code block**. This tells the computer which lines are included in your loop.


--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 6,7
---
while True:
    sensor_data = randint(-180,180)
    print(sensor_data)

--- /code ---

--- /task ---

--- task ---

At the end of your code, press Enter to add another indented line. On this line type `sleep(0.1)`.


--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 5
line_highlights: 8
---
while True:
    sensor_data = randint(-180,180)
    print(sensor_data)
    sleep(0.1)

--- /code ---

--- /task ---

--- task ---

Your modified program should look this this:

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
---
from random import randint
from time import sleep
from buildhat import Motor

while True:
    sensor_data = randint(-180,180)
    print(sensor_data)
    sleep(0.1)
--- /code ---

--- /task ---

Now we have some reliable data, we can use this to control the position of a motor.

--- task ---
Connect a LEGO Technic motor to port A on the Build HAT. Add some additional LEGO elements to the motor axle so that it is easy to see the motor turning (a ling straight piece works well as a pointer). 

--- /task ---

--- task ---
Line up the element with the line mark on the motor and then set the motor to the zero position:

![A photo of a LEGO technic motor showing the lollipop and zero labels used to set the encoder to 0 degrees](images/zero.JPG)

--- /task ---

Now, modify the main body of your program so that angle turned to by the motor is the same as the latest value produced by our simulated sensor. 

To do this, we need to set up our motor to be accessed in the program. 

--- task ---

Add two new lines above your `while True:` loop by pressing Enter twice.

--- /task ---

--- task ---

On the first new line enter `motor_y = Motor('A')` - this tells the computer there is a motor connected to port A.

--- /task ---

--- task ---

On the line beneath this type `motor_y.run_to_position(0, 100)` to make sure the motor resets to 0 when you run the script. The two numbers in this command represent the position to turn to, and the speed at which to turn.

--- /task ---

--- task ---

The final line of code required makes the motor turn to the angle generated each loop. Above your last line of code, press Enter to create a new line and add `motor_y.run_to_position(0, 100)` 

--- /task ---

Your final script should look like this: 

--- code ---
---
language: python
filename: plotter.py
line_numbers: true
line_number_start: 1
---
from random import randint
from time import sleep
from buildhat import Motor

motor_y = Motor('A')
motor_y.run_to_position(0, 100)

while True:
    sensor_data = randint(-180,180)
    print(sensor_data)
    motor_y.run_to_position(sensor_data, 100)
    sleep(0.1)

--- /code ---

--- task ---

Click **Run** and you should see your motor spin clockwise to different positions in response to the changing data. If you run the program again it should initially reset the motor position back to 0 before following the simulated data values. 

![A movie clip showing a LEGO motor with a black beam element attached. The motor is turning and the attached beam rotating like a clock hand in response to the data. The motor only turns between 0 and 180 degrees, travelling clockwise and anti-clockwise ](images/motor_180.gif)

--- /task ---

In the next step we will stop our plotter motor from doing full circles, as this will break the machine we are building. 