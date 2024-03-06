from pyray import *
from raylib.colors import *
from classes.Time import Time

class JustAnimation(Time):
  def __init__(self, frames_list=None, pos=Vector2(0, 0), animation_speed=5, is_looped=False, alpha=255, layer: int = 0, first_frame=0):
    if frames_list is None:
      frames_list = []
    super().__init__(animation_speed)
    self.pos = pos
    self.frames: list = frames_list
    if is_looped:
      self.frames.append(self.frames[-1])
    self.frame_index: int = 0
    self.first_frame: int = first_frame
    self.last_frame: int = len(frames_list)-1
    self.color = [255, 255, 255, alpha]
    self.layer_order = layer

    self.is_animation_finished: bool = False
    self.is_animation_ended: bool = False
    self.is_animation_looped: bool = is_looped

    if animation_speed != 0:
      self.start_time()
    self.debug_message: str = None
    self.temp_loops: int = 0

  def resize(self, new_size: Vector2):
    arr = []
    for item in self.frames:
      image = load_image_from_texture(item)
      image_resize(image, int(new_size.x), int(new_size.y))
      arr.append(load_texture_from_image(image))
    self.frames = arr

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

  def restart(self):
    self.frame_index = 0
    self.go = True
    self.is_animation_finished = False
    self.is_animation_ended = False
    self.temp_loops = 0
    self.start_time()

  def step(self):
    if self.go:
      self.frame_index = self.time_current - self.temp_loops * self.last_frame

  def draw(self):
    if self.frame_index <= self.last_frame:
      draw_texture_v(self.frames[self.frame_index], self.pos, self.color)
    else:
      self.frame_index = self.last_frame
      draw_texture_v(self.frames[self.frame_index], self.pos, self.color)

  def draw_debug(self, name, x, y):
    self.debug_message = f"name: {name}\nstarted: {self.go}\n\nindex: {self.frame_index}\nlast: {self.last_frame}\nis_looped: {self.is_animation_looped}\nloop: {self.temp_loops}\nended: {self.is_animation_ended}\nfinished: {self.is_animation_finished}"
    draw_text(self.debug_message, x, y, 10, WHITE)


class SelectableAnimation(JustAnimation):
  def __init__(self, animations_list_init_frames_list=None, pos=Vector2(0, 0), animation_speed=5, is_looped=False, alpha=255, layer: int = 0, first_frame=0):
    if animations_list_init_frames_list is None:
      self.animations_list = []
    else:
      self.animations_list = animations_list_init_frames_list

    super().__init__(self.animations_list[0], pos, animation_speed, is_looped, alpha, layer, first_frame)
    self.animation_index = 0

  def resize(self, new_size: Vector2):
    for index in range(self.animations_list.__len__()):
      arr = []
      for item in self.animations_list[index]:
        image = load_image_from_texture(item)
        image_resize(image, int(new_size.x), int(new_size.y))
        arr.append(load_texture_from_image(image))
      self.animations_list[index] = arr

  def change_current_animation(self):
    if self.frames is not self.animations_list[self.animation_index]:
      self.restart()
    self.frames = self.animations_list[self.animation_index]
    self.last_frame = len(self.frames)-1

  def update(self):
    self.change_current_animation()
    if self.is_animation_looped:
      self.check_looped()
    if self.go:
      self.update_time()
      self.step()
    self.check_ended()
    self.finished_ended()
    self.draw()
