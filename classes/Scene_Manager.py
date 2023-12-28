import datetime
import time

from pyray import *
from raylib.colors import *
import config

class Scene_Manager:
  def __init__(self, scenes_names: list):
    self.scene_dict = {}
    for i in range(len(scenes_names)):
      self.scene_dict[i] = scenes_names[i]
    self.scene_index = 0
    self.scene_changed = True
    self.time_start = time.time()
    self.time_current = int(time.time() - self.time_start)

  def start_time(self):
    self.time_start = time.time()

  def update_time(self):
    self.time_current = int(time.time() - self.time_start)

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
