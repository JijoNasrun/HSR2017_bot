from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
pir = MotionSensor(4)
camera = PiCamera()
while True:
	pir.wait_for_motion()
	print "Motion is detected"
	filename = datetime.now().strftime("result/%Y-%m-%d_ %H:%M:%S.jpg")	 
	camera.capture(filename)
	print "Image is saved name:%s" %filename 
	pir.wait_for_no_motion()
