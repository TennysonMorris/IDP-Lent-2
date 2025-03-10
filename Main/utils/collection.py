from pathfinding import set_path

def detect_colour(): #detect color update path
    colourDetector.value()
     = 
    return destination

def collect_block(): #collect block, update destination and path, reverse out 
    while True:
        dist = tof.ping() - 25
        delta_dist = dist - prev_dist
        if delta_dist < 5 and dist > 50:
            leftWheel.fwd(50)
            rightWheel.fwd(50)
        elif dist < 50:
            destination = detect_colour()
            activate_servo()
            break
        prev_dist = dist
        sleep(0.1)
    
    return destination

def reverse_out(lineSensorLeft, lineSensorRight)
    
    #Veer controlled by slowing down the wheel on the outside of the veer.
    if lineSensorLeft.value() == 0:
        rightSpeed = 50
    else:
        rightSpeed = 100
        
    if lineSensorRight.value() == 0:
        leftSpeed = 50
    else:
        leftSpeed = 100
        
        
def drop_off(robot):
    #use tof to reverse and drop off
    while :
        reverse_out

    robot.next_box()
    if robot.box_no < 4:
        destination = robot.pickups[robot.box_no]
    else:
        destination = 0
    
    robot.change_path() = set_path[current_node][destination]
    
    return robot
