from gpiozero import MotionSensor
from gpiozero import Buzzer
from picamera import PiCamera
from datetime import datetime
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
buzzer = Buzzer(14)
while True:
	pir.wait_for_motion()
	print "Motion is detected"
	filename = datetime.now().strftime("result/%Y-%m-%d_ %H:%M:%S.jpg")	 
	camera.capture(filename)
	for num in range(0,5):
		buzzer.on()
        	sleep(0.1)
        	buzzer.off()
		sleep(0.01)
	print "Alarm has been rung"
	print "Image is saved name:%s" %filename 
	pir.wait_for_no_motion()
