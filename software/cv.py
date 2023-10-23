# cv code

import time

def cv(drive_q, lights_q):
    while True:
        time.sleep(3)
        drive_q.put(0)
        drive_q.put(-1)
        drive_q.put(1)
        # placeholder for cv code
        # put 0 for straight, -1 to -10 for L, 1 to 10 for R