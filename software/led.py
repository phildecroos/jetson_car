# Test program to test simple GPIO usage on the Jetson Nano

import RPi.GPIO as GPIO
import time

LED_PIN = 24

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

running = True

while(running):
    x = input("command >>>")
    
    if x == 'f':
        print("flash")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
    elif x == 's':
        print("stop")
        running = False
        GPIO.cleanup()
    else:
        print("bad input, please input f or s")
