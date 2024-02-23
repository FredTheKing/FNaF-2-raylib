from random import randint

from pyray import *
from classes.Managers import Scene_Manager, Sound_Manager
from classes.Text import JustText, BoxText, LinkText
from classes.Animation import JustAnimation
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

def do_valid_filetype():
  if release_path is not "":
    config.fullscreen = True
    config.debug = False
    scenes.set_scene('preview')

def change_needs() -> None:
  settings_top_text.center_text()

  extras_top_text.center_text()
  extras_credits_raylib_logo.resize(Vector2(128, 128))
  extras_credits_scott_logo.resize(Vector2(128, 128))
  extras_credits_dudfoot_logo.resize(Vector2(306, 123))

  custom_night_top_text.center_text()
  custom_night_with_freddy_text.center_text(212)
  custom_night_with_bonnie_text.center_text(362)
  custom_night_with_chica_text.center_text(512)
  custom_night_with_foxy_text.center_text(662)
  custom_night_golden_freddy_text.center_text(812)
  custom_night_toy_freddy_text.center_text(212)
  custom_night_toy_bonnie_text.center_text(362)
  custom_night_toy_chica_text.center_text(512)
  custom_night_mangle_text.center_text(662)
  custom_night_balloon_boy_text.center_text(812)

  jumpscares_top_text.center_text()
  jumpscares_office_preview.resize(Vector2(512, 384))
  jumpscares_withered_freddy.resize(Vector2(512, 384))
  jumpscares_withered_bonnie.resize(Vector2(512, 384))
  jumpscares_withered_chica.resize(Vector2(512, 384))
  jumpscares_withered_foxy.resize(Vector2(512, 384))

  development_moments_top_text.center_text()

def load(filename: str) -> Texture:
  return load_texture_from_image(load_image(release_path + filename))


# dirname to dir, not the file!
def load_animation(dirname: str, times: int) -> list:
  arr = []
  for item in range(times):
    arr.append(load(dirname + f"/{item}.png"))
  return arr


# ----------------------------------------------- #
scenes = Scene_Manager(["menu", "settings", "extras", "custom night", "jumpscares", "development moments", "newspaper", "night", "game", "paycheck", "pixel minigame", "creepy minigame", "loading", "error boot", "preview", "test scene"])
sounds = Sound_Manager(scenes)
# ----------------------------------------------- #
multi_static = JustAnimation(load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Static", 8), Vector2(0, 0),
                               26, True, 101)
multi_back_button = BoxText("<<", 48, Vector2(10, 10), font_filename="assets/fonts/consolas.ttf")
# ----------------------------------------------- #
menu_twitch = JustAnimation(load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Misc", 4), Vector2(0, 0), 3,
                              True)
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
settings_volume_slider = BarButtons(Vector2(557, 409), Vector2(300, 40), 6, False, config.volume)
settings_debug_text = JustText("Debug mode: ", 40, Vector2(75, 545))
settings_debug_checkbox = Checkbox(Vector2(890, 547), 40, False)
# ----------------------------------------------- #
extras_top_text = JustText("Extras", 48, Vector2(0, 10))
extras_proj_github = LinkText("https://github.com/DudFootStud/FNaF-2-raylib", "Project's Github", 40, Vector2(75, 200))
extras_auth_github = LinkText("https://github.com/FredTheKing", "Author's Github", 40, Vector2(75, 269))
extras_custom_night = BoxText("Custom night", 40, Vector2(75, 338))
extras_jumpscares = BoxText("Jumpscares", 40, Vector2(75, 407))
extras_development_moments = BoxText("Developments", 40, Vector2(75, 476))

extras_credits_text = BoxText("Credits:", 40, Vector2(600, 135))
extras_credits_raylib_text = JustText("powered with", 16, Vector2(600, 222), WHITE, 2, font_filename=get_font_default(), spacing=2)
extras_credits_raylib_logo = JustImage(load("assets/graphics/PreviewLogos/raylib.png"), Vector2(600, 240))
extras_credits_dudfoot_text = JustText("designed and built by", 16, Vector2(600, 422), WHITE, 2, font_filename=get_font_default(), spacing=2)
extras_credits_dudfoot_logo = JustImage(load("assets/graphics/PreviewLogos/dudfoot.png"), Vector2(600, 450))
extras_credits_scott_text = JustText("OG game idea", 16, Vector2(800, 222), WHITE, 2, font_filename=get_font_default(), spacing=2)
extras_credits_scott_logo = JustImage(load("assets/graphics/PreviewLogos/scott.png"), Vector2(800, 240))
# ----------------------------------------------- #
custom_night_top_text = JustText("Custom Night", 48, Vector2(0, 10))
# 125x125
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
custom_night_mangle_text = JustText("Mangle", 22, Vector2(662, 328))
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

custom_night_start = BoxText("START", 80, Vector2(645, 600))
# ----------------------------------------------- #
jumpscares_top_text = JustText("Jumpscares", 48, Vector2(0, 10))

jumpscares_office_preview = BorderImage(load("assets/graphics/TheOffice_Nights_Menu/TheOffice/office_preview.png"), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50))
jumpscares_withered_freddy = JustAnimation(load_animation("assets/graphics/Jumpscares/WitheredFreddy", 13), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50), layer=2, animation_speed=20, is_looped=True)
jumpscares_withered_bonnie = JustAnimation(load_animation("assets/graphics/Jumpscares/WitheredBonnie", 16), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50), layer=2, animation_speed=20, is_looped=True)
jumpscares_withered_chica = JustAnimation(load_animation("assets/graphics/Jumpscares/WitheredChica", 12), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50), layer=2, animation_speed=20, is_looped=True)
jumpscares_withered_foxy = JustAnimation(load_animation("assets/graphics/Jumpscares/WitheredFoxy", 14), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50), layer=2, animation_speed=20, is_looped=True)
# ----------------------------------------------- #
development_moments_top_text = JustText("Developments", 48, Vector2(0, 10))
# ----------------------------------------------- #
preview_raylib_logo_text = JustText("powered with", 24, Vector2(config.resolution[0] // 2 - 128, config.resolution[1] // 2 - 154), WHITE, 2, font_filename=get_font_default(), spacing=2)
preview_raylib_logo = JustImage(load("assets/graphics/PreviewLogos/raylib.png"), Vector2(config.resolution[0] // 2 - 128, config.resolution[1] // 2 - 128))
# ----------------------------------------------- #
test_digit_bar = DigitButtons(Vector2(100, 500))
test_slider = BarButtons(Vector2(100, 600))
# ----------------------------------------------- #
menu_to_test_tp = BoxText("\t", 60, Vector2(950, 670))
# ----------------------------------------------- #


menu_list = {
  'Animation': [menu_twitch,
                multi_static],
  'Image': [],
  'Text': [menu_title_1,
           menu_title_2,
           menu_title_3,
           menu_title_4,
           menu_title_5,
           menu_new_game,
           menu_continue,
           menu_settings,
           menu_extras,
           menu_set,
           menu_to_test_tp],
  'Stuff': []
}

settings_list = {
  'Animation': [multi_static],
  'Image': [],
  'Text': [multi_back_button,
           settings_top_text,
           settings_fullscreen_text,
           settings_wait_textures_text,
           settings_wait_textures_notice,
           settings_funny_text,
           settings_funny_notice,
           settings_volume_text,
           settings_debug_text],
  'Stuff': [settings_fullscreen_checkbox,
            settings_wait_textures_checkbox,
            settings_funny_checkbox,
            settings_volume_slider,
            settings_debug_checkbox]
}
extras_list = {
  'Animation': [multi_static],
  'Image': [extras_credits_raylib_logo,
            extras_credits_dudfoot_logo,
            extras_credits_scott_logo],
  'Text': [multi_back_button,
           extras_top_text,
           extras_proj_github,
           extras_auth_github,
           extras_custom_night,
           extras_jumpscares,
           extras_development_moments,
           extras_credits_text,
           extras_credits_raylib_text,
           extras_credits_dudfoot_text,
           extras_credits_scott_text],
  'Stuff': []
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
           custom_night_start],
  'Stuff': [custom_night_with_freddy_slider,
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
jumpscares_list = {
  'Animation': [multi_static,
                jumpscares_withered_freddy,
                jumpscares_withered_bonnie,
                jumpscares_withered_chica,
                jumpscares_withered_foxy],
  'Image': [jumpscares_office_preview],
  'Text': [multi_back_button,
           jumpscares_top_text],
  'Stuff': []
}
development_moments_list = {
  'Animation': [multi_static],
  'Image': [],
  'Text': [multi_back_button,
           development_moments_top_text],
  'Stuff': []
}
newspaper_list = {
  'Animation': [],
  'Image': [],
  'Text': [],
  'Stuff': []
}
night_list = {
  'Animation': [],
  'Image': [],
  'Text': [],
  'Stuff': []
}
game_list = {
  'Animation': [],
  'Image': [],
  'Text': [],
  'Stuff': []
}
paycheck_list = {
  'Animation': [],
  'Image': [],
  'Text': [],
  'Stuff': []
}
pixel_minigame_list = {
  'Animation': [],
  'Image': [],
  'Text': [],
  'Stuff': []
}
creepy_minigame_list = {
  'Animation': [],
  'Image': [],
  'Text': [],
  'Stuff': []
}
loading_list = {
  'Animation': [],
  'Image': [],
  'Text': [],
  'Stuff': []
}
error_boot_list = {
  'Animation': [],
  'Image': [],
  'Text': [],
  'Stuff': []
}
preview_list = {
  'Animation': [multi_static],
  'Image': [preview_raylib_logo],
  'Text': [preview_raylib_logo_text],
  'Stuff': []
}
test_scene_list = {
  'Animation': [],
  'Image': [],
  'Text': [multi_back_button],
  'Stuff': [test_slider,
            test_digit_bar]
}

scenes_list = [menu_list, settings_list, extras_list, custom_night_list, jumpscares_list, development_moments_list, newspaper_list, night_list, game_list, paycheck_list, pixel_minigame_list, creepy_minigame_list, error_boot_list, loading_list, preview_list, test_scene_list]

# ----------------------------------------------- #
change_needs()
def unload_all_textures(mod: int = -1):
  a = 0
  b = 2
  if mod <= 0:
    b = 0
  else:
    b = mod+1
  for scene_id in range(scenes_list.__len__()):
    for arr_id in 'Animation', 'Image', 'Text', 'Stuff':
      arr = scenes_list[scene_id][arr_id]
      for item in arr:
        if not randint(a, b):
          if arr_id == 'Animation':
            for frame in item.frames:
              unload_texture(frame)
          elif arr_id == 'Image':
            unload_texture(item.texture)
          elif arr_id == 'Text':
            unload_texture(item.font.texture)
          elif arr_id == 'Stuff':
            try:
              unload_texture(item.left_button.font.texture)
              unload_texture(item.right_button.font.texture)
              unload_texture(item.text.font.texture)
            except AttributeError:
              pass
          unload_texture(config.def_font.texture)


def check_all_textures():
  global all_textures_ready
  all: int = 0
  ready: int = 0

  for scene_id in range(scenes_list.__len__()):
    for arr_id in 'Animation', 'Image', 'Text':
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
        elif arr_id == 'Text':
          all += 1
          if is_font_ready(item.font):
            ready += 1

  text = f"progress: {int(100 / all * ready)}%"
  measure = measure_text(text, 14)
  draw_text(text, config.resolution[0] // 2 - measure // 2, config.resolution[1] // 2 + 16, 14, WHITE)
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
  broken_order = {}
  for arr_id in 'Animation', 'Image', 'Text', 'Stuff':
    arr = scenes_list[scenes.scene_index][arr_id]
    for item in arr:
      broken_order[item] = item.layer_order
  fixed_order = sorted(broken_order.items(), key=lambda x: x[1])
  for item in fixed_order:
    item[0].update()
