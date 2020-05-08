#import RPi.GPIO as GPIO
import time

class motor(object):
	def __init__(self, MotorRightForward, MotorLeftForward, MotorRightBack, MotorLeftBack, MotorRightSpeed, MotorLeftSpeed):
		self.MotorRightForward = MotorRightForward
		self.MotorLeftForward = MotorLeftForward
		self.MotorRightBack = MotorRightBack
		self.MotorLeftBack = MotorLeftBack
		self.MotorRightSpeed = MotorRightSpeed
		self.MotorLeftSpeed = MotorLeftSpeed
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.cleanup()
		GPIO.setup(self.MotorRightForward, GPIO.OUT)
		GPIO.setup(self.MotorLeftForward, GPIO.OUT)
		GPIO.setup(self.MotorRightBack, GPIO.OUT)
		GPIO.setup(self.MotorLeftBack, GPIO.OUT)
		GPIO.setup(self.MotorRightSpeed, GPIO.OUT)
		GPIO.setup(self.MotorLeftSpeed, GPIO.OUT)

	def back(self, speed, pause):
		self.speed = speed
		self.pause = pause
		pwmA = GPIO.PWM(self.MotorRightSpeed, 35)
		pwmA.start(0)
		GPIO.output(self.MotorRightSpeed, GPIO.HIGH)
		pwmA.ChangeDutyCycle(self.speed)
		pwmB = GPIO.PWM(self.MotorLeftSpeed, 35)
		pwmB.start(0)
		GPIO.output(self.MotorLeftSpeed, GPIO.HIGH)
		pwmB.ChangeDutyCycle(self.speed)
		GPIO.output(self.MotorRightForward, GPIO.HIGH)
		GPIO.output(self.MotorLeftForward, GPIO.HIGH)
		time.sleep(self.pause)
		GPIO.output(self.MotorRightForward, GPIO.LOW)
		GPIO.output(self.MotorLeftForward, GPIO.LOW)
		GPIO.output(self.MotorRightSpeed, GPIO.LOW)
		pwmA.ChangeDutyCycle(0)
		pwmA.stop()
		GPIO.output(self.MotorLeftSpeed, GPIO.LOW)
		pwmB.ChangeDutyCycle(0)
		pwmB.stop()

	def forward(self, speed, pause):
		self.speed = speed
		self.pause = pause
		pwmA = GPIO.PWM(self.MotorRightSpeed, 35)
		pwmA.start(0)
		GPIO.output(self.MotorRightSpeed, GPIO.HIGH)
		pwmA.ChangeDutyCycle(self.speed)
		pwmB = GPIO.PWM(self.MotorLeftSpeed, 35)
		pwmB.start(0)
		GPIO.output(self.MotorLeftSpeed, GPIO.HIGH)
		pwmB.ChangeDutyCycle(self.speed)
		GPIO.output(self.MotorRightBack, GPIO.HIGH)
		GPIO.output(self.MotorLeftBack, GPIO.HIGH)
		time.sleep(self.pause)
		GPIO.output(self.MotorRightBack, GPIO.LOW)
		GPIO.output(self.MotorLeftBack, GPIO.LOW)
		GPIO.output(self.MotorRightSpeed, GPIO.LOW)
		pwmA.ChangeDutyCycle(0)
		pwmA.stop()
		GPIO.output(self.MotorLeftSpeed, GPIO.LOW)
		pwmB.ChangeDutyCycle(0)
		pwmB.stop()

	def right(self, speed, pause):
		self.speed = speed
		self.pause = pause
		pwmB = GPIO.PWM(self.MotorLeftSpeed, 35)
		pwmB.start(0)
		GPIO.output(self.MotorLeftSpeed, GPIO.HIGH)
		pwmB.ChangeDutyCycle(self.speed + 7)
		GPIO.output(self.MotorLeftBack, GPIO.HIGH)
		time.sleep(self.pause)
		GPIO.output(self.MotorLeftBack, GPIO.LOW)
		GPIO.output(self.MotorLeftSpeed, GPIO.LOW)
		pwmB.ChangeDutyCycle(0)
		pwmB.stop()

	def left(self, speed, pause):
		self.speed = speed
		self.pause = pause
		pwmA = GPIO.PWM(self.MotorRightSpeed, 35)
		pwmA.start(0)
		GPIO.output(self.MotorRightSpeed, GPIO.HIGH)
		pwmA.ChangeDutyCycle(self.speed)
		GPIO.output(self.MotorRightBack, GPIO.HIGH)
		time.sleep(self.pause)
		GPIO.output(self.MotorRightBack, GPIO.LOW)
		GPIO.output(self.MotorRightSpeed, GPIO.LOW)
		pwmA.ChangeDutyCycle(0)
		pwmA.stop()
