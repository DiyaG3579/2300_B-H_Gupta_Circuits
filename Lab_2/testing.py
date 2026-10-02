import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

r1 = 12
#r2 = 11
#y2 = 13
#y1 = 16
#b2 = 15
#b1 = 18
#g1 = 22
#g2 = 29

GPIO.setup(r1,GPIO.OUT)
#GPIO.setup(r2,GPIO.OUT)
#GPIO.setup(y1,GPIO.OUT)
#GPIO.setup(y2,GPIO.OUT)
#GPIO.setup(g1,GPIO.OUT)
#GPIO.setup(g2,GPIO.OUT)
#GPIO.setup(b1,GPIO.OUT)
#GPIO.setup(b2,GPIO.OUT)

GPIO.output(r1,True)
time.sleep(5)
GPIO.output(r1,False)
