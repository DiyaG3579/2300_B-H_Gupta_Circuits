import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # use board pin numbers

Data = 36 #GPIO 16
Clock = 22 #GPIO 25
Latch = 32 #GPIO 12
button = 40

t = 0
j = 0

# Set all pins as output
GPIO.setup(Data, GPIO.OUT)
GPIO.setup(Clock, GPIO.OUT)
GPIO.setup(Latch, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

while t < 25:
    if GPIO.input(button) == GPIO.HIGH:
        time.sleep(1.0)
        while GPIO.input(button) == GPIO.LOW:
            if j == 0:
                light("00001000") #9
                time.sleep(0.5)
                j = j + 1
            if j == 1:
                light("00000000") #8
                time.sleep(0.5)
                j = j + 1
            if j == 2:
                j = j + 1
                light("00011111") #7
                time.sleep(0.5)
            if j == 3:
                light("01000000") #6
                time.sleep(0.5)
                j = j + 1
            if j == 4:
                light("01001000") #5
                time.sleep(0.5)
                j = j + 1
            if j == 5:
                light("10011000") #4
                time.sleep(0.5)
                j = j + 1
            if j == 6:
                light("00001100") #3
                time.sleep(0.5) 
                j = j + 1
            if j == 7:
                light("00100100")    #2
                time.sleep(0.5)
                j = j + 1
            if j == 8:
                light("100111100") #1
                time.sleep(0.5)
                j = j + 1
            if j == 9:
                light("00000011") #0
                time.sleep(0.5)
                j = j + 1
            if j == 10:
                light("000100010") #A
                time.sleep(0.5)
                j = j + 1
            if j == 11:
                light("11000000") #B
                time.sleep(0.5)
                j = j + 1
            if j == 12:
                light("01100010") #C
                time.sleep(0.5)
                j = j + 1
            if j == 13:
                light("10000100") #D
                time.sleep(0.5)
                j = j + 1
            if j == 14:
                light("01100000") #E
                time.sleep(0.5)
                j = j + 1
            if j == 15:
                light("01110001") #F
                time.sleep(0.5)
                j = j + 1
            if j == 16:
                light("00001001") #G
                time.sleep(0.5)
                j = j + 1
            if j == 17:
                light("10010001") #H
                time.sleep(0.5)
    else: 
        t = t + 1
        time.sleep(1.0)
        light("11111111")