import config
from classes.Hitbox import Hitbox
from pyray import *
from raylib.colors import *

class Checkbox(Hitbox):
  def __init__(self, pos: Vector2 = Vector2(0, 0), size: int = 30, layer: int = 3, auto_changing: bool = True):
    self.pos = pos
    self.size = size
    self.state: bool = False
    self.layer_order = layer
    self.auto_changing: bool = auto_changing
    super().__init__(pos, Vector2(size, size), YELLOW, config.def_set_sound)

  def check_state(self):
    if self.clicked_verdict:
      if self.auto_changing:
        self.state ^= 1
        self.reset()

  def update(self):
    Hitbox.update(self)
    self.check_state()
    self.draw()
    if config.debug:
      self.draw_debug()

  def draw(self):
    rec = Rectangle(int(self.pos.x), int(self.pos.y), self.size, self.size)
    draw_rectangle_lines_ex(rec, self.size*0.1, WHITE)

    if self.state:
      space = self.size * 0.2
      state_rec = Rectangle(int(self.pos.x) + space, int(self.pos.y) + space, self.size - (space*2), self.size - (space*2))
      draw_rectangle_rec(state_rec, WHITE)
