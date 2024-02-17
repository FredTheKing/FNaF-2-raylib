from pyray import *
from raylib.colors import *

class Hitbox:
  def __init__(self, pos: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(0, 0), hitbox_color: Color = RED):
    self.rec = Rectangle(int(pos.x), int(pos.y), int(size.x), int(size.y))
    self.hitbox_color = hitbox_color

    self.hover_verdict: bool = False
    self.clicked_verdict: bool = False

  def reset(self):
    self.hover_verdict = False
    self.clicked_verdict = False

  def check_collision_mouse(self):
    point = get_mouse_position()
    rec = self.rec

    if check_collision_point_rec(point, rec):
      self.hover_verdict = True
    else:
      self.hover_verdict = False

  def check_mouse_interaction(self, mouse_button: MouseButton = MouseButton.MOUSE_BUTTON_LEFT):
    point = get_mouse_position()
    rec = self.rec
    button = mouse_button

    if check_collision_point_rec(point, rec) and is_mouse_button_pressed(button):
      self.clicked_verdict = True
    else:
      self.clicked_verdict = False

  def draw_debug(self):
    rec_pos = Vector2(self.rec.x, self.rec.y)
    rec_size = Vector2(self.rec.width, self.rec.height)
    color = self.hitbox_color
    draw_rectangle_v(rec_pos, rec_size, (color[0], color[1], color[2], 100))

    x = int(self.pos.x) + int(self.rec.width) + 4
    y = int(self.pos.y) + int(self.rec.height // 2) - 4
    draw_text(f'{int(self.hover_verdict)}; {int(self.clicked_verdict)}', x, y, 20, WHITE)
