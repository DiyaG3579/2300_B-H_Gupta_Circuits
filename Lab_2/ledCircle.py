import RPi.GPIO as GPIO
import time

#Setting up the board
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Reading in all the pins the the board is connected to
l1 = 12
l2 = 16
l3 = 36
l4 = 38
l5 = 32
l6 = 37
l7 = 33
l8 = 31
l9 = 13

#Setting up all the pins to be LED pins
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(l3,GPIO.OUT)
GPIO.setup(l4,GPIO.OUT)
GPIO.setup(l5,GPIO.OUT)
GPIO.setup(l6,GPIO.OUT)
GPIO.setup(l7,GPIO.OUT)
GPIO.setup(l8,GPIO.OUT)
GPIO.setup(l9,GPIO.OUT)

t = 0

GPIO.output(l1, False)
GPIO.output(l2, False)
GPIO.output(l3, False)
GPIO.output(l4, False)
GPIO.output(l5, False)
GPIO.output(l6, False)
GPIO.output(l7, False)
GPIO.output(l8, False)
GPIO.output(l9, False)

while t < 5:
    GPIO.output(l1,True)
    time.sleep(0.5)
    GPIO.output(l1, False)
    GPIO.output(l2, True)
    time.sleep(0.5)
    GPIO.output(l2, False)
    GPIO.output(l3, True)
    time.sleep(0.5)
    GPIO.output(l3, False)
    GPIO.output(l4, True)
    time.sleep(0.5)
    GPIO.output(l4, False)
    GPIO.output(l5, True)
    time.sleep(0.5)
    GPIO.output(l5, False)
    GPIO.output(l6, True)
    time.sleep(0.5)
    GPIO.output(l6, False)
    GPIO.output(l7, True)
    time.sleep(0.5)
    GPIO.output(l7, False)
    GPIO.output(l8, True)
    time.sleep(0.5)
    GPIO.output(l8, False)
    GPIO.output(l9, True)
    time.sleep(0.5)
    GPIO.output(l9,False)