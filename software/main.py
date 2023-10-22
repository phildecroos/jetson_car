# main driving program

from Queue import Queue
from threading import Thread
from io import io
from drive import *
from lights import *
from sensors import *
from cv import *

# def functions & setup code

try:
    print("starting...")
    drive_q = Queue()
    lights_q = Queue()
    sensors_q = Queue()
    cv_q = Queue()
    io_thread = Thread(target=io, args=(drive_q, lights_q, sensors_q, cv_q, ))
    drive_thread = Thread(target=drive, args=(drive_q, ))
    lights_thread = Thread(target=lights, args=(lights_q, ))
    sensors_thread = Thread(target=sensors, args=(sensors_q, ))
    cv_thread = Thread(target=cv, args=(cv_q, ))
    io_thread.start()
    drive_thread.start()
    lights_thread.start()
    sensors_thread.start()
    cv_thread.start()
    # start sensors, lights, & cv threads
    # wait for start button press then start motor control thread
finally:
    pass
    # shutdown code to stop motors & make all outputs low