from pyray import *
from raylib.colors import *
import config

class Animation:
  def __init__(self, frames_list=None, x=0, y=0, animation_speed=30, is_looped=False, first_frame=0, last_frame=-1):
    if frames_list is None:
      frames_list = []
    self.x = x
    self.y = y
    self.frames: list = frames_list
    self.frame_index: int = 0
    self.animation_speed: int = animation_speed
    self.first_frame: int = first_frame
    if last_frame != -1:
      self.last_frame: int = last_frame
    else:
      self.last_frame: int = len(frames_list)-1

    self.is_animation_finished: bool = False
    self.is_animation_ended: bool = False
    self.is_animation_looped: bool = is_looped

  def update(self):
    self.check_ended()
    self.finished_ended()
    self.check_looped()
    self.step()
    self.draw()

  def check_looped(self):
    if self.frame_index >= self.last_frame+1:
      self.frame_index = self.first_frame

  def check_ended(self):
    if self.frame_index >= self.last_frame+1:
      self.is_animation_ended = True
    else:
      self.is_animation_ended = False

  def finished_ended(self):
    if self.frame_index >= self.last_frame+1 and not self.is_animation_looped:
      self.is_animation_finished = True
    else:
      self.is_animation_finished = False

  def step(self):
    pass

  def draw(self):
    draw_texture(self.frames[self.frame_index], self.x, self.y, WHITE)
