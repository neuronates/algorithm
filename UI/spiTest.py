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

import spidev
import time
import os
import numpy as np

#if __name__ == '__main__':
def spiTestRun():
	# Open SPI bus
	spi = spidev.SpiDev()
	spi.open(0,0)
	spi.max_speed_hz = 122000
	spi.mode = 0b01

	# Function to read SPI data from MCP3008 chip
	# Channel must be an integer 0-7

  
	# Define sensor channels
	chan = [0, 1, 2, 3, 4, 5, 6, 7]
	sampling_rate = 256
	window_length = 30
	num_samples = sampling_rate * window_length
	precision = 3
	# Define delay between readings
	#delay = (1.0/sampling_rate)
	delay = 1

	eegData = np.empty((sampling_rate * window_length,len(chan)))

	while True:
	
		try:
			for i in xrange(num_samples):
				eegData[i] = [ConvertVolts(ReadChannel(c), precision) for c in xrange(len(chan))]

	 			# Print out results
	 			print "--------------------------------------------"  
	 			print("Voltage : {}V".format(eegData[i]))  

				# Wait before repeating loop
		 		time.sleep(delay)

		except KeyboardInterrupt:
			np.savetxt('out2.txt', eegData, delimiter=',')
			spi.close() 
			print "Stopped!\n"
			exit()

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
 # spi.xfer2([32, 0])
  return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places. 
def ConvertVolts(data,places):
  volts = (data * 3.3)/float(1023)#2**24-1)
  volts = round(volts,places)  
  return volts
