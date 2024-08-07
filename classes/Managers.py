from pyray import *
import objects
from classes.Time import Time
import config

class Scene_Manager(Time):
  def __init__(self, scenes_names: list, objects_dict: dict, sounds_dict: dict, variables_dict: dict, timers_dict: dict):
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

    def init_scene_sounds(all_sounds: dict) -> dict:
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

    def init_scene_variables(all_variables: dict) -> dict:
      new_dict = {}
      for item in scenes_names:
        new_dict[item] = {}

      for dict_name in all_variables.keys():
        split_scene: list = dict_name.split('>')
        new_dict[split_scene[0]][split_scene[-1]] = all_variables[dict_name]
      return new_dict

    def init_scene_timers(all_variables: dict) -> dict:
      new_dict = {}
      for item in scenes_names:
        new_dict[item] = {}

      for dict_name in all_variables.keys():
        split_scene: list = dict_name.split('>')
        new_dict[split_scene[0]][split_scene[-1]] = all_variables[dict_name]
      return new_dict


    super().__init__(1)
    self.scene_list = []
    self.hidden_layers = []
    self.scene_objects = {}
    for item in scenes_names:
      self.scene_list.append(item)

    self.scene_objects = init_scene_objects(scenes_names, objects_dict)
    self.scene_sounds = init_scene_sounds(sounds_dict)
    self.scene_variables = init_scene_variables(variables_dict)
    self.scene_timers = init_scene_timers(timers_dict)

    self.scene_index = 14
    self.scene_changed: int = 1
    self.scene_counter = 0

    self.start_time()

  def hide_layer(self, layer_order: int or list):
    layer_list = layer_order if type(layer_order) is list else [layer_order]
    for layer_item in layer_list:
      if layer_item not in self.hidden_layers:
        self.hidden_layers.append(layer_item)

  def show_layer(self, layer_order: int or list):
    layer_list = layer_order if type(layer_order) is list else [layer_order]
    for layer_item in layer_list:
      if layer_item in self.hidden_layers:
        self.hidden_layers.pop(self.hidden_layers.index(layer_item))

  def set_scene(self, id: str, show_all_layers: bool = True):
    if show_all_layers:
      self.hidden_layers.clear()
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
      KeyboardKey.KEY_FOUR,
      KeyboardKey.KEY_FIVE,
      KeyboardKey.KEY_SIX,
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
    ]

    for i in range(len(keys_arr)):
      if keys_arr[i] is not None:
        if config.key_pressed == keys_arr[i]:
          self.set_scene(i)
          break
