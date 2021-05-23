import led, time, RPi.GPIO as GPIO

ledPin = 17
sec = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

for n in range(0, 5):
    GPIO.output(ledPin, GPIO.HIGH)
    time.sleep(sec)
    GPIO.output(ledPin, GPIO.LOW)
    time.sleep(sec)

GPIO.output(ledPin, GPIO.LOW)
GPIO.cleanup()
