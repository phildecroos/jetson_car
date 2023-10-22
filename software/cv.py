# placeholder for cv code

import time

def cv(cv_q):
    while True:
        time.sleep(5)
        cv_q.put(1)
        print("cv data produced")