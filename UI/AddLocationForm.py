from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class textScreen(GridLayout):
	pass

kivywidget = Builder.load_string('''
<textScreen>:
	GridLayout:
		Label:
			text: 'What do you want to print?'
		TextInput:
''')

class MyApp(App):
	def build(self):
		return kivywidget


#class kivywidget(GridLayout):
#
#	def __init__(self, **kwargs):
#		super(kivywidget,self).__init__(**kwargs)
#		self.cols = 2
#		self.add_widget(Label(text='What do you want to print?'))
#		self.text_input = TextInput(multiline=False)
#		self.add_widget(self.text_input)
#
#class MyApp(App):
#	def build(self):
#		return kivywidget()
#
if __name__ == '__main__':
	MyApp().run()

