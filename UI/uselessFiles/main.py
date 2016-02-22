from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ListProperty

#class CustomDropDown(DropDown):
#	dropdown = DropDown()
#	for index in range(10):
#		btn = Button(text='Value %d' % index, size_hint_y=None, height=44)
#		btn.bind(on_release=lambda btn: dropdown.select(btn.text))
#		dropdown.add_widget(btn)
#	mainbutton = Button(text='hello', size_hint=(None,None))
#	mainbutton.bind(on_release=dropdown.open)
#	dropdown.bind(on_select=lambda instance, x: setattr(mainbutton,'text',x))

class HomeScreen(FloatLayout):
	pass

load_screen = Builder.load_string('''

<HomeScreen>:
	FloatLayout:
		Label:
			text: 'Hello'
		BoxLayout:		
			Button:
				text: 'Neonatal EEG'
			#	font_size: 50
''')

class myApp(App):
	def build(self):
		return load_screen
myApp().run()
