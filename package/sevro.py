from machine import Pin, PWM
from time import sleep
servo = PWM(Pin(25), freq=50) 
while True:
    servo.duty(20)
    sleep(2)
    servo.duty(80)
    sleep(2)