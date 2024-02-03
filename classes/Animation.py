from pyray import *
from raylib.colors import *
from classes.Time import Time

class Smart_Animation(Time):
  def __init__(self, frames_list=None, pos=Vector2(0, 0), animation_speed=5, is_looped=False, alpha=255, first_frame=0):
    if frames_list is None:
      frames_list = []
    super().__init__(animation_speed)
    self.pos = pos
    self.frames: list = frames_list
    if is_looped:
      self.frames.append(self.frames[len(frames_list)-1])
    self.frame_index: int = 0
    self.first_frame: int = first_frame
    self.last_frame: int = len(frames_list)-1
    self.color = [255, 255, 255, alpha]

    self.is_animation_finished: bool = False
    self.is_animation_ended: bool = False
    self.is_animation_looped: bool = is_looped

    if animation_speed != 0:
      self.start_time()
    self.temp_loops: int = 0

  def update(self):
    if self.is_animation_looped:
      self.check_looped()
    if self.go:
      self.update_time()
      self.step()
    self.check_ended()
    self.finished_ended()
    self.draw()

  def check_looped(self):
    if self.frame_index == self.last_frame and self.is_animation_looped:
      self.temp_loops += 1
    elif self.frame_index == self.last_frame and not self.is_animation_looped:
      self.kill_time()

  def check_ended(self):
    if self.frame_index >= self.last_frame:
      self.is_animation_ended = True
    else:
      self.is_animation_ended = False

  def finished_ended(self):
    if self.frame_index >= self.last_frame and not self.is_animation_looped:
      self.is_animation_finished = True
    else:
      self.is_animation_finished = False

  def step(self):
    if self.go:
      self.frame_index = self.time_current - self.temp_loops * self.last_frame

  def restart(self):
    self.frame_index = 0
    self.go = True
    self.is_animation_finished = False
    self.is_animation_ended = False

  def draw(self):
    if self.frame_index <= self.last_frame:
      draw_texture_v(self.frames[self.frame_index], self.pos, self.color)
    else:
      self.frame_index = self.last_frame
      draw_texture_v(self.frames[self.frame_index], self.pos, self.color)

  def draw_debug(self, name, x, y):
    draw_text(
      f"name: {name}\nstarted: {self.go}\n\nindex: {self.frame_index}\nlast: {self.last_frame}\nloop: {self.temp_loops}\nended: {self.is_animation_ended}\nfinished: {self.is_animation_finished}", x, y, 14, WHITE)
