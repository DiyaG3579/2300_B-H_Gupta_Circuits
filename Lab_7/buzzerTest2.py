import RPi.GPIO as GPIO
import time

BL1 = 40
BL2 = 38

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BL1, GPIO.OUT)
GPIO.setup(BL2, GPIO.OUT)

def tone(freq, duration):
    half = 1.0 / freq / 2
    end = time.perf_counter() + duration
    state = True
    while time.perf_counter() < end:
        GPIO.output(BL1, state)
        GPIO.output(BL2, not state)   # opposite of A
        state = not state
        t = time.perf_counter() + half
        while time.perf_counter() < t:
            pass
    GPIO.output(BL1, False)
    GPIO.output(BL2, False)

try:
    for freq in (2000, 2400, 2800):
        print(f"{freq} Hz")
        tone(freq, 0.4)
        time.sleep(0.5)
finally:
    GPIO.cleanup()