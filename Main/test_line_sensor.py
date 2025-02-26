from machine import Pin, PWM
from time import sleep

#Set pins for LED and line sensor (adjustable).
led = Pin(12, Pin.OUT)
lineSensor = Pin(10, Pin.IN, Pin.PULL_UP)
lineSensor2 = Pin(11, Pin.IN, Pin.PULL_UP)

#Loop to match line sensor and led value to test operational distance.
while True:
    led.value(1)
    sleep(1)
    led.value(0)


