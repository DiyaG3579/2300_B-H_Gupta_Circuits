#This is mostly the same code, so a lot of the comments are the same
#Importing all the usual imputs
import RPi.GPIO as GPIO
import time

#Setting up the board...
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Reading in all the pins the the board is connected to - same except now there is a button
led = 38
buzzer = 40
button = 36
t = 0
#Setting up all the pins to be LED pins
GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)

#Our button was floating and so it was never returning an input of 1, so we fixed it permenantly to one unless pressed
#and then just inverted the code that way - because otherwise it was never going to turn on the light cycle
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(led, False)
GPIO.output(buzzer, False)

#Did t < 5, so it is infinite
while t < 5: 

    #Here the if ensures that only at the beginning the first one is lit up, but the rest of the time it is based on the button
    if GPIO.input(button) == GPIO.LOW:
      GPIO.output(led,True)
      GPIO.output(buzzer,True)
    else:
        GPIO.output(led, False)
        GPIO.output(buzzer, False)

GPIO.cleanup()
