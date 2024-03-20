from pyray import *
import screeninfo

def get_res():
  screen_info = screeninfo.get_monitors()
  for screen in screen_info:
    return screen.width, screen.height


resolution = (1024, 768)
screen_resolution = get_res()
init_window(resolution[0], resolution[1], "Five Nights at Freddy's 2")
init_audio_device()
set_window_icon(load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithChica.png"))
key_pressed: int
set_target_fps(-1)
def_font_filename = "assets/fonts/regular.ttf"
def_font: Font
def_set_sound: Sound

actual_night = 0
upcoming_night = 0

fullscreen = False
wait_textures = False
funny = False
debug = True
volume = 1
show_preview = False

difficulty_withered_freddy = 0
difficulty_withered_bonnie = 0
difficulty_withered_chica = 0
difficulty_withered_foxy = 0
difficulty_golden_freddy = 0
difficulty_toy_freddy = 0
difficulty_toy_bonnie = 0
difficulty_toy_chica = 0
difficulty_mangle = 0
difficulty_balloon_boy = 0
