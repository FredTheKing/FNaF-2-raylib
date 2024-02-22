from pyray import *
from raylib.colors import *
import objects
from classes.Hitbox import Hitbox
import config
from webbrowser import open

class JustText:
  def __init__(self, text: str = "PLACEHOLDER", size: float = 30, pos: Vector2 = Vector2(0, 0), color: list = WHITE, spacing: float = 0, font_filename = None):
    if font_filename is None:
      self.font = load_font_ex(objects.release_path + config.def_font_filename, size, None, 0)
    else:
      self.font = load_font_ex(objects.release_path + font_filename, size, None, 0)
    self.text = text
    self.fontsize = size
    self.pos = pos
    self.color = color
    self.spacing = spacing

  def update(self):
    self.draw()

  def center_text(self, anchor_point: int = 1024//2):
    measure = measure_text(self.text, self.fontsize)
    self.pos.x = anchor_point - measure//2

  def draw(self):
    draw_text_ex(self.font, self.text, self.pos, self.fontsize, self.spacing, self.color)

class BoxText(JustText, Hitbox):
  def __init__(self, text: str = "PLACEHOLDER", size: float = 30, pos: Vector2 = Vector2(0, 0), color: tuple = WHITE, spacing: float = 0, font_filename = None):
    JustText.__init__(self, text, size, pos, color, spacing, font_filename)
    measure = measure_text_ex(self.font, self.text, self.fontsize, 0)
    Hitbox.__init__(self, Vector2(int(self.pos.x), int(self.pos.y) + 5), Vector2(int(measure.x) + self.spacing * self.text.__len__() - self.spacing, int(measure.y) - 10))

  def set_position(self, pos: Vector2):
    self.pos = pos
    self.rec.x = pos.x
    self.rec.y = pos.y

  def update(self):
    self.check_collision_mouse()
    self.check_mouse_interaction()
    JustText.update(self)
    if config.debug:
      self.draw_debug()

class LinkText(BoxText):
  def __init__(self, link: str = "https://link.here", text: str = "PLACEHOLDER", size: float = 30, pos: Vector2 = Vector2(0, 0), color: tuple = WHITE, spacing: float = 0, font_filename = None):
    super().__init__(text, size, pos, color, spacing, font_filename)
    self.hitbox_color = BLUE
    self.link = link

  def update(self):
    self.goto_link()
    BoxText.update(self)

  def goto_link(self):
    if self.clicked_verdict:
      open(f'{self.link}')
