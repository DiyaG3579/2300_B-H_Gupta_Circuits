import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

led = 32
buzzer = 40
button = 36
t = 0

GPIO.setup(led,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(led, False)

buzzerB = GPIO.PWM(buzzer, 2000)

while t < 15: 

    #Here the if ensures that only at the beginning the first one is lit up, but the rest of the time it is based on the button
    if GPIO.input(button) == GPIO.LOW:
       GPIO.output(led, False)
       buzzerB.start(50)
       time.sleep(0.5)
       GPIO.output(led,False)
       buzzerB.stop()
    else:
        GPIO.output(led, False)
        buzzerB.stop()
        t = t + 1
        time.sleep(1)

GPIO.cleanup()
