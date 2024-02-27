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
  all_objects['settings>top_text'].center_text()

  all_objects['extras>top_text'].center_text()
  all_objects['extras>credits_raylib_logo'].resize(Vector2(128, 128))
  all_objects['extras>credits_scott_logo'].resize(Vector2(128, 128))
  all_objects['extras>credits_dudfoot_logo'].resize(Vector2(306, 123))

  all_objects['custom_night>top_text'].center_text()
  all_objects['custom_night>with_freddy_text'].center_text(212)
  all_objects['custom_night>with_bonnie_text'].center_text(362)
  all_objects['custom_night>with_chica_text'].center_text(512)
  all_objects['custom_night>with_foxy_text'].center_text(662)
  all_objects['custom_night>golden_freddy_text'].center_text(812)
  all_objects['custom_night>toy_freddy_text'].center_text(212)
  all_objects['custom_night>toy_bonnie_text'].center_text(362)
  all_objects['custom_night>toy_chica_text'].center_text(512)
  all_objects['custom_night>mangle_text'].center_text(662)
  all_objects['custom_night>balloon_boy_text'].center_text(812)

  all_objects['jumpscares>top_text'].center_text()
  all_objects['jumpscares>office_preview'].resize(Vector2(512, 384))
  all_objects['jumpscares>withered_freddy'].resize(Vector2(512, 384))
  all_objects['jumpscares>withered_bonnie'].resize(Vector2(512, 384))
  all_objects['jumpscares>withered_chica'].resize(Vector2(512, 384))
  all_objects['jumpscares>withered_foxy'].resize(Vector2(512, 384))

  all_objects['development_moments>top_text'].center_text()

def load(filename: str) -> Texture:
  return load_texture_from_image(load_image(release_path + filename))


# dirname to dir, not the file!
def load_animation(dirname: str, times: int) -> list:
  arr = []
  for item in range(times):
    arr.append(load(dirname + f"/{item}.png"))
  return arr

# ----------------------------------------------- #


all_objects = {
  'multi>menu|settings|extras|custom_night|jumpscares|development_moments|preview>static': JustAnimation(load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Static", 8), Vector2(0, 0), 26, True, 101, 1),
  'multi>settings|extras|custom_night|jumpscares|development_moments|test_scene>back_button': BoxText("<<", 48, Vector2(10, 10), font_filename="assets/fonts/consolas.ttf"),
  # ----------------------------------------------- #
  'menu>twitch': JustAnimation(load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Misc", 4), Vector2(0, 0), 3, True),
  'menu>title_1': JustText("Five", 63, Vector2(75, 21), spacing=3),
  'menu>title_2': JustText("Nights", 63, Vector2(75, 81), spacing=3),
  'menu>title_3': JustText("at", 63, Vector2(75, 141), spacing=3),
  'menu>title_4': JustText("Freddy's", 63, Vector2(75, 201), spacing=3),
  'menu>title_5': JustText("2", 63, Vector2(75, 261), spacing=3),
  'menu>new_game': BoxText("New game", 48, Vector2(75, 361)),
  'menu>continue': BoxText("Continue", 48, Vector2(75, 430)),
  'menu>settings': BoxText("Settings", 48, Vector2(75, 499)),
  'menu>extras': BoxText("Extras", 48, Vector2(75, 568)),
  'menu>set': JustText(">>", 48, Vector2(15, 362), font_filename="assets/fonts/consolas.ttf"),

  'menu>to_test_tp': BoxText("\t", 60, Vector2(950, 670)),
  # ----------------------------------------------- #
  'settings>top_text': JustText("Settings", 48, Vector2(0, 10)),
  'settings>fullscreen_text': JustText("Fullscreen: ", 40, Vector2(75, 200)),
  'settings>fullscreen_checkbox': Checkbox(Vector2(890, 202), 40, auto_changing=False),
  'settings>wait_textures_text': JustText("Boot up waiting for Assets: ", 40, Vector2(75, 269)),
  'settings>wait_textures_checkbox': Checkbox(Vector2(890, 271), 40, auto_changing=False),
  'settings>wait_textures_notice': JustText("Useful only if you boot up game through python console, ignore in ported version", 14, Vector2(78, 307), color=[255, 161, 0, 0]),
  'settings>funny_text': JustText("Constant shaky effect: ", 40, Vector2(75, 338)),
  'settings>funny_checkbox': Checkbox(Vector2(890, 340), 40, auto_changing=False),
  'settings>funny_notice': JustText("Does not work with fullscreen option and do lag your game. Dont even ask me why I added this one :/", 14, Vector2(78, 374), color=[255, 161, 0, 0]),
  'settings>volume_text': JustText("Volume: ", 40, Vector2(75, 407)),
  'settings>volume_slider': BarButtons(Vector2(557, 409), Vector2(300, 40), 6, goes_zero=False, default_state=config.volume),
  'settings>debug_text': JustText("Debug mode: ", 40, Vector2(75, 545)),
  'settings>debug_checkbox': Checkbox(Vector2(890, 547), 40, auto_changing=False),
  # ----------------------------------------------- #
  'extras>top_text': JustText("Extras", 48, Vector2(0, 10)),
  'extras>proj_github': LinkText("https://github.com/DudFootStud/FNaF-2-raylib", "Project's Github", 40, Vector2(75, 200)),
  'extras>auth_github': LinkText("https://github.com/FredTheKing", "Author's Github", 40, Vector2(75, 269)),
  'extras>custom_night': BoxText("Custom night", 40, Vector2(75, 338)),
  'extras>jumpscares': BoxText("Jumpscares", 40, Vector2(75, 407)),
  'extras>development_moments': BoxText("Developments", 40, Vector2(75, 476)),

  'extras>credits_text': BoxText("Credits:", 40, Vector2(600, 135)),
  'extras>credits_raylib_text': JustText("powered with", 16, Vector2(600, 222), WHITE, 2, font_filename=get_font_default(), spacing=2),
  'extras>credits_raylib_logo': JustImage(load("assets/graphics/PreviewLogos/raylib.png"), Vector2(600, 240)),
  'extras>credits_dudfoot_text': JustText("designed and built by", 16, Vector2(600, 422), WHITE, 2, font_filename=get_font_default(), spacing=2),
  'extras>credits_dudfoot_logo': JustImage(load("assets/graphics/PreviewLogos/dudfoot.png"), Vector2(600, 450)),
  'extras>credits_scott_text': JustText("OG game idea", 16, Vector2(800, 222), WHITE, 2, font_filename=get_font_default(), spacing=2),
  'extras>credits_scott_logo': JustImage(load("assets/graphics/PreviewLogos/scott.png"), Vector2(800, 240)),
  # ----------------------------------------------- #
  'custom_night>top_text': JustText("Custom Night", 48, Vector2(0, 10)),
  # 125x125
  'custom_night>with_freddy': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithFreddy.png"), Vector2(150, 150)),
  'custom_night>with_bonnie': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithBonnie.png"), Vector2(300, 150)),
  'custom_night>with_chica': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithChica.png"), Vector2(450, 150)),
  'custom_night>with_foxy': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithFoxy.png"), Vector2(600, 150)),
  'custom_night>golden_freddy': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/GoldenFreddy.png"), Vector2(750, 150)),
  'custom_night>toy_freddy': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyFreddy.png"), Vector2(150, 350)),
  'custom_night>toy_bonnie': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyBonnie.png"), Vector2(300, 350)),
  'custom_night>toy_chica': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyChica.png"), Vector2(450, 350)),
  'custom_night>mangle': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/Mangle.png"), Vector2(600, 350)),
  'custom_night>balloon_boy': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/BalloonBoy.png"), Vector2(750, 350)),

  'custom_night>with_freddy_text': JustText("W. Freddy", 22, Vector2(212, 128)),
  'custom_night>with_bonnie_text': JustText("W. Bonnie", 22, Vector2(362, 128)),
  'custom_night>with_chica_text': JustText("W. Chica", 22, Vector2(512, 128)),
  'custom_night>with_foxy_text': JustText("W. Foxy", 22, Vector2(662, 128)),
  'custom_night>golden_freddy_text': JustText("G. Freddy", 22, Vector2(812, 128)),
  'custom_night>toy_freddy_text': JustText("T. Freddy", 22, Vector2(212, 328)),
  'custom_night>toy_bonnie_text': JustText("T. Bonnie", 22, Vector2(362, 328)),
  'custom_night>toy_chica_text': JustText("T. Chica", 22, Vector2(512, 328)),
  'custom_night>mangle_text': JustText("Mangle", 22, Vector2(662, 328)),
  'custom_night>balloon_boy_text': JustText("BB", 22, Vector2(812, 328)),

  'custom_night>with_freddy_slider': DigitButtons(Vector2(150, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>with_bonnie_slider': DigitButtons(Vector2(300, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>with_chica_slider': DigitButtons(Vector2(450, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>with_foxy_slider': DigitButtons(Vector2(600, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>golden_freddy_slider': DigitButtons(Vector2(750, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>toy_freddy_slider': DigitButtons(Vector2(150, 480), Vector2(53, 30), 20, default_state=0),
  'custom_night>toy_bonnie_slider': DigitButtons(Vector2(300, 480), Vector2(53, 30), 20, default_state=0),
  'custom_night>toy_chica_slider': DigitButtons(Vector2(450, 480), Vector2(53, 30), 20, default_state=0),
  'custom_night>mangle_slider': DigitButtons(Vector2(600, 480), Vector2(53, 30), 20, default_state=0),
  'custom_night>balloon_boy_slider': DigitButtons(Vector2(750, 480), Vector2(53, 30), 20, default_state=0),

  'custom_night>start': BoxText("START", 80, Vector2(645, 600)),
  # ----------------------------------------------- #
  'jumpscares>top_text': JustText("Jumpscares", 48, Vector2(0, 10)),
  
  'jumpscares>office_preview': BorderImage(load("assets/graphics/TheOffice_Nights_Menu/TheOffice/office_preview.png"), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50)),
  'jumpscares>withered_freddy': JustAnimation(load_animation("assets/graphics/Jumpscares/WitheredFreddy", 13), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50), layer=2, animation_speed=20, is_looped=True),
  'jumpscares>withered_bonnie': JustAnimation(load_animation("assets/graphics/Jumpscares/WitheredBonnie", 16), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50), layer=2, animation_speed=20, is_looped=True),
  'jumpscares>withered_chica': JustAnimation(load_animation("assets/graphics/Jumpscares/WitheredChica", 12), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50), layer=2, animation_speed=20, is_looped=True),
  'jumpscares>withered_foxy': JustAnimation(load_animation("assets/graphics/Jumpscares/WitheredFoxy", 14), Vector2(config.resolution[0]//2 - 512//2, config.resolution[1]//2 - 384//2 - 50), layer=2, animation_speed=20, is_looped=True),
  # ----------------------------------------------- #
  'development_moments>top_text': JustText("Developments", 48, Vector2(0, 10)),
  # ----------------------------------------------- #
  'preview>logo_text': JustText("powered with", 24, Vector2(config.resolution[0] // 2 - 128, config.resolution[1] // 2 - 154), WHITE, 2, font_filename=get_font_default(), spacing=2),
  'preview>logo': JustImage(load("assets/graphics/PreviewLogos/raylib.png"), Vector2(config.resolution[0] // 2 - 128, config.resolution[1] // 2 - 128)),
  # ----------------------------------------------- #
  'test_scene>digit_bar': DigitButtons(Vector2(100, 500)),
  'test_scene>slider': BarButtons(Vector2(100, 600)),
}

scenes = Scene_Manager(["menu", "settings", "extras", "custom_night", "jumpscares", "development_moments", "newspaper", "night", "game", "paycheck", "pixel_minigame", "creepy_minigame", "loading", "error", "preview", "test_scene"], all_objects)
sounds = Sound_Manager(scenes)


# ----------------------------------------------- #

change_needs()
def unload_all_textures(mod: int = -1):
  a = 0
  b = 2
  if mod <= 0:
    b = 0
  else:
    b = mod+1
  for arr_id in scenes.scene_list:
    arr = scenes.scene_objects[arr_id]
    for item in arr.items():
      if not randint(a, b):
        item_type = str(type(item[1])).split('.')[1]
        if item_type == 'Animation':
          for frame in item[1].frames:
            unload_texture(frame)
        elif item_type == 'Image':
          unload_texture(item[1].texture)
        elif item_type == 'Text':
          unload_texture(item[1].font.texture)
        else:
          try:
            unload_texture(item[1].left_button.font.texture)
            unload_texture(item[1].right_button.font.texture)
            unload_texture(item[1].text.font.texture)
          except AttributeError:
            pass
        unload_texture(config.def_font.texture)



def check_all_textures():
  global all_textures_ready
  all: int = 0
  ready: int = 0

  for arr_id in scenes.scene_list:
    arr = scenes.scene_objects[arr_id]
    for item in arr.items():
      item_type = str(type(item[1])).split('.')[1]
      if item_type == 'Animation':
        for frame in item[1].frames:
          all += 1
          if is_texture_ready(frame):
            ready += 1
      elif item_type == 'Image':
        all += 1
        if is_texture_ready(item[1].texture):
          ready += 1
      elif item_type == 'Text':
        all += 1
        if is_font_ready(item[1].font):
          ready += 1

  text = f"progress: {int(100 / all * ready)}%"
  measure = measure_text(text, 14)
  draw_text(text, config.resolution[0] // 2 - measure // 2, config.resolution[1] // 2 + 16, 14, WHITE)
  if all == ready:
    all_textures_ready = True

def animations_draw_debug():
  space = Vector2(10, 630)
  current_scene = list(scenes.scene_objects)[scenes.scene_index]
  arr = scenes.scene_objects[current_scene]
  for item in arr.items():
    item_type = str(type(item[1])).split('.')[1]
    if item_type == 'Animation':
      if space.x < config.resolution[0]:
        name = list(scenes.scene_objects[current_scene].keys())[list(scenes.scene_objects[current_scene].values()).index(item[1])]
        item[1].draw_debug(name, int(space.x), int(space.y))
        space.x += measure_text(item[1].debug_message, 10) + 10




def restart_animations():
  current_scene = list(scenes.scene_objects)[scenes.scene_index]
  arr = scenes.scene_objects[current_scene]
  for item in arr.items():
    item_type = str(type(item[1])).split('.')[1]
    if item_type == 'Animation':
      item[1].restart()


def textures_update():
  broken_order = {}
  current_scene = list(scenes.scene_objects)[scenes.scene_index]
  scene_objects = scenes.scene_objects[current_scene]
  for item in scene_objects.items():
    broken_order[item[1]] = item[1].layer_order
  fixed_order = sorted(broken_order.items(), key=lambda x: x[1])
  for item in fixed_order:
    item[0].update()
