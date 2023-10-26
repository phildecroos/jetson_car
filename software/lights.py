# lights control code

import RPi.GPIO as GPIO

DRIVING = 7

def lights(stop_q, lights_q):
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DRIVING, GPIO.OUT, initial=GPIO.LOW)

    while not stop_q.qsize():
        data = lights_q.get()
        if data == 1:
            GPIO.output(DRIVING, GPIO.HIGH)
        elif data == 0:
            GPIO.output(DRIVING, GPIO.LOW)