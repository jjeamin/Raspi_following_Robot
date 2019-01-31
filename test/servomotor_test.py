import RPi.GPIO as GPIO
import time
import numpy as np
 
pin = 4 # PWM pin num 18
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 50)
p.start(0)
cnt = 0

degree = np.array([4.5,5.5,6.5,7.5,8.5,9.5,10.5])

try:
    while True:
        print('start')
        p.ChangeDutyCycle(degree[cnt])
        time.sleep(1)
        cnt += 1
        if cnt == 7:
            break
except KeyboardInterrupt:
    p.stop()
GPIO.cleanup()
