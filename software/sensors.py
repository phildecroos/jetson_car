# sensor reading code

import time
import RPi.GPIO as GPIO

WHEELS = 12
BUMPER = 13

def sensors(drive_q, lights_q):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(WHEELS, GPIO.IN)
    GPIO.setup(BUMPER, GPIO.IN)
    wheels_latch = 0
    bumper_latch = 0
    drive_latch = 0

    while True:
        wheels_data = GPIO.input(WHEELS)
        bumper_data = GPIO.input(BUMPER)

        if bumper_data and not bumper_latch:
            bumper_latch = 1
            drive_latch = 0
            drive_q.put("STOP")
            lights_q.put(0)
        elif not bumper_data and bumper_latch:
            bumper_latch = 0
        elif not wheels_data and not wheels_latch:
            wheels_latch = 1
            drive_latch = 0
            drive_q.put("STOP")
            lights_q.put(0)
        elif wheels_data and wheels_latch:
            wheels_latch = 0
        
        if not bumper_data and wheels_data and not drive_latch:
            drive_latch = 1
            drive_q.put("START")
            lights_q.put(1)

        time.sleep(0.1)