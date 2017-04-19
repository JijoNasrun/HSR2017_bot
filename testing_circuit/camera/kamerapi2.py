import picamera
from time import sleep

camera = picamera.PiCamera()
sleep(5)
camera.capture('test.jpg')
sleep(5)
camera.capture('test2.jpg')

