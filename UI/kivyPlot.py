#!/usr/bin/python
import matplotlib
matplotlib.use('Agg')
from pylab import *
import pylab as pl
from math import sin
from kivy.garden.graph import Graph, LinePlot
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import *
import numpy as np
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView

dataMatrix1 = genfromtxt('DemoEEGFile.txt')

x = dataMatrix1[:,0]
y = dataMatrix1[:,1]

class kivyPlotApp(App):
	def build(self):
		scrollV = ScrollView(size_hint=(None,None),size=(800,400))
		scrollV.do_scroll_y=False
		graph = Graph()
		plot = LinePlot(mode='line_strip', color=[1,0,0,1])
		plot.points = [(x[i],y[i]) for i in xrange(len(x))]
		graph.add_plot(plot)
		graph.x_ticks_major=1
		graph.xmin=5
		graph.xmax=7
		graph.ymin=3800
		graph.ymax=3880
		graph.y_ticks_major=25
		graph.y_grid_label=True
		graph.x_grid_label=True
		graph.xlabel='X axis'
		graph.ylabel='Y axis'
		graph.y_grid = True
		graph.x_grid = True
#		graph.bind(minimum_height=graph.setter('height'))
		scrollV.add_widget(graph)
		return scrollV

if __name__ == '__main__':
	kivyPlotApp().run()

