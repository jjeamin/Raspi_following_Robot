import RPi.GPIO as GPIO
import time
 
pin = 4 # PWM pin num 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(7.5)
cnt = 0
try:
    while True:
        p.ChangeDutyCycle(5)
        
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()
