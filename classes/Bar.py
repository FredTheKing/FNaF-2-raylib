from classes.Text import BoxText, JustText
from pyray import *
from raylib.colors import *

class SideButtons:
  def __init__(self):
    self.space = 10
    self.left_button = BoxText("<", 48, font_filename="assets/fonts/consolas.ttf")
    self.right_button = BoxText(">", 48, font_filename="assets/fonts/consolas.ttf")

    x_left = int(self.pos.x)
    x_right = int(self.pos.x) + int(self.right_button.rec.width) + int(self.size.x) + self.space * 2
    y_new = (int(self.pos.y) + int(self.size.y) // 2) - 38 // 2 - 2
    self.left_button.set_position(Vector2(x_left, y_new))
    self.right_button.set_position(Vector2(x_right, y_new))

class BarButtons(SideButtons):
  def __init__(self, pos: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(300, 30), states: int | list = 10, layer: int = 3, goes_zero: bool = True, default_state: int = None):
    self.pos = pos
    self.size = size
    self.states = states
    if default_state is None:
      self.current_state = states
    else:
      self.current_state = default_state
    self.layer_order = layer
    self.goes_zero = goes_zero

    super().__init__()

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
    rec = Rectangle(int(self.pos.x) + self.left_button.rec.width + self.space, int(self.pos.y), int(self.size.x), int(self.size.y))
    draw_rectangle_lines_ex(rec, int(self.size.y)*0.08, WHITE)

    new_space = int(self.size.y) * 0.2
    state_rec = Rectangle((int(self.pos.x) + new_space + self.left_button.rec.width + self.space), int(self.pos.y) + new_space, (int(self.size.x) - (new_space * 2)) / self.states * self.current_state,
                          int(self.size.y) - (new_space * 2))
    draw_rectangle_rec(state_rec, WHITE)


class DigitButtons(BarButtons):
  def __init__(self, pos: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(300, 30), states: int = 10, layer: int = 3, goes_zero: bool = True, default_state: int = None):
    super().__init__(pos, size, states, layer, goes_zero, default_state)
    self.text = JustText(str(self.current_state), int(size.y), Vector2((int(self.pos.x) + self.left_button.rec.width + self.space + int(size.x)) - int(self.size.x)//2, int(pos.y)))
    self.text_pos_x = self.text.pos.x

  def update(self):
    self.left_button.update()
    self.right_button.update()
    self.check_buttons()
    self.check_state()
    self.text.text = str(self.current_state)
    self.text.center_text(self.text_pos_x)
    self.draw()

  def draw(self):
    draw_text_ex(self.text.font, self.text.text, self.text.pos, self.text.fontsize, self.text.spacing, self.text.color)


class TextButtons(BarButtons):
  def __init__(self, pos: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(300, 30), states: list = ['PLACE-', '-HOLDER'], layer: int = 3, default_state: int = None):
    super().__init__(pos, size, layer=layer)
    del self.goes_zero
    self.states = states
    if default_state is None:
      self.current_state = self.states[-1]
      self.current_index = self.states.__len__()-1
    else:
      self.current_state = self.states[default_state]
      self.current_index = default_state
    self.text = JustText(self.current_state, int(size.y), Vector2((int(self.pos.x) + self.left_button.rec.width + self.space + int(size.x)) - int(self.size.x)//2, int(pos.y)))
    self.text_pos_x = self.text.pos.x

  def check_buttons(self):
    if self.left_button.clicked_verdict:
      self.current_index -= 1
    elif self.right_button.clicked_verdict:
      self.current_index += 1

  def check_state(self):
    if self.current_index < 0:
      self.current_index = self.states.__len__()-1
    if self.current_index >= self.states.__len__():
      self.current_index = 0

  def update(self):
    self.left_button.update()
    self.right_button.update()
    self.check_buttons()
    self.check_state()
    self.current_state = self.states[self.current_index]
    self.text.text = str(self.current_state)
    self.text.center_text(self.text_pos_x)
    self.draw()

  def draw(self):
    draw_text_ex(self.text.font, self.text.text, self.text.pos, self.text.fontsize, self.text.spacing, self.text.color)
