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
	# Open SPI bus
	'''
	spi = spidev.SpiDev()
	spi.open(0,0)
	spi.max_speed_hz = 122000
	spi.mode = 0b01

	# Function to read SPI data from MCP3008 chip
	# Channel must be an integer 0-7
	def ReadChannel(channel):
  		adc = spi.xfer2([1,(8+channel)<<4,0])
  		data = ((adc[1]&3) << 8) + adc[2]
 		# spi.xfer2([32, 0])
  		return data
  	'''

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
	delay = 1

	eegData = np.empty((samples_per_chan, len(chan)))
	ser = serial.Serial('/dev/ttyUSB0', 115200, timeout = 0)
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
	
	def processData():
		data = np.copy(eegData)
		res = autocorrelation.seizure(data)
		autoFlags = np.ones(samples_per_chan, 1) * res
		epiFlags = epileptogenicity(data)
		finalFlags = combineFlags(autoFlags, epiFlags)
		eegData = np.append(data, finalFlags)
		saveWindow(data)
	
	while True:
		
		windowNum += 1
		p1 = Process(target = processData)
		
		for i in xrange(samples_per_chan):
			print i
			for c in chan:
				temp = ser.readline().strip('\0')
				while(len(temp) == 0 or temp == '-'):
					print 'bad input'
					temp = ser.readline()
				print 'Length'
				print len(temp)
				print 'Value'
				print temp
				eegData[i,c] = ConvertVolts(int(temp.strip('\0')), precision)
			
			#eegData[i] = [ConvertVolts(eegData[c]) for c in xrange(len(chan))]
 			# Print out results
 			print "--------------------------------------------"  
 			print("Voltage : {}V".format(eegData[i]))
		
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
