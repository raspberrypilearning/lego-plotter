## Simulated data

Before you use your plotter to record real data, let's test it with sime simulated measurements.

--- task ---

Connect a monitor, keyboard and mouse to your Raspberry Pi.

Attach the Build HAT to your Raspberry Pi and connect a 7.5v power supply to the barrel jack of the BuildHAT. 
--- /task ---

--- task ---

Open Thonny and add the following lines to begin your program by importing the libraries you will be using:

```python
from random import randint
from time import sleep
from build_hat import BuildHAT
```

--- /task ---

--- task ---

Now you can use the `randint` function to create a random value between a pre-defined range and store it in a variable:

```python3
sensor_data = randint(0,360)
print(sensor_data)
```

--- /task ---

--- task ---

Now you can use the `randint` function to create a random value between a pre-defined range and store it in a variable:

```python3
sensor_data = randint(0,100)
print(sensor_data)
```

--- /task ---
If you run that program you should see a single integer value displayed. Run it again and you should gt a different value.

--- task ---

Now if you wrap those lines in a loop you should be able to create a simulated data source that produces a new value every 10th of a second.

--- hints ---
--- hint ---
To run the same lines continuously you can use a `while True:` loop
--- /hint ---
--- hint ---
To set the time between each value being generated, you can use `sleep(0.1)` tp pause for a 10th of second (0.1 seconds) in between each iteration.
--- /hint ---
--- hint ---
You modified program should look this this (with the `import` lines at the top)
```python
while True:
    sensor_data = randint(0,360)
    print(sensor_data)
    sleep(0.1)
```
--- /hint ---
--- /hints ---
--- /task ---

Now we have some relaible data, we can use this to control the position of a motor
--- task ---
Connect a LEGO Technic motor to port A on the Build HAT. Add some additional LEGO elemnets to the motor axel so that it is easy to see the motor turning (a ling staright piece works well as a pointer). Line up the elemnet with the line mark on the motor and then set the motor to the zero position

![encoder](images/zero.JPG)

--- /task ---

--- task ---
Modify the main body of your program so that angle turned to by the motor is the same as the latest value produced by our simulated sensor. You can probably see that the choice of range for the values was important.

```python

bh = BuildHAT()
motor_y = bh.port.A.motor
motor_y.run_to_position(0, 100)
while True:
    sensor_data = randint(0,360)
    print(sensor_data)
    motor_y.run_to_position(sensor_data, 100)
    sleep(0.1)
```
--- /task ---
You should see your motor spin clockwise to different positions in response to the chnaging data. If you run the progarm again it should initially reset the motor position back to 0 before following the simulated data values. 

The second parameter passed to the `run_to_position()` function sets the speed at which the motor moves (100 is the fastest). Whne the plotter is in action you will want the trace to repsond quickly to changes in data so it will need to move as quickly as possible.

This approach will be fine for a data source that only ever produces positive values. How about data which might also have values less than zero (e.g. temperature, acceleration)?

--- task ---
Modify the main body of your program so that the data produced can be either positive or negative, but has the same overall difference between minimum and maximum values. 

--- hints ---
--- hint ---
Currently the random values can be between 0 and 360, always positive. To keep the same difference between maximum and minimum while producing negative values you should change you code so that the values generated are between -180 and +180.
--- /hint ---
--- hint ---
You need to adjust the parameters passed to the `randint()` function.
--- /hint ---
--- hint ---
Change the line to be 
```python

    sensor_data = randint(-180,180)

```
--- /hint ---
--- /hints ---
--- /task ---

Run your program again. This time the motor should swing both clockwise and anti-clockwise depending on the sign of the simulated data.

--- save ---