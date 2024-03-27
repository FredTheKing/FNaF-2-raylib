from pyray import *
import config
from classes.Hitbox import Hitbox

class JustImage:
  def __init__(self, texture: Texture, pos=Vector2(0, 0), layer: int = 1, alpha: int = 255):
    self.texture = texture
    self.width = self.texture.width
    self.height = self.texture.height
    self.pos = pos
    self.color = [255, 255, 255, alpha]
    self.layer_order = layer

  def resize(self, new_size: Vector2):
    image = load_image_from_texture(self.texture)
    image_resize(image, int(new_size.x), int(new_size.y))
    self.texture = load_texture_from_image(image)

  def update(self):
    self.draw()

  def draw(self):
    draw_texture_v(self.texture, self.pos, self.color)

class BorderImage(JustImage):
  def __init__(self, texture: Texture, pos: Vector2 = Vector2(0, 0), border_thick:int = 2, layer: int = 1, alpha: int = 255):
    super().__init__(texture, pos, layer, alpha)
    self.border_thick = border_thick

  def update(self):
    JustImage.update(self)
    draw_rectangle_lines_ex(Rectangle(int(self.pos.x), int(self.pos.y), int(self.texture.width), int(self.texture.height)), self.border_thick, WHITE)

class BoxImage(JustImage, Hitbox):
  def __init__(self, texture: Texture, pos=Vector2(0, 0), layer: int = 1, alpha=255):
    JustImage.__init__(self, texture, pos, layer, alpha)
    Hitbox.__init__(self, pos, Vector2(self.width, self.height), BROWN)

  def update(self):
    Hitbox.update(self)
    JustImage.update(self)
    if config.debug:
      self.draw_debug()

class SelectableImage(JustImage):
  def __init__(self, textures_list_init=None, pos: Vector2 = Vector2(0, 0), layer: int = 1, alpha: int = 255):
    if textures_list_init is None:
      self.textures_list = []
    else:
      self.textures_list = textures_list_init
    self.texture_index = 0

    super().__init__(self.textures_list[0], pos, layer, alpha)

  def resize(self, new_size: Vector2):
    for index in range(self.textures_list.__len__()):
      image = load_image_from_texture(self.textures_list[index])
      image_resize(image, int(new_size.x), int(new_size.y))
      self.textures_list[index] = load_texture_from_image(image)

  def change_current_texture(self):
    self.texture = self.textures_list[self.texture_index]

  def update(self):
    self.change_current_texture()
    JustImage.update(self)
