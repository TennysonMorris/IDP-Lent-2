from machine import Pin, PWM, I2C
from settings import Robot
from time import sleep, time
from lib.motor import Motor
import lib.moving as mv
import lib.pathfinding as pf
import lib.collection as clt
from lib.tcs34725 import TCS34725
from vl53l0x import VL53L0X


#Set pins for each wheel
leftWheel = Motor(5,4)
rightWheel = Motor(6,7)

#Set pins for LED and line sensor (adjustable).
lineSensorRight = Pin(17, Pin.IN, Pin.PULL_UP)
lineSensorLeft = Pin(16, Pin.IN, Pin.PULL_UP)
juncSensorRight = Pin(20, Pin.IN, Pin.PULL_UP)
juncSensorLeft = Pin(19, Pin.IN, Pin.PULL_UP)
led = Pin(10, Pin.OUT)
# Set up PWM Pin for servo control
servo_pin = machine.Pin(13)
servo = machine.PWM(servo_pin)

#button, colour sensor and tof
colour_sensor = TCS34725(I2C(0, scl = Pin(9), sda = Pin(8), freq = 50000))
button = Pin(21, Pin.IN, Pin.PULL_UP)
#initialize initial node, path, direction
destination = 3
path = pf.set_path(-1, destination) #hard coded to first pickup
robot = Robot(path)
clt.activate_servo(servo,"drop")

led.value(0)
while button.value() == 0:
    continue

led.value(1)
while True:
    #Check whether it is necessary to turn
    junction = mv.detect_junction(juncSensorLeft, juncSensorRight, robot)
    if junction[0] is True: #function updates current direction
        turnDirection = junction[1]
        #Conditional to determine which wheel should be driven forwards to turn in the desired direction.
        if turnDirection == "Left":
            mv.turn(leftWheel, rightWheel, lineSensorLeft, lineSensorRight)
        elif turnDirection == "Right":
            mv.turn(rightWheel, leftWheel, lineSensorLeft, lineSensorRight)
        start = time()
        while time() - start < 0.5:
            leftSpeed, rightSpeed = mv.line_follower(lineSensorLeft, lineSensorRight)
            leftWheel.fwd(leftSpeed)
            rightWheel.fwd(rightSpeed)
    #line follower
    else:
        leftSpeed, rightSpeed = mv.line_follower(lineSensorLeft, lineSensorRight)
        leftWheel.fwd(leftSpeed)
        rightWheel.fwd(rightSpeed)
    
    #What to do when pickup location reached
    if robot.current_path[-1] in (3, 10, 15, 13):
        #Robot has reached pickup location
        if robot.current_path[robot.current_node + 1] == robot.current_path[-1]:
            
            destination = clt.collect_block(colour_sensor, servo, leftWheel, rightWheel) #Use colour detetction to determine new location and set new path.
            clt.activate_servo(servo, "Lift")
            new_path = pf.set_path(robot.current_path[robot.current_node], destination)
            robot.change_path(new_path)
            print(robot.current_direction, robot.current_path)
            while juncSensorLeft.value() == 0 or juncSensorRight.value() == 0: #Reverse out of pickup point until node reached.
                leftSpeed, rightSpeed = mv.reverse(lineSensorLeft, lineSensorRight)
                leftWheel.rvrs(leftSpeed)
                rightWheel.rvrs(rightSpeed)
    
    #Robot has returned to start
    elif robot.current_path[-1] == 0 and robot.current_path[robot.current_node] == robot.current_path[-1]:
        led.value(0)
        leftWheel.kill()
        rightWheel.kill()
        break
    
    #Robot is in a depot
    elif robot.current_path[robot.current_node] == robot.current_path[-1]:
        leftWheel.kill()
        rightWheel.kill()
        robot = clt.drop_off(robot, servo) #drop off box and set new path
        #reverse for 1 second
        leftWheel.rvrs(100)
        rightWheel.rvrs(100)
        sleep(1)
        #Do a u-turn, depending on location turn in different direction to avoid hitting walls.
        #update current direction to N
        if robot.current_path[robot.current_node] == 5:
            robot = mv.uturn(leftWheel, rightWheel, lineSensorLeft, lineSensorRight, robot)
        elif robot.current_path[robot.current_node] == 19:
            robot = mv.uturn(rightWheel, leftWheel, lineSensorLeft, lineSensorRight, robot)
        
        


