from pyray import *

class Image:
  def __init__(self, filename: str, pos=Vector2(0, 0)):
    self.texture = load_texture_from_image(load_image(filename))
    self.width = self.texture.width
    self.height = self.texture.height
    self.pos = pos

  def draw(self):
    draw_texture_v(self.texture, self.pos, WHITE)
