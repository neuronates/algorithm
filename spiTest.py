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
import numpy

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0,0)

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places. 
def ConvertVolts(data,places):
  volts = (data * 3.3) / float(2^24-1)
  volts = round(volts,places)  
  return volts
  
# Define sensor channels
chan = [0, 1, 2, 3, 4, 5, 6, 7]
sampling_rate = 256
window_length = 30
num_samples = sampling_rate * window_length
precision = 3
# Define delay between readings
delay = (1.0/sampling_rate)

eegData = np.empty(sampling_rate * window_length,len(chan))

while True:
	try:
		for i in xrange(num_samples):
		 	
			eegData[i] = [ConvertVolts(ReadChannel(c), precision) for c in xrange(len(chan))]
		 	
		# Read the light sensor data
 		chan_data = ReadChannel(chan)
 		chan_volts = ConvertVolts(chan_data,2)

 		# Print out results
 		print "--------------------------------------------"  
 		print("Voltage : {}V".format(eegData[i,0]))  

		# Wait before repeating loop
 		time.sleep(delay)

	except KeyboardInterrupt:
		print "Stopped!"
		exit()
