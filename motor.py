from time import sleep
from machine import Pin, PWM

class Motor:
    def __init__(self, pino):
        self._pino = Pin(pino, Pin.OUT)
        self._pwm = PWM(self._pino)
        self._pwm.freq(50)
        self._pwm.duty_u16(0)
        
    def girar180(self):
        for pos in range(1000, 5000, 50):
            self._pwm.duty_u16(pos)
            sleep(0.01)
    
    def girar(self):
        self._pwm.duty_u16(4000)
            
    def parar(self):
        self._pwm.duty_u16(0)
