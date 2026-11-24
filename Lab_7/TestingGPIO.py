import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Data, Clock, Latch = 36, 22, 32
for pin in (Data, Clock, Latch):
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def light(pattern):
    # pattern[0] = QA ... pattern[7] = QH, 1 = LED on
    for n in range(8):
        GPIO.output(Data, int(pattern[7 - n]))
        GPIO.output(Clock, 1)
        time.sleep(0.001)
        GPIO.output(Clock, 0)
        time.sleep(0.001)
    GPIO.output(Latch, 1)
    time.sleep(0.001)
    GPIO.output(Latch, 0)

try:
    light("00000000")
    time.sleep(1)
    light("11111111")        # all on
    time.sleep(1)
    for i in range(8):       # running light
        pattern = ["0"] * 8
        pattern[i] = "1"
        light("".join(pattern))
        time.sleep(0.3)
    light("00000000")
finally:
    pass                     # no cleanup, so the pins stay put
