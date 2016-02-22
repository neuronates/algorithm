#!/usr/bin/python
import kivy
import os
#kivy.require('1.4.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout

class TestCamera(App):
	def doscreenshot(self,*largs):
		Window.screenshot(name='~algorithm/UI/screenshot_save.png')
#		print os.getcwd()
#		exit()
	def build(self):
		root = FloatLayout()
		camwidget = Widget()
		cam = Camera()
		cam = Camera(resolution=(640,480),size=(500,500))
		cam.play = True
		camwidget.add_widget(cam)


		button = Button(text='screenshot',size_hint=(0.12,0.12))
		button.bind(on_press=self.doscreenshot)
		camwidget.add_widget(button)
		root.add_widget(camwidget)
		return root

if __name__ == '__main__':
	TestCamera().run()
