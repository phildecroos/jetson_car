import RPi.GPIO as GPIO


def leds(pinout, status_q, stop_q, leds_q):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinout["RUNNING_LED"], GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pinout["FAULT_LED"], GPIO.OUT, initial=GPIO.LOW)

    while not stop_q.qsize():
        data = leds_q.get()
        if data == "RUNNING":
            GPIO.output(pinout["RUNNING_LED"], GPIO.HIGH)
        elif data == "STOPPED":
            GPIO.output(pinout["RUNNING_LED"], GPIO.LOW)
        elif data == "FAULT":
            GPIO.output(pinout["FAULT_LED"], GPIO.HIGH)
        elif data == "FAULT_FIXED":
            GPIO.output(pinout["FAULT_LED"], GPIO.LOW)
