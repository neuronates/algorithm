#!/usr/bin/python
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot

graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5, 
x_ticks_major=25, y_ticks_major=1,
y_grid_label=True, x_grid_label=True, padding=5,
x_grid=True, y_grid=True, xmin =-0, xmax=100, ymin=-1, ymax=1)
plot = MeshLinePlot(color=[1,0,0,1])
plot.points=  [(x,sin(x/10.)) for x in range (0,101)]
graph.add_plot(plot)

"""
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
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
"""
