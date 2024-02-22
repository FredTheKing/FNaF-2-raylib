from pyray import *
import screeninfo

def get_res():
  screen_info = screeninfo.get_monitors()
  for screen in screen_info:
    return screen.width, screen.height


resolution = (1024, 768)
init_window(resolution[0], resolution[1], "Five Nights at Freddy's 2")
init_audio_device()
set_window_icon(load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/WithChica.png"))
key_pressed: int
set_target_fps(-1)
def_font_filename = "assets/fonts/regular.ttf"
def_font: Font

actual_night = 0
upcoming_night = 0

fullscreen = False
wait_textures = False
funny = False
debug = True
volume = 6
screen_resolution = get_res()
