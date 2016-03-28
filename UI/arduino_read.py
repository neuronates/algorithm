#! usr/bin/python
# from http://playground.arduino.cc/interfacing/python
import serial
import numpy


def takeSamples(numSamples):

	samples = np.empty(numSamples)

	ser = serial.Serial('/dev/ttyAMA0', 115200)
	for i in range(numSamples):
		samples[i] = ser.readline()
		
	return samples
