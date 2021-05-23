# Library to use an HC-SR04 ultrasonic distance sensor
# May 14, 2021 v0.02
# Jun Suzuki (https://github.com/jxsboston)
# IoT for Kids: https://jxsboston.github.io/IoT-Kids/

import time, RPi.GPIO as GPIO
from typing import Optional

GPIO.setmode(GPIO.BCM)

# MAX_DISTANCE: Maximum sensing distance in cm
#   The distance sensor may be manufactured to work for
#   the range of 2cm to 400cm (or 500cm), but 10cm-250cm
#   would get you the best results. 220cm is set to MAX_DISTANCE.
MAX_DISTANCE = 220
maxRoundTripDistance = MAX_DISTANCE*2
timeOut = maxRoundTripDistance/100/340

# Function to send a trigger signal to the sensor's trigger pin 
#   for 10 microseconds. This trigger makes the sensor propagate
#   an ultrasonic wave. 
#
#   triggerPin: GPIO pin (pin number) connected to the trigger pin
#
def triggerSensor(triggerPin: int) -> None:
    GPIO.output(triggerPin, GPIO.HIGH)
    # 10 microseconds (0.0001 sec)
    time.sleep(0.00001)
    GPIO.output(triggerPin, GPIO.LOW)

# Function to measure the "echo time," which indicates how soon
#   the sensor receive an echo of the propagated ultrasonic wave.
#
#   echoPin: GPIO pin (pin number) connected to the echo pin
#
#   Returns the measured "echo time". None is returned if the sensor
#     failed to initiate distance measurement. Zero is returned if
#     distance measurement is timed out (i.e. no objects are detected
#     in the sensing range) OR if a nearby object is too close to
#     the sensor (< 2 cm).
#
# The echo pin (echoPin) goes high (GPIO.HIGH) when the ultrasonic
# wave is propagated in response to a trigger signal and stays high
# until the sensor receives an echo, at which point echoPin goes low
# (GPIO.LOW). Echo time is the duration in which echoPin stays high. 
#
def getEchoTime(echoPin: int) -> Optional[float]:
    t0 = time.time()
    while(GPIO.input(echoPin) == GPIO.LOW):
        # The sensor fails to initiate distance measurement
        # by sending a trigger signal to the echo pin.
        if((time.time() - t0) > timeOut): return None
    t0 = time.time()
    while(GPIO.input(echoPin) == GPIO.HIGH):
        # Distance measurement got timed out. The sensor detects
        # no nearby objects. 
        if((time.time() - t0) > timeOut): return 0
    return time.time() - t0

# Function to measure the distance to a nearby object (in cm).
#
#   triggerPin: GPIO pin (pin number) connected to the trigger pin
#   echoPin: GPIO pin (pin number) connected to the echo pin
#   
#   Returns the distance to a nearby object (in cm). None is
#     returned if the sensor failed to initiate distance measurement.
#     Zero is returned if distance measurement was timed out (i.e.
#     no objects were detected in the sensing range) OR if a nearby
#     object is too close to the sensor (< 2 cm).
#
def getDistance(triggerPin: int, echoPin: int) -> Optional[float]:
    triggerSensor(triggerPin)
    echoTime = getEchoTime(echoPin)
    if(echoTime==None): return None
    else: distance = echoTime * 340.0 / 2.0 * 100.0
    return distance

