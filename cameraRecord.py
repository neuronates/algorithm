from kivy.app import App
from kivy.lang import Builder

kv = '''
BoxLayout:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (800, 480)
        play: False
    ToggleButton:
        text: 'Record'
        on_press: camera.play = not camera.play
        size_hint_y: 0.1
'''


class TestCamera(App):
    def build(self):
        return Builder.load_string(kv)

TestCamera().run()
