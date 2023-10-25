# cv code

import time
import random

def cv(drive_q, lights_q):
    while True:
        drive_q.put(random.randint(-10, 10))
        time.sleep(1)
        # placeholder for cv code
        # put 0 for straight, -1 to -10 for L, 1 to 10 for R