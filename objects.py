from pyray import *
from classes.Text import JustText, BoxText, LinkText
from classes.Animation import Smart_Animation
from classes.Image import JustImage, BoxImage
from classes.Checkbox import Checkbox
import config
import sys, os

all_textures_ready = False
release_path = ""


if os.path.basename(sys.argv[0])[os.path.basename(sys.argv[0]).rfind(".")::] == ".exe":
  release_path = "_internal/"


def load(filename: str) -> Texture:
  return load_texture_from_image(load_image(release_path + filename))

# dirname to dir, not the file!
def load_animation(dirname: str, times: int) -> list:
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
menu_title_1 = JustText("Five", 63, Vector2(75, 21), spacing=3)
menu_title_2 = JustText("Nights", 63, Vector2(75, 81), spacing=3)
menu_title_3 = JustText("at", 63, Vector2(75, 141), spacing=3)
menu_title_4 = JustText("Freddy's", 63, Vector2(75, 201), spacing=3)
menu_title_5 = JustText("2", 63, Vector2(75, 261), spacing=3)
menu_new_game = BoxText("New game", 48, Vector2(75, 361))
menu_continue = BoxText("Continue", 48, Vector2(75, 430))
menu_settings = BoxText("Settings", 48, Vector2(75, 499))
menu_extras = BoxText("Extras", 48, Vector2(75, 568))
menu_set = JustText(">>", 48, Vector2(15, 362), font_filename="assets/fonts/consolas.ttf")
multi_back_button = BoxText("<<", 48, Vector2(10, 10), font_filename="assets/fonts/consolas.ttf")


settings_top_text = JustText("Settings", 48, Vector2(0, 10))
settings_fullscreen_text = JustText("Fullscreen: ", 40, Vector2(75, 200))
settings_fullscreen_checkbox = Checkbox(Vector2(890, 202), 40)
settings_wait_textures_text = JustText("Boot up waiting for Assets: ", 40, Vector2(75, 269))
settings_wait_textures_checkbox = Checkbox(Vector2(890, 271), 40)
settings_wait_textures_notice = JustText("Useful only if you boot up game through python console, ignore in ported version", 14, Vector2(76, 306), color=(255, 161, 0, 153))
settings_debug_text = JustText("Debug mode: ", 40, Vector2(75, 338))
settings_debug_checkbox = Checkbox(Vector2(890, 340), 40)

extras_proj_github = LinkText("https://github.com/DudFootStud/FNaF-2-raylib", "Project's Github", 40, Vector2(75, 200))
extras_auth_github = LinkText("https://github.com/FredTheKing", "Author's Github", 40, Vector2(75, 269))
extras_top_text = JustText("Extras", 48, Vector2(0, 10))


menu_test_image = BoxImage(load("assets/graphics/Unused_RareScreens/185.png"), Vector2(600, 100))




menu_list = {
  'Animation': [menu_twitch,
                multi_static],
  'Image': [menu_test_image],
  'Text': [menu_new_game,
           menu_continue,
           menu_title_1,
           menu_title_2,
           menu_title_3,
           menu_title_4,
           menu_title_5,
           menu_settings,
           menu_extras,
           menu_set]
}

settings_list = {
  'Animation': [multi_static],
  'Image': [],
  'Text': [multi_back_button,
           settings_top_text,
           settings_fullscreen_text,
           settings_fullscreen_checkbox,
           settings_wait_textures_text,
           settings_wait_textures_checkbox,
           settings_wait_textures_notice,
           settings_debug_text,
           settings_debug_checkbox]
}
extras_list = {
  'Animation': [multi_static],
  'Image': [],
  'Text': [multi_back_button,
           extras_top_text,
           extras_proj_github,
           extras_auth_github]
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
loading_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
error_boot_list = {
  'Animation': [],
  'Image': [],
  'Text': []
}
test_scene_list = {
  'Animation': [],
  'Image': [],
  'Text': [multi_back_button]
}

scenes_list = [menu_list, settings_list, extras_list, newspaper_list, night_list, game_list, paycheck_list, pixel_minigame_list, creepy_minigame_list, error_boot_list, loading_list, test_scene_list]

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
    for name_ in globals():
      if id(globals()[name_]) == id(variable):
        return name_
    return None

  space = Vector2(10, 630)
  arr = scenes_list[config.scenes.scene_index]['Animation']
  for item in arr:
    if space.x < config.resolution.x:
      name = get_variable_name(item)
      _index = name.find("_")
      new_name = name[_index + 1::]
      item.draw_debug(new_name, int(space.x), int(space.y))
      space.x += 90

def restart_animations():
  arr = scenes_list[config.scenes.scene_index]['Animation']
  for item in arr:
    item.restart()

def textures_update():
  for arr_id in 'Animation', 'Image', 'Text':
    arr = scenes_list[config.scenes.scene_index][arr_id]
    for item in arr:
      item.update()
