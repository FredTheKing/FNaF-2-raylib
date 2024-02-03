from pyray import *
from classes.Time import Time
import config

class Scene_Manager(Time):
  def __init__(self, scenes_names: list):
    super().__init__(1)
    self.scene_dict = {}
    for i in range(len(scenes_names)):
      self.scene_dict[i] = scenes_names[i]
    self.scene_index = 9
    self.scene_changed = True

  def update_new_key(self, key: KeyboardKey):
    if config.key_pressed == key:
      self.scene_index = 9
      self.scene_changed = True
      self.start_time()

  def set_scene(self, id):
    self.scene_index = id
    self.scene_changed = True
    print('ding!')

  def check_input(self):
    keys_arr = [
      KeyboardKey.KEY_ZERO,
      KeyboardKey.KEY_TWO,
      KeyboardKey.KEY_THREE,
      None,
      None,
      KeyboardKey.KEY_ONE,
    ]

    for i in range(len(keys_arr)):
      if keys_arr[i] is not None:
        if config.key_pressed == keys_arr[i]:
          self.set_scene(i)
          break
    else:
      self.scene_changed = False

class Sound_Manager:
  def __init__(self, scenes: Scene_Manager):
    self.channel = {}
    for item in range(scenes.scene_dict.__len__()):
      self.channel[item] = []

