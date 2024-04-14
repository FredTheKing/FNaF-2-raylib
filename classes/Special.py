import random
import string
from pyray import *
import config
from classes.Animation import SelectableAnimation
from classes.Time import Time

class Special:
  class WhiteShhrrt:
    def __init__(self, release_path):
      def spec_load_image(filename: str, animation_subtype: bool = False) -> Texture or list[Texture]:
        if animation_subtype:
          arr = [load_texture_from_image(load_image(release_path + filename))]
          return arr
        else:
          return load_texture_from_image(load_image(release_path + filename))
      def spec_load_animation(dirname: str, times: int) -> list:
        arr = []
        for item in range(times):
          arr.append(spec_load_image(dirname + f"/{item}.png"))
        return arr

      self.item: SelectableAnimation = SelectableAnimation([
        spec_load_image('assets/graphics/Other/Static/1/white.png', True),
        spec_load_animation('assets/graphics/Other/Static/1', 5),
        spec_load_image('assets/graphics/Other/Static/1/invisible.png', True),
      ], animation_speed=50, is_looped=True)
      self.time: Time = Time(10)
      self.layer_order = self.item.layer_order

      self.go: bool = False
      self.activation_completed: bool = False
      self.white_progress: int = 0

    def check_go(self):
      if self.go and not self.activation_completed:
        self.activation_completed = True
        self.white_progress = 0
        self.item.animation_index = 0
        self.time.start_time()


    def update(self):
      self.check_go()
      self.item.update()
      self.time.update_time()
      if self.go:
        self.check_coca_cola()
      # if config.debug:
      #   self.draw_debug()

    def draw_debug(self):
      text = f"go: {int(self.go)}\nact: {int(self.activation_completed)}\ntime: {self.time.time_current}"
      draw_text(text, 700, 600, 40, RED)

    def check_coca_cola(self):
      if self.time.time_current >= 1 and self.white_progress == 0:
        self.white_progress = 1
        self.item.animation_index = 1
        self.time.start_time()
      elif self.time.time_current >= 1 and self.white_progress == 1:
        self.white_progress = 2
        self.item.animation_index = 2
        self.go = False
        self.activation_completed = False
        self.time.time_current = 0
        self.time.kill_time()

  class InvisibleAnchor:
    def __init__(self, pos: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(0, 0), layer: int = 5):
      self.pos: Vector2 = pos
      self.size: Vector2 = size
      self.layer_order: int = layer

    def draw(self):
      transparent_white = Color(255, 255, 255, 153)
      draw_rectangle_v(self.pos, self.size, transparent_white)

    def update(self):
      if config.debug:
        self.draw()

  class Animatronic:
    def __init__(self, name: str, active_cameras: list[str]):
      self.name = name or 'NaN' + str(random.choice(string.ascii_letters))
      self.difficulty = 0
      self.active_cameras = active_cameras
