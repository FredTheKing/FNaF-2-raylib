from classes.Scene_Manager import Scene_Manager
from etc import *

resolution = Vector2(1024, 768)
init_window(int(resolution.x), int(resolution.y), "Five Nights at Freddy's 2")
init_audio_device()
set_window_icon(load_image("assets/graphics/TheOffice_Nights_Menu/Nights_CustomNight/CustomNightIcons/338.png"))
key_pressed: int
set_target_fps(-1)
mouse = get_mouse_position()

actual_night = 0
upcoming_night = 0

wait_textures = False
debug = True
fullscreen = False
scenes = Scene_Manager(["menu", "settings", "custom night", "newspaper", "night", "game", "paycheck", "pixel minigame", "creepy minigame", "loading", "error boot"])
