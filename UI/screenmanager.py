from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.camera import Camera
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from numpy import *
from functools import partial

with open('patientData.txt','r') as f:
    data=f.read()
data = data.splitlines()

num_lines = sum(1 for line in open('patientData.txt'))

class HomeScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class ThirdScreen(Screen):
#    def saveName(self,name, *args):
#        f = open('choosePatient.txt','w')
#        f.write(name + '\n')
#        f.close()

    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1,spacing=10,size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(num_lines):
            btn = Button(text=data[i],size_hint_y=None,height=40)
            btn.bind(on_release=partial(self.saveName,data[i]))
            layout.add_widget(btn)
        root = ScrollView(size_hint=(None,None),size=(400,400),pos_hint={'Center_x':.5, 'Center_y':.5})
        root.add_widget(layout)
        self.add_widget(root)
    def saveName(self,name, *args):
        f = open('choosePatient.txt','w')
        f.write(name + '\n')
        f.close()


class FourthScreen(Screen):
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
    FourthScreen:
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
#	Camera:
#	    id: camera
#	    resolution: (640,480)
#	    play: False
	Label:
	    text: 'Neonatal EEG Monitoring System'
	BoxLayout:
	    Button:
	    	text: 'Home'
    		size_hint: .1,.1
    		on_release: app.root.current = 'Home'
	    Button: 
	    	text: 'Run EEG System'
	    	size_hint: .1,.1
<FirstScreen>:
    name: 'First'
    FloatLayout:
	Label: 
		text: 'Patient Name'
		pos_hint: {'x':0.2,'y':0.3}
		size_hint: .1,.1

	TextInput:
		id: name_input
		multiline: False
		size_hint: .3,.1
		pos_hint: {'x':0.5,'y':0.3}
	Label:
		text: 'Date'
		pos_hint: {'x':0.2,'y':0.7}
		size_hint: .1,.1
	TextInput:
		id: date_input
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
    	        on_release: app.root.current = 'Second'
                on_release: app.save(name_input.text, date_input.text)
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
    		on_release: app.root.current = 'Fourth'
<FourthScreen>:
    name: 'Fourth'
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
                on_release: app.root.current = 'Third'
            #Button:
            #    text: 'Next'
            #    size_hint: .1, .1
            #    on_release: app.root.current = 'Second'
''')

class ScreenManagerApp(App):

    def build(self):
        layout = GridLayout(cols=1,spacing=10,size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        for i in range(30):
            btn = Button(text=str(i),size_hint_y=None,height=40)
            layout.add_widget(btn)
        root = ScrollView(size_hint=(None,None),size=(400,400),pos_hint={'center_x':.5, 'center_y':.5})
        return load_screen
    
    def save(self, name, date):
	f = open('patientData.txt','a')
	f.write(name + ' ')
	f.write(date + '\n')
	f.close()
    def saveName(self,name):
        f = open('choosePatient.txt','w')
        f.write(name)
        f.close()

ScreenManagerApp().run()
