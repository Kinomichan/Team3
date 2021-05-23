import time, hcsr04, kintone, RPi.GPIO as GPIO
from kintone import getCurrentTimeStamp
GPIO.setmode(GPIO.BCM)
# Start writing your program below

triggerPin = 14
echoPin = 23
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

distance = hcsr04.getDistance(triggerPin, echoPin)
print ("Distance (cm): " + str(distance))

# Write your program above this line
GPIO.cleanup()

    
