#Yay doing the countdown now
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Doing the same thing with the buzzer on two GPIO pins
buzzerA = 16
buzzerB = 18
button = 12
#These are each of the pins that the Countdown is attached to, so that it can be set up in a loop
segments = [40, 36, 32, 38, 35, 37, 33]

#Timing points
t = 0
j = 0

#I might stop commenting on all the things that are the same - usual setup
GPIO.setup(buzzerA, GPIO.OUT)
GPIO.setup(buzzerB, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Buzzer setup
GPIO.output(buzzerA, False)
buzz = GPIO.PWM(buzzerB, 2000)

#Setting up the pins in a for loop so that we didn't have to do it a million times
for pin in segments:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)

#Kinda genius to use a function if I do say so myself...and I do
def light(pattern):
   
     for i in range(len(pattern)):
        pin = segments[i]
        value = pattern[i]         

         #Ooh fancy lighting up the board, crazy
        if value == 1:
            GPIO.output(pin, False)
        else:
            GPIO.output(pin, True) 

while t < 25:
    #Acutal countdown for when the buzzer is pressed
    if GPIO.input(button) == GPIO.HIGH:
        light([1, 1, 1, 1, 0, 1, 1])
        time.sleep(1)
        light([1, 1, 1, 1, 1, 1, 1])
        time.sleep(1)
        light([1, 1, 1, 0, 0, 0, 0])
        time.sleep(1)
        light([1, 0, 1, 1, 1, 1, 1])
        time.sleep(1)
        light([1, 0, 1, 1, 0, 1, 1])
        time.sleep(1)
        light([0, 1, 1, 0, 0, 1, 1])
        time.sleep(1)
        light([1, 1, 1, 1, 0, 0, 1])
        time.sleep(1)
        light([1, 1, 0, 1, 1, 0, 1])
        time.sleep(1)
        light([0, 1, 1, 0, 0, 0, 0])
        time.sleep(1)
        light([1, 1, 1, 1, 1, 1, 0])

        #Inside the loop, while the button 
        while GPIO.input(button) == GPIO.LOW:
            buzz.start(50)
            light([1, 1, 1, 1, 1, 1, 1])
            time.sleep(0.05)
            light([0, 0, 0, 0, 0, 0, 0])
            time.sleep(0.05)
            j = j + 1
            #Again just because the buzzer can't continuously beep, we have to do some work arounds
            if j >= 5:
                buzz.stop()
                j = 0
                time.sleep(0.1)
        #Finally exiting the loop
        buzz.stop()
        t = t + 25
    #Waiting for the countdown to start
    else:
        t = t + 1
        time.sleep(1)

GPIO.cleanup()

#GPIO.output(segments[0], False)
#GPIO.output(segments[1], False)
#GPIO.output(segments[2], False)
#GPIO.output(segments[3], False)
#GPIO.output(segments[4], False)
#GPIO.output(segments[5], False)
#GPIO.output(segments[6], False)
#time.sleep(0.7)
#GPIO.output(segments[0], True)
#GPIO.output(segments[1],True)
#GPIO.output(segments[2],True)
#GPIO.output(segments[3], True)
#GPIO.output(segments[4], True)
#GPIO.output(segments[5], True)
#GPIO.output(segments[6], True)
