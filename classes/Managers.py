from pyray import *
import objects
from classes.Time import Time
import config

class Scene_Manager(Time):
  def __init__(self, scenes_names: list):
    super().__init__(1)
    self.scene_list = []
    for item in scenes_names:
      self.scene_list.append(item)
    self.scene_index = 10
    self.scene_changed: int = 1
    self.scene_counter = 0
    self.start_time()

  def set_scene(self, id: str):
    try:
      a = int(id)
      self.scene_index = a
    except ValueError:
      a = self.scene_list.index(id)
      self.scene_index = a
    self.scene_changed = 2
    self.scene_counter += 1
    self.start_time()
    objects.restart_animations()
    if config.debug:
      is_changed: str = "IS"
      if not self.scene_changed:
        is_changed = is_changed.lower()
        is_changed += " NOT"
      print(f'scene DING! (for {self.scene_counter} time), goto "{str(self.scene_list[self.scene_index]).upper()}" ({self.scene_index}) and {is_changed} changed')

  def check_changed(self):
    if self.scene_changed:
      self.scene_changed -= 1

  def check_input(self):
    keys_arr = [
      KeyboardKey.KEY_ZERO,
      KeyboardKey.KEY_ONE,
      KeyboardKey.KEY_TWO,
      KeyboardKey.KEY_THREE,
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      None,
      KeyboardKey.KEY_NINE,
      None,
    ]

    for i in range(len(keys_arr)):
      if keys_arr[i] is not None:
        if config.key_pressed == keys_arr[i]:
          self.set_scene(i)
          break

class Sound_Manager:
  def __init__(self, scenes: Scene_Manager):
    self.channel = {}
    for item in range(scenes.scene_list.__len__()):
      self.channel[item] = []

