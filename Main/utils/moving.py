import pathfinding as pf
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
        robot.current_node +=1
        #update current and turn direction
        robot.current_direction, turning  = pf.turn_direction(robot)

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
    
    t = 0
    while t < 1:
        if leftLineFollower.value() == 0:
            rightWheel.fwd(50)
        else:
            rightWheel.fwd(100)
            
        if rightLineFollower.value() == 0:
            leftWheel.fwd(50)
        else:
            leftWheel.fwd(100)
        t += 0.05
        sleep(0.05)
        
    return
        




