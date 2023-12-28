from pyray import *
import config

def debug_draw_everywhere_text():
  t_dict = config.scenes.scene_dict
  t_index = config.scenes.scene_index
  t_changed = config.scenes.scene_changed
  t_current_time = config.scenes.time_current
  draw_text(f"Scene name-index:\t{t_dict[t_index]}-{t_index}\nScene changed: {t_changed}\nFrame time: {t_current_time}s\n\nFPS: {get_fps()}", 5, 5, 14, (255, 255, 255, 153))

def update_new_key(key: KeyboardKey):
  if config.key_pressed == key:
    config.scenes.scene_index = 0
    config.scenes.scene_changed = True

def set_fullscreen(key: KeyboardKey):
  if config.key_pressed == key:
    config.fullscreen ^= 1

  if config.fullscreen and not is_window_fullscreen():
    toggle_fullscreen()
  elif not config.fullscreen and is_window_fullscreen():
    toggle_fullscreen()

