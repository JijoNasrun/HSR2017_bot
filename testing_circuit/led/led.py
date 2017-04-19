import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT)
for x in range(0,5):
	print "LED ON"
	GPIO.output(40,GPIO.HIGH)
	time.sleep(1)
	print "LED OFF"
	GPIO.output(40,GPIO.LOW)
	time.sleep(1)
