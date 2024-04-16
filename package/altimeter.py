from mpl3115a2 import MPL3115A2
from machine import I2C, Pin
from time import sleep


i2c = I2C(sda=Pin(21), scl=Pin(22))
mpl = MPL3115A2(i2c, mode=MPL3115A2.ALTITUDE)

while True:
        

    altitude = mpl.altitude()
    temperature = mpl.temperature()

    print(altitude,temperature)
    sleep(0.5)
