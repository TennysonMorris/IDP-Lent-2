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
    
    
    return
