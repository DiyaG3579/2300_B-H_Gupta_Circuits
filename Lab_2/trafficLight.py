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
g2 = 29

GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(y1,GPIO.OUT)
GPIO.setup(y2,GPIO.OUT)
GPIO.setup(g1,GPIO.OUT)
GPIO.setup(g2,GPIO.OUT)
GPIO.setup(b1,GPIO.OUT)
GPIO.setup(b2,GPIO.OUT)

t = 0
t1 = 0
t2 = 0


while t <= 75:
   GPIO.output(g1, True)
   GPIO.output(r2, True)
   GPIO.output(b1, True)
   time.sleep(13.5)
   GPIO.output(g1, False)
   GPIO.output(b1,True)
   while t1 < 1.5:
      GPIO.output(y1, True)
      time.sleep(0.25)
      GPIO.output(y1, False)
      time.sleep(0.25)
      t1 = t1 + 0.5
   t1 = 0
   GPIO.output(y1, False)
   GPIO.output(r2, False)
   GPIO.output(r1, True)
   GPIO.output(g2, True)
   GPIO.output(b2, True)
   time.sleep(13.5)
   GPIO.output(g2, False)
   GPIO.output(b2, False)
   while t2 < 1.5:
      GPIO.output(y2,True)
      time.sleep(0.25)
      GPIO.output(y2, False)
      time.sleep(0.25)
      t2 = t2 + 0.5
   t2 =  0
   GPIO.output(y2, False)
   t = t + 30
