import pathfinding as pf

def line_follower():
    #Veer controlled by slowing down the wheel on the outside of the veer.
    if leftLineFollower.value() == 1:
        rightWheel.fwd(50)
    if rightLineFollower.value() == 1:
        leftWheel.fwd(50)

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
    #disable line follower

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


    