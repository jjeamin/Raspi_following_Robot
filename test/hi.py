import RPi.GPIO as GPIO
from time import sleep

class Motor:
	def __init__(self):
		GPIO.setmode(GPIO.BCM)

		self.Motor1A = 23
		self.Motor1B = 24
		self.Motor1E = 25

		self.Motor2A = 20
		self.Motor2B = 21
		self.Motor2E = 22

		GPIO.setup(self.Motor1A,GPIO.OUT)
		GPIO.setup(self.Motor1B,GPIO.OUT)
		GPIO.setup(self.Motor1E,GPIO.OUT)

		GPIO.setup(self.Motor2A,GPIO.OUT)
		GPIO.setup(self.Motor2B,GPIO.OUT)
		GPIO.setup(self.Motor2E,GPIO.OUT)

		p1 = GPIO.PWM(self.Motor1E,100)
		p2 = GPIO.PWM(self.Motor2E,100)

	def left_tire(mode):
		if mode == 1:
			GPIO.output(self.Motor1A,GPIO.HIGH)
			GPIO.output(self.Motor1B,GPIO.LOW)
			GPIO.output(self.Motor1E,GPIO.HIGH)
			setSpeed(3,3)
		elif mode == 0:
			GPIO.output(self.Motor1A,GPIO.LOW)
			GPIO.output(self.Motor1B,GPIO.HIGH)
			GPIO.output(self.Motor1E,GPIO.HIGH)
			setSpeed(3,3)
		elif mode == -1:
			GPIO.output(self.Motor1E,GPIO.LOW)	
			left_setSpeed(0)
		else:
			print('left_tire mode error')

	def right_tire(mode):
		if mode == 1:
			GPIO.output(self.Motor2A,GPIO.HIGH)
			GPIO.output(self.Motor2B,GPIO.LOW)
			GPIO.output(self.Motor2E,GPIO.HIGH)
			setSpeed(3,3)
		elif mode == 0:
			GPIO.output(self.Motor2A,GPIO.LOW)
			GPIO.output(self.Motor2B,GPIO.HIGH)
			GPIO.output(self.Motor2E,GPIO.HIGH)
			setSpeed(3,3)
		elif mode == -1:
			GPIO.output(self.Motor2E,GPIO.LOW)
			right_setSpeed(0)
		else:
			print('right_tire mode error')

	def go():
		right_tire(1)
		left_tire(1)	

	def back():
		right_tire(0)
		left_tire(0)

	def left():
		left_tire(1)
		right_tire(-1)

	def right():
		right_tire(1)
		left_tire(-1)
		
	def stop():
		GPIO.output(Motor1E,GPIO.LOW)
		GPIO.output(Motor2E,GPIO.LOW)
		setSpeed(0,0)
		
	def left_setSpeed(speed):
		p1.start(0)
		p1.ChangeDutyCycle(speed*10)

	def right_setSpeed(speed):
		p2.start(0)
		p2.ChangeDutyCycle(speed*10)
		
	def setSpeed(left_speed,right_speed):
		p1.start(0)
		p2.start(0)

		p1.ChangeDutyCycle(left_speed*10)
		p2.ChangeDutyCycle(right_speed*10)

	def clean():
		GPIO.cleanup()
	'''
	def go_left():
		GPIO.output(Motor1A,GPIO.HIGH)
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor1E,GPIO.HIGH)

		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor2E,GPIO.HIGH)

	def go_right():
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor1E,GPIO.HIGH)

		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor2E,GPIO.HIGH)

	def back_left():
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor1E,GPIO.HIGH)

		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor2E,GPIO.HIGH)

	def back_right():
		GPIO.output(Motor1A,GPIO.LOW)
		GPIO.output(Motor1B,GPIO.HIGH)
		GPIO.output(Motor1E,GPIO.HIGH)

		GPIO.output(Motor2A,GPIO.LOW)
		GPIO.output(Motor2B,GPIO.HIGH)
		GPIO.output(Motor2E,GPIO.HIGH)
	'''
'''
go()
sleep(2)
back()
sleep(2)
left()
sleep(2)
right()
sleep(2)
clean()
'''

m = Motor()
m.go(self)
sleep(3)
m.clean()
