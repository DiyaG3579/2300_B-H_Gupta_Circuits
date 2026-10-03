import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led = 12
button = 18
GPIO.setup(led,GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.output(led,False)

t = 0

while t <= 14: 
   if GPIO.input(button)==GPIO.LOW:
    GPIO.output(led,True)
   else:
    GPIO.output(led,False)
    t = t + 1
    time.sleep(1)
GPIO.cleanup()

