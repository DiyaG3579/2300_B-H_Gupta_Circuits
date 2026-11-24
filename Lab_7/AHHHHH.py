import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Data, Clock, Latch = 36, 22, 32
for pin in (Data, Clock, Latch):
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def light(pattern):
    for n in range(8):
        GPIO.output(Data, int(pattern[7 - n]))
        time.sleep(0.01)
        GPIO.output(Clock, 1)
        time.sleep(0.01)
        GPIO.output(Clock, 0)
        time.sleep(0.01)
    GPIO.output(Latch, 1)
    time.sleep(0.01)
    GPIO.output(Latch, 0)

for i in range(3):
    light("00000000")
    print("OFF: pin 15 should read ~0 V")
    time.sleep(8)
    light("11111111")
    print("ON: pin 15 should read ~3.3 V")
    time.sleep(8)