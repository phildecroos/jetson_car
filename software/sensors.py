# placeholder for sensor reading code

import time

def sensors(sensors_q):
    while True:
        time.sleep(1)
        sensors_q.put(1)
        print("sensors data produced")