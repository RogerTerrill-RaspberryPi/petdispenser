from nanpy import (ArduinoApi, SerialManager, Lcd)
from time import sleep
import datetime

lcd = Lcd([8, 9, 4, 5, 6, 7], [16, 2])
status = 't'
while status == 't':
    lcd.clear()
    lcd.printString(datetime.datetime.now())
    
    status = input("What status do you want: ")
lcd.clear()
lcd.printString('Dead!!!')

ledPin = 13
ledState = True

try:
    connection = SerialManager()
    a = ArduinoApi(connection = connection)
except:
    print("Failed to connect to Arduino")

a.pinMode(ledPin, a.OUTPUT)

try:
    while True:
        if ledState:
            a.digitalWrite(ledPin, a.LOW)
            ledState = False
            lcd.clear()
            print("LED OFF")
            sleep(1)
        else:
            a.digitalWrite(ledPin, a.HIGH)
            ledState = True
            print("LED ON")
            sleep(1)
except:
    a.digitalWrite(ledPin, a.LOW)



