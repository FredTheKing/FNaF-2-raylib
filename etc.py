from random import randint
from pyray import *
import config
import objects


def debug_draw_everywhere_text():
  t_index = objects.scenes.scene_index
  t_dict_index = objects.scenes.scene_dict[t_index]
  t_changed = objects.scenes.scene_changed
  t_current_time = objects.scenes.time_current
  t_fps = get_fps()
  t_ms = get_frame_time() * 1000

  text = f"Scene name-index: {t_dict_index}-{t_index}\nScene changed: {t_changed}\nFrame time: {t_current_time}s\n\nFPS: {t_fps}\nMS: {t_ms}"

  pos = Vector2(0, 0)
  font_size = 14
  text_scale = measure_text_ex(get_font_default(), text, font_size, 1)

  shift = 5

  text_scale.x += shift * 2
  text_scale.y += shift * 2

  pos.x += shift+2
  pos.y += shift+2

  rec = Rectangle(pos.x - shift, pos.y - shift, text_scale.x, text_scale.y)

  alpha = 189
  draw_rectangle_rounded(rec, 0, 0, [0, 0, 0, alpha])
  draw_rectangle_rounded_lines(rec, 0, 0, 2, [255, 255, 255, alpha])
  draw_text(text, int(pos.x), int(pos.y), font_size, WHITE)

def bottom_text_draw(text: str, size: float = 16):
  measure = measure_text_ex(config.def_font, text, size, 0)
  draw_text_ex(config.def_font, text, Vector2(config.resolution[0] // 2 - measure.x // 2, config.resolution[1] - 17.2), size, 0, (255, 255, 255, 153))

def funny_mode(mod: int = 1):
  x_mod = mod
  y_mod = round(mod*(9/16))

  x = config.screen_resolution[0]//2 - config.resolution[0]//2 + randint(x_mod*-1, x_mod+1)
  y = config.screen_resolution[1]//2 - config.resolution[1]//2 + randint(y_mod*-1, y_mod+1)
  set_window_position(x, y)

def set_fullscreen(key: KeyboardKey = None):
  if config.key_pressed == key:
    config.fullscreen ^= 1

  if (config.fullscreen and not is_window_fullscreen()) or (not config.fullscreen and is_window_fullscreen()):
    toggle_fullscreen()

def xor_debug():
  if config.key_pressed == KeyboardKey.KEY_D:
    config.debug ^= True
