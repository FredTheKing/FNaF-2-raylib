from pyray import *
from classes.Animation import Animation_
from classes.Image import Image_
import config

all_textures_ready = False

def load(filename):
  return load_texture_from_image(load_image(filename))


menu_twitch = Animation_(
  [
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/321.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/215.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/362.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/470.png")
  ], Vector2(0, 0), 3, True
)
multi_static = Animation_(
  [
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Static/357.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Static/358.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Static/359.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Static/360.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Static/361.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Static/363.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Static/650.png"),
    load("assets/graphics/TheOffice_Nights_Menu/Menu/Static/651.png")
  ], Vector2(0, 0), 26, True, 101
)
menu_title = Image_("assets/graphics/TheOffice_Nights_Menu/Menu/Logos/469.png", Vector2(80, 30))
menu_new_game = Image_("assets/graphics/TheOffice_Nights_Menu/Menu/Logos/301.png", Vector2(80, 370))
menu_continue = Image_("assets/graphics/TheOffice_Nights_Menu/Menu/Logos/303.png", Vector2(80, 430))
menu_set = Image_("assets/graphics/TheOffice_Nights_Menu/Menu/Logos/229.png", Vector2(20, 370))


menu_list = {
  'Animation': [menu_twitch, multi_static],
  'Image': [menu_title, menu_new_game, menu_continue, menu_set]
}
settings_list = {
  'Animation': [],
  'Image': []
}
custom_night_list = {
  'Animation': [],
  'Image': []
}
newspaper_list = {
  'Animation': [],
  'Image': []
}
night_list = {
  'Animation': [],
  'Image': []
}
game_list = {
  'Animation': [],
  'Image': []
}
paycheck_list = {
  'Animation': [],
  'Image': []
}
pixel_minigame_list = {
  'Animation': [],
  'Image': []
}
creepy_minigame_list = {
  'Animation': [],
  'Image': []
}
error_boot_list = {
  'Animation': [],
  'Image': []
}

scenes_list = [menu_list, settings_list, custom_night_list, newspaper_list, night_list, game_list, paycheck_list, pixel_minigame_list, creepy_minigame_list, error_boot_list]

def check_all_textures():
  global all_textures_ready
  all = 0
  ready = 0

  for scene_id in range(9):
    for arr_id in 'Animation', 'Image':
      arr = scenes_list[scene_id][arr_id]
      for item in arr:
        if arr_id == 'Animation':
          for frame in item.frames:
            all += 1
            if is_texture_ready(frame):
              ready += 1
        elif arr_id == 'Image':
          all += 1
          if is_texture_ready(item.texture):
            ready += 1

  text = f"progress: {int(100/all*ready)}%"
  measure = measure_text(text, 14)
  draw_text(text, int(config.resolution.x)//2 - measure//2, int(config.resolution.y)//2+16, 14, WHITE)
  if all == ready:
    all_textures_ready = True


def animations_draw_debug():
  def get_variable_name(variable):
    for name in globals():
      if id(globals()[name]) == id(variable):
        return name
    return None

  space = Vector2(10, 640)
  arr = scenes_list[config.scenes.scene_index]['Animation']
  for item in arr:
    name = get_variable_name(item)
    _index = name.find("_")
    new_name = name[_index + 1::]
    item.draw_debug(new_name, int(space.x), int(space.y))
    space.x += 120

def textures_update():
  for arr_id in 'Animation', 'Image':
    arr = scenes_list[config.scenes.scene_index][arr_id]
    for item in arr:
      item.update()
