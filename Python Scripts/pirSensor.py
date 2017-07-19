import RPi.GPIO as GPIO
import time

ledPin = 13
sensorPin = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(sensorPin, GPIO.IN)

while True:
	sensor = GPIO.input(sensorPin)
	if sensor == 0:
		GPIO.output(ledPin, 0)
		time.sleep(0.5)
	elif sensor == 1:
		GPIO.output(ledPin, 1)
		time.sleep(0.5)
