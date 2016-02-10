import kivy

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout

class Main(BoxLayout):
	pass
load_screen = Builder.load_string('''
<Main>:
	Label: 
		text: 'Neonatal EEG Monitoring System'
		font_size: 50
''')

class myApp(App):
	def build(self):
		return load_screen

myApp().run()
