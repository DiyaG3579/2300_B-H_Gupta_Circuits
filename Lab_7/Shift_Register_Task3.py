import RPi.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # use board pin numbers

Data = 36 #GPIO 16
Clock = 22 #GPIO 25
Latch = 32 #GPIO 12

# Set all pins as output
GPIO.setup(Data, GPIO.OUT)
GPIO.setup(Clock, GPIO.OUT)
GPIO.setup(Latch, GPIO.OUT)

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