import RPi.GPIO as GPIO
import time

def LedOnOff3Sec(ledPin, sec):
    for n in range(0, round(3*(1/(sec*2)))):
        GPIO.output(ledPin, GPIO.HIGH)
        time.sleep(sec)
        GPIO.output(ledPin, GPIO.LOW)
        time.sleep(sec)
