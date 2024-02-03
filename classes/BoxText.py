from pyray import *
from raylib.colors import *
import config

class BoxText:
  def __init__(self, text: str = "PLACEHOLDER", size: float = 30, pos: Vector2 = Vector2(0, 0), color: tuple = WHITE, spacing: float = 1, font_filename = None):
    if font_filename is None:
      self.font = load_font_ex(config.def_font_filename, size, None, 0)
    else:
      self.font = load_font(font_filename)
    self.text = text
    self.size = size
    self.pos = pos
    self.color = color
    self.spacing = spacing
    measure = measure_text_ex(self.font, self.text, self.size, 0)
    self.rec = Rectangle(self.pos.x, self.pos.y + 5, measure.x + self.spacing * len(self.text), measure.y - 10)

    self.last_verdict: bool = False


  def update(self):
    self.draw()
    if config.debug:
      self.draw_debug()

  def check_collision_mouse(self) -> bool:
    point = get_mouse_position()
    rec = self.rec
    verdict: bool

    if check_collision_point_rec(point, rec):
      self.last_verdict = True
    else:
      self.last_verdict = False

    return self.last_verdict

  def draw(self):
    draw_text_ex(self.font, self.text, self.pos, self.size, self.spacing, self.color)

  def draw_debug(self):
    rec_pos = Vector2(self.rec.x, self.rec.y)
    rec_size = Vector2(self.rec.width, self.rec.height)
    draw_rectangle_v(rec_pos, rec_size, (255, 0, 0, 153))

    x = int(self.pos.x) + int(self.rec.width) + 4
    y = int(self.pos.y) + int(self.rec.height//2) - 4
    draw_text(str(self.last_verdict), x, y, 20, WHITE)