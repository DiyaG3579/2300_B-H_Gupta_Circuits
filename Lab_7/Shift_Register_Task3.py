#Bet you didn't see this coming - task 3 that's crazy
import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # use board pin numbers

#The only three pins of the Board that are connected to GPIO pins
Data = 36 #GPIO 16
Clock = 22 #GPIO 25
Latch = 32 #GPIO 12

# Seting up all the pins
GPIO.setup(Data, GPIO.OUT)
GPIO.setup(Clock, GPIO.OUT)
GPIO.setup(Latch, GPIO.OUT)

#Since it is an 8 bit binary, instead of True/False, we are using 1/0. So setting the clock and latch to False
GPIO.output(Latch, 0)
GPIO.output(Clock, 0)

#Reference code for the goal
Sequence_i = "11111111"
Sequence_ii = "00000000"

#Setting it all up in a function, because I am just that good (Lowkey just modified the function from Task 2)
def light(pattern):
    #This is all kinda from the given code, but it basically lights up each bit sequentially, however it does it so fast (since there is no time.sleep that it looks immediate
    for n in range(8):
        bit = int(pattern[7 - n])
        GPIO.output(Data, bit)
        GPIO.output(Clock, 1)
        GPIO.output(Clock, 0)

    GPIO.output(Latch, 1)
    GPIO.output(Latch, 0)
    
#The pattern that we were given to follow
light("11111111")
time.sleep(1.0)
light("00000000")
time.sleep(1.0)
light("10101010")
time.sleep(1.0)
light("01010101")
time.sleep(1.0)
light('00000000')
time.sleep(1.0)
light('11111111')
time.sleep(1.0)
light('00000000')
time.sleep(1.0)
