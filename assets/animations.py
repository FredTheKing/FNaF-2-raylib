from pyray import *
from classes.BoxText import BoxText
from classes.Animation import Smart_Animation
from classes.Image import Smart_Image
import config

all_textures_ready = False

def load(filename):
  return load_texture_from_image(load_image(filename))

# dirname to dir, not the file!
def load_animation(dirname: str, times: int):
  arr = []
  for item in range(times):
    arr.append(load(dirname + f"/{item}.png"))
  return arr

menu_twitch = Smart_Animation(
  load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Misc", 4),
  Vector2(0, 0), 3, True
)
multi_static = Smart_Animation(
  load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Static", 8),
  Vector2(0, 0), 26, True, 101
)
menu_title = Smart_Image("assets/graphics/TheOffice_Nights_Menu/Menu/Logos/469.png", Vector2(80, 30))
menu_new_game = BoxText("New Game", 48, Vector2(75, 361))
menu_continue = BoxText("Continue", 48, Vector2(75, 430))
menu_set = Smart_Image("assets/graphics/TheOffice_Nights_Menu/Menu/Logos/229.png", Vector2(20, 371))

menu_list = {
  'Animation': [menu_twitch, multi_static],
  'Image': [menu_title, menu_set],
  'Text': [menu_new_game, menu_continue]
}
settings_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
custom_night_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
newspaper_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
night_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
game_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
paycheck_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
pixel_minigame_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
creepy_minigame_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
error_boot_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}

scenes_list = [menu_list, settings_list, custom_night_list, newspaper_list, night_list, game_list, paycheck_list, pixel_minigame_list, creepy_minigame_list, error_boot_list]

def check_all_textures():
  global all_textures_ready
  all: int = 0
  ready: int = 0

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
    if space.x < config.resolution.x:
      name = get_variable_name(item)
      _index = name.find("_")
      new_name = name[_index + 1::]
      item.draw_debug(new_name, int(space.x), int(space.y))
      space.x += 120

def restart_animations():
  arr = scenes_list[config.scenes.scene_index]['Animation']
  for item in arr:
    item.restart()

def textures_update():
  for arr_id in 'Animation', 'Image', 'Text':
    arr = scenes_list[config.scenes.scene_index][arr_id]
    for item in arr:
      item.update()
