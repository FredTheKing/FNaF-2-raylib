from pyray import *
import screeninfo

from classes.Special import Special


def get_res():
  screen_info = screeninfo.get_monitors()
  for screen in screen_info:
    return screen.width, screen.height

def set_night(night: int, actual_or_upcoming: bool = True):
  if actual_or_upcoming:
    global upcoming_night
    upcoming_night = night
  else:
    global actual_night
    actual_night = night


resolution = (1024, 768)
screen_resolution = get_res()
init_window(resolution[0], resolution[1], "Five Nights at Freddy's 2")
init_audio_device()
set_window_icon(load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithChica.png"))
key_pressed: int
ctrl_hold: bool = False
delta: float
set_target_fps(-1)
def_font_filename = "assets/fonts/regular.ttf"
def_set_sound_filename = "assets/audios/blip3.wav"
def_font: Font
def_set_sound: Sound

actual_night = 1
upcoming_night = 0

fullscreen = False
wait_textures = False
funny = False
debug = True
volume = 1
show_preview = False

animatronics_arr = [
  Special.Animatronic(
    'Withered_Freddy',
    '8|7|3|OFFICE_HALLWAY',
    [
      '8>7-100',
      '7>OFFICE_HALLWAY-80|3-20',
      '3>OFFICE_HALLWAY-97|7-3',
    ],
    'HALLWAY|INSIDE',
    [
      'FAR',
    ],
  ),
  # Special.Animatronic('Withered_Bonnie', ['8', '7', '1', '5', '']),
  # Special.Animatronic('Withered_Chica', ['8', '4', '2', '6']),
  # Special.Animatronic('Withered_Foxy', ['8', '']),
  # Special.Animatronic('Balloon_Boy', ['10', '5']),
  # Special.Animatronic('Toy_Freddy', ['9', '10', '']),
  # Special.Animatronic('Toy_Bonnie', ['9', '3', '4', '2', '6']),
  # Special.Animatronic('Toy_Chica', ['9', '7', '4', '1', '5']),
  # Special.Animatronic('Mangle', ['12', '11', '10', '7', '1', '2', '6']),
  # Special.Animatronic('Golden_Freddy', []),
]
