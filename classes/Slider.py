from classes.Text import BoxText
from pyray import *
from raylib.colors import *

class SliderButtons:
  def __init__(self, pos: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(300, 30), states: int = 10, goes_zero: bool = True):
    self.pos = pos
    self.size = size
    self.states = states
    self.current_state = states
    self.goes_zero = goes_zero

    space = 10
    self.left_button = BoxText("<", 48, font_filename="assets/fonts/consolas.ttf")
    self.right_button = BoxText(">", 48, font_filename="assets/fonts/consolas.ttf")

    x_left = int(self.pos.x) - int(self.left_button.rec.width) - space
    x_right = int(self.pos.x) + int(self.size.x) + space
    y_new = (int(self.pos.y) + int(self.size.y)//2) - 38//2 - 2
    self.left_button.set_position(Vector2(x_left, y_new))
    self.right_button.set_position(Vector2(x_right, y_new))

  def check_buttons(self):
    if self.left_button.clicked_verdict:
      self.current_state -= 1
    elif self.right_button.clicked_verdict:
      self.current_state += 1

  def check_state(self):
    if self.goes_zero:
      if self.current_state < 0:
        self.current_state = 0
    else:
      if self.current_state < 1:
        self.current_state = 1

    if self.current_state > self.states:
      self.current_state = self.states


  def update(self):
    self.left_button.update()
    self.right_button.update()
    self.check_buttons()
    self.check_state()
    self.draw()

  def draw(self):
    rec = Rectangle(int(self.pos.x), int(self.pos.y), int(self.size.x), int(self.size.y))
    draw_rectangle_lines_ex(rec, int(self.size.y)*0.08, WHITE)

    space = int(self.size.y) * 0.2
    state_rec = Rectangle((int(self.pos.x) + space), int(self.pos.y) + space, (int(self.size.x) - (space * 2)) / self.states * self.current_state,
                          int(self.size.y) - (space * 2))
    draw_rectangle_rec(state_rec, WHITE)
