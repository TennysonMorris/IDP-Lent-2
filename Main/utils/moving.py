import pathfinding as pf

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

def detect_junction(leftJuncDetector, rightJuncDetector):
    #if junction detected
    if leftJuncDetector.value() == 1 or rightJuncDetector.value() == 1:
        
        global current_direction, current_path, current_node
        #update current node
        current_node +=1
        #update current and turn direction
        current_direction, turning  = pf.turn_direction(current_direction, current_path, current_node)

        #execute turn 
        return True, turning
        
    return False, "Straight"

def turn(insideWheel, outsideWheel, leftLineFollower, rightLineFollower):

    #turn off original line
    while leftLineFollower.value() == 1 and rightLineFollower.value() == 1:
        outsideWheel.fwd(50)
        insideWheel.rvrs(50)
    #turn until new line reached
    while leftLineFollower.value() == 0 or rightLineFollower.value() == 0:
        outsideWheel.fwd(50)
        insideWheel.rvrs(50)
            
    return


