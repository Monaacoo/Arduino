from pyfirmata2 import Arduino, OUTPUT, util
import random

PORTA = Arduino.AUTODETECT
arduino = Arduino(PORTA)

it = util.Iterator(arduino)
it.start()
arduino.analog[0].enable_reporting()
arduino.digital[9].mode = OUTPUT
estado = True

while True:
    valor = str(arduino.analog[0].read())
    print (valor)
    if valor != 'None':
        arduino.digital[9].write(estado)
        valor = float(valor)
    estado = not estado
    arduino.pass_time(valor)
