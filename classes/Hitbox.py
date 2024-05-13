from pyray import *
from raylib.colors import *

class Hitbox:
  def __init__(self, pos: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(0, 0), hitbox_color: Color = RED, click_sound: Sound = None):
    self.rec = Rectangle(int(pos.x), int(pos.y), int(size.x), int(size.y))
    self.hitbox_color = hitbox_color
    self.click_sound = click_sound

    self.temp_hover: int = -1
    self.hover_verdict: bool = False
    self.hover_activation_verdict: bool = False
    self.clicked_verdict: bool = False
    self.hold_verdict: bool = False

  def reset(self):
    self.hover_verdict = False
    self.hover_activation_verdict = False
    self.clicked_verdict = False
    self.hold_verdict = False

  def hitbox_with_model(self):
    self.rec.x = self.pos.x
    self.rec.y = self.pos.y

  def update(self):
    self.check_hover_activation_interaction()
    self.check_collision_mouse()
    self.check_hold_interaction()
    self.check_click_interaction()
    self.check_hover_click_sound()
    self.hitbox_with_model()

  def check_hover_activation_interaction(self):
    point = get_mouse_position()
    rec = self.rec

    if check_collision_point_rec(point, rec) and not self.hover_verdict:
      self.hover_activation_verdict = True
    else:
      self.hover_activation_verdict = False

  def check_collision_mouse(self):
    point = get_mouse_position()
    rec = self.rec

    if check_collision_point_rec(point, rec):
      self.hover_verdict = True
    else:
      self.hover_verdict = False

  def check_hover_click_sound(self):
    if self.hover_verdict:
      if 0 <= self.temp_hover < 2:
        self.temp_hover += 1
      if self.temp_hover == 1:
        try:
          play_sound(self.click_sound)
        except TypeError:
          pass
    else:
      if self.temp_hover != -1:
        self.temp_hover = 0

  def check_click_interaction(self, mouse_button: MouseButton = MouseButton.MOUSE_BUTTON_LEFT):
    point = get_mouse_position()
    rec = self.rec
    button = mouse_button

    if check_collision_point_rec(point, rec) and is_mouse_button_pressed(button):
      self.clicked_verdict = True
      try:
        play_sound(self.click_sound)
      except TypeError:
        pass
    else:
      self.clicked_verdict = False

  def check_hold_interaction(self, mouse_button: MouseButton = MouseButton.MOUSE_BUTTON_LEFT):
    point = get_mouse_position()
    rec = self.rec
    button = mouse_button

    half_verdict = check_collision_point_rec(point, rec) and is_mouse_button_down(button)
    if self.clicked_verdict and not self.hold_verdict and half_verdict:
      self.hold_verdict = True
    elif self.hold_verdict and not half_verdict:
      self.hold_verdict = False

  def draw_debug(self):
    rec_pos = Vector2(self.rec.x, self.rec.y)
    rec_size = Vector2(self.rec.width, self.rec.height)
    color = self.hitbox_color
    draw_rectangle_v(rec_pos, rec_size, (color[0], color[1], color[2], 100))
    draw_rectangle_v(Vector2(self.rec.x-2, self.rec.y-2), Vector2(4, 4), BLUE)

    x = int(self.pos.x) + int(self.rec.width) + 4
    y = int(self.pos.y) + int(self.rec.height // 2) - 4
    draw_text(f'{int(self.hover_verdict)}; {int(self.hover_activation_verdict)}; {int(self.clicked_verdict)}; {int(self.hold_verdict)}', x, y, 20, WHITE)
