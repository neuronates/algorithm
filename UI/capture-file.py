import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (800, 480)
	camera.framerate = 30
	camera.start_preview()
	camera.start_recording('video_demo.h264')
	camera.wait_recording(60)
	camera.stop_recording()
