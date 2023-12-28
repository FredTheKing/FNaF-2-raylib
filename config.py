from pyray import *
from raylib.colors import *
from classes.Scene_Manager import Scene_Manager
from etc import *

resolution = Vector2(1024, 768)
init_window(int(resolution.x), int(resolution.y), "Five Nights at Freddy's 2")
init_audio_device()
set_exit_key(KeyboardKey.KEY_F4)
key_pressed: int

actual_night = 0
upcoming_night = 0

debug = True
scenes = Scene_Manager(["menu", "settings", "custom night", "newspaper", "night", "game", "paycheck", "pixel minigame", "creepy minigame"])
