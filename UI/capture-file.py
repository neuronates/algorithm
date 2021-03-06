from multiprocessing import Process
import spiTest
import picamera
from subprocess import call
import time
from subprocess import check_call

with open('patientData.txt','r') as f:
    data=f.read()
name = data.split('\n')
print name
if(name[-1] == ''):
	name[-1] = 'testName'
nameh264 = 'videos/' + name[-1] + ".h264"
namemp4 = 'videos/' + name[-1] + ".mp4"


with picamera.PiCamera() as camera:
	
	try:
		time = 60
		print 'start'
		#Initialize concurrent processes
 #		camera.wait_recording(time)
		p1 = Process(target = camera.wait_recording, args = (time,))
		print 'before'
		p2 = Process(target = spiTest.spiTestRun, args = (name[-1],))#execfile("spiTest.py"))
		print 'after'
		camera.resolution = (800, 480)
		camera.framerate = 30
		camera.start_preview()
		
		#=============================================
		# Comment out the lines between the other set of ========
		# Uncommen the lines below
		# That should correct for the delay in video monitoring and eeg recording
#		p2.start()
#		time.sleep(6)
#		camera.start_recording(nameh264)
		#=============================================
		
		#============================================
		camera.start_recording(nameh264)
		p2.start()
		#=============================================
		
		camera.wait_recording(time)
		#Process(target = spiTest).start()
		##Process(target = camera.wait_recording, args = (time,)).start()
		#print 'wait recording'
		#print type(spiTest.spiTestRun)
		#p1.start()
		#p2.start()
		camera.stop_recording()
		p2.terminate()	
		print 'recording stopped'
		
		# essentially, you need a bash script that
		# concatenates all files that match window_*.txt
		# cat ls -tr window_*.txt > [patientname].txt
		# then delete all files that match window_*.txt (rm data/window_*.txt)
	
	except KeyboardInterrupt:
		print 'Stopped by Keyboard'
		camera.stop_recording()
		p2.terminate()	
concat_files = "ls -tr | window_*.txt > " + name[-1] + ".txt"
txtName = name[-1] + ".txt"
d = "/home/pi/algorithm/UI/data"

remove_files = "rm window_*.txt"

call([concat_files], cwd=d, shell = True)
#call()
#check_call(["ls","-tr","|","cat","window_*.txt",">",txtName], cwd=d)
#check_call(["rm","window_*.txt"], cwd=d)

convert_video = "MP4Box -fps 30 -add " + nameh264 + " " + namemp4 
delete_video = "rm " + nameh264
call([convert_video], shell = True)
call([delete_video], shell = True)
