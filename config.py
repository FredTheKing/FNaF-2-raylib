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
release_path = ''

actual_night = 1
upcoming_night = 0

fullscreen = False
wait_textures = False
funny = False
debug = True
volume = 1
show_preview = False
blinko_after_preview = False

animatronics_arr = [
  Special.Animatronic(
    'Withered_Freddy',
    'OLD',
    #  OLD - Withered animatronics and golden dude
    #  NEW - Toy animatronics
    #  OFFICE_STAYER - Mangle and bb
    #  MARIONETTE - Marionette
    '8|7|3|HALLWAY|INSIDE',
    [
      '8>7-100',
      '7>HALLWAY-60|3-40',
      '3>HALLWAY-76|7-24',
      'HALLWAY>INSIDE-100',
      #  FROM_WHERE>TO_WHERE1-PERCENT1|TO_WHERE2-PERCENT2
      #  FROM_WHERE - from what room you need to move
      #  TO_WHERE1, TO_WHERE2 etc. - the room to which the animatronic must move
      #  PERCENT1, PERCENT2 etc. - chance of room changing (all of percents MUST be summed up to 100)
      #  (| - OR between all animatronics)
    ],
    [
      '7<Toy_Chica|Withered_Bonnie',
      'HALLWAY<Withered_Foxy|Withered_Bonnie|Toy_Freddy|Toy_Chica|Mangle|Golden_Freddy'
      'INSIDE<Toy_Bonnie|Toy_Chica|Withered_Bonnie|Withered_Chica'
      #  ROOM<ANIMATRONIC1|ANIMATRONIC2|ANIMATRONIC3
      #  ROOM - the room that main animatronic is trying to get into
      #  ANIMATRONIC1|ANIMATRONIC2 etc. - what animatronics have not to be on a room you declared a moment before
      #  (| - AND between all animatronics)
    ],
    'INSIDE',
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
