# motor control code

import RPi.GPIO as GPIO
import subprocess

set_pwm = subprocess.Popen("software/pwm.sh")
set_pwm.wait()

SPEED = 50 # 1 to 99
ENL = 32
IN1 = 35
IN2 = 36
ENR = 33
IN3 = 38
IN4 = 40

def get_steer(data):
    steer_speed = int(SPEED * (1 - (abs(data) / 10)))
    if steer_speed == 0:
        steer_speed = 1
    return steer_speed

def drive(stop_q, drive_q):
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ENL, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(ENR, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(IN4, GPIO.OUT, initial=GPIO.LOW)
    pwmL = GPIO.PWM(ENL, 100)
    pwmR = GPIO.PWM(ENR, 100)
    pwmL.start(SPEED)
    pwmR.start(SPEED)
    stop_latch = 1

    while not stop_q.qsize():
        data = drive_q.get()
        
        if stop_latch:
            if data == "START":
                stop_latch = 0
                pwmL.start(SPEED)
                pwmR.start(SPEED)
                GPIO.output(IN1, GPIO.HIGH)
                GPIO.output(IN2, GPIO.LOW)
                GPIO.output(IN3, GPIO.HIGH)
                GPIO.output(IN4, GPIO.LOW)
        elif data == "STOP":
            stop_latch = 1
            pwmL.stop()
            pwmR.stop()
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