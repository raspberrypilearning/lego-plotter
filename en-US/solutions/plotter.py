#!/usr/bin/python3
from random import randint
from time import sleep
from buildhat import Motor, ForceSensor
from vcgencmd import Vcgencmd

motor_y = Motor('A')
motor_x = Motor('B')
button = ForceSensor('C')
vcgm = Vcgencmd()

def remap(min_temp, max_temp, min_angle, max_angle, temp):
    temp_range = (max_temp - min_temp)
    motor_range = (max_angle - min_angle)
    mapped = (((temp - min_temp) * motor_range) / temp_range) + min_angle
    return int(mapped)

motor_y.run_to_position(0, 100)
motor_x.start(speed=-25)

while not button.is_pressed():
    temp = vcgm.measure_temp()
    current_angle = motor_y.get_aposition()
    new_angle = remap(53, 57, -170, 170, temp)
    print(f'temp is {temp} current_angle is {current_angle} new_angle is {new_angle}')
    if new_angle > current_angle:
        motor_y.run_to_position(new_angle, 100, direction="clockwise")
        print('Turning CW')
    elif new_angle < current_angle:
        motor_y.run_to_position(new_angle, 100, direction="anticlockwise")
        print('Turning ACW')
    sleep(0.1)
    
motor_x.stop()
motor_y.run_to_position(0, 100)