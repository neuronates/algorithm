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
  volts = (data * 3.3)/float(1023)
  volts = round(volts,places)  
  return volts
  
# Define sensor channels
pot_channel = 0

# Define delay between readings
delay = 5

while True:
  try:

    # Read the light sensor data
    pot_level = ReadChannel(pot_channel)
    pot_volts = ConvertVolts(pot_level,2)
  
    # Print out results
    print "--------------------------------------------"  
    print("Voltage : {} ({}V)".format(pot_level,pot_volts))  

    # Wait before repeating loop
    time.sleep(delay)
    
  except KeyboardInterrupt:
    print "Stopped!"
    exit()
