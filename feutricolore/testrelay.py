import wiringpi
import time

RELAY_J5 = 37
RELAY_J4 = 31
RELAY_J3 = 15
RELAY_J2 = 7

wiringpi.wiringPiSetupPhys()
wiringpi.pinMode(RELAY_J5,1)
wiringpi.pinMode(RELAY_J4,1)
wiringpi.pinMode(RELAY_J3,1)
wiringpi.pinMode(RELAY_J2,1)

wiringpi.digitalWrite(RELAY_J5,0)
wiringpi.digitalWrite(RELAY_J4,0)
wiringpi.digitalWrite(RELAY_J3,0)
wiringpi.digitalWrite(RELAY_J2,0)

while True:
    print("ON")
    wiringpi.digitalWrite(RELAY_J5,1)
    time.sleep(1)
    print("OFF")
    wiringpi.digitalWrite(RELAY_J5,0)
    time.sleep(1)

