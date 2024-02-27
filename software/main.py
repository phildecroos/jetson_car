# main driving program

import time
from queue import Queue
from threading import Thread

import RPi.GPIO as GPIO
from cv import *  # replace wildcards with functions after code structure finalized
from drive import *
from lights import *
from sensors import *

STARTSTOP = 11

print("initializing...")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(STARTSTOP, GPIO.IN)

drive_q = Queue()
lights_q = Queue()
stop_q = Queue()

drive_thread = Thread(target=drive, args=(stop_q, drive_q))
lights_thread = Thread(target=lights, args=(stop_q, lights_q))
sensors_thread = Thread(target=sensors, args=(stop_q, drive_q, lights_q))
cv_thread = Thread(target=cv, args=(stop_q, drive_q, lights_q))

print("starting...")
lights_thread.start()
sensors_thread.start()
cv_thread.start()

print("waiting for start button...")
GPIO.wait_for_edge(STARTSTOP, GPIO.RISING)

print("driving...")
drive_thread.start()
time.sleep(1)

print("waiting for stop button...")
while True:
    data = GPIO.input(STARTSTOP)
    if data:
        print("hold for 3s to stop...")
        time.sleep(3)
        if data:
            break

print("stopping...")
stop_q.put(1)
drive_q.put("STOP")
lights_q.put(0)
while sensors_thread.is_alive():
    pass
while lights_thread.is_alive():
    pass
while drive_thread.is_alive():
    pass
while cv_thread.is_alive():
    pass
GPIO.cleanup()
print("stopped")
