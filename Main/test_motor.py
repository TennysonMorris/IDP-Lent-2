from machine import Pin, PWM, I2C
from time import sleep
from lib.motor import Motor
from tcs34725 import TCS34725

#Assign motors to each wheel.
leftWheel = Motor(6,7)
rightWheel = Motor(5,4)

#leftWheel.fwd(100)
#rightWheel.fwd(100)

#Set pins for colour sensor (adjustable).
i2c_bus = I2C(0, sda=Pin(16), scl=Pin(17), freq = 400000)
tcs = TCS34725(i2c_bus)

print('raw: {}'.format(tcs.read('raw')))

print('rgb: {}'.format(tcs.read('rgb')))
