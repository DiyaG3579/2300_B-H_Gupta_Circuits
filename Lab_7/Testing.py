import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

Data = 36
Clock = 22
Latch = 32

GPIO.setup(Data, GPIO.OUT)
GPIO.setup(Clock, GPIO.OUT)
GPIO.setup(Latch, GPIO.OUT)

GPIO.output(Latch, False)
GPIO.output(Clock, False)

# Shift in 8 bits. The LAST bit sent ends up on QA.
# So: seven 0s first, then a 1 last -> only QA is on.
for n in range(7):
    GPIO.output(Data, 0)
    GPIO.output(Clock, True)
    GPIO.output(Clock, False)

GPIO.output(Data, 1)        # this bit lands on QA
GPIO.output(Clock, True)
GPIO.output(Clock, False)

# Latch: copy the 8 bits to the output pins
GPIO.output(Latch, True)
GPIO.output(Latch, False)

print("QA should be on. Holding for 30 seconds.")
time.sleep(30)
GPIO.cleanup()