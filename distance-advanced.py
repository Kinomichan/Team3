import time, hcsr04, kintone, RPi.GPIO as GPIO
from kintone import getCurrentTimeStamp
# Start writing your program below

triggerPin = 14
echoPin = 23
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

hcsr04.triggerSensor(triggerPin)
echoTime = hcsr04.getEchoTime(echoPin)
distance = echoTime / 2 * 340  * 100

print ("Distance (cm): " + str(distance))

# Write your program above this line
GPIO.cleanup()

    
