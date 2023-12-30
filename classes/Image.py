from pyray import *
import config

class Image_:
  def __init__(self, filename: str, pos=Vector2(0, 0), alpha=255):
    self.texture = load_texture_from_image(load_image(filename))
    self.width = self.texture.width
    self.height = self.texture.height
    self.pos = pos
    self.color = [255, 255, 255, alpha]

  def update(self):
    self.draw()

  def draw(self):
    draw_texture_v(self.texture, self.pos, self.color)

  def check_collision_mouse(self):
    point = config.mouse
    rec = Rectangle(self.pos.x, self.pos.y, self.width, self.height)
    verdict: bool

    if check_collision_point_rec(point, rec):
      verdict = True
    else:
      verdict = False

    draw_text(str(verdict), 500, 0, 14, WHITE)
    return verdict
