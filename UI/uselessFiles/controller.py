import kivy

from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

class Controller(BoxLayout):

	label_wid = ObjectProperty()
	info = StringProperty()

	def do_action(self):
		self.label_wid.text = 'My label after button press'
		self.info = 'New info text'

class ControllerApp(App):

	def build(self):
		return Controller(info='Hello world')

if __name__ == '__main__':
	ControllerApp().run()
