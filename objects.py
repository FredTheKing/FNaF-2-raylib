from random import randint

from pyray import *
from classes.Time import Time

from classes.Special import Special
from classes.Managers import Scene_Manager
from classes.Text import JustText, BoxText, LinkText, SelectableJustText
from classes.Animation import JustAnimation, SelectableAnimation
from classes.Image import JustImage, BorderImage, BoxImage, SelectableJustImage, DoubleSelectableJustImage, SelectableBoxImage
from classes.Checkbox import Checkbox
from classes.Bar import BarSlider, DigitSlider, TextSlider, BarCircle
from classes.Sound import JustSound

import config
import sys
import os

all_textures_ready = False
release_path = ""

temp_extension = os.path.basename(sys.argv[0])
if temp_extension[temp_extension.rfind(".")::] == ".exe":
  release_path = "_internal/"
  config.release_path = release_path
del temp_extension

config.def_font = load_font(release_path + config.def_font_filename)
config.def_set_sound = load_sound(release_path + config.def_set_sound_filename)

def do_valid_filetype():
  if release_path is not "":
    config.fullscreen = True
    config.debug = False
    scenes.set_scene('preview')

def change_needs() -> None:
  for scene in scenes.scene_list:
    try:
      scenes.scene_objects[scene]['top_text'].center_text()
    except KeyError:
      continue

  scenes.scene_objects['menu']['new_game'].temp_hover = 0
  scenes.scene_objects['menu']['continue'].temp_hover = 0
  scenes.scene_objects['menu']['settings'].temp_hover = 0
  scenes.scene_objects['menu']['extras'].temp_hover = 0
  scenes.scene_objects['menu']['to_test_tp'].click_sound = None

  scenes.scene_objects['extras']['credits_raylib_logo'].resize(Vector2(128, 128))
  scenes.scene_objects['extras']['credits_scott_logo'].resize(Vector2(128, 128))
  scenes.scene_objects['extras']['credits_dudfoot_logo'].resize(Vector2(306, 123))
  scenes.scene_objects['extras']['proj_github'].temp_hover = 0
  scenes.scene_objects['extras']['auth_github'].temp_hover = 0
  scenes.scene_objects['extras']['custom_night'].temp_hover = 0
  scenes.scene_objects['extras']['jumpscares'].temp_hover = 0
  scenes.scene_objects['extras']['development_moments'].temp_hover = 0
  scenes.scene_objects['extras']['credits_text'].click_sound = None


  scenes.scene_objects['custom_night']['slider'].left_button.set_position(Vector2(scenes.scene_objects['custom_night']['slider'].left_button.pos.x, scenes.scene_objects['custom_night']['slider'].left_button.pos.y + 15))
  scenes.scene_objects['custom_night']['slider'].right_button.set_position(Vector2(scenes.scene_objects['custom_night']['slider'].right_button.pos.x, scenes.scene_objects['custom_night']['slider'].right_button.pos.y + 15))
  scenes.scene_objects['custom_night']['with_freddy_text'].center_text(212)
  scenes.scene_objects['custom_night']['with_bonnie_text'].center_text(362)
  scenes.scene_objects['custom_night']['with_chica_text'].center_text(512)
  scenes.scene_objects['custom_night']['with_foxy_text'].center_text(662)
  scenes.scene_objects['custom_night']['golden_freddy_text'].center_text(812)
  scenes.scene_objects['custom_night']['toy_freddy_text'].center_text(212)
  scenes.scene_objects['custom_night']['toy_bonnie_text'].center_text(362)
  scenes.scene_objects['custom_night']['toy_chica_text'].center_text(512)
  scenes.scene_objects['custom_night']['mangle_text'].center_text(662)
  scenes.scene_objects['custom_night']['balloon_boy_text'].center_text(812)
  scenes.scene_objects['custom_night']['confirm_button'].temp_hover = 0
  scenes.scene_objects['custom_night']['start'].temp_hover = 0

  scenes.scene_objects['jumpscares']['office_preview'].resize(Vector2(516, 388))
  scenes.scene_objects['jumpscares']['stack'].resize(Vector2(512, 384))

  scenes.scene_objects['development_moments']['stack'].resize(Vector2(512, 384))
  scenes.scene_objects['development_moments']['dont_aks_me_why'].center_text()

  scenes.scene_objects['night']['night_am'].center_text()
  scenes.scene_objects['night']['night_count'].center_text()

  scenes.scene_objects['test_scene']['circle_button'].click_sound = None

def spec_load_image(filename: str, animation_subtype: bool = False) -> Texture or list[Texture]:
  image = load_texture_from_image(load_image(release_path + filename))
  return [image] if animation_subtype else image

def spec_load_sound(filename: str) -> Sound:
  return load_sound(release_path + filename)

# dirname to dir, not the file!
def spec_load_animation(dirname: str, times: int, is_reversed: bool = False) -> list:
  arr = []
  for item in range(times):
    arr.append(spec_load_image(dirname + f"/{item}.png"))
  return list(reversed(arr)) if is_reversed else arr

# ----------------------------------------------- #


all_objects = {
  'multi>menu|settings|extras|custom_night|jumpscares|development_moments|preview>static': JustAnimation(spec_load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Static", 8), Vector2(0, 0), 26, True, 84, 1),
  'multi>settings|extras|custom_night|jumpscares|development_moments|test_scene>back_button': BoxText("<<", 48, Vector2(10, 10), font_filename="assets/fonts/consolas.ttf"),
  # ----------------------------------------------- #
  'config>actual_night_text': JustText('Actual Night: ', 32, Vector2(300, 100)),
  'config>actual_night_slider': DigitSlider(Vector2(700, 100), Vector2(80, 30), 6, goes_zero=False, default_state=config.actual_night),
  # ----------------------------------------------- #
  'menu>boot_up_white_blinko': Special.WhiteShhrrt(60),
  'menu>twitch': SelectableJustImage([
    spec_load_image("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/still.png"),
    spec_load_image("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/freddy.png"),
    spec_load_image("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/bonnie.png"),
    spec_load_image("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/chica.png"),
  ], Vector2(0, 0), 0),
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
  'settings>volume_slider': BarSlider(Vector2(557, 409), Vector2(300, 40), 6, goes_zero=False, default_state=config.volume),
  'settings>debug_text': JustText("Debug mode: ", 40, Vector2(75, 545)),
  'settings>debug_checkbox': Checkbox(Vector2(890, 547), 40, auto_changing=False),
  # ----------------------------------------------- #
  'extras>top_text': JustText("Extras", 48, Vector2(0, 10)),
  'extras>proj_github': LinkText("https://github.com/FredTheKing/FNaF-2-raylib", "Project's Github", 40, Vector2(75, 200)),
  'extras>auth_github': LinkText("https://github.com/FredTheKing", "Author's Github", 40, Vector2(75, 269)),
  'extras>custom_night': BoxText("Custom night", 40, Vector2(75, 338)),
  'extras>jumpscares': BoxText("Jumpscares", 40, Vector2(75, 407)),
  'extras>development_moments': BoxText("Developments", 40, Vector2(75, 476)),
  'extras>set': JustText(">>", 40, Vector2(22, 201), font_filename="assets/fonts/consolas.ttf"),

  'extras>credits_text': BoxText("Credits:", 40, Vector2(600, 135)),
  'extras>credits_raylib_text': JustText("powered with", 16, Vector2(600, 222), WHITE, 2, font_filename=get_font_default(), spacing=2),
  'extras>credits_raylib_logo': JustImage(spec_load_image("assets/graphics/PreviewLogos/raylib.png"), Vector2(600, 240)),
  'extras>credits_dudfoot_text': JustText("designed and built by", 16, Vector2(600, 422), WHITE, 2, font_filename=get_font_default(), spacing=2),
  'extras>credits_dudfoot_logo': JustImage(spec_load_image("assets/graphics/PreviewLogos/dudfoot.png"), Vector2(600, 450)),
  'extras>credits_scott_text': JustText("OG game idea", 16, Vector2(800, 222), WHITE, 2, font_filename=get_font_default(), spacing=2),
  'extras>credits_scott_logo': JustImage(spec_load_image("assets/graphics/PreviewLogos/scott.png"), Vector2(800, 240)),
  # ----------------------------------------------- #
  'custom_night>top_text': JustText("Custom Night", 48, Vector2(0, 10)),
  # 125x125
  'custom_night>with_freddy': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithFreddy.png"), Vector2(150, 150)),
  'custom_night>with_bonnie': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithBonnie.png"), Vector2(300, 150)),
  'custom_night>with_chica': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithChica.png"), Vector2(450, 150)),
  'custom_night>with_foxy': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithFoxy.png"), Vector2(600, 150)),
  'custom_night>balloon_boy': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/BalloonBoy.png"), Vector2(750, 150)),
  'custom_night>toy_freddy': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyFreddy.png"), Vector2(150, 350)),
  'custom_night>toy_bonnie': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyBonnie.png"), Vector2(300, 350)),
  'custom_night>toy_chica': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/ToyChica.png"), Vector2(450, 350)),
  'custom_night>mangle': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/Mangle.png"), Vector2(600, 350)),
  'custom_night>golden_freddy': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/GoldenFreddy.png"), Vector2(750, 350)),

  'custom_night>with_freddy_text': JustText("W. Freddy", 22, Vector2(212, 128)),
  'custom_night>with_bonnie_text': JustText("W. Bonnie", 22, Vector2(362, 128)),
  'custom_night>with_chica_text': JustText("W. Chica", 22, Vector2(512, 128)),
  'custom_night>with_foxy_text': JustText("W. Foxy", 22, Vector2(662, 128)),
  'custom_night>balloon_boy_text': JustText("BB", 22, Vector2(812, 128)),
  'custom_night>toy_freddy_text': JustText("T. Freddy", 22, Vector2(212, 328)),
  'custom_night>toy_bonnie_text': JustText("T. Bonnie", 22, Vector2(362, 328)),
  'custom_night>toy_chica_text': JustText("T. Chica", 22, Vector2(512, 328)),
  'custom_night>mangle_text': JustText("Mangle", 22, Vector2(662, 328)),
  'custom_night>golden_freddy_text': JustText("G. Freddy", 22, Vector2(812, 328)),

  'custom_night>with_freddy_slider': DigitSlider(Vector2(150, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>with_bonnie_slider': DigitSlider(Vector2(300, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>with_chica_slider': DigitSlider(Vector2(450, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>with_foxy_slider': DigitSlider(Vector2(600, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>balloon_boy_slider': DigitSlider(Vector2(750, 280), Vector2(53, 30), 20, default_state=0),
  'custom_night>toy_freddy_slider': DigitSlider(Vector2(150, 480), Vector2(53, 30), 20, default_state=0),
  'custom_night>toy_bonnie_slider': DigitSlider(Vector2(300, 480), Vector2(53, 30), 20, default_state=0),
  'custom_night>toy_chica_slider': DigitSlider(Vector2(450, 480), Vector2(53, 30), 20, default_state=0),
  'custom_night>mangle_slider': DigitSlider(Vector2(600, 480), Vector2(53, 30), 20, default_state=0),
  'custom_night>golden_freddy_slider': DigitSlider(Vector2(750, 480), Vector2(53, 30), 20, default_state=0),


  'custom_night>slider': TextSlider(Vector2(150, 606), states=['20/20/20/20', 'New & Shiny  ', 'Double Trouble', 'Night of Misfits   ', 'Foxy Foxy', 'Ladies Night   ', "Freddy's Circus", 'Cupcake Challenge', 'Fazbear Fever', 'Golden Freddy'], default_state=0),
  'custom_night>confirm_button': BoxText('APPLY SELECTED', 34, Vector2(202, 636), gray_hover=True),
  
  'custom_night>start': BoxText("START", 48, Vector2(735, 615), gray_hover=True),
  # ----------------------------------------------- #
  'jumpscares>top_text': JustText("Jumpscares", 48, Vector2(0, 10)),
  'jumpscares>office_preview': BorderImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/TheOffice/office_preview.png"), Vector2(config.resolution[0]//2 - 512//2 - 1, config.resolution[1]//2 - 384//2 - 51)),
  'jumpscares>stack': SelectableAnimation([
    spec_load_animation("assets/graphics/Jumpscares/WitheredFreddy", 13),
    spec_load_animation("assets/graphics/Jumpscares/WitheredBonnie", 16),
    spec_load_animation("assets/graphics/Jumpscares/WitheredChica", 12),
    spec_load_animation("assets/graphics/Jumpscares/WitheredFoxy", 14),
    spec_load_animation("assets/graphics/Jumpscares/WitheredGoldenFreddy", 13),
    spec_load_animation("assets/graphics/Jumpscares/ToyFreddy", 12),
    spec_load_animation("assets/graphics/Jumpscares/ToyBonnie", 13),
    spec_load_animation("assets/graphics/Jumpscares/ToyChica", 13),
    spec_load_animation("assets/graphics/Jumpscares/Mangle", 16),
    spec_load_animation("assets/graphics/Jumpscares/TheMarionette", 15)
  ], Vector2(config.resolution[0]//2 - 512//2 + 1, config.resolution[1]//2 - 384//2 - 49), layer=2, animation_speed=20, is_looped=True),

  'jumpscares>selector': TextSlider(Vector2(config.resolution[0]//2 - 512//2 - 1, config.resolution[1]//2 - 384//2 + 350), Vector2(444, 30), default_state=0, states=['Withered Freddy', 'Withered Bonnie', 'Withered Chica', 'Withered Foxy', 'Golden Freddy', 'Toy Freddy', 'Toy Bonnie', 'Toy Chica', 'Mangle', 'Marionette/Puppet']),
  # ----------------------------------------------- #
  'development_moments>top_text': JustText("Developments", 48, Vector2(0, 10)),
  'development_moments>stack': SelectableJustImage([
    spec_load_image("assets/graphics/Development_Moments/boris.png"),
    spec_load_image("assets/graphics/Development_Moments/am_i_right.png"),
    spec_load_image("assets/graphics/Development_Moments/hate_this_thing.png"),
    spec_load_image("assets/graphics/Development_Moments/X).png"),
    spec_load_image("assets/graphics/Development_Moments/poor_restart.png"),
    spec_load_image("assets/graphics/Development_Moments/funkin_no_loop.png"),
    spec_load_image("assets/graphics/Development_Moments/not_tested.png")
  ], Vector2(config.resolution[0]//2 - 512//2 + 1, config.resolution[1]//2 - 384//2 - 49), layer=2),

  'development_moments>selector': TextSlider(Vector2(config.resolution[0]//2 - 512//2 - 1, config.resolution[1]//2 - 384//2 + 350), Vector2(444, 30), default_state=0, states=['boris', 'am i right  ', 'gitignore one love :heart:    ', 'they ARE pretty ;)', 'i fixed it later)0))     ', 'sounds are pain :(  ', 'just checked, its great ']),
  'development_moments>dont_aks_me_why': JustText("do not ask me why these pictures are so funked up", 20, Vector2(0, 736), color=DARKGRAY),
  # ----------------------------------------------- #
  'newspaper>news': BoxImage(spec_load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/Paychecks_Fire/news.png")),
  # ----------------------------------------------- #
  'night>night_am': JustText('12:00 AM', 40, Vector2(350, 320)),
  'night>night_count': JustText('0th Night', 40, Vector2(350, 400)),
  'night>white_blinko': Special.WhiteShhrrt(white_on_start=True),
  # ----------------------------------------------- #
  'game>office_scroll_anchor': Special.InvisibleAnchor(Vector2(-293, 0), Vector2(10, 10), layer=50),
  'game>office_scroll_line': Special.InvisibleAnchor(Vector2(config.resolution[0]//2, 0), Vector2(1, 768), layer=50),
  'game>office_fun_fan': JustAnimation(spec_load_animation('assets/graphics/TheOffice_Nights_Menu/TheOffice/Inside/fun_fan', 4), animation_speed=28, is_looped=True, layer=4),
  'game>office_selectable': SelectableJustImage([
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/office_empty.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Hallway/office_fine_frontlight.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Vents/office_fine_leftlight.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Vents/office_fine_rightlight.png'),

    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/office_broken_frontlight.png'),

    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Inside/office_witheredbonnie_inside.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Inside/office_witheredchica_inside.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Inside/office_witheredfreddy_inside.png'),

    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Vents/office_toychica_leftlight.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Vents/office_bb_leftlight.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Vents/office_toybonnie_rightlight.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/TheOffice/Vents/office_mangle_rightlight.png'),
  ]),
  'game>office_left_light': SelectableBoxImage([
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/OfficeUtilities/office_left_disabled.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/OfficeUtilities/office_left_enabled.png'),
  ]),
  'game>office_right_light': SelectableBoxImage([
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/OfficeUtilities/office_right_disabled.png'),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/OfficeUtilities/office_right_enabled.png'),
  ]),

  'game>camera_white_shhrrt': Special.WhiteShhrrt(9),
  'game>camera_scroll_anchor': Special.InvisibleAnchor(Vector2(-200, 0)),
  'game>camera_static': JustAnimation(spec_load_animation("assets/graphics/TheOffice_Nights_Menu/Menu/Static", 8), Vector2(0, 0), 26, True, 84, 5),
  'game>camera_selectable': DoubleSelectableJustImage([
    [
      spec_load_image('assets/graphics/Locations/Partyrooms/1/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/1/light_empty.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/1/light_withered_bonnie.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/1/light_toy_chica.png.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/Partyrooms/2/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/2/light_empty.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/2/dark_withered_chica.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/2/light_withered_chica.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/2/light_toy_bonnie.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/Partyrooms/3/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/3/light_empty.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/3/dark_withered_freddy.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/3/light_withered_freddy.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/3/light_toy_bonnie.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/Partyrooms/4/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/4/light_empty.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/4/dark_toy_bonnie.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/4/light_toy_bonnie.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/4/light_toy_chica.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/4/light_withered_chica.png'),
      spec_load_image('assets/graphics/Locations/Partyrooms/4/light_easter_egg.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/Vents/Left/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/Vents/Left/light_empty.png'),
      spec_load_image('assets/graphics/Locations/Vents/Left/light_toy_chica.png'),
      spec_load_image('assets/graphics/Locations/Vents/Left/light_withered_bonnie.png'),
      spec_load_image('assets/graphics/Locations/Vents/Left/light_bb.png'),
      spec_load_image('assets/graphics/Locations/Vents/Left/light_endo.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/Vents/Right/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/Vents/Right/light_empty.png'),
      spec_load_image('assets/graphics/Locations/Vents/Right/light_toy_bonnie.png'),
      spec_load_image('assets/graphics/Locations/Vents/Right/light_withered_chica.png'),
      spec_load_image('assets/graphics/Locations/Vents/Right/light_mangle.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/MainHall/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/MainHall/light_empty.png'),
      spec_load_image('assets/graphics/Locations/MainHall/dark_toy_chica.png'),
      spec_load_image('assets/graphics/Locations/MainHall/light_toy_chica.png'),
      spec_load_image('assets/graphics/Locations/MainHall/light_withered_bonnie.png'),
      spec_load_image('assets/graphics/Locations/MainHall/light_withered_freddy.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/Parts_Service/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/Parts_Service/light_empty.png'),
      spec_load_image('assets/graphics/Locations/Parts_Service/light_withered_bonnie_gone.png'),
      spec_load_image('assets/graphics/Locations/Parts_Service/light_withered_freddy_only.png'),
      spec_load_image('assets/graphics/Locations/Parts_Service/light_all_gone.png'),
      spec_load_image('assets/graphics/Locations/Parts_Service/light_withered_foxy_only.png'),
      spec_load_image('assets/graphics/Locations/Parts_Service/light_shadow_only.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/Stage/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/Stage/light_empty.png'),
      spec_load_image('assets/graphics/Locations/Stage/dark_toy_bonnie_gone.png'),
      spec_load_image('assets/graphics/Locations/Stage/light_toy_bonnie_gone.png'),
      spec_load_image('assets/graphics/Locations/Stage/dark_toy_freddy_only.png'),
      spec_load_image('assets/graphics/Locations/Stage/light_toy_freddy_only.png'),
      spec_load_image('assets/graphics/Locations/Stage/dark_all_gone.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Games_Corner/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Games_Corner/light_empty.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Games_Corner/dark_bb_gone.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Games_Corner/light_bb_gone.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Games_Corner/light_toy_freddy_and_bb_gone.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Games_Corner/light_toy_freddy.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Prize_Corner/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Prize_Corner/light_empty.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Prize_Corner/light_marionette_1.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Prize_Corner/light_marionette_2.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Prize_Corner/light_marionette_3.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Prize_Corner/light_endo.png'),
    ],
    [
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Kids_Cove/dark_empty.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Kids_Cove/light_empty.png'),
      spec_load_image('assets/graphics/Locations/KidsCove_Prize_GameCorner/Kids_Cove/light_mangle_gone.png'),
    ]
  ], layer=2),
  'game>map_cams': Special.CameraUI([
    Vector2(587, 575),
    Vector2(720, 576),
    Vector2(586, 508),
    Vector2(722, 508),
    Vector2(592, 670),
    Vector2(715, 670),
    Vector2(742, 450),
    Vector2(588, 437),
    Vector2(900, 408),
    Vector2(833, 528),
    Vector2(934, 484),
    Vector2(921, 577),
  ], 6, 8),

  'game>ui_camera_border': JustImage(spec_load_image('assets/graphics/Monitor_Cameras/CameraUtilities/Monitor_Border.png'), layer=2),
  'game>ui_camera_map': JustImage(spec_load_image('assets/graphics/Monitor_Cameras/CameraUtilities/Map.png'), Vector2(560, 385), 2),
  'game>ui_camera_name': SelectableJustText([
    'Party Room 1',
    'Party Room 2',
    'Party Room 3',
    'Party Room 4',
    'Left Air Vent',
    'Right Air Vent',
    'Main Hall',
    'Parts/Services',
    'Show Stage',
    'Game Area',
    'Prize Corner',
    "Kid's Cove",
  ], Vector2(563, 330), 40, layer=9),
  'game>ui_camera_red': JustImage(spec_load_image('assets/graphics/Monitor_Cameras/CameraUtilities/red.png'), Vector2(49, 93), 9),

  'game>ui_mask_button': BoxImage(spec_load_image('assets/graphics/TheOffice_Nights_Menu/OfficeUtilities/mask.png'), Vector2(10, 720), 40),
  'game>ui_cams_button': BoxImage(spec_load_image('assets/graphics/TheOffice_Nights_Menu/OfficeUtilities/laptop.png'), Vector2(515, 720), 40),

  'game>laptop': SelectableAnimation([
    spec_load_image('assets/graphics/Monitor_Cameras/Monitor/nothing.png', True),
    spec_load_animation('assets/graphics/Monitor_Cameras/Monitor', 11),
    spec_load_animation('assets/graphics/Monitor_Cameras/Monitor', 11, True),
    spec_load_image('assets/graphics/Monitor_Cameras/Monitor/nothing.png', True),
  ], layer=30, animation_speed=23),
  'game>mask': SelectableAnimation([
    spec_load_image('assets/graphics/Monitor_Cameras/Monitor/nothing.png', True),
    spec_load_animation('assets/graphics/TheOffice_Nights_Menu/Mask', 9),
    spec_load_animation('assets/graphics/TheOffice_Nights_Menu/Mask', 9, True),
    spec_load_image('assets/graphics/TheOffice_Nights_Menu/Mask/8.png', True),
  ], layer=30, animation_speed=23),

  'game>ui_battery_text': JustText("flashlight", 16, Vector2(46, 22), layer=40),
  'game>ui_battery': SelectableJustImage([
    spec_load_image('assets/graphics/Monitor_Cameras/Battery/0-4.png'),
    spec_load_image('assets/graphics/Monitor_Cameras/Battery/1-4.png'),
    spec_load_image('assets/graphics/Monitor_Cameras/Battery/2-4.png'),
    spec_load_image('assets/graphics/Monitor_Cameras/Battery/3-4.png'),
    spec_load_image('assets/graphics/Monitor_Cameras/Battery/4-4.png'),
  ], Vector2(39, 35), layer=40),
  # ----------------------------------------------- #
  'preview>logo_text': JustText("powered with", 24, Vector2(config.resolution[0] // 2 - 128, config.resolution[1] // 2 - 154), WHITE, 2, font_filename=get_font_default(), spacing=2),
  'preview>logo': JustImage(spec_load_image("assets/graphics/PreviewLogos/raylib.png"), Vector2(config.resolution[0] // 2 - 128, config.resolution[1] // 2 - 128)),
  # ----------------------------------------------- #
  'test_scene>digit_bar': DigitSlider(Vector2(100, 500)),
  'test_scene>slider': BarSlider(Vector2(100, 600)),
  'test_scene>circle_bar': BarCircle(Vector2(100, 400), default_state=360, speed=10),
  'test_scene>circle_button': BoxText('<------->\nPUSH-HERE\n<------->', 20, Vector2(230, 360)),
}

all_sounds = {
  'menu>reset_sounds': False,
  'menu>activation>menu_music': JustSound(spec_load_sound('assets/audios/The_Sand_Temple_Loop_G.wav'), True),
  # ----------------------------------------------- #
  'settings>reset_sounds': False,
  # ----------------------------------------------- #
  'extras>reset_sounds': False,
  # ----------------------------------------------- #
  'custom_night>reset_sounds': False,
  # ----------------------------------------------- #
  'jumpscares>reset_sounds': False,
  # ----------------------------------------------- #
  'development_moments>reset_sounds': False,
  # ----------------------------------------------- #
  'newspaper>reset_sounds': False,
  # ----------------------------------------------- #
  'night>activation>start_up_sound': JustSound(spec_load_sound(release_path + config.def_set_sound_filename)),
  # ----------------------------------------------- #
  'game>activation>bg_ambience': JustSound(spec_load_sound('assets/audios/CMPTR_Low_Tech_Stat.wav'), True),
  'game>activation>bg_ambience2': JustSound(spec_load_sound('assets/audios/CMPTR_Low_Tech_Stat.wav'), True),
  'game>storage>bg_fan': JustSound(spec_load_sound('assets/audios/fansound.wav'), True),
  'game>storage>light_sound': JustSound(spec_load_sound('assets/audios/buzzlight.wav'), True),
  'game>storage>broken_light': JustSound(spec_load_sound('assets/audios/popstatic.wav'), True),

  'game>storage>mask_breathing': JustSound(spec_load_sound('assets/audios/deepbreaths.wav'), True),
  'game>storage>mask_on': JustSound(spec_load_sound('assets/audios/FENCING_42_GEN-HDF10953.wav')),
  'game>storage>mask_off': JustSound(spec_load_sound('assets/audios/FENCING_43_GEN-HDF10954.wav')),
  'game>storage>laptop_on': JustSound(spec_load_sound('assets/audios/STEREO_CASSETTE__90097701.wav')),
  'game>storage>laptop_off': JustSound(spec_load_sound('assets/audios/STEREO_CASSETTE__90097704.wav')),
  'game>storage>wind_sound': JustSound(spec_load_sound('assets/audios/windup2.wav'), True),
  'game>storage>set_sound': JustSound(spec_load_sound('assets/audios/blip3.wav')),
  # ----------------------------------------------- #
  'test_scene>storage>wind_sound': JustSound(spec_load_sound('assets/audios/windup2.wav')),
}

all_variables = {
  'menu>selected_hover_item': None,
  'menu>selection_arr': None,
  # ----------------------------------------------- #
  'extras>selection_arr': None,
  # ----------------------------------------------- #
  'night>upcoming_end': 'th',
  # ----------------------------------------------- #
  'game>scroll_space': 240,
  'game>scroll_left': 0,
  'game>scroll_right': 0,
  'game>scroll_sensitivity': 37,

  'game>gameplay_battery': 4,
  'game>gameplay_mask': 0,
  'game>gameplay_laptop': 0,
  
  'game>light_left_status': False,
  'game>light_right_status': False,
  'game>light_not_working': False,

  'game>camera_scroll_state': 0  # 0 - goto left, 1 - standstill left, 2 - goto right, 3 - standstill right
}

all_timers = {
  'menu>bottom_text_change': Time(0.25),
  'menu>random_twitch': Time(10),
  # ----------------------------------------------- #
  'game>camera_scroll': Time(1),
  'game>red_timer': Time(1),
}

scenes = Scene_Manager(["config", "menu", "settings", "extras", "custom_night", "jumpscares", "development_moments", "newspaper", "night", "game", "win_or_lose", "paycheck", "pixel_minigame", "creepy_minigame", "loading", "error", "preview", "test_scene"], all_objects, all_sounds, all_variables, all_timers)

del all_objects, all_sounds
change_needs()


# ----------------------------------------------- #

def unload_all_textures(mod: int = -1):
  a = 0
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
        item[1].draw_debug(item[0], int(space.x), int(space.y))
        space.x += measure_text(item[1].debug_message, 10) + 10


def sounds_draw_debug():
  space = Vector2(10, 524)  # 16px = new line
  current_scene = list(scenes.scene_objects)[scenes.scene_index]
  arr = scenes.scene_sounds[current_scene]
  for group_dict in arr.items():
    try:
      for item in group_dict[1].items():
        item_type = str(type(item[1])).split('.')[1]
        if item_type == 'Sound':
          if space.x < config.resolution[0]:
            item[1].draw_debug(item[0], group_dict[0], int(space.x), int(space.y))
            space.x += measure_text(item[1].debug_message, 10) + 10
    except AttributeError:
      pass




def restart_animations():
  current_scene = list(scenes.scene_objects)[scenes.scene_index]
  arr = scenes.scene_objects[current_scene]
  for item in arr.items():
    item_type = str(type(item[1])).split('.')[1]
    if item_type == 'Animation':
      item[1].restart()


def process_update():
  # textures
  broken_order = {}
  current_scene = list(scenes.scene_objects)[scenes.scene_index]
  scene_objects = scenes.scene_objects[current_scene]
  for item in scene_objects.items():
    try:
      layer = item[1].layer_order
    except AttributeError:
      print(f"{'\033[93m'}error DING! object {item[1]} doesnt have 'layer_order' field!{'\033[0m'}")
    finally:
      if layer not in scenes.hidden_layers:
        broken_order[item[1]] = item[1].layer_order
  fixed_order = sorted(broken_order.items(), key=lambda x: x[1])
  for item in fixed_order:
    item[0].update()


  # audios and timers
  for scene in scenes.scene_list:
    for mode in 'activation', 'storage':
      for item in scenes.scene_sounds[scene][mode].items():
        item[1].update()

    for item in scenes.scene_timers[scene].items():
      item[1].update_time()

def reset_sounds():
  for scene in scenes.scene_list:
    for item in scenes.scene_sounds[scene]['activation'].items():
      item[1].stop()
      item[1].update()
    for item in scenes.scene_sounds[scene]['storage'].items():
      item[1].stop()
      item[1].update()

def audio_activation_update():
  current_scene = list(scenes.scene_objects)[scenes.scene_index]
  scene_sounds = scenes.scene_sounds[current_scene]
  if scene_sounds['reset_sounds']:
    reset_sounds()

  for item in scene_sounds['activation'].items():
    item[1].play()
