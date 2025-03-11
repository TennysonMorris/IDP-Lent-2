from machine import Pin, PWM, I2C
from settings import Robot
from time import sleep
from lib.motor import Motor
import lib.moving as mv
import lib.pathfinding as pf
import lib.collection as clt
from lib.tcs34725 import TCS34725
from lib.vl53l0x import VL53L0X

#Set pins for each wheel
leftWheel = Motor(5,4)
rightWheel = Motor(6,7)

#Set pins for LED and line sensor (adjustable).
lineSensorRight = Pin(17, Pin.IN, Pin.PULL_UP)
lineSensorLeft = Pin(16, Pin.IN, Pin.PULL_UP)
juncSensorRight = Pin(19, Pin.IN, Pin.PULL_UP)
juncSensorLeft = Pin(20, Pin.IN, Pin.PULL_UP)
led = Pin(0, Pin.OUT)
colour_sensor = TCS34725(I2C(1, sda = Pin(14), scl = Pin(15)))
tof = VL53L0X(I2C(id = 1, sda = Pin(10), scl = Pin(11)))

# Set up PWM Pin for servo control
servo_pin = machine.Pin(15)
servo = PWM(servo_pin)

destination = collect_block(colour_sensor, servo)
while juncSensorLeft.value() == 0 or junSensorRight.value() == 0: #Reverse out of pickup point until node reached.
                leftSpeed, rightSpeed = clt.reverse_out(lineSensorLeft, lineSensorRight)
                leftWheel.rvrs(leftSpeed)
                rightWheel.rvrs(rightSpeed)

