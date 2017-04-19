from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.sharpness = 0
camera.contrast = 0
camera.brightness = 60
camera.saturation = 0
camera.ISO = 0
camera.video_stabilization = False
camera.exposure_compensation = 0
camera.exposure_mode = 'auto'
camera.meter_mode = 'average'
camera.awb_mode = 'auto'
camera.image_effect = 'none'
camera.color_effects = None
camera.start_preview(alpha=255)
sleep(10)
camera.stop_preview()
camera.stop_preview()
 
