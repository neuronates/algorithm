#!/usr/bin/python3

from pylab import *
from matplotlib import rc, rcParams
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl


# working code using matplotlib to plot
dataMatrix1 = genfromtxt('DemoEEGFile.txt')

x = dataMatrix1[:,0]
y = dataMatrix1[:,1]

fig = plt.figure()

ax1 = fig.add_subplot(111)

ax1.set_title("EEG Data")
ax1.set_xlabel('Time (minutes)')
ax1.set_ylabel('EEG Voltage (mV)')

ax1.plot(x,y, c='r', label='A-O Montage')

leg = ax1.legend()

plt.show()
plt.savefig('testplot.png')
