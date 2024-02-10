from pyray import *
import objects
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
    self.scene_counter = 0
    self.start_time()

  def update_new_key(self, key: KeyboardKey):
    if config.key_pressed == key:
      self.set_scene(9)
      self.start_time()

  def set_scene(self, id):
    self.scene_index = id
    self.scene_changed = True
    self.scene_counter += 1
    self.start_time()
    objects.restart_animations()
    print(f'{self.scene_counter} ding!, goto {self.scene_index} and checked [{self.scene_changed}]')

  def check_changed(self):
    if self.scene_changed:
      self.scene_changed = False

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

class Sound_Manager:
  def __init__(self, scenes: Scene_Manager):
    self.channel = {}
    for item in range(scenes.scene_dict.__len__()):
      self.channel[item] = []

