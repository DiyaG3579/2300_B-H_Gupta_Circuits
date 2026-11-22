import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 38

GPIO.setup(led,GPIO.OUT)
GPIO.output(led,False)

GPIO.cleanup()
