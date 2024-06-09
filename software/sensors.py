import time

import RPi.GPIO as GPIO


def sensors(pinout, status_q, stop_q, map_q, motors_q, leds_q):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinout["FLOOR_SENSOR"], GPIO.IN)
    GPIO.setup(pinout["BUMPER_SENSOR"], GPIO.IN)
    wheels_latch = 0
    bumper_latch = 0
    drive_latch = 0

    while not stop_q.qsize():
        # TODO - process inputs from motor encoders into apprx distance moved and send data to map_q
        wheels_data = GPIO.input(pinout["FLOOR_SENSOR"])
        bumper_data = GPIO.input(pinout["BUMPER_SENSOR"])

        if bumper_data and not bumper_latch:
            bumper_latch = 1
            drive_latch = 0
            motors_q.put("STOP")
            leds_q.put(0)
        elif not bumper_data and bumper_latch:
            bumper_latch = 0
        elif not wheels_data and not wheels_latch:
            wheels_latch = 1
            drive_latch = 0
            motors_q.put("STOP")
            leds_q.put(0)
        elif wheels_data and wheels_latch:
            wheels_latch = 0

        if not bumper_data and wheels_data and not drive_latch:
            drive_latch = 1
            motors_q.put("START")
            leds_q.put(1)

        time.sleep(0.1)
