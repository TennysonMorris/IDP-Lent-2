from machine import Pin, PWM

class Motor:
    def __init__(self, pwrPin, dirPin):
        self.m1Dir = Pin(dirPin , Pin.OUT)
        self.pwm1 = PWM(Pin(pwrPin))
        self.pwm1.freq(1000)
        self.pwm1.duty_u16(0)
        
    def kill(self):
        self.pwm1.duty_u16(0)
        
    def fwd(self,speed):
        self.m1Dir.value(0)
        self.pwm1.duty_u16(int(65535*speed/100))
        
    def rvrs(self,speed):
        self.m1Dir.value(1)
        self.pwm1.duty_u16(int(65535*speed/100))
        

