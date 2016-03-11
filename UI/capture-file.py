from multiprocessing import Process
#import spiTest
import picamera

with picamera.PiCamera() as camera:
	
	time = 60
	print 'start'
	#Initialize concurrent processes
	p1 = Process(target = camera.wait_recording, args = (time,))
	print 'before'
	#p2 = Process(target = execfile("spiTest.py"))
	print 'after'
	camera.resolution = (800, 480)
	camera.framerate = 30
	camera.start_preview()
	camera.start_recording('video_demo.h264')
	#camera.wait_recording(60)
	#Process(target = spiTest).start()
	#Process(target = camera.wait_recording, args = (time)).start()
	print 'wait recording'
	p1.start()
	print 'done'
	#p2.start()
	camera.stop_recording()
	print 'recording stopped'
