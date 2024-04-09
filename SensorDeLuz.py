import pyfirmata2 import Aarduino, util
import random

PORTA = Arduino.AUTODETEC
arduino = Arduino(PORTA)

it = util.Iterator(arduino)
it.start()
ldr = arduino.get_pin('a:0:i')
led = arduino.get_pin('d:11:p')
ldr.enable_reporting()

arduino.analog[0].enable_reporting()

while True:
    valor = str(ldr.read())
    print(valor)
    if valor != 'None':
        valor = float(valor)
        led.write(1-valor)
    arduino.pass_time(0.1)
