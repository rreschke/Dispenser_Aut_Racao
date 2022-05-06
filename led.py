from machine import Pin

class Led:
    #Construtor da class
    def __init__(self, pino):
        self._pino = Pin(pino, Pin.OUT)
        self._estado = 1 # 1 = DESLIGADO; 0 = LIGADO 
        self._atualiza_estado()
        
    def _atualiza_estado(self):
        self._pino.value(self._estado)
        
    def ligar(self):
        self._estado = 0
        self._atualiza_estado()
        
    def desligar(self):
        self._estado = 1
        self._atualiza_estado()
        
    def inverterEstado(self):
        if estaLigado():
            desligar()
        else:
            ligar()
            
    def estaLigado(self):
        return self._estado == 0