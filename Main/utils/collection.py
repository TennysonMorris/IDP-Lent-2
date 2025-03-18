from pathfinding import set_path
from time import sleep

def activate_servo(servo, movement):
    # Set Duty Cycle for Different Angles
    max_duty = 7864
    lifted = int(5*max_duty/8)
    default = int(max_duty/2)
    #Set PWM frequency
    frequency = 50
    servo.freq(frequency)
    if movement == "lift":
        servo.duty_u16(lifted)
    elif movement == "drop":
        servo.duty_u16(default)
        

def detect_colour(colour_sensor): #detect color update path
    colour_info = colour_sensor.read('rgb')
    if colour_info[0] > 7:
        return 5
    elif colour_info[1] > 7:
        return 19
    elif colour_info[2] > 7:
        return 19
    else:
        return 5

def collect_block(colour_sensor, servo, tof, leftWheel, rightWheel):#collect block, update destination and path, reverse out 
    tof.ping()
    while True:
        dist = tof.ping() - 25
        print(dist)
        if dist > 50:
            leftWheel.fwd(100)
            rightWheel.fwd(100)
        elif dist < 50:
            leftWheel.kill()
            rightWheel.kill()
            destination = detect_colour(colour_sensor)
            activate_servo(servo, "lift")
            break
        prev_dist = dist
        sleep(0.1)
    
    return destination

        
        
def drop_off(robot, servo):
    activate_servo(servo, "drop")
    #use tof to reverse and drop off
    robot.next_box()
    if robot.box_no < 4:
        destination = robot.pickups[robot.box_no]
    else:
        destination = 0
    
    robot.change_path(set_path(robot.current_path[robot.current_node], destination))
    
    return robot

