#Importing everything
import RPi.GPIO as GPIO
import time

#Setting up the board
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Reading in all the pins the the board is connected to
r1 = 12
r2 = 11
y2 = 13
y1 = 16
b2 = 15
b1 = 18
g1 = 22
g2 = 7

#Setting up all the pins to be LED pins
GPIO.setup(r1,GPIO.OUT)
GPIO.setup(r2,GPIO.OUT)
GPIO.setup(y1,GPIO.OUT)
GPIO.setup(y2,GPIO.OUT)
GPIO.setup(g1,GPIO.OUT)
GPIO.setup(g2,GPIO.OUT)
GPIO.setup(b1,GPIO.OUT)
GPIO.setup(b2,GPIO.OUT)

#All my time constants, because like the time.time() was getting tedious
t = 0
t1 = 0
t2 = 0

#The actual loop, I chose 75, because that would be around 3 full cycles of the traffic light
while t < 75:
   #Running the first part, where it is red on one side and green/blue on the other side
   GPIO.output(g1, True)
   GPIO.output(r2, True)
   GPIO.output(b1, True)
   GPIO.output(b2, False)
   time.sleep(13.5)
   GPIO.output(g1, False)
   GPIO.output(b1,False)
   #Blinking yellow to indicate the end of a cycle
   while t1 < 1.5:
      GPIO.output(y1, True)
      time.sleep(0.25)
      GPIO.output(y1, False)
      time.sleep(0.25)
      t1 = t1 + 0.5
   #Reseting the blink time   
   t1 = 0
   #Running the second light where it is red on the other side now
   GPIO.output(y1, False)
   GPIO.output(r2, False)
   GPIO.output(r1, True)
   GPIO.output(g2, True)
   GPIO.output(b2, True)
   time.sleep(13.5)
   GPIO.output(g2, False)
   GPIO.output(b2, False)
   #Blinking light yay
   while t2 < 1.5:
      GPIO.output(y2,True)
      time.sleep(0.25)
      GPIO.output(y2, False)
      time.sleep(0.25)
      t2 = t2 + 0.5
   #With yet another reset, kinda repetitive   
   t2 =  0
   GPIO.output(y2, False)

   #Resetting everything so that it works correctly next time
   t = t + 30
   GPIO.output(r1,False)
   GPIO.output(r2,False)
   GPIO.output(y1,False)
   GPIO.output(y2,False)
   GPIO.output(g1,False)
   GPIO.output(g2,False)
   GPIO.output(b1,False)
   GPIO.output(b2,False)

#Final reset so that it doesn't get stuck in on mode somehow
GPIO.output(r1,False)
GPIO.output(r2,False)
GPIO.output(y1,False)
GPIO.output(y2,False)
GPIO.output(g1,False)
GPIO.output(g2,False)
GPIO.output(b1,False)
GPIO.output(b2,False)
GPIO.cleanup()