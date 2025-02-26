import pathfinding as pf

def line_follower():
    #Veer controlled by slowing down the wheel on the outside of the veer.
    if leftLineFollower.value() == 1:
        rightWheel.fwd(50)
    if rightLineFollower.value() == 1:
        leftWheel.fwd(50)

def update_junction(current_direction, current_path, current_node):
    #update current node 
    current_node = map[current_node][current_direction]
    return current_node

def detect_junction():
    #if junction detected
    if leftJuncDetector.value() == 1 or rightJuncDetector.value() == 1:

        #update current node
        current_node = update_junction(current_direction, current_path, current_node)
        #update turn direction
        turning  = pf.turn_direction(current_direction, current_path, current_node)

        #execute turn 
        if turning != "Straight":
            turn(turning)

def turn(direction):
    ## todo


    