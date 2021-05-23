import time, motor28bjy as motor, RPi.GPIO as GPIO

ControlPin = [12,16,20,21]
GPIO.setmode(GPIO.BCM)

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

motor.rotate(0, ControlPin)

GPIO.cleanup()
