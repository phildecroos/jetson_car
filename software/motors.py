import RPi.GPIO as GPIO

SPEED = 50  # 1 to 99


def get_steer(data):
    steer_speed = int(SPEED * (1 - (abs(data) / 10)))
    if steer_speed == 0:
        steer_speed = 1
    return steer_speed


def motors(pinout, status_q, stop_q, motors_q):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinout["L_ENABLE"], GPIO.OUT)
    GPIO.setup(pinout["L_PHASE"], GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(pinout["R_ENABLE"], GPIO.OUT)
    GPIO.setup(pinout["R_PHASE"], GPIO.OUT, initial=GPIO.LOW)
    pwmL = GPIO.PWM(pinout["L_ENABLE"], 100)
    pwmR = GPIO.PWM(pinout["R_ENABLE"], 100)
    pwmL.start(SPEED)
    pwmR.start(SPEED)
    stop_latch = True

    while not stop_q.qsize():
        data = motors_q.get()

        if stop_latch:
            if data == "START":
                stop_latch = False
                pwmL.start(SPEED)
                pwmR.start(SPEED)
                GPIO.output(pinout["L_PHASE"], GPIO.HIGH)
                GPIO.output(pinout["R_PHASE"], GPIO.HIGH)
        elif data == "STOP":
            stop_latch = True
            pwmL.stop()
            pwmR.stop()
            GPIO.output(pinout["L_PHASE"], GPIO.LOW)
            GPIO.output(pinout["R_PHASE"], GPIO.LOW)
        elif data == 0:
            pwmL.ChangeDutyCycle(SPEED)
            pwmR.ChangeDutyCycle(SPEED)
        elif data < 0:
            pwmL.ChangeDutyCycle(get_steer(data))
        elif data > 0:
            pwmR.ChangeDutyCycle(get_steer(data))
