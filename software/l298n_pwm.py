# Test program to test L298N motor control with PWM inputs

import RPi.GPIO as GPIO
import time

ENA = 26
IN1 = 24
IN2 = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENA, GPIO.OUT, initial=GPIO.HIGH)

# Forward
print("forward")
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
time.sleep(1)

# Stop
print("stop")
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
time.sleep(1)

GPIO.cleanup()
