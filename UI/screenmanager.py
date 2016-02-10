from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class HomeScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass


load_screen = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:
    transition: FadeTransition()
    HomeScreen:
    SecondScreen:
    FirstScreen:
    ThirdScreen:

<HomeScreen>:
    name: 'Home'
    FloatLayout:
        Label:
            text: 'Neonatal EEG Monitoring System'
            font_size: 50
        BoxLayout:
            Button:
                text: 'Home'
                size_hint: .1, .1
                on_release: app.root.current = 'Home'
            Button:
                text: 'Run'
                size_hint: .1, .1
                on_release: app.root.current = 'First'
            Button:
                text: 'Review Data'
                size_hint: .1, .1
                on_release: app.root.current = 'Third'
<SecondScreen>:
    name: 'Second'
    FloatLayout:
<FirstScreen>:
    name: 'First'
    FloatLayout:
	Label: 
		text: 'Patient Name'
		pos_hint: {'x':0.2,'y':0.3}
		size_hint: .1,.1

	TextInput:
		id: name
		multiline: False
		size_hint: .3,.1
		pos_hint: {'x':0.5,'y':0.3}
	Label:
		text: 'Date'
		pos_hint: {'x':0.2,'y':0.7}
		size_hint: .1,.1
	TextInput:
		id: date
		multiline: False
		size_hint: .3,.1
		pos_hint: {'x':0.5,'y':0.7}
    FloatLayout:
        BoxLayout:
            Button:
                text: 'Home'
                size_hint: .1, .1
                on_release: app.root.current = 'Home'
            Button:
                text: 'Back'
                size_hint: .1, .1
                on_release: app.root.current = 'Home'
            Button:
                text: 'Next'
                size_hint: .1, .1
#		on_release: app.root.current = 'Second'
#    FloatLayout:
#	BoxLayout:
#	    Button:
#		text: 'Home'
#		size_hint: .1,.1
#		on_release: app.root.current = 'Home'
 #  	    Button:
#		text: 'Back'
#		size_hint: .1,.1
#		on_release: app.root.current = 'First'
		
<ThirdScreen>:
    name: 'Third'
    FloatLayout:
        Image:
            source: 'testplot.png'
            size_hint: 1, 1
            allow_stretch: True
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'Home'
                size_hint: .1, .1
                on_release: app.root.current = 'Home'
            Button:
                text: 'Back'
                size_hint: .1, .1
                on_release: app.root.current = 'First'
            Button:
                text: 'Next'
                size_hint: .1, .1
                on_release: app.root.current = 'Second'
''')

class ScreenManagerApp(App):

    def build(self):
        return load_screen

ScreenManagerApp().run()
