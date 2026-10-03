#Restarting, because we did it wrong...(keeping most of the comments the same)
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

#Setting up the states so that they can be saved and the cycle can either stay on or stay off until the button is pressed
#(i is for indexing though)
i = 0
on = False
last = GPIO.HIGH

#Did t < 5, since t never increases and therefore it is an infinite loop
while t < 5: 
    #Reading the current state
    curr = GPIO.input(button)
    #If the last state doesn't match the current state (ie. went from 0 to 1 (since our button is flipped) then turn it on)
    if last == GPIO.HIGH and curr == GPIO.LOW:
        on = not on
        time.sleep(0.005)
        #Now it is on rather than off
        last = curr
    #Otherwise we are saying that last will be whatever curr is (more important after a cycle)    
    else:
        last = curr
    #print(on)
    
    if on:
        #Basically tranverse through the LEDs
        GPIO.output(leds[i], True)
        
        #This is equivalent to 0.5 from before, only now it checks for if the button is pressed
        for e in range(50):
            time.sleep(0.01)
            curr = GPIO.input(button)
            #if the button went from off to on then the input has flipped
            if last == GPIO.HIGH and curr == GPIO.LOW:
                on = False
                last = curr
                break
            last = curr
            
        #Runs the exact same as before
        GPIO.output(leds[i], False)
        i = i + 1
        if i == len(leds):
           i = 0         

    #This is just a basic turn all off when not pressed kinda deal
    if not on:
        GPIO.output(l1, False)
        GPIO.output(l2, False)
        GPIO.output(l3, False)
        GPIO.output(l4, False)
        GPIO.output(l5, False)
        GPIO.output(l6, False)
        GPIO.output(l7, False)
        GPIO.output(l8, False)
        GPIO.output(l9, False)