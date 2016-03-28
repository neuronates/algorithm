from multiprocessing import Process
#import spiTest
import picamera
from subprocess import call

with open('choosePatient.txt','r') as f:
    data=f.read()
name = data.split()
nameh264 = name[0] + ".h264"
namemp4 = name[0] + ".mp4"
print nameh264
print namemp4

with picamera.PiCamera() as camera:
	
	try:
		time = 30
#		print 'start'
		#Initialize concurrent processes
#		camera.wait_recording(time)
#		p1 = Process(target = camera.wait_recording, args = (time,))
#		print 'before'
#		p2 = Process(target = spiTest.spiTestRun)#execfile("spiTest.py"))
#		print 'after'
		camera.resolution = (800, 480)
		camera.framerate = 30
		camera.start_preview()
		camera.start_recording(nameh264)
#		p2.start()
		camera.wait_recording(time)
		#Process(target = spiTest).start()
		#Process(target = camera.wait_recording, args = (time)).start()
#		print 'wait recording'
		#p1.start()
#		print 'done'
		#p2.start()
		camera.stop_recording()
#		p2.terminate()	
#		print 'recording stopped'
	
	except KeyboardInterrupt:
		print 'Stopped by Keyboard'
		camera.stop_recording()
#		p2.terminate()	
conversion = "\"MP4Box -fps 30 -add " + nameh264 + " " + namemp4 + "\"" 
print conversion
convert_video = "MP4Box -fps 30 -add video_demo.h264 video_demo.mp4"
call([convert_video], shell = True)
