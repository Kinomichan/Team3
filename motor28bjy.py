import sys, time, RPi.GPIO as GPIO

seq0 = [ [1,0,0,0],
         [1,1,0,0],
         [0,1,0,0],
         [0,1,1,0],
         [0,0,1,0],
         [0,0,1,1],
         [0,0,0,1],
         [1,0,0,1] ]

seq = [seq0, sorted(seq0)]

def rotate(num, ControlPin):

    # num is the direction of rotation
    if num !=0 and num != 1:
        print("The number should be 0 or 1.")
        sys.exit(1)

    for i in range(128): # ~= 1 sec 
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], seq[num][halfstep][pin])
            time.sleep(0.001)
