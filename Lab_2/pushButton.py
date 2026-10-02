import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
led = 12
button = 16
GPIO.setup(led,GPIO.OUT)
GPIO.setup(button, GPIO.IN)
GPIO.output(led,False)

t = 0

while t <= 14: 
   if GPIO.input(button):
    GPIO.output(led,True)
   else:
    GPIO.output(led,False)

t = t + 1
GPIO.cleanup()

