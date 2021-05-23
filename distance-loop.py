import time, hcsr04, kintone, RPi.GPIO as GPIO
from kintone import getCurrentTimeStamp
# Start writing your program below

triggerPin = 14
echoPin = 23
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

sensingInterval = 1

while(True):
    try:
        distance = hcsr04.getDistance(triggerPin, echoPin)
        print(getCurrentTimeStamp())
        print("Distance (cm): " + str(distance))
        time.sleep(sensingInterval)
    except KeyboardInterrupt:
        break

# Write your program above this line
GPIO.cleanup()

    
