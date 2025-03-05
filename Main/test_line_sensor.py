from machine import Pin, PWM
from time import sleep
from lib.motor import Motor
from moving import turn

leftWheel = Motor(6,7)
rightWheel = Motor(5,4)
#Set pins for LED and line sensor (adjustable).
rightLineFollower = Pin(17, Pin.IN, Pin.PULL_UP)
leftLineFollower = Pin(16, Pin.IN, Pin.PULL_UP)
leftJuncDetector = Pin(19, Pin.IN, Pin.PULL_UP)

x = 0
#Loop to match line sensor and led value to test operational distance.
while True:
    
    if leftLineFollower.value() == 0:
        rightWheel.fwd(50)
    else:
        rightWheel.fwd(100)
        
    if rightLineFollower.value() == 0:
        leftWheel.fwd(50)
    else:
        leftWheel.fwd(100)
        
#     if leftJuncDetector.value() == 1 or x == 0:
#         x += 1
#         turn(leftWheel, rightWheel,  leftLineFollower, rightLineFollower, leftJuncDetector)
#         break
#   x -= 0.05
#   x = max(0, x)
#   sleep(0.05)
