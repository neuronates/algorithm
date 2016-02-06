#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

with open("DemoEEGFile.txt") as f:
	data = f.read()

data = data.split('\n')

x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[0] for row in data]

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("EEG Data")
ax1.set_xlabel('Time (minutes)')
ax1.set_ylabel('EEG Voltage (mV)')

ax1.plot(x,y, c='r', label='A-O Montage')

leg = ax1.legend()

plt.show()
