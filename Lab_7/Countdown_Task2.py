import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

buzzerA = 16
buzzerB = 18
button = 12
segments = [40, 36, 32, 38, 35, 37, 33]
t = 0
j = 0

GPIO.setup(buzzerA, GPIO.OUT)
GPIO.setup(buzzerB, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(buzzerA, False)
buzz = GPIO.PWM(buzzerB, 2000)

for pin in segments:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)

def light(pattern):
   
     for i in range(len(pattern)):
        pin = segments[i]
        value = pattern[i]         

        if value == 1:
            GPIO.output(pin, False)
        else:
            GPIO.output(pin, True) 

while t < 25:
    if GPIO.input(button) == GPIO.HIGH:
        light([1, 1, 1, 1, 0, 1, 1])
        time.sleep(1)
        light([1, 1, 1, 1, 1, 1, 1])
        time.sleep(1)
        light([1, 1, 1, 0, 0, 0, 0])
        time.sleep(1)
        light([1, 0, 1, 1, 1, 1, 1])
        time.sleep(1)
        light([1, 0, 1, 1, 0, 1, 1])
        time.sleep(1)
        light([0, 1, 1, 0, 0, 1, 1])
        time.sleep(1)
        light([1, 1, 1, 1, 0, 0, 1])
        time.sleep(1)
        light([1, 1, 0, 1, 1, 0, 1])
        time.sleep(1)
        light([0, 1, 1, 0, 0, 0, 0])
        time.sleep(1)
        light([1, 1, 1, 1, 1, 1, 0])
        
        while GPIO.input(button) == GPIO.LOW:
            buzz.start(50)
            light([1, 1, 1, 1, 1, 1, 1])
            time.sleep(0.05)
            light([0, 0, 0, 0, 0, 0, 0])
            time.sleep(0.05)
            j = j + 1
            if j >= 5:
                buzz.stop()
                j = 0
                time.sleep(0.1)
        
        buzz.stop()
        t = t + 25
    
    else:
        t = t + 1
        time.sleep(1)

GPIO.cleanup()

#GPIO.output(segments[0], False)
#GPIO.output(segments[1], False)
#GPIO.output(segments[2], False)
#GPIO.output(segments[3], False)
#GPIO.output(segments[4], False)
#GPIO.output(segments[5], False)
#GPIO.output(segments[6], False)
#time.sleep(0.7)
#GPIO.output(segments[0], True)
#GPIO.output(segments[1],True)
#GPIO.output(segments[2],True)
#GPIO.output(segments[3], True)
#GPIO.output(segments[4], True)
#GPIO.output(segments[5], True)
#GPIO.output(segments[6], True)
