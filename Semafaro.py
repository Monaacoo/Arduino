from pyfirmata2 import Arduino, OUTPUT

PORTA = Arduino.AUTODETECT
arduino = Arduino(PORTA)

vermelho_car = arduino.get_pin('d:13:o')
amarelo_car = arduino.get_pin('d:12:o')
verde_car = arduino.get_pin('d:11:o')
vermedlho_ped = arduino.get_pin('d:10:o')
verde_ped = arduino.get_pin('d:9:0')

while True:
    vermelho_car.write(1)
    verde_ped.write(1)
    arduino.pass_time(5.0)
    vermelho_car.write(0)
    verde_car.write(1)
    verde_ped.write(0)
    vermelho_ped.write(1)
    arduino.pass_time(3.0)
    verde_car.write(0)
    amarelo_car.write(1)
    arduino.pass_time(1.0)
    amarelo_car.write(0)
    vermelho_ped.write(0)
