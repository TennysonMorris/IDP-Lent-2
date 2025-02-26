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

def detect_junction():
    #if junction detected
    if leftJuncDetector.value() == 1 or rightJuncDetector.value() == 1:

        #update current node
        current_node +=1
        #update current and turn direction
        current_direction, turning  = pf.turn_direction(current_direction, current_path, current_node)

        #execute turn 
        if turning != "Straight":
            turn(turning)

def turn(direction):
    ## todo

    if direction == "Left":
        #turn off original line
        while leftLineFollower.value() == 0 and rightLineFollower.value() == 0:
            rightWheel.fwd(50)
            leftWheel.rvrs(50)
        #turn until new line reached
        while leftLineFollower.value() == 1 and rightLineFollower.value() == 1:
            rightWheel.fwd(50)
            leftWheel.rvrs(50)

    if direction == "right":
        #turn off original line
        while leftLineFollower.value() == 0 and rightLineFollower.value() == 0:
            rightWheel.rvrs(50)
            leftWheel.fwd(50)
        #turn until new line reached
        while leftLineFollower.value() == 1 and rightLineFollower.value() == 1:
            rightWheel.rvrs(50)
            leftWheel.fwd(50)

        #reactivate line follower


