from machine import Pin

class Botao:
    #Construtor da classe
    def __init__(self, pino):
        self._pino = Pin(pino, Pin.IN, Pin.PULL_DOWN)
        self._pino.value(0)
        
    def estaPressionado(self):
        return self._pino.value() == 1
    
    def configurarInterrupcao(self, trigger, handler):
        self._pino.irq(trigger = trigger, handler = handler)