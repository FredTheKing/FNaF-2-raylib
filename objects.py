from pyray import *
from classes.Managers import Scene_Manager, Sound_Manager
from classes.Text import JustText, BoxText, LinkText
from classes.Animation import Smart_Animation
from classes.Image import JustImage, BorderImage, BoxImage
from classes.Checkbox import Checkbox
from classes.Bar import BarButtons, DigitButtons
import config
import sys
import os

all_textures_ready = False
release_path = ""

if os.path.basename(sys.argv[0])[os.path.basename(sys.argv[0]).rfind(".")::] == ".exe":
  release_path = "_internal/"


config.def_font = load_font(release_path + config.def_font_filename)

def load(filename: str) -> Texture:
  return load_texture_from_image(load_image(release_path + filename))

# dirname to dir, not the file!
def load_animation(dirname: str, times: int) -> list:
  arr = []
  for item in range(times):
    arr.append(load(dirname + f"/{item}.png"))
  return arr


# ----------------------------------------------- #
scenes = Scene_Manager(["menu", "settings", "extras", "custom night", "newspaper", "night", "game", "paycheck", "pixel minigame", "creepy minigame", "loading", "error boot", "test scene"])
sounds = Sound_Manager(scenes)
# ----------------------------------------------- #
multi_static = Smart_Animation(load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Static", 8), Vector2(0, 0), 26, True, 101)
multi_back_button = BoxText("<<", 48, Vector2(10, 10), font_filename="assets/fonts/consolas.ttf")
# ----------------------------------------------- #
menu_twitch = Smart_Animation(load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Misc", 4), Vector2(0, 0), 3, True)
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
# ----------------------------------------------- #
settings_top_text = JustText("Settings", 48, Vector2(0, 10))
settings_fullscreen_text = JustText("Fullscreen: ", 40, Vector2(75, 200))
settings_fullscreen_checkbox = Checkbox(Vector2(890, 202), 40, False)
settings_wait_textures_text = JustText("Boot up waiting for Assets: ", 40, Vector2(75, 269))
settings_wait_textures_checkbox = Checkbox(Vector2(890, 271), 40, False)
settings_wait_textures_notice = JustText("Useful only if you boot up game through python console, ignore in ported version", 14, Vector2(78, 307), color=[255, 161, 0, 0])
settings_funny_text = JustText("Constant shaky effect: ", 40, Vector2(75, 338))
settings_funny_checkbox = Checkbox(Vector2(890, 340), 40, False)
settings_funny_notice = JustText("Does not work with fullscreen option and do lag your game. Dont even ask me why I added this one :/", 14, Vector2(78, 374), color=[255, 161, 0, 0])
settings_volume_text = JustText("Volume: ", 40, Vector2(75, 407))
settings_volume_slider = BarButtons(Vector2(557, 409), Vector2(300, 40), 6, False)
settings_debug_text = JustText("Debug mode: ", 40, Vector2(75, 545))
settings_debug_checkbox = Checkbox(Vector2(890, 547), 40, False)
# ----------------------------------------------- #
extras_top_text = JustText("Extras", 48, Vector2(0, 10))
extras_proj_github = LinkText("https://github.com/DudFootStud/FNaF-2-raylib", "Project's Github", 40, Vector2(75, 200))
extras_auth_github = LinkText("https://github.com/FredTheKing", "Author's Github", 40, Vector2(75, 269))
extras_custom_night = BoxText("Custom night", 40, Vector2(75, 338))
# ----------------------------------------------- #
custom_night_top_text = JustText("Custom Night", 48, Vector2(0, 10))
#125x125
custom_night_with_freddy = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithFreddy.png"), Vector2(150, 150))
custom_night_with_bonnie = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithBonnie.png"), Vector2(300, 150))
custom_night_with_chica = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithChica.png"), Vector2(450, 150))
custom_night_with_foxy = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithFoxy.png"), Vector2(600, 150))
custom_night_golden_freddy = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/GoldenFreddy.png"), Vector2(750, 150))
custom_night_toy_freddy = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyFreddy.png"), Vector2(150, 350))
custom_night_toy_bonnie = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyBonnie.png"), Vector2(300, 350))
custom_night_toy_chica = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyChica.png"), Vector2(450, 350))
custom_night_mangle = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/Mangle.png"), Vector2(600, 350))
custom_night_balloon_boy = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/BalloonBoy.png"), Vector2(750, 350))

custom_night_with_freddy_text = JustText("W. Freddy", 22, Vector2(212, 128))
custom_night_with_bonnie_text = JustText("W. Bonnie", 22, Vector2(362, 128))
custom_night_with_chica_text = JustText("W. Chica", 22, Vector2(512, 128))
custom_night_with_foxy_text = JustText("W. Foxy", 22, Vector2(662, 128))
custom_night_golden_freddy_text = JustText("G. Freddy", 22, Vector2(812, 128))
custom_night_toy_freddy_text = JustText("T. Freddy", 22, Vector2(212, 328))
custom_night_toy_bonnie_text = JustText("T. Bonnie", 22, Vector2(362, 328))
custom_night_toy_chica_text = JustText("T. Chica", 22, Vector2(512, 328))
custom_night_mangle_text = JustText("mangle", 22, Vector2(662, 328))
custom_night_balloon_boy_text = JustText("BB", 22, Vector2(812, 328))

custom_night_with_freddy_slider = DigitButtons(Vector2(150, 280), Vector2(53, 30), 20, default_state=0)
custom_night_with_bonnie_slider = DigitButtons(Vector2(300, 280), Vector2(53, 30), 20, default_state=0)
custom_night_with_chica_slider = DigitButtons(Vector2(450, 280), Vector2(53, 30), 20, default_state=0)
custom_night_with_foxy_slider = DigitButtons(Vector2(600, 280), Vector2(53, 30), 20, default_state=0)
custom_night_golden_freddy_slider = DigitButtons(Vector2(750, 280), Vector2(53, 30), 20, default_state=0)
custom_night_toy_freddy_slider = DigitButtons(Vector2(150, 480), Vector2(53, 30), 20, default_state=0)
custom_night_toy_bonnie_slider = DigitButtons(Vector2(300, 480), Vector2(53, 30), 20, default_state=0)
custom_night_toy_chica_slider = DigitButtons(Vector2(450, 480), Vector2(53, 30), 20, default_state=0)
custom_night_mangle_slider = DigitButtons(Vector2(600, 480), Vector2(53, 30), 20, default_state=0)
custom_night_balloon_boy_slider = DigitButtons(Vector2(750, 480), Vector2(53, 30), 20, default_state=0)
# ----------------------------------------------- #
menu_to_test_tp = BoxText("\t", 60, Vector2(950, 670))
# ----------------------------------------------- #
test_digit_bar = DigitButtons(Vector2(100, 500))
test_slider = BarButtons(Vector2(100, 600))
# ----------------------------------------------- #

menu_list = {
  'Animation': [menu_twitch,
                multi_static],
  'Image': [],
  'Text': [menu_new_game,
           menu_continue,
           menu_title_1,
           menu_title_2,
           menu_title_3,
           menu_title_4,
           menu_title_5,
           menu_settings,
           menu_extras,
           menu_set,
           menu_to_test_tp]
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
           settings_funny_text,
           settings_funny_checkbox,
           settings_funny_notice,
           settings_volume_text,
           settings_volume_slider,
           settings_debug_text,
           settings_debug_checkbox]
}
extras_list = {
  'Animation': [multi_static],
  'Image': [],
  'Text': [multi_back_button,
           extras_top_text,
           extras_proj_github,
           extras_auth_github,
           extras_custom_night]
}
custom_night_list = {
  'Animation': [multi_static],
  'Image': [custom_night_with_freddy,
            custom_night_with_bonnie,
            custom_night_with_chica,
            custom_night_with_foxy,
            custom_night_golden_freddy,
            custom_night_toy_freddy,
            custom_night_toy_bonnie,
            custom_night_toy_chica,
            custom_night_mangle,
            custom_night_balloon_boy],
  'Text': [multi_back_button,
           custom_night_top_text,
           custom_night_with_freddy_text,
           custom_night_with_bonnie_text,
           custom_night_with_chica_text,
           custom_night_with_foxy_text,
           custom_night_golden_freddy_text,
           custom_night_toy_freddy_text,
           custom_night_toy_bonnie_text,
           custom_night_toy_chica_text,
           custom_night_mangle_text,
           custom_night_balloon_boy_text,
           custom_night_with_freddy_slider,
           custom_night_with_bonnie_slider,
           custom_night_with_chica_slider,
           custom_night_with_foxy_slider,
           custom_night_golden_freddy_slider,
           custom_night_toy_freddy_slider,
           custom_night_toy_bonnie_slider,
           custom_night_toy_chica_slider,
           custom_night_mangle_slider,
           custom_night_balloon_boy_slider]
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
  'Text': [multi_back_button,
           test_slider,
           test_digit_bar]
}

scenes_list = [menu_list, settings_list, extras_list, custom_night_list, newspaper_list, night_list, game_list, paycheck_list, pixel_minigame_list, creepy_minigame_list, error_boot_list, loading_list, test_scene_list]

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
  draw_text(text, config.resolution[0]//2 - measure//2, config.resolution[1]//2+16, 14, WHITE)
  if all == ready:
    all_textures_ready = True


def animations_draw_debug():
  def get_variable_name(variable):
    for name_ in globals():
      if id(globals()[name_]) == id(variable):
        return name_
    return None

  space = Vector2(10, 630)
  arr = scenes_list[scenes.scene_index]['Animation']
  for item in arr:
    if space.x < config.resolution[0]:
      name = get_variable_name(item)
      _index = name.find("_")
      new_name = name[_index + 1::]
      item.draw_debug(new_name, int(space.x), int(space.y))
      space.x += 90

def restart_animations():
  arr = scenes_list[scenes.scene_index]['Animation']
  for item in arr:
    item.restart()

def textures_update():
  for arr_id in 'Animation', 'Image', 'Text':
    arr = scenes_list[scenes.scene_index][arr_id]
    for item in arr:
      item.update()
