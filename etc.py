from pyray import *
import config

def debug_draw_everywhere_text():
  t_index = config.scenes.scene_index
  t_dict_index = config.scenes.scene_dict[t_index]
  t_changed = config.scenes.scene_changed
  t_current_time = config.scenes.time_current

  text = f"Scene name-index: {t_dict_index}-{t_index}\nScene changed: {t_changed}\nFrame time: {t_current_time}s\n\nFPS: {get_fps()}"
  # n_times = text.count("\n")

  pos = Vector2(0, 0)
  font_size = 14
  text_scale = measure_text_ex(get_font_default(), text, font_size, 1)

  shift = 5

  text_scale.x += shift * 2
  text_scale.y += shift * 2

  # text_scale.y -= shift * (n_times * (shift / ((5/1.3)*((shift/5)**2))))

  pos.x += shift+2
  pos.y += shift+2

  rec = Rectangle(pos.x - shift, pos.y - shift, text_scale.x, text_scale.y)

  alpha = 189
  draw_rectangle_rounded(rec, 0, 0, [0, 0, 0, alpha])
  draw_rectangle_rounded_lines(rec, 0, 0, 2, [255, 255, 255, alpha])
  draw_text(text, int(pos.x), int(pos.y), font_size, WHITE)

def bottom_text_draw(text: str, size: float = 16):
  measure = measure_text_ex(config.def_font, text, size, 0)
  draw_text_ex(config.def_font, text, Vector2(int(config.resolution.x // 2 - measure.x // 2), int(config.resolution.y) - 17.2), size, 0, (255, 255, 255, 153))

def set_fullscreen(key: KeyboardKey = None):
  if config.key_pressed == key:
    config.fullscreen ^= 1

  if (config.fullscreen and not is_window_fullscreen()) or (not config.fullscreen and is_window_fullscreen()):
    toggle_fullscreen()

def xor_debug():
  if config.key_pressed == KeyboardKey.KEY_D:
    config.debug ^= True
