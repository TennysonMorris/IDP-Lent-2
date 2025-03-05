from machine import Pin, PWM
from time import sleep
from lib.motor import Motor
import lib.moving as mv
import lib.pathfinding as pf
import lib.settings as foo
foo.init()
#Set pins for each wheel
leftWheel = Motor(5,4)
rightWheel = Motor(6,7)

#Set pins for LED and line sensor (adjustable).
lineSensorRight = Pin(17, Pin.IN, Pin.PULL_UP)
lineSensorLeft = Pin(16, Pin.IN, Pin.PULL_UP)
juncSensorRight = Pin(19, Pin.IN, Pin.PULL_UP)
juncSensorLeft = Pin(20, Pin.IN, Pin.PULL_UP)

#initialize initial node, path, direction
foo.current_node = 0
destination = 3
current_path = pf.set_path() #hard coded to first pickup
foo.current_direction = "N"
position = [current_node, current_direction, current_path]

while True:
        
    #Check whether it is necessary to turn
    if mv.detect_junction(juncSensorLeft, juncSensorRight)[0] is True: #function updates current direction
        turnDirection = mv.detect_junction[1]
        print("turnign", turnDirection)
        #Conditional to determine which wheel should be driven forwards to turn in the desired direction.
        if turnDirection == "Left":
            mv.turn(leftWheel, rightWheel, lineSensorLeft, lineSensorRight)
        elif turnDirection == "Right":
            mv.turn(rightWheel, leftWheel, lineSensorLeft, lineSensorRight)
    #line follower
    else:
        leftSpeed, rightSpeed = mv.line_follower(lineSensorLeft, lineSensorRight)
        leftWheel.fwd(leftSpeed)
        rightWheel.fwd(rightSpeed)
    
    #what to do when destination reached
    if current_path[current_node] == destination:
        break
#         #at depot
#         if destination == 5 or destination == 19:
#             #box dropoff
#         elif destination == 0:
#             #???
#         else:
#             #boxpickup

