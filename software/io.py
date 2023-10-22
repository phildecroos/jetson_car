# placeholder for IO processing code

def io(drive_q, lights_q, sensors_q, cv_q):
    while True:
        data = cv_q.get()
        if data != 0:
            drive_q.put(data)
            print("cv data processed")
        data = sensors_q.get()
        if data != 0:
            lights_q.put(data)
            print("sensors data processed")