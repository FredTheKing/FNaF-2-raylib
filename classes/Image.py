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

  def resize(self, new_size: Vector2):
    image = load_image_from_texture(self.texture)
    image_resize(image, int(new_size.x), int(new_size.y))
    self.texture = load_texture_from_image(image)

  def update(self):
    self.draw()

  def draw(self):
    draw_texture_v(self.texture, self.pos, self.color)

class BorderImage(JustImage):
  def __init__(self, texture: Texture, pos: Vector2 = Vector2(0, 0), border_thick:int = 2, alpha: int = 255):
    super().__init__(texture, pos, alpha)
    self.border_thick = border_thick

  def update(self):
    JustImage.update(self)
    draw_rectangle_lines_ex(Rectangle(int(self.pos.x), int(self.pos.y), int(self.texture.width), int(self.texture.height)), self.border_thick, WHITE)

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
