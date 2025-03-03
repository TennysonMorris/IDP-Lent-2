from machine import Pin, PWM
from time import sleep
from lib.motor import Motor
import lib.moving as mv
import lib.pathfinding as pf

#Set pins for each wheel
leftWheel = Motor(5,4)
rightWheel = Motor(6,7)

#Set pins for LED and line sensor (adjustable).
lineSensorRight = Pin(17, Pin.IN, Pin.PULL_UP)
lineSensorLeft = Pin(16, Pin.IN, Pin.PULL_UP)
juncSensorRight = Pin(, Pin.IN, Pin,PULL_UP)
juncSensorLeft = Pin(, Pin.IN, Pin,PULL_UP)

#Set pin for the button (used to initiate the code)
button = Pin(18, Pin.IN, Pin.PULL_DOWN)

current_node = 0
current_path = []
current_direction = "N"

while True:
    
    #Find direction to turn towards.
        
    #Check whether it is necessary to turn
    if mv.detect_junction(juncSensorLeft, juncSensorRight)[0] is True:
        turnDirection = mv.detect_junction[1]
        #Conditional to determine which wheel should be driven forwards to turn in the desired direction.
        if turnDirection == "Left":
            mv.turn(leftWheel, rightWheel, lineSensorLeft, lineSensorRight)
        elif turnDirection == "Right":
            mv.turn(rightWheel, leftWheel, lineSensorLeft, lineSensorRight)
    else:
        leftSpeed, rightSpeed = mv.line_follower(lineSensorLeft, lineSensorRight)