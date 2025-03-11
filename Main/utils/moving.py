import pathfinding as pf
import time
from time import sleep
import settings as foo

def line_follower(lineSensorLeft, lineSensorRight):
    #Veer controlled by slowing down the wheel on the outside of the veer.
    if lineSensorLeft.value() == 0:
        rightSpeed = 50
    else:
        rightSpeed = 100
        
    if lineSensorRight.value() == 0:
        leftSpeed = 50
    else:
        leftSpeed = 100
        
    return (leftSpeed, rightSpeed)

def detect_junction(leftJuncDetector, rightJuncDetector, robot):
    #if junction detected
    if leftJuncDetector.value() == 1 or rightJuncDetector.value() == 1:
        #update current node
        robot.next_node()
        #update current and turn direction
        new_direction, turning, robot  = pf.turn_direction(robot)
        robot.change_direction(new_direction)
        #execute turn 
        return True, turning, robot
        
    return False, "Straight", robot

def turn(insideWheel, outsideWheel, leftLineFollower, rightLineFollower):

    #turn off original line
    while leftLineFollower.value() == 1 and rightLineFollower.value() == 1:
        outsideWheel.fwd(50)
        insideWheel.rvrs(50)
    #turn until new line reached
    while leftLineFollower.value() == 0 or rightLineFollower.value() == 0:
        outsideWheel.fwd(50)
        insideWheel.rvrs(50)
    
    start = time.time()
    print("straight")
    while time.time() - start < 1:
        if leftLineFollower.value() == 0:
            insideWheel.fwd(50)
        else:
            insideWheel.fwd(100)
            
        if rightLineFollower.value() == 0:
            outsideWheel.fwd(50)
        else:
            outsideWheel.fwd(100)
        
    return
        

def uturn(insideWheel, outsideWheel, leftLineFollower, rightLineFollower):

    #turn off original line
    while leftLineFollower.value() == 1 and rightLineFollower.value() == 1:
        outsideWheel.fwd(50)
        insideWheel.rvrs(50)
    #turn until new line reached
    while leftLineFollower.value() == 0 or rightLineFollower.value() == 0:
        outsideWheel.fwd(50)
        insideWheel.rvrs(50)


