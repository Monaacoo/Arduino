import http.client
from pyfirmata2 import Arduino, INPUT, OUTPUT, util

CHAVE = 'C8UISOEBALZ98PP0'
SERVIDOR = 'api.thingspeak.com'

PORTA = "COM4"
arduino = Arduino(PORTA)

it = util.Iterator(arduino)
it.start()
pot = arduino.get_pin('a:0:i')
led = arduino.get_pin('d:9:p')
pot.enable_reporting()
#estado = True

while True:
    valor = str(pot.read())
    print(valor)
    if valor != 'None':
        valor = float(valor)
        led.write(valor)
    #estado = not estado
    
    url = '/update?api_key=' + CHAVE + '&field1=' + str(valor)
    print(url)
    con = http.client.HTTPSConnection(SERVIDOR)
    con.request('GET', url)
    resp = con.getresponse()
    print(resp.status, resp.reason)
    arduino.pass_time(2)
