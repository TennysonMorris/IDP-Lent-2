# Pin 0  PWM Motor 1               Ground---[]              []-------------------------------
# Pin 1  DIR Motor 1               Ground---[]              []------                     ----3V3
#                                  Ground---[]              []------                     ----Ground
# Pin 2  PWM Motor 2               Ground---[]              []-------------------------------
# Pin 3  DIR Motor 2               Ground---[]              []-------------------------------
# Pin 4  DIR Motor 3 or Servo 1    Ground---[]              []-------------------------------
# Pin 5  PWM Motor 3               Ground---[]              []-------------------------------
#                                  Ground...[]              []-------------------------------
# Pin 6  PWM Motor 4 or Servo 2    Ground---[]              []-------------------------------
# Pin 7  DIR Motor 4               Ground---[]              []-------------------------------
# Pin 8  GPIO...............................[]              []-------------------------------
# Pin 9  GPIO...............................[]              []-------------------------------
#                                  Ground                   []-------------------------------Ground
# Pin 10 GPIO...............................[]              []-------------------------------
# Pin 11 GPIO...............................[]              []-------------------------------Pin 20 GPIO
# Pin 12 GPIO...............................[]              []-------------------------------Pin 19 GPIO
# Pin 13 GPIO............... ..       ......[]              []-------------------------------Pin 18 GPIO
# Ground....................................[]              []-------------------------------Ground
# Pin 14 GPIO...............................[]              []-------------------------------Pin 17 GPIO
# Pin 15 GPIO...............................[]              []-------------------------------Pin 16 GPIO
from machine import Pin, PWM
from time import sleep

#Set pins for LED and line sensor (adjustable).
led = Pin(14, Pin.OUT)
lineSensor = Pin(12, Pin.IN, Pin.PULL_UP)

#Loop to match line sensor and led value to test operational distance.
while True:
    led.value(lineSensor(Value))


