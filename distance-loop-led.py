import time, hcsr04, led, kintone, RPi.GPIO as GPIO
from kintone import getCurrentTimeStamp
# Start writing your program below

triggerPin = 14
echoPin = 23

ledPin = 17

GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

while(True):
    try:
        distance = hcsr04.getDistance(triggerPin, echoPin)
        print(getCurrentTimeStamp())
        print("Distance (cm): " + str(distance))

        if 10 <= distance < 20: 
            led.LedOnOff3Sec(ledPin, 0.1)
        elif 20 <= distance < 30:
            led.LedOnOff3Sec(ledPin, 0.5)
        else:
            time.sleep(3)

    except KeyboardInterrupt:
        break

# Write your program above this line
GPIO.output(ledPin, GPIO.LOW)
GPIO.cleanup()
