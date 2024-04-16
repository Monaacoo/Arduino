from pyfirmata2 import Arduino, PWM, util
import random

arduino = Arduino('COM6')

it = util.Iterator(arduino)
it.start()
pot = arduino.get_pin('a:0:i')
led_verde = arduino.get_pin('d:5:p')
led_vermelho = arduino.get_pin('d:6:p')
pot.enable_reporting()
valor_vermelho = 255
valor_verde = 0
valor = 0

while True:
    texto = str(pot.read())
    print (valor)
    valor = float(pot.read())
    valor_vermelho = 1 - valor
    valor_verde = valor
    print(str(valor_vermelho) + " vermelho " + str(valor_verde) + " verde ")
    led_verde.write(valor_verde)
    led_vermelho.write(valor_vermelho)
    arduino.pass_time(0.05)

