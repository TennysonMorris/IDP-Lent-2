from machine import Pin, PWM
from time import sleep
from lib.motor import Motor
from lib.moving import line_follower
import lib.pathfinding as pf

#Set pins for each wheel
leftWheel = Motor(5,4)
rightWheel = Motor(6,7)

#Set pins for LED and line sensor (adjustable).
lineSensorRight = Pin(17, Pin.IN, Pin.PULL_UP)
lineSensorLeft = Pin(16, Pin.IN, Pin.PULL_UP)

#Set pin for the button (used to initiate the code)
button = Pin(18, Pin.IN, Pin.PULL_DOWN)

while True:
    
    turnDirection = pf.turn_direction(current_direction, current_path, current_node)
    if turnDirection == "Straight":
        (leftSpeed, rightSpeed) = line_follower(lineSensorLeft, lineSensorRight)
        leftWheel.fwd(leftSpeed)
        rightWheel.fwd(rightSpeed)
        
    elif turnDirection == "Left":
    
    elif turnDirection == "Right":
    