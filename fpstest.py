import io
import time
import picamera

my_stream = io.BytesIO()
with picamera.PiCamera() as camera:
	camera.start_preview()
	time.sleep(2)
	camera.capture(my_stream, 'jpeg')
