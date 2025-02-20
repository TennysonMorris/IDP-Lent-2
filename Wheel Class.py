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

class Motor:
    
    __init__(self, pwrPin, dirPin):
        self.pwm = PWM(Pin(pwrPin))
        self.dir = Pin(dirPin, Pin.OUT)
        self.pwm.freq(1000) # Set max frequency
        self.pwm.duty_u16(0) # Set motor's duty cycle
        
    # Turn off the motor
    def kill(self):
        self.pwm.duty_u16(0) 
        
    # Drive the motor forwards
    def fwd(self):
        self.dir.value(0)
        self.pwm.duty_u16(65535 * 70/100) # Motor speed given as x/100, here x = 70
        
    # Drive the motor in reverse
    def rvrs(self):
        self.dir.value(1)
        self.pwm.duty_u16(65535 * 30/100)
        
leftWheel = Motor(0,1)
rightWheel = Motor(2,3)
        