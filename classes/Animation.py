from pyray import *
from raylib.colors import *
from classes.Time import Time

class Animation(Time):
  def __init__(self, frames_list=None, x=0, y=0, animation_speed=30, is_looped=False, first_frame=0, last_frame=-1):
    if frames_list is None:
      frames_list = []
    super().__init__(animation_speed)
    self.x = x
    self.y = y
    self.frames: list = frames_list
    self.frames.append(self.frames[len(frames_list)-1])
    self.frame_index: int = 0
    self.first_frame: int = first_frame
    if last_frame != -1:
      self.last_frame: int = last_frame
    else:
      self.last_frame: int = len(frames_list)-1

    self.is_animation_finished: bool = False
    self.is_animation_ended: bool = False
    self.is_animation_looped: bool = is_looped

    if animation_speed != 0: self.start_time()
    self.shift_time = Time
    self.shift_add: float = animation_speed
    self.temp_loops = 0

  def update(self):
    self.update_time()
    self.check_looped()
    self.step()
    self.check_ended()
    self.finished_ended()
    self.draw()

  def check_looped(self):
    if self.frame_index >= self.last_frame and self.is_animation_looped:
      self.temp_loops += 1
    elif self.frame_index >= self.last_frame and not self.is_animation_looped:
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

  def draw(self):
    draw_texture(self.frames[self.frame_index], self.x, self.y, WHITE)
    draw_text(f"index: {self.frame_index}\nlast: {self.last_frame}\nloop: {self.temp_loops}\nended: {self.is_animation_ended}\nfinished: {self.is_animation_finished}", 0, 100, 14, WHITE)
