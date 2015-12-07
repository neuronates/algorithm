import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (300, 240)
	camera.framerate = 25
	camera.start_preview()
	camera.start_recording('video_demo.h264')
	camera.wait_recording(10)
	camera.stop_recording()
