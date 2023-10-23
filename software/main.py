# main driving program

from Queue import Queue
from threading import Thread
import RPi.GPIO as GPIO
from drive import *
from lights import *
from sensors import *
from cv import *

START = 11

print("initializing...")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(START, GPIO.IN)

drive_q = Queue()
lights_q = Queue()

drive_thread = Thread(target=drive, args=(drive_q, ))
lights_thread = Thread(target=lights, args=(lights_q, ))
sensors_thread = Thread(target=sensors, args=(drive_q, lights_q, ))
cv_thread = Thread(target=cv, args=(drive_q, lights_q, ))

print("starting...")
lights_thread.start()
sensors_thread.start()
cv_thread.start()
print("waiting for start button...")
GPIO.wait_for_edge(START, GPIO.RISING)
print("driving...")
drive_thread.start()