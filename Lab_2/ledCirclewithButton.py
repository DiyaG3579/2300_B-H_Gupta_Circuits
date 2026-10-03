#Importing all the usual imputs
import RPi.GPIO as GPIO
import time

#Setting up the board...
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Reading in all the pins the the board is connected to - same except now there is a button
l1 = 12
l2 = 16
l3 = 36
l4 = 38
l5 = 32
l6 = 37
l7 = 33
l8 = 31
l9 = 13
button = 18

#Setting up all the pins to be LED pins
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
GPIO.setup(l3,GPIO.OUT)
GPIO.setup(l4,GPIO.OUT)
GPIO.setup(l5,GPIO.OUT)
GPIO.setup(l6,GPIO.OUT)
GPIO.setup(l7,GPIO.OUT)
GPIO.setup(l8,GPIO.OUT)
GPIO.setup(l9,GPIO.OUT)

#Our button was floating and so it was never returning an input of 1, so we fixed it permenantly to one unless pressed
#and then just inverted the code that way - because otherwise it was never going to turn on the light cycle
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

t = 0

#Putting them into a vector, so that our loop has an out should it need one (ie. the button becoming unpressed)

leds = [l1, l2, l3, l4, l5, l6, l7, l8, l9]


#Still starting everything as false
GPIO.output(l1, False)
GPIO.output(l2, False)
GPIO.output(l3, False)
GPIO.output(l4, False)
GPIO.output(l5, False)
GPIO.output(l6, False)
GPIO.output(l7, False)
GPIO.output(l8, False)
GPIO.output(l9, False)

i = 0
#Did t < 5, since t never increases and therefore it is an infinite loop
while t < 5:
    #Here is the like actual new stuff, so whenever the GPIO is on low (ie. pressed) then it will start the led light cycle
    #it will save where it left off, when it gets pulled away using the indexes and then start back up there 
    
    if GPIO.input(button) == GPIO.LOW:
            GPIO.output(leds[i], True)
            time.sleep(0.5)
            GPIO.output(leds[i], False)
            i = i + 1
            if i == len(leds):
                i = 0
                
    #This is just a basic turn all off when not pressed kinda deal
    else:
        GPIO.output(l1, False)
        GPIO.output(l2, False)
        GPIO.output(l3, False)
        GPIO.output(l4, False)
        GPIO.output(l5, False)
        GPIO.output(l6, False)
        GPIO.output(l7, False)
        GPIO.output(l8, False)
        GPIO.output(l9, False)
