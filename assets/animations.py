import time
from pyray import *
from classes.Animation import Animation
from classes.Time import Time

all_is_ready: bool = False

menu_twitching = Animation(
  [
    load_texture_from_image(load_image("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/321.png")),
    load_texture_from_image(load_image("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/215.png")),
    load_texture_from_image(load_image("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/362.png")),
    load_texture_from_image(load_image("assets/graphics/TheOffice_Nights_Menu/Menu/Misc/470.png")),
  ], 0, 0, 0, True
)

menu_animations_list = [menu_twitching]

def textures_activation():
  for item in menu_animations_list:
    item.start_time()

def textures_update():
  for item in menu_animations_list:
    item.update()

def textures_draw():
  for item in menu_animations_list:
    item.draw()
