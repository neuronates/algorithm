from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

class MainApp(App):
	def build(self):
		root = BoxLayout(orientation='vertical')
		clearbtn = Button(text='clear')
		root.add_widget(clearbtn)

class RootWidget(BoxLayout):
	pass

if __name__ == '__main__':
	MainApp().run
