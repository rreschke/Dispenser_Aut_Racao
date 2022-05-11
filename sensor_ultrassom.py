from machine import Pin
import utime

class SensorUltrassom:
    #Construtor da class
    def __init__(self, trigPin: int, echoPin: int):
        self._trigPin = Pin(trigPin, Pin.OUT)
        self._echoPin = Pin(echoPin, Pin.IN)

        self._trigPin.low()
    
    def medirDistancia(self):
        self._trigPin.low()
        utime.sleep_us(2)

        self._trigPin.high()
        utime.sleep_us(5)
        self._trigPin.low()

        while self._echoPin.value() == 0:
            signaloff = utime.ticks_us()
            
        while self._echoPin.value() == 1:
            signalon = utime.ticks_us()
       
        timepassed = signalon - signaloff

        distance = (timepassed * 0.0343) / 2
        
        return distance