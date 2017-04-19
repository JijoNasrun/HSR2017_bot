from gpiozero import MotionSensor
from gpiozero import Buzzer
from picamera import PiCamera
from datetime import datetime
from time import sleep
import telepot
pir = MotionSensor(4)
camera = PiCamera()
buzzer = Buzzer(14)
bot = telepot.Bot('354530879:AAH-HQKKE1sZsXsQp4trhPBxdOoAIIqdKkM')
while True:
	pir.wait_for_motion()
	print "Motion is detected"
	filename = datetime.now().strftime("result/%Y-%m-%d_ %H:%M:%S.jpg")	 
	bot.sendMessage('169500564', filename[7:27])
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
