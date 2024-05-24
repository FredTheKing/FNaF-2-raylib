from pyray import *

class JustSound:
  def __init__(self, audio: Sound, is_looped: bool = False):
    self.audio: Sound = audio
    self.played_once: bool = False
    self.start_sound: bool = False
    self.is_looped = is_looped
    self.debug_message: str = None

  def play(self):
    self.start_sound = True

  def stop(self):
    stop_sound(self.audio)
    self.start_sound = False
    self.played_once = False
    self.holding = [0, 0]

  def check_playing(self):
    if self.start_sound:
      if self.is_looped:
        if not is_sound_playing(self.audio):
          play_sound(self.audio)
      elif not self.is_looped and not self.played_once:
        play_sound(self.audio)
        self.played_once = True


  def update(self):
    self.check_playing()


  def draw_debug(self, name, group, x, y):
    self.debug_message = f"name: {name}\ngroup: {group}\n\nstart_sound: {self.start_sound}\nplayed_once: {self.played_once}\nis_looped: {self.is_looped}\n-------------------"
    draw_text(self.debug_message, x, y, 10, (255, 255, 255, 100))
