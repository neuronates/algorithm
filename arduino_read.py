#! usr/bin/python
# from http://playground.arduino.cc/interfacing/python
import serial

ser = serial.Serial('/dev/ttyAMA0', 115200)
while True:
	print ser.readline()
