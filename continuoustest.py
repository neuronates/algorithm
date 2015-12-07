import time
import picamera

with picamera.PiCamera() as camera:
	camera.start_preview()
	time.sleep(1)
	for filename in camera.capture_continuous('img{counter:03d}.jpg'):
		print('Captured %s' % filename)


