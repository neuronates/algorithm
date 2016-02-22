#!/usr/bin/python
import matplotlib
from kivy.uix.boxlayout import BoxLayout
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
from kivy.uix.button import Button
import math

dataMatrix1 = genfromtxt('DemoEEGFile.txt')

x = dataMatrix1[:,0]
y = dataMatrix1[:,1]
xmin = math.trunc(x[0])
ymin = math.trunc(min(y))#math.trunc(y[0])
xmax = xmin+1
#xmax = math.trunc(x[len(x)-1])
ymax = math.trunc(max(y))#math.trunc(y[len(y)-1])


class kivyPlotApp(App):
	def build(self):
		root = FloatLayout(orientation='horizontal')
		btnRight = Button(text='Scroll', size_hint=(.05,1),pos_hint={'right':1})#,'y':0})
		btnLeft = Button(text='Scroll', size_hint=(.05,1),pos_hint={'left':1})			
		root.add_widget(btnRight)
		root.add_widget(btnLeft)
#		scrollV = ScrollView(size_hint=(None,None),size=(800,400))
#		scrollV.do_scroll_y=False
		graph = Graph()
		plot = LinePlot(mode='line_strip', color=[1,0,0,1])
		plot.points = [(x[i],y[i]) for i in xrange(len(x))]
		graph.add_plot(plot)
		graph.x_ticks_major=1
		graph.xmin=xmin
		graph.xmax=xmax
		graph.ymin=ymin
		graph.ymax=ymax
		graph.y_ticks_major=25
		graph.y_grid_label=True
		graph.x_grid_label=True
		graph.xlabel='X axis'
		graph.ylabel='Y axis'
		graph.y_grid = True
		graph.x_grid = True
		def moveRight(obj):
			global xmin
			global xmax
			xmin=xmin+.5
			xmax=xmax+.5
			graph.xmin=xmin
			graph.xmax=xmax
			#graph.remove_plot(plot)
			#graph.add_plot(plot)
			#graph._redraw_size(xmin,ymin,xmax,ymax)
		btnRight.bind(on_release=moveRight)
		def moveLeft(obj):
			global xmin
			global xmax
			xmin=xmin-.5
			xmax=xmax-.5
			graph.xmin=xmin
			graph.xmax=xmax
		btnLeft.bind(on_release=moveLeft)
		root.add_widget(graph)
#		graph.bind(minimum_height=graph.setter('height'))
#		scrollV.add_widget(graph)
		return root

if __name__ == '__main__':
	kivyPlotApp().run()

