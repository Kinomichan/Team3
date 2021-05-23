import time, motor28bjy as motor, hcsr04, kintone, RPi.GPIO as GPIO
from kintone import getCurrentTimeStamp
# Start writing your program below

triggerPin = 14
echoPin = 23
ControlPin = [12,16,20,21]

GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

for pin in ControlPin:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,0)

while(True):
    try:
        distance = hcsr04.getDistance(triggerPin, echoPin)
        print(getCurrentTimeStamp())
        print("Distance (cm): " + str(distance))

        if 2 <= distance < 10: 
            motor.rotate(0, ControlPin)
        elif 10 <= distance < 20:
            time.sleep(1)
        elif 20 <= distance < 35:
            motor.rotate(1, ControlPin)
        else:
            time.sleep(1)

    except KeyboardInterrupt:
        break

# Write your program above this line
GPIO.cleanup()
