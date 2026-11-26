#Adding all the regular set up items
import RPi.GPIO as GPIO
import time

#In case there is any straggler GPIOs in place
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#And we add all the pins that everything is connected to, (Used Board for Pin Numbers)
led = 32
#One thing worth noting here is that we had to use two GPIO pins for the buzzer, because we needed to deliver more than 3.3 V to it, so we combined them to get 6.6 V
buzzerA = 40
buzzerB = 38
button = 36
t = 0

#Set up, yay no one saw that coming - we used the same code for the button that we used in the last led raspberry pi lab
GPIO.setup(led,GPIO.OUT)
#Again setting up two buzzers so that it will run at an adequet sound
GPIO.setup(buzzerA,GPIO.OUT)
GPIO.setup(buzzerB,GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(led, False)

#One of the buzzer pins had to be permenantly set to false so that it can still get 6.6 and oscillate
GPIO.output(buzzerA, False)

#We also got a passive buzzer, so here is the code for the frequency (Note 4200 was not close at all to the resonance frequency so we did 2000
buzz = GPIO.PWM(buzzerB, 2000)

#Loop so that it keeps running the code while responding to the buzzer
while t < 14:
    if GPIO.input(button) == GPIO.HIGH:
        #The buzzer with the 6.6V could probably only stay on for half a second and so the light turns on then the buzzer
        GPIO.output(led, True)
        time.sleep(0.25)
        buzz.start(50)
        time.sleep(0.5)
        buzz.stop()
        time.sleep(0.25)
        GPIO.output(led,False)
    else: #Loop while waiting for the buzzer to be pressed (If we expanded the timeframe, it could be pressed multiple times - since there is no t in the
          #button loop
        t = t + 1
        buzz.stop()
        GPIO.output(led,False)
        time.sleep(1.0)

GPIO.cleanup()
