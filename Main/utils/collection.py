from pathfinding import set_path
from time import sleep
from vl53l0x import VL53L0X
from machine import Pin, PWM, I2C


def activate_servo(servo, movement):
    # Set Duty Cycle for Different Angles
    max_duty = 7864
    lifted = int(5*max_duty/8)
    default = int(max_duty/2)
    #Set PWM frequency
    frequency = 50
    servo.freq(frequency)
    #lift or drop based on argument
    if movement == "lift":
        servo.duty_u16(lifted)
    elif movement == "drop":
        servo.duty_u16(default)
        

def detect_colour(colour_sensor): #detect color update path
    #read rgb
    colour_info = colour_sensor.read('rgb')
    #return depot number
    if colour_info[0] > 1 and colour_info[2] < 5:
        return 5
    else:
        return 19

def collect_block(colour_sensor, servo, leftWheel, rightWheel):#collect block, update destination and path, reverse out 
    #initialize tof
    tof = VL53L0X(I2C(1, sda = Pin(14), scl = Pin(11)))
    while True:
        #measuer distance
        dist = tof.ping() - 25
        if dist > 50:
            leftWheel.fwd(100)
            rightWheel.fwd(100)
        #when near the box
        elif dist < 50:
            leftWheel.kill() #stop wheels
            rightWheel.kill()
            activate_servo(servo, "lift") #lift box
            break
        prev_dist = dist
        sleep(0.1)
    
    #detect colour and return new destination
    destination = detect_colour(colour_sensor)
    return destination

        
        
def drop_off(robot, servo):
    activate_servo(servo, "drop") #drop off box
    #set path for new box
    robot.next_box()
    if robot.box_no < 4:
        destination = robot.pickups[robot.box_no]
    else:
        destination = 0
    
    robot.change_path(set_path(robot.current_path[robot.current_node], destination))
    
    return robot

