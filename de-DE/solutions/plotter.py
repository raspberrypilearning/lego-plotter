#!/usr/bin/python3
from random import randint
from time import sleep
from buildhat import Motor, ForceSensor
from vcgencmd import Vcgencmd

motor_y = Motor('A')
motor_x = Motor('B')
taster = ForceSensor('C')
vcgm = Vcgencmd()

def umwandlung(min_temp, max_temp, min_winkel, max_winkel, temp):
    temp_bereich = (max_temp - min_temp)
    motor_bereich = (max_winkel - min_winkel)
    gewandelt = (((temp - min_temp) * motor_bereich) / temp_bereich) + min_winkel
    return int(gewandelt)

motor_y.run_to_position(0, 100)
motor_x.start(speed=-25)

while not taster.is_pressed():
    temp = vcgm.measure_temp()
    winkel_jetzt = motor_y.get_aposition()
    winkel_neu = umwandlung(53, 57, -170, 170, temp)
    print(f'temp is {temp} Motorstellung ist {winkel_jetzt} sensor-wert ist {winkel_neu}')
    if winkel_neu > winkel_jetzt:
        motor_y.run_to_position(sensor_daten, 100, direction="clockwise")
        print('im Uhrzeigersinn')
    elif winkel_neu < winkel_jetzt:
        motor_y.run_to_position(winkel_neu, 100, direction="anticlockwise")
        print('gegen Uhrzeigersinn')
    sleep(0.1)
    
motor_x.stop()
motor_y.run_to_position(0, 100)