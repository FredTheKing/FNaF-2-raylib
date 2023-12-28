from pyray import *
from classes.Time import Time
import config

class Scene_Manager(Time):
  def __init__(self, scenes_names: list):
    super().__init__(1)
    self.scene_dict = {}
    for i in range(len(scenes_names)):
      self.scene_dict[i] = scenes_names[i]
    self.scene_index = 0
    self.scene_changed = True

  def check_input(self):
    keys_arr = [
      KeyboardKey.KEY_ZERO,
      KeyboardKey.KEY_TWO,
      KeyboardKey.KEY_THREE,
      None,
      None,
      KeyboardKey.KEY_ONE,
      None,
      None,
      None
    ]

    for i in range(len(keys_arr)):
      if keys_arr[i] is not None:
        if config.key_pressed == keys_arr[i]:
          self.scene_index = i
          self.scene_changed = True
          break
    else:
      self.scene_changed = False
