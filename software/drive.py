# motor control code

'''
# Note: the pwm configs on my machine don't work properly so i made a .sh file that runs on startup with these commands to set them manually
# Enable pin 32 / PWM0
sudo busybox devmem 0x700031fc 32 0x45
sudo busybox devmem 0x6000d504 32 0x2
# Enable pin 33 / PWM2
sudo busybox devmem 0x70003248 32 0x46
sudo busybox devmem 0x6000d100 32 0x00
'''

import RPi.GPIO as GPIO

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
        pwmR = GPIO.PWM(ENR, 100)
        pwmL.start(10)
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
                    GPIO.output(IN2, GPIO.LOW)
                    GPIO.output(IN3, GPIO.HIGH)
                    GPIO.output(IN4, GPIO.LOW)
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
