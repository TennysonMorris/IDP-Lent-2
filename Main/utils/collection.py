from pathfinding import set_path
from machine import Pin, PWM

def activate_servo(servo, movement):
    # Set up PWM Pin for servo control
    servo_pin = machine.Pin(15)
    servo = machine.PWM(servo_pin)
    # Set Duty Cycle for Different Angles
    max_duty = 7864
    lifted = int(5*max_duty/8)
    default = int(max_duty/2)
    #Set PWM frequency
    frequency = 50
    servo.freq (frequency)
    if movement = "lift":
        servo.duty_u16(lifted)
    elif movement = "drop":
        servo.duty_u16(default)
        
    sleep(2)

def detect_colour(colour_sensor): #detect color update path
    colour_info = colour_sensor.value()
    if colour_info[0] > threshold:
        return 5
    elif colour_info[1] > threshold:
        return 19
    elif colour_info[2] > threshold:
        return 19
    else:
        return 5

def collect_block(colour_sensor, servo): #collect block, update destination and path, reverse out 
    while True:
        dist = tof.ping() - 25
        delta_dist = dist - prev_dist
        if delta_dist < 5 and dist > 50:
            leftWheel.fwd(50)
            rightWheel.fwd(50)
        elif dist < 50:
            destination = detect_colour(colour_sensor)
            activate_servo(servo, "lift")
            break
        prev_dist = dist
        sleep(0.1)
    
    return destination

def reverse_out(lineSensorLeft, lineSensorRight):
    
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
    activate_servo(servo, "drop")
    #use tof to reverse and drop off
    robot.next_box()
    if robot.box_no < 4:
        destination = robot.pickups[robot.box_no]
    else:
        destination = 0
    
    robot.change_path(set_path[current_node][destination])
    
    return robot
