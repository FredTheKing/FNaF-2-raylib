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

debug_animatronics_positions = {
  '1': Vector2(527, 564),
  '2': Vector2(780, 565),
  '3': Vector2(532, 500),
  '4': Vector2(782, 500),
  '5': Vector2(542, 642),
  '6': Vector2(776, 642),
  '7': Vector2(694, 430),
  '8': Vector2(588, 392),
  '9': Vector2(850, 388),
  '10': Vector2(833, 480),
  '11': Vector2(888, 470),
  '12': Vector2(881, 582),
  'HALLWAY': Vector2(664, 562),
  'INSIDE': Vector2(664, 642),
}
aggressive = 0
animatronics_arr: list[Special.Animatronic] = [
  Special.Animatronic(
    'Withered_Freddy',
    'assets/graphics/Monitor_Cameras/DebugAnimatronics/WitheredFreddy.png',
    'BLACKOUT',
    #  BLACKOUT - Withered animatronics and golden dude
    #  FLASH - Withered foxy
    #  SIBLINGS - Toy Bonnie and Toy Chica
    #  SITTER - Mangle and bb
    #  MUSIC - Marionette
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
      'HALLWAY<Withered_Foxy|Withered_Bonnie|Toy_Freddy|Toy_Chica|Mangle|Golden_Freddy',
      'INSIDE<Toy_Freddy|Toy_Bonnie|Toy_Chica|Withered_Bonnie|Withered_Chica',
      #  ROOM<ANIMATRONIC1|ANIMATRONIC2|ANIMATRONIC3
      #  ROOM - the room that main animatronic is trying to get into
      #  ANIMATRONIC1|ANIMATRONIC2 etc. - what animatronics have not to be on a room you declared a moment before
      #  (| - OR between all animatronics)
    ],
    'INSIDE',
  ),
  Special.Animatronic(
    'Withered_Bonnie',
    'assets/graphics/Monitor_Cameras/DebugAnimatronics/WitheredBonnie.png',
    'BLACKOUT',
    [
      '8>HALLWAY-60|7-40',
      '7>HALLWAY-70|1-30',
      '1>5-70|HALLWAY-30',
      '5>INSIDE-100',
      'HALLWAY>INSIDE-50|1-50',
    ],
    [
      '7<Withered_Freddy|Toy_Chica',
      '1<Toy_Chica',
      '5<Toy_Chica|Balloon_Boy',
      'HALLWAY<Mangle|Golden_Freddy|Toy_Chica|Toy_Freddy|Withered_Freddy',
      'INSIDE<Toy_Freddy|Toy_Bonnie|Toy_Chica|Withered_Freddy|Withered_Chica'
    ],
    'INSIDE',
  ),
  Special.Animatronic(
    'Withered_Chica',
    'assets/graphics/Monitor_Cameras/DebugAnimatronics/WitheredChica.png',
    'BLACKOUT',
    [
      '8>4-50|2-50',
      '4>2-100',
      '2>6-80|4-20',
      '6>INSIDE-100',
    ],
    [
      '4<Toy_Chica|Toy_Bonnie',
      '2<Toy_Bonnie',
      '6<Toy_Bonnie|Mangle',
      'INSIDE<Toy_Freddy|Toy_Bonnie|Toy_Chica|Withered_Freddy|Withered_Bonnie'
    ],
    'INSIDE',
  ),
  Special.Animatronic(
    'Withered_Foxy',
    'assets/graphics/Monitor_Cameras/DebugAnimatronics/Foxy.png',
    'FLASH',
    [
      '8>HALLWAY-100',
      'HALLWAY>INSIDE-100',
    ],
    [
      'HALLWAY<Golden_Freddy|Toy_Chica|Toy_Freddy|Withered_Freddy',
    ],
    'INSIDE',
  ),
  Special.Animatronic(
    'Balloon_Boy',
    'assets/graphics/Monitor_Cameras/DebugAnimatronics/BB.png',
    'SITTER',
    [
      '10>5-100',
      '5>INSIDE-100',
    ],
    [
      '5<Withered_Bonnie|Toy_Chica',
    ],
    'INSIDE',
  ),
  Special.Animatronic(
    'Toy_Freddy',
    'assets/graphics/Monitor_Cameras/DebugAnimatronics/ToyFreddy.png',
    'BLACKOUT',
    [
      '9>HALLWAY-60|10-40',
      '10>HALLWAY-100',
      'HALLWAY>INSIDE-100',
    ],
    [
      'HALLWAY<Withered_Freddy|Withered_Foxy|Withered_Bonnie|Toy_Chica|Mangle|Golden_Freddy',
      'INSIDE<Withered_Freddy|Withered_Bonnie|Withered_Chica|Toy_Bonnie|Toy_Chica',
    ],
    'INSIDE',
  ),
  Special.Animatronic(
    'Toy_Bonnie',
    'assets/graphics/Monitor_Cameras/DebugAnimatronics/ToyBonnie.png',
    'SIBLINGS',
    [
      '9>2-40|3-30|4-30',
      '2>6-90|4-10',
      '4>2-90|3-5|6-5',
      '3>2-70|4-30',
      '6>INSIDE-100',
    ],
    [
      '3<Withered_Freddy',
      '4<Toy_Chica|Withered_Chica',
      '6<Mangle|Withered_Chica',
      '2<Withered_Chica',
      'INSIDE<Withered_Freddy|Withered_Bonnie|Withered_Chica|Toy_Freddy|Toy_Chica',
    ],
    'INSIDE',
  ),
  Special.Animatronic(
    'Toy_Chica',
    'assets/graphics/Monitor_Cameras/DebugAnimatronics/ToyFreddy.png',
    'SIBLINGS',
    [
      '9>7-70|4-20|HALLWAY-10',
      '7>HALLWAY-60|4-20|1-20',
      '4>HALLWAY-80|1-20',
      'HALLWAY>1-95|4-5'
      '1>HALLWAY-50|5-50',
      '5>INSIDE-100',
    ],
    [
      '7<Withered_Freddy|Withered_Bonnie',
      '4<Withered_Chica|Toy_Bonnie',
      '1<Withered_Bonnie',
      '5<Balloon_Boy|Withered_Bonnie',
      'HALLWAY<Withered_Freddy|Withered_Foxy|Withered_Bonnie|Toy_Freddy|Mangle|Golden_Freddy',
      'INSIDE<Withered_Freddy|Withered_Bonnie|Withered_Chica|Toy_Bonnie|Toy_Freddy',
    ],
    'INSIDE',
  ),
  # Special.Animatronic('Mangle', ['12', '11', '10', '7', '1', '2', '6']),
  # Special.Animatronic('Golden_Freddy', []),
]
