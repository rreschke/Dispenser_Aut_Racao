from led import Led
from botao import Botao
#from servo import Servo
#from sensor_us import SensorUltrassom
from time import sleep
from machine import Pin

#Ref Interrupcao: https://www.youtube.com/watch?v=Qw2xr5a2rSA
class Program:
    #Botoes
    _botao1Porcao = Botao(11)
    _botao2Porcao = Botao(12)
    _botao3Porcao = Botao(13)
    _botaoGirar = Botao(14)
    _botaoParar = Botao(15)
    
    #LEDs
    _led1Porcao = Led(27)
    _led2Porcao = Led(26)
    _led3Porcao = Led(22)
    _ledGirar = Led(21)
    _ledParar = Led(20)
    _ledPoucaRacao = Led(10)
    
    #Implementar sensor
    
    #Implementar servo
    
    
    @staticmethod
    def iniciar():
        Program._led1Porcao.desligar()
        Program._led2Porcao.desligar()
        Program._led3Porcao.desligar()
        Program._ledGirar.desligar()
        Program._ledParar.desligar()
        Program._ledPoucaRacao.desligar()
    
    @staticmethod
    def despejar1Porcao(pin):
        Program._botao1Porcao.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._led1Porcao.ligar()
        #Implementar rotação do motor
        print(f"girando motor p/ 1 porcao")   #
        sleep(2)                              # ELIMINAR
        print(f"parando de girar o motor")    #
        Program._led1Porcao.desligar()
        #Implementar leitura da quantidade de ração
        Program._botao1Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar1Porcao)
        
    @staticmethod
    def despejar2Porcao(pin):
        Program._botao2Porcao.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._led2Porcao.ligar()
        #Implementar rotação do motor
        print(f"girando motor p/ 2 porcoes")  #
        sleep(2)                              # ELIMINAR
        print(f"parando de girar o motor")    #
        Program._led2Porcao.desligar()
        #Implementar leitura da quantidade de ração
        Program._botao2Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar2Porcao)
        
    @staticmethod
    def despejar3Porcao(pin):
        Program._botao3Porcao.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._led3Porcao.ligar()
        #Implementar rotação do motor
        print(f"girando motor p/ 3 porcoes")  #
        sleep(2)                              # ELIMINAR
        print(f"parando de girar o motor")    #
        Program._led3Porcao.desligar()
        #Implementar leitura da quantidade de ração
        Program._botao3Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar3Porcao)
    
    @staticmethod
    def despejarIndefinido(pin):
        Program._botaoGirar.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._ledGirar.ligar()
        #Implementar rotação do motor
        print(f"girando motor ate pedir p/ parar")   # ELIMINAR
        sleep(2)
        Program._botaoGirar.configurarInterrupcao(Pin.IRQ_RISING, Program.despejarIndefinido)
    
    @staticmethod    
    def pararDespejo(pin):
        Program._botaoParar.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._ledParar.ligar()
        #Implementar PARADA de rotação do motor
        sleep(1)
        print(f"parando de girar o motor")
        Program._ledGirar.desligar()
        Program._ledParar.desligar()
        #Implementar leitura da quantidade de ração
        Program._botaoParar.configurarInterrupcao(Pin.IRQ_RISING, Program.pararDespejo)
    
    @staticmethod
    def run():
        Program.iniciar()
        Program._botao1Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar1Porcao)
        Program._botao2Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar2Porcao)
        Program._botao3Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar3Porcao)
        Program._botaoGirar.configurarInterrupcao(Pin.IRQ_RISING, Program.despejarIndefinido)
        Program._botaoParar.configurarInterrupcao(Pin.IRQ_RISING, Program.pararDespejo)

