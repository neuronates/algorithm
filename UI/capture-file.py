from multiprocessing import Process
import spiTest
import picamera
from subprocess import call

with picamera.PiCamera() as camera:
	
	try:
		time = 30
		print 'start'
		#Initialize concurrent processes
		p1 = Process(target = camera.wait_recording, args = (time,))
		print 'before'
		p2 = Process(target = spiTest.spiTestRun)#execfile("spiTest.py"))
		print 'after'
		camera.resolution = (800, 480)
		camera.framerate = 30
		camera.start_preview()
		camera.start_recording('video_demo.h264')
		p2.start()
		camera.wait_recording(time)
		#Process(target = spiTest).start()
		#Process(target = camera.wait_recording, args = (time)).start()
		print 'wait recording'
		#p1.start()
		print 'done'
		#p2.start()
		camera.stop_recording()
		p2.terminate()	
		print 'recording stopped'
	
	except KeyboardInterrupt:
		print 'Stopped by Keyboard'
		camera.stop_recording()
		p2.terminate()	
convert_video = "MP4Box -fps 30 -add video_demo.h264 video_demo.mp4"
call([convert_video], shell = True)
