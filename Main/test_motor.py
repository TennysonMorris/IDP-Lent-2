from machine import Pin, PWM
from time import sleep
from lib.motor import Motor

#Assign motors to each wheel.
leftWheel = Motor(6,7)
rightWheel = Motor(5,4)

leftWheel.fwd(100)
rightWheel.fwd(100)
sleep(2)
leftWheel.rvrs(100)
rightWheel.rvrs(100)
sleep(2)
leftWheel.kill()
rightWheel.kill()
