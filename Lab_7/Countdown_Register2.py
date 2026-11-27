#This was option 2, we ran it by Professer Nussiov and she said it was fine 
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # use board pin numbers

#Adding a button in, glad there is no buzzer
Data = 36 #GPIO 16
Clock = 22 #GPIO 25
Latch = 32 #GPIO 12
button = 40

#Indexors
t = 0
j = 0

# Set upppppp
GPIO.setup(Data, GPIO.OUT)
GPIO.setup(Clock, GPIO.OUT)
GPIO.setup(Latch, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#same deal same deal
GPIO.output(Latch, 0)
GPIO.output(Clock, 0)

Sequence_i = "11111111"
Sequence_ii = "00000000"


def light(pattern):
    for n in range(8):
        bit = int(pattern[7 - n])
        GPIO.output(Data, bit)
        GPIO.output(Clock, 1)
        GPIO.output(Clock, 0)

    GPIO.output(Latch, 1)
    GPIO.output(Latch, 0)
#Ah where it finally gets interesting, so the countdown starts upon the push of the button - however the pause was what was interesting
while t < 25:
    if GPIO.input(button) == GPIO.HIGH:
        while j < 25:
            light("00001000") #9 #Added these, because after trying to read the other code, omg I needed this
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH: #So if the button gets pushed again, no matter where in the countdown it is, it will exit
                break
            light("00000000") #8 #You will notice that all zeros is off, because we had a common cathode rather than a common annode
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("00011111") #7
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("01000000") #6
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("01001000") #5
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("10011000") #4
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("00001100") #3
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("00100100")    #2
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("100111100") #1
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("00000011") #0
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("000100010") #A
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("11000000") #B
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("01100010") #C
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("10000100") #D
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("01100000") #E
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("01110001") #F
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("00001001") #G
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
            light("10010001") #H
            time.sleep(0.5)
            if GPIO.input(button) == GPIO.HIGH:
                break
        time.sleep(1.0)
    else: 
        t = t + 1
        time.sleep(1.0)
        light("11111111")
        j = 0
