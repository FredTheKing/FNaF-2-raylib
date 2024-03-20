from pyray import *

class JustSound:
  def __init__(self, audio: Sound, is_looped: bool = False):
    self.audio: Sound = audio
    self.go_play: int = 0
    self.is_looped = is_looped

  def play(self):
    self.go_play = 1

  def stop(self):
    self.go_play = 0

  def check_playing(self):
    if self.go_play == 1:
      if not is_sound_playing(self.audio):
        if not self.is_looped:
          play_sound(self.audio)
          self.go_play = 2
        else:
          play_sound(self.audio)

    if not self.go_play:
      stop_sound(self.audio)


  def update(self):
    self.check_playing()
