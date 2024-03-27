from pyray import *
import objects
from classes.Time import Time
import config

class Scene_Manager(Time):
  def __init__(self, scenes_names: list, objects_dict: dict, sounds_dict: dict, variables_dict: dict):
    def init_scene_objects(all_scenes: list, all_objects: dict) -> dict:
      new_dict = {}
      for item in scenes_names:
        new_dict[item] = {}

      for dict_name in all_objects.keys():
        split_scene: list = dict_name.split('>')
        if split_scene[0] == 'multi' and split_scene.__len__() == 3:
          multi_split_scenes: list = split_scene[1].split('|')
          for item_multi_scene in multi_split_scenes:
            for item_all_scenes in all_scenes:
              if item_multi_scene == item_all_scenes:
                new_dict[item_multi_scene][split_scene[-1]] = all_objects[dict_name]
                pass
        else:
          new_dict[split_scene[0]][split_scene[-1]] = all_objects[dict_name]
      return new_dict

    def init_scene_sounds(all_scenes: list, all_sounds: dict) -> dict:
      new_dict = {}
      for item in scenes_names:
        new_dict[item] = {
          'activation': {},
          'storage': {},
          'reset_sounds': True
        }

      for dict_name in all_sounds.keys():
        split_scene: list = dict_name.split('>')
        if split_scene[1] == 'activation':
          new_dict[split_scene[0]]['activation'][split_scene[-1]] = all_sounds[dict_name]
        elif split_scene[1] == 'storage':
          new_dict[split_scene[0]]['storage'][split_scene[-1]] = all_sounds[dict_name]
        elif split_scene[1] == 'reset_sounds':
          new_dict[split_scene[0]]['reset_sounds'] = all_sounds[dict_name]
      return new_dict

    def init_scene_variables(all_scenes: list, all_variables: dict) -> dict:
      new_dict = {}
      for item in scenes_names:
        new_dict[item] = {}

      for dict_name in all_variables.keys():
        split_scene: list = dict_name.split('>')
        new_dict[split_scene[0]][split_scene[-1]] = all_variables[dict_name]
      return new_dict

    super().__init__(1)
    self.scene_list = []
    self.scene_objects = {}
    for item in scenes_names:
      self.scene_list.append(item)
    self.scene_objects = init_scene_objects(scenes_names, objects_dict)
    self.scene_sounds = init_scene_sounds(scenes_names, sounds_dict)
    self.scene_variables = init_scene_variables(scenes_names, variables_dict)
    self.scene_index = 12
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
    objects.audio_activation_update()
    if config.debug:
      is_changed: str = "IS"
      if not self.scene_changed:
        is_changed = is_changed.lower()
        is_changed += " NOT"
      print(f'scene DING! (for {self.scene_counter} time), goto "{str(self.scene_list[self.scene_index]).upper()}" ({self.scene_index}) scene')

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
