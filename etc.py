from random import randint
from pyray import *
import config
import objects


def debug_draw_everywhere_text():
  t_index = objects.scenes.scene_index
  t_list_index = objects.scenes.scene_list[t_index]
  t_changed = objects.scenes.scene_changed
  t_current_time = objects.scenes.time_current
  t_actual_night = config.actual_night
  t_upcoming_night = config.upcoming_night
  t_fps = get_fps()
  t_ms = config.delta
  t_volume = str(round(config.volume * 100)) + '%'
  t_hold = config.ctrl_hold

  text = f"Scene name-index: {t_list_index}-{t_index}\nScene changed: {t_changed}\nFrame time: {t_current_time}s\n\nActual night: {t_actual_night}\nUpcoming night: {t_upcoming_night}\n\nFPS: {t_fps}\nMS: {t_ms}\n\nVolume: {t_volume}\nHold: {t_hold}"

  pos = Vector2(0, 0)
  font_size = 14
  text_scale = measure_text_ex(get_font_default(), text, font_size, 1)

  shift = 5

  text_scale.x += shift * 2
  text_scale.y += shift * 2

  pos.x += shift+3
  pos.y += shift+3

  rec = Rectangle(pos.x - shift, pos.y - shift, text_scale.x, text_scale.y)

  alpha = 189
  draw_rectangle_rounded(rec, 0, 0, [0, 0, 0, alpha])
  draw_rectangle_rounded_lines(rec, 0, 0, 2, [255, 255, 255, alpha])
  draw_text(text, int(pos.x), int(pos.y), font_size, WHITE)

def debug_draw_game_text():
  t_broken_light = objects.scenes.scene_variables['game']['light_not_working']

  text = f"Broken light: {t_broken_light}"

  pos = Vector2(0, 0)
  font_size = 14
  text_scale = measure_text_ex(get_font_default(), text, font_size, 1)

  shift = 5

  text_scale.x += shift * 2
  text_scale.y += shift * 2

  pos.x += config.resolution[0] + 2 - int(text_scale.x)
  pos.y += shift+3

  rec = Rectangle(pos.x - shift, pos.y - shift, text_scale.x, text_scale.y)

  alpha = 189
  draw_rectangle_rounded(rec, 0, 0, [0, 0, 0, alpha])
  draw_rectangle_rounded_lines(rec, 0, 0, 2, [255, 255, 255, alpha])
  draw_text(text, int(pos.x), int(pos.y), font_size, WHITE)

def bottom_text_draw(text: str, size: float = 16):
  measure = measure_text_ex(config.def_font, text, size, 0)
  draw_text_ex(config.def_font, text, Vector2(config.resolution[0] // 2 - measure.x // 2, config.resolution[1] - 17.2), size, 0, [255, 255, 255, 153])

def tests_do_testing(scenes):
  objects = [
    scenes.scene_objects['game']['testos_broke_light']
  ]
  if config.debug:
    if objects[0].clicked_verdict:
      scenes.scene_variables['game']['light_not_working'] ^= True

def funny_mode(mod: int = 1):
  x_mod = mod
  y_mod = round(mod*(9/16))

  x = config.screen_resolution[0]//2 - config.resolution[0]//2 + randint(x_mod*-1, x_mod+1)
  y = config.screen_resolution[1]//2 - config.resolution[1]//2 + randint(y_mod*-1, y_mod+1)
  set_window_position(x, y)

def border_anchor_point(object):
  right_border = 576

  if object.pos.x > 0: object.pos.x = 0
  elif object.pos.x < right_border*-1: object.pos.x = right_border*-1

def glue_subjects_to_object(scenes):
  class SetGlueOffset:
    def __init__(self, subject, offset: Vector2 = Vector2(0, 0)):
      self.subject = subject
      self.offset = offset

  object = scenes.scene_objects['game']['scroll_anchor']
  subjects = [
    SetGlueOffset(scenes.scene_objects['game']['office_selectable']),
    SetGlueOffset(scenes.scene_objects['game']['office_fun_fan'], Vector2(560, 333)),
    SetGlueOffset(scenes.scene_objects['game']['office_left_light'], Vector2(90, 356)),
    SetGlueOffset(scenes.scene_objects['game']['office_right_light'], Vector2(1420, 356)),
    SetGlueOffset(scenes.scene_objects['game']['testos_broke_light'], Vector2(100, 100)),
  ]
  for item in subjects:
    x = object.pos.x + item.offset.x
    y = object.pos.y + item.offset.y
    item.subject.pos = Vector2(x, y)

def global_keys_update():
  config.key_pressed = get_key_pressed()
  config.ctrl_hold = is_key_down(KeyboardKey.KEY_LEFT_CONTROL)

def define_ending(night: int) -> str:
  if night == 1:
    return 'st'
  elif night == 2:
    return 'nd'
  elif night == 3:
    return 'rd'
  else:
    return 'th'

def set_fullscreen(key: KeyboardKey = None):
  if config.key_pressed == key:
    config.fullscreen ^= 1

  if (config.fullscreen and not is_window_fullscreen()) or (not config.fullscreen and is_window_fullscreen()):
    toggle_fullscreen()

def volume_makes_sense(value: objects.BarSlider):
  config.volume = 1 / value.states * value.current_state
  set_master_volume(config.volume)

def xor_debug():
  if config.key_pressed == KeyboardKey.KEY_D:
    config.debug ^= True
