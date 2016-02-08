from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class HomeScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
    pass

load_screen = Builder.load_string('''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition

MyScreenManager:
    transition: FadeTransition()
    HomeScreen:
    FirstScreen:
    SecondScreen:

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
                on_release: app.root.current = 'Second'
<FirstScreen>:
    name: 'First'
    FloatLayout:
        Image:
            source: 'testplot.png'
            size_hint: 1, 50
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
<SecondScreen>:
    name: 'Second'
    FloatLayout:
        Image:
            source: 'EEG_baby.jpg'
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
