from led import Led
from botao import Botao
from motor import Motor
from sensor_ultrassom import SensorUltrassom
from time import sleep
from machine import Pin
import utime

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
    _sensorUltrassom = SensorUltrassom(19, 18)

    #Implementar servo
    _motor = Motor(4)
    
    @staticmethod
    def debounce():
        utime.sleep_us(200)
        
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
        Program.disableAllIrq()
        Program.debounce()
        print("Entrou aqui")
        if Program._botao1Porcao.estaPressionado() == True:
            Program._led1Porcao.ligar()
            #Implementar rotação do motor
            print(f"girando motor p/ 1 porcao")
            Program._motor.girar90()                          
            print(f"parando de girar o motor")
            Program._led1Porcao.desligar()
            #Implementar leitura da quantidade de ração
            Program.medirQuantidadeRacao()
        Program.enableAllIrq()
        
    @staticmethod
    def despejar2Porcao(pin):
        Program.disableAllIrq()
        Program.debounce()
        if Program._botao2Porcao.estaPressionado() == True:
            Program._led2Porcao.ligar()
            #Implementar rotação do motor
            print(f"girando motor p/ 2 porcoes")  #
            Program._motor.girar90()
            Program._motor.girar90()
            print(f"parando de girar o motor")    #
            Program._led2Porcao.desligar()
            #Implementar leitura da quantidade de ração
            Program.medirQuantidadeRacao()
        Program.enableAllIrq()
        
    @staticmethod
    def despejar3Porcao(pin):
        Program.disableAllIrq()
        Program.debounce()
        if Program._botao3Porcao.estaPressionado() == True:
            Program._led3Porcao.ligar()
            #Implementar rotação do motor
            print(f"girando motor p/ 3 porcoes")  #
            Program._motor.girar90()
            Program._motor.girar90()
            Program._motor.girar90()  
            print(f"parando de girar o motor")    #
            Program._led3Porcao.desligar()
            #Implementar leitura da quantidade de ração
            Program.medirQuantidadeRacao()
        Program.enableAllIrq()
    
    @staticmethod
    def despejarIndefinido(pin):
        Program.disableAllIrq()
        Program.debounce()
        if Program._botaoGirar.estaPressionado() == True:
            Program.enableStopIrq()
            Program._ledGirar.ligar()
            Program._motor.girar() 
            print(f"girando motor ate pedir p/ parar")
    
    @staticmethod    
    def pararDespejo(pin):
        Program.disableAllIrq()
        Program.debounce()
        if Program._botaoParar.estaPressionado() == True:
            Program._ledParar.ligar()
            Program._motor.parar() 
            print(f"parando de girar o motor")
            Program._ledGirar.desligar()
            sleep(2)
            Program._ledParar.desligar()
            Program.medirQuantidadeRacao()
        Program.enableAllIrq()
    
    @staticmethod
    def run():
        Program.iniciar()
        Program._botao1Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar1Porcao)
        Program._botao2Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar2Porcao)
        Program._botao3Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar3Porcao)
        Program._botaoGirar.configurarInterrupcao(Pin.IRQ_RISING, Program.despejarIndefinido)

    @staticmethod
    def disableAllIrq():
        Program._botao1Porcao.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._botao2Porcao.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._botao3Porcao.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._botaoGirar.configurarInterrupcao(Pin.IRQ_RISING, None)
        Program._botaoParar.configurarInterrupcao(Pin.IRQ_RISING, None)

    @staticmethod
    def enableAllIrq():
        Program._botao1Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar1Porcao)
        Program._botao2Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar2Porcao)
        Program._botao3Porcao.configurarInterrupcao(Pin.IRQ_RISING, Program.despejar3Porcao)
        Program._botaoGirar.configurarInterrupcao(Pin.IRQ_RISING, Program.despejarIndefinido)
    

    @staticmethod
    def medirQuantidadeRacao():
        distanciaRacao = Program._sensorUltrassom.medirDistancia()
        print("distancia: ", distanciaRacao)
        if (distanciaRacao > 20):
            Program._ledPoucaRacao.ligar()
        else:
            Program._ledPoucaRacao.desligar()

    @staticmethod
    def enableStopIrq():
        Program._botaoParar.configurarInterrupcao(Pin.IRQ_RISING, Program.pararDespejo)