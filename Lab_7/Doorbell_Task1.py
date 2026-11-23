import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 32
buzzerA = 40
buzzerB = 38
button = 36
t = 0

GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzerA,GPIO.OUT)
GPIO.setup(buzzerB,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(led, False)
GPIO.output(buzzerA, False)

buzz = GPIO.PWM(buzzerB, 2000)

while t < 14:
    if GPIO.input(button) == GPIO.HIGH:
        GPIO.output(led, True)
        time.sleep(0.25)
        buzz.start(50)
        time.sleep(0.5)
        buzz.stop()
        time.sleep(0.25)
        GPIO.output(led,False)
    else:
        t = t + 1
        buzz.stop()
        GPIO.output(led,False)
        time.sleep(1.0)

GPIO.cleanup()
