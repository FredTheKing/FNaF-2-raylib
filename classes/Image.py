from pyray import *
import config
from classes.Hitbox import Hitbox

class JustImage:
  def __init__(self, texture: Texture, pos=Vector2(0, 0), alpha=255):
    self.texture = texture
    self.width = self.texture.width
    self.height = self.texture.height
    self.pos = pos
    self.color = [255, 255, 255, alpha]

  def update(self):
    self.draw()

  def draw(self):
    draw_texture_v(self.texture, self.pos, self.color)

class BoxImage(JustImage, Hitbox):
  def __init__(self, texture: Texture, pos=Vector2(0, 0), alpha=255):
    JustImage.__init__(self, texture, pos, alpha)
    Hitbox.__init__(self, pos, Vector2(self.width, self.height), BROWN)

  def update(self):
    self.check_collision_mouse()
    self.check_mouse_interaction()
    JustImage.update(self)
    if config.debug:
      self.draw_debug()
