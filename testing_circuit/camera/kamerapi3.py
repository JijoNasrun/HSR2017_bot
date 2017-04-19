from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview(alpha = 255)
camera.start_recording('/home/pi/testing_circuit/kamera.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()
