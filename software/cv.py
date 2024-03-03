# cv code

import random
import time

import tensorflow as tf


def cv(stop_q, drive_q, lights_q):
    while not stop_q.qsize():
        drive_q.put(random.randint(-10, 10))
        time.sleep(1)
        # placeholder for cv code
