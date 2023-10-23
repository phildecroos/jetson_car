# lights control code

import RPi.GPIO as GPIO

DRIVING = 7

def lights(lights_q):
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(DRIVING, GPIO.OUT, initial=GPIO.LOW)

        while True:
            data = lights_q.get()
            if data == 1:
                GPIO.output(DRIVING, GPIO.HIGH)
            elif data == 0:
                GPIO.output(DRIVING, GPIO.LOW)
    finally:
        GPIO.output(DRIVING, GPIO.LOW)
        GPIO.cleanup()