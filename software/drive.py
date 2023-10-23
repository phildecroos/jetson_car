# motor control code

import RPi.GPIO as GPIO

SPEED = 50 # 1 to 99
ENL = 32
IN1 = 35
IN2 = 36
ENR = 33
IN3 = 38
IN4 = 40

def get_steer(data):
    steer_speed = SPEED * (1 - (int(abs(data) / 10)))
    if steer_speed == 0:
        steer_speed = 1
    return steer_speed

def drive(drive_q):
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(ENL, GPIO.OUT)
        GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(ENR, GPIO.OUT)
        GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
        pwmL = GPIO.PWM(ENL, 100)
        pwmL.start(10)
        pwmR = GPIO.PWM(ENR, 100)
        pwmR.start(10)
        stop_latch = 1

        while True:
            data = drive_q.get()
            
            if stop_latch:
                if data == "START":
                    stop_latch = 0
                    pwmL.ChangeDutyCycle(SPEED)
                    pwmR.ChangeDutyCycle(SPEED)
                    GPIO.output(IN1, GPIO.HIGH)
                    GPIO.output(IN3, GPIO.HIGH)
            elif data == "STOP":
                stop_latch = 1
                GPIO.output(IN1, GPIO.LOW)
                GPIO.output(IN2, GPIO.LOW)
                GPIO.output(IN3, GPIO.LOW)
                GPIO.output(IN4, GPIO.LOW)
            elif data == 0:
                pwmL.ChangeDutyCycle(SPEED)
                pwmR.ChangeDutyCycle(SPEED)
            elif data < 0:
                pwmL.ChangeDutyCycle(get_steer(data))
            elif data > 0:
                pwmR.ChangeDutyCycle(get_steer(data))
    finally:
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        GPIO.cleanup()