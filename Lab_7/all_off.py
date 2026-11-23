import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 32
buzzerA = 40
buzzerB = 38
button = 36

GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzerA,GPIO.OUT)
GPIO.output(led,False)



GPIO.cleanup()
