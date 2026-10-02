import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

r1 = 12
r2 = 11
y2 = 13
y1 = 16
b2 = 15
b1 = 18
g1 = 22
g2 = 7

GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(y1,GPIO.OUT)
GPIO.setup(y2,GPIO.OUT)
GPIO.setup(g1,GPIO.OUT)
GPIO.setup(g2,GPIO.OUT)
GPIO.setup(b1,GPIO.OUT)
GPIO.setup(b2,GPIO.OUT)

GPIO.output(r1,False)
GPIO.output(r2,False)
GPIO.output(y1,False)
GPIO.output(y2,False)
GPIO.output(g1,False)
GPIO.output(g2,False)
GPIO.output(b1,False)
GPIO.output(b2,False)
GPIO.cleanup()