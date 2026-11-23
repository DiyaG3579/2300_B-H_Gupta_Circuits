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

buzzerB = GPIO.PWM(buzzer, 2400)

GPIO.output(led, False)
buzzer.start(50)
time.sleep(1.0)

GPIO.output(led,False)
buzzerB.stop()



GPIO.cleanup()