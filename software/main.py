import json
import subprocess
import time
from queue import Queue
from threading import Thread

import RPi.GPIO as GPIO
from cv import cv
from leds import leds
from motors import motors
from path import path
from sensors import sensors


def main():
    print("initializing")

    set_pwm = subprocess.Popen("software/pwm.sh")
    set_pwm.wait()

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    with open("pinout.json") as f:
        pinout = json.load(f)

    GPIO.setup(pinout["START_BUTTON"], GPIO.IN)

    status_q = Queue()
    stop_q = Queue()
    motors_q = Queue()
    leds_q = Queue()
    map_q = Queue()

    motors_thread = Thread(target=motors, args=(pinout, status_q, stop_q, motors_q))
    leds_thread = Thread(target=leds, args=(pinout, status_q, stop_q, leds_q))
    sensors_thread = Thread(target=sensors, args=(pinout, status_q, stop_q, map_q, motors_q, leds_q))
    path_thread = Thread(target=path, args=(pinout, status_q, stop_q, map_q, motors_q))
    cv_thread = Thread(target=cv, args=(pinout, status_q, stop_q, map_q, leds_q))

    leds_thread.start()
    sensors_thread.start()
    path_thread.start()
    cv_thread.start()

    print("ready, waiting for start button")
    GPIO.wait_for_edge(pinout["START_BUTTON"], GPIO.RISING)

    print("starting")
    motors_thread.start()
    time.sleep(2)

    print("waiting for stop button")
    while True:
        if GPIO.input(pinout["START_BUTTON"]):
            print("hold for 2s to stop")
            time.sleep(2)
            if GPIO.input(pinout["START_BUTTON"]):
                print("stopping")
                stop_q.put(1)
                break
        if status_q.qsize():
            print(status_q.get())

    print("printing backlogged status messages")
    while status_q.size():
        print(status_q.get())

    while sensors_thread.is_alive():
        pass
    while leds_thread.is_alive():
        pass
    while motors_thread.is_alive():
        pass
    while path_thread.is_alive():
        pass
    while cv_thread.is_alive():
        pass
    GPIO.cleanup()
    print("stopped")


main()
