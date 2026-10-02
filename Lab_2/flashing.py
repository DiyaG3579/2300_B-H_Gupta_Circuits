import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led = 37
GPIO.setup(led,GPIO.OUT)

t = 0

while t <= 50: 
   GPIO.output(led,True)
   time.sleep(1)
   GPIO.output(led,False)
   time.sleep(1)
   t = t + 5
