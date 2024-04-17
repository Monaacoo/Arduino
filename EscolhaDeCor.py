from pyfirmata2 import Arduino
import random
arduino = Arduino('COM6')
red = arduino.get_pin('d:11:p')
blue = arduino.get_pin('d:9:p')
green = arduino.get_pin('d:10:p')
def acender(cor, brilho):
    if cor == "red":
        red.write(brilho)
        blue.write(0)
        green.write(0)
    elif cor == "green":
        red.write(0)
        blue.write(0)
        green.write(brilho)
    elif cor == "blue":
        red.write(0)
        blue.write(brilho)
        green.write(0)
    elif cor == "apagar":
        red.write(0)
        blue.write(0)
        green.write(0)
    else: print("invalido")
while True:
    cor = input("Escolha uma cor (vermelho, verde, azul ou apagar): ")
    if cor == "apagar":
        acender(cor, 0)
    else:
        brilho = float(input("Digite a proporção de brilho (entre 0 e 1): "))
        acender(cor, brilho)
