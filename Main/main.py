from machine import Pin, PWM
from settings import Robot
from time import sleep
from lib.motor import Motor
import lib.moving as mv
import lib.pathfinding as pf
import lib.collection as clt

#Set pins for each wheel
leftWheel = Motor(5,4)
rightWheel = Motor(6,7)

#Set pins for LED and line sensor (adjustable).
lineSensorRight = Pin(17, Pin.IN, Pin.PULL_UP)
lineSensorLeft = Pin(16, Pin.IN, Pin.PULL_UP)
juncSensorRight = Pin(19, Pin.IN, Pin.PULL_UP)
juncSensorLeft = Pin(20, Pin.IN, Pin.PULL_UP)
led = Pin(0, Pin.OUT)
#initialize initial node, path, direction
destination = 13
path = pf.set_path(0, destination) #hard coded to first pickup
robot = Robot(path, destination)

led.value(0)
sleep(1)
led.value(1)
while True:
    #Check whether it is necessary to turn
    junction = mv.detect_junction(juncSensorLeft, juncSensorRight, robot)
    if junction[0] is True: #function updates current direction
        print("junction reached")
        turnDirection = junction[1]
        #Conditional to determine which wheel should be driven forwards to turn in the desired direction.
        if turnDirection == "Left":
            print("turn left")
            mv.turn(leftWheel, rightWheel, lineSensorLeft, lineSensorRight)
        elif turnDirection == "Right":
            print("turn right")
            mv.turn(rightWheel, leftWheel, lineSensorLeft, lineSensorRight)
    #line follower
    else:
        leftSpeed, rightSpeed = mv.line_follower(lineSensorLeft, lineSensorRight)
        leftWheel.fwd(leftSpeed)
        rightWheel.fwd(rightSpeed)
    
    #What to do when destination reached
    if robot.current_path[-1] in (3, 10, 15, 13):
        #Robot has reached pickup location
        if robot.current_path[robot.current_node + 1] == robot.current_path[-1]:
            
            destination = clt.collect_block() #Use colour detetction to determine new location and set new path.
            new_path = pf.set_path(robot.current_path[current_node], destination)
            robot.change_path(new_path)
            while juncSensorLeft.value() == 0 or junSensorRight.value() == 0: #Reverse out of pickup point until node reached.
                leftSpeed, rightSpeed = clt.reverse_out(lineSensorLeft, lineSensorRight)
                leftWheel.rvrs(leftSpeed)
                rightWheel.rvrs(rightSpeed)
    
    #Robot has returned to start
    elif robot.path[-1] == 0 and robot.current_path[robot.current_node] == robot.path[-1]:
        leftWheel.kill()
        rightWheel.kill()
        break
    
    #Robot is in a depot
    elif robot.current_path[robot.current_node] == robot.path[-1]:
        #robot = clt.drop_off(robot) #drop off box
        leftWheel.rvrs(100)
        rightWheel.rvrs(100)
        sleep(1)
        leftWheel.kill()
        rightWheel.kill()
        
        #Do a u-turn, depending on location turn in different direction to avoid hitting walls.
        if robot.current_path[robot.current_node] == 5:
            mv.uturn(leftWheel, rightWheel, lineSensorLeft, lineSensorRight)
        elif robot.current_path[robot.current_node] == 19:
            mv.uturn(rightWheel, leftWheel, lineSensorLeft, lineSensorRight)
        
        

