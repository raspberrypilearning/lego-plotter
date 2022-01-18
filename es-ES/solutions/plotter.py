#!/usr/bin/python3
from random import randint
from time import sleep
from buildhat import Motor, ForceSensor
from vcgencmd import Vcgencmd

motor_y = Motor('A')
motor_x = Motor('B')
boton = ForceSensor('C')
vcgm = Vcgencmd()

def remap(min_temp, max_temp, min_angulo, max_angulo, temp):
    temp_rango = (max_temp - min_temp)
    motor_rango = (max_angulo - min_angulo)
    mapeado = (((temp - min_temp) * motor_rango) / temp_rango) + min_angulo
    return int(mapeado)

motor_y.run_to_position(0, 100)
motor_x.start(speed=-25)

while not boton.is_pressed():
    temp = vcgm.measure_temp()
    angulo_actual = motor_y.get_aposition()
    nuevo_angulo = remap(53, 57, -170, 170, temp)
    print(f'temp is {temp} angulo_actual is {angulo_actual} nuevo_angulo is {nuevo_angulo}')
    if nuevo_angulo > angulo_actual:
        motor_y.run_to_position(nuevo_angulo, 100, direction="clockwise")
        print('Girando en sentido horario')
    elif nuevo_angulo < angulo_actual:
        motor_y.run_to_position(nuevo_angulo, 100, direction="anticlockwise")
        print('girando en sentido antihorario')
    sleep(0.1)
    
motor_x.stop()
motor_y.run_to_position(0, 100)