# Test program to test motor control with PWM inputs

'''
Need to run these commands to enable the PWM pins

# Enable pin 32 / PWM0
sudo busybox devmem 0x700031fc 32 0x45
sudo busybox devmem 0x6000d504 32 0x2

# Enable pin 33 / PWM2
sudo busybox devmem 0x70003248 32 0x46
sudo busybox devmem 0x6000d100 32 0x00
'''

import RPi.GPIO as GPIO
import time

ENA = 32
IN1 = 24
IN2 = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2, GPIO.OUT, initial=GPIO.LOW)
pwm = GPIO.PWM(ENA, 100)
pwm.start(10)

print("forward low")
pwm.ChangeDutyCycle(10)
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
time.sleep(1)

print("forward high")
pwm.ChangeDutyCycle(90)
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)
time.sleep(1)

print("stop")
pwm.stop()
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
time.sleep(1)

GPIO.cleanup()
