from pyfirmata import Arduino, INPUT, OUTPUT, util

PORTA = Arduino.AUTODETECT
arduino = Arduino(PORTA)
led1 = arduino.get_pin('d:11:o')
led2 = arduino.get_pin('d:12:o')
led3 = arduino.get_pin('d:13:o')
botao = arduino.get_pin('d:2:i')
anterior = False
num = 0
digito = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],
          [1,0,0],[1,0,1],[1,1,0],[1,1,1]]
it = util.Iterator(arduino)

it.start()

while True:
    valor = botao.read()
    if valor == True and anterior == False:
        num = num+1
        if num > 7:
            num = 0
        print('Decimal:',num,'Binario:',
              str('{0:b}'.format(num).zfill(3))
    led1.write(digito[num] [0])
    led1.write(digito[num] [1])
    led1.write(digito[num] [2])
    anterior = valor
    arduino.pass_time(0.05)
