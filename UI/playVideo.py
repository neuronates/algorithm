from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.video import Video
from kivy.uix.videoplayer import VideoPlayer

playVideo = Builder.load_string('''
FloatLayout:
    VideoPlayer:
        id: video
        source: 'video_demo.h264'
        size_hint: 1, 0.5
        pos: 0, self.height
        play: False
    VideoPlayer:
        id: video2
        source: 'Minions Banana Song.mp4'
        size_hint: 1, 0.5
        pos: 0, 0
        play: False
''')

class PlayVideo(App):
    def build(self):
        return playVideo

PlayVideo().run()

#
# BoxLayout:
# Button:
#     text: 'Play'
#     on_press: video.play = True
#     size_hint: .1, .1
# Button:
#     text: 'Stop'
#     on_press: video.play = False
#     size_hint: .1, .1
