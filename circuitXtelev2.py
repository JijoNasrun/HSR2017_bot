from gpiozero import MotionSensor
from gpiozero import Buzzer
from picamera import PiCamera
from datetime import datetime
from time import sleep
import os
from datetime import datetime

import telepot
pir = MotionSensor(4)
camera = PiCamera()
buzzer = Buzzer(14)
bot = telepot.Bot('354530879:AAH-HQKKE1sZsXsQp4trhPBxdOoAIIqdKkM')
dirname = datetime.strftime(datetime.now(), '%Y-%m-%d')
while True:
	pir.wait_for_motion()
	print "Motion is detected"
	if os.path.exists(dirname):
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d/%H:%M:%S.jpg')
        else:
                os.makedirs(dirname)
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d/%H:%M:%S.jpg')
	camera.capture(filename)
	for num in range(0,5):
		buzzer.on()
        	sleep(0.1)
        	buzzer.off()
		sleep(0.01)
	print "Alarm has been rung"
	print "Image is saved name:%s" %filename 
	bot.sendMessage('169500564', 'Perimeter has been breached')
	bot.sendPhoto('169500564', open(filename,'rb'))
	pir.wait_for_no_motion()


        
        
