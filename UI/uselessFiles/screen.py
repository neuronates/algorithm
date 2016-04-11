import kivy
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

class MyScreenManager(ScreenManager):
    pass

class ScreenManagerApp(App):

    def build(self):
        return screenmanager()

ScreenManagerApp().run()
