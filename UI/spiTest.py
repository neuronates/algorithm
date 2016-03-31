#!/usr/bin/python
#--------------------------------------   
# This script reads data from a 
# MCP3008 ADC device using the SPI bus.
#
# Author : Matt Hawkins
# Date   : 13/10/2013
#
# http://www.raspberrypi-spy.co.uk/
#
#--------------------------------------

#import spidev
import autocorrelation
import epileptogenicity
import time
import os
import numpy as np
import atexit
import serial
from multiprocessing import Process
from subprocess import check_call

def spiTestRun():

	# Function to convert data to voltage level,
	# rounded to specified number of decimal places. 
	def ConvertVolts(data,places):
		volts = (data * 3.3)/float(1023)#2**24-1)
  		volts = round(volts,places)  
  		return volts
  
	# Define sensor channels
	chan = [0, 1, 2, 3, 4, 5, 6, 7]
	sampling_rate = 256
	window_length = 30
	samples_per_chan = sampling_rate * window_length
	precision = 3
	# Define delay between readings
	#delay = (1.0/sampling_rate)
	delay = 0

	eegData = np.empty((samples_per_chan, len(chan)))
	ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 0)
	ser.stopbits = 2
	windowNum = 0


	# build and upload arduino code onto arduino uno
	d = "/home/pi/algorithm/arduino"
	#os.chdir(d)
	check_call(["ino", "clean"],cwd=d)
	check_call(["ino", "build"],cwd=d)
	check_call(["ino", "upload"],cwd=d)
	time.sleep(10)
#	os.system("ino build -d ~/algorithm/UI/arduino")
#	os.system("ino upload -d ~/algorithm/UI/arduino")
	
	def processData(eeg):
		data = np.copy(eeg[0])
		print data.shape
		res = autocorrelation.seizure(data)
		autoFlags = np.ones((data.shape[0], 1)) * res
		epiFlags = epileptogenicity.seizure(data)
		finalFlags = np.logical_or(autoFlags, epiFlags)#combineFlags(autoFlags, epiFlags)
		data = np.append(data, finalFlags)
		saveWindow(data)
	
	while True:
		
		windowNum += 1
		#p1 = Process(target = processData)
		
		for i in xrange(samples_per_chan-1):
			for c in chan:
				temp = ser.readline()#.splitlines()[0]
				#temp = ser.readline().strip('\r\n')	#remove new line
				#temp = temp.splitlines()[0]
#				if(temp[0] == '-' and temp[1] == '-'):
#					temp = temp[1:]
#				if(temp == '-' or temp == ''):
#					print 'bad input'
#					time.delay(2)
#					temp = temp.strip('-')
#					temp = temp.strip('')
				temp = temp.strip('\r\n')
				temp = temp.strip('\x00')		#remove null bytes
				flag = True
				while(flag):
					try:
						temp = int(temp)
						flag = False
					except ValueError:
#					print '======================================\n\n\n\n'
					#time.sleep(2)
					
						temp = ser.readline()	
				test = temp
				#if(temp[0] == '-' and temp[1] == '-'):
				#	temp = temp[1:]
				#while(len(temp) == 0 or temp == '-' or temp == ''):
					
				#	print 'bad input'
				#	print len(temp)
				#	temp = ser.readline().strip()
				#	temp = temp.rstrip('\0')
				#	if(temp[0] == '-' and temp[1] == '-'):
				#		temp = temp[1:]
				#temp = temp[1:]
#				if(temp == '-' or temp == ''):
#					temp = 0
#					print 'bad input'
				#time.sleep(2) # added to see whether this loop is ever entered
#				print i
			#	print 'Length'
			#	print len(temp)
#				print 'Value'
#				print temp
#				print '\n'
			#eegData[i,1] = ConvertVolts(1, precision)
			eegData[i,c] = ConvertVolts(int(test), precision)
			
			#eegData[i] = [ConvertVolts(eegData[c]) for c in xrange(len(chan))]
 			# Print out results
# 			print "--------------------------------------------"  
# 			print("Voltage : {}V".format(eegData[i]))
		
		p1 = Process(target = processData, args = (eegData,))
		p1.start()

	 	time.sleep(delay)
	

	
	def saveFile():
		np.savetxt('data/out.txt', eegData, delimiter=',')
		print "Stopped!\n"
	def saveWindow(data):
		np.savetxt('data/window_'+str(windowNum)+'.txt', data, delimiter=',')

	def combineFlags(autoFlags, epiFlags):
		results = np.logical_or(autoFlags, epiFlags)

	import atexit
	atexit.register(saveFile)


if __name__ == '__main__':
	spiTestRun()
 

