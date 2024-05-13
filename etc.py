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
  t_scroll_left = objects.scenes.scene_variables['game']['scroll_left']
  t_scroll_right = objects.scenes.scene_variables['game']['scroll_right']

  t_broken_light = objects.scenes.scene_variables['game']['light_not_working']
  t_scroll_pos_x = int(objects.scenes.scene_objects['game']['scroll_anchor'].pos.x)

  t_left_light = objects.scenes.scene_variables['game']['light_left_status']
  t_right_light = objects.scenes.scene_variables['game']['light_right_status']

  t_laptop = objects.scenes.scene_variables['game']['gameplay_laptop']
  t_mask = objects.scenes.scene_variables['game']['gameplay_mask']

  text = f"Scroll coords: ({t_scroll_left}, {t_scroll_right})\nScroll anchor x: {t_scroll_pos_x}\n\nBroken light [L]: {int(t_broken_light)}\n\nLeft light: {int(t_left_light)}\nRight light: {int(t_right_light)}\n\nLaptop state: {t_laptop}\nMask state: {t_mask}"

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
  if config.debug:
    if config.key_pressed == KeyboardKey.KEY_L:
      scenes.scene_variables['game']['light_not_working'] ^= True
    if config.key_pressed == KeyboardKey.KEY_MINUS and scenes.scene_objects['game']['ui_battery'].texture_index > 0:
      scenes.scene_objects['game']['ui_battery'].texture_index -= 1
    if config.key_pressed == KeyboardKey.KEY_EQUAL and scenes.scene_objects['game']['ui_battery'].texture_index < 4:
      scenes.scene_objects['game']['ui_battery'].texture_index += 1

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
  ]
  for item in subjects:
    x = object.pos.x + item.offset.x
    y = object.pos.y + item.offset.y
    item.subject.pos = Vector2(x, y)

def call_activation(scenes, audio_check):
  scenes.scene_changed -= 1
  audio_check()
  for scene in scenes.scene_list:
    for item in scenes.scene_timers[scene].items():
      item[1].start_time()

def pullup_camera():
  working = objects.scenes.scene_variables['game']['gameplay_mask'] == 0 or objects.scenes.scene_variables['game']['gameplay_mask'] == 2
  if objects.scenes.scene_objects['game']['ui_cams_button'].hover_activation_verdict and working:
    if objects.scenes.scene_variables['game']['gameplay_laptop'] == 0:
      objects.scenes.scene_variables['game']['gameplay_laptop'] = 1
    elif objects.scenes.scene_variables['game']['gameplay_laptop'] == 3:
      objects.scenes.scene_variables['game']['gameplay_laptop'] = 2

  elif objects.scenes.scene_variables['game']['gameplay_laptop'] == 1 and objects.scenes.scene_objects['game']['laptop'].is_animation_finished:
    objects.scenes.scene_variables['game']['gameplay_laptop'] = 3
  elif objects.scenes.scene_variables['game']['gameplay_laptop'] == 2 and objects.scenes.scene_objects['game']['laptop'].is_animation_finished:
    objects.scenes.scene_variables['game']['gameplay_laptop'] = 0

def pullup_mask():
  working = objects.scenes.scene_variables['game']['gameplay_laptop'] == 0 or objects.scenes.scene_variables['game']['gameplay_laptop'] == 2
  if objects.scenes.scene_objects['game']['ui_mask_button'].hover_activation_verdict and working:
    if objects.scenes.scene_variables['game']['gameplay_mask'] == 0:
      objects.scenes.scene_variables['game']['gameplay_mask'] = 1
    elif objects.scenes.scene_variables['game']['gameplay_mask'] == 3:
      objects.scenes.scene_variables['game']['gameplay_mask'] = 2

  elif objects.scenes.scene_variables['game']['gameplay_mask'] == 1 and objects.scenes.scene_objects['game']['mask'].is_animation_finished:
    objects.scenes.scene_variables['game']['gameplay_mask'] = 3
  elif objects.scenes.scene_variables['game']['gameplay_mask'] == 2 and objects.scenes.scene_objects['game']['mask'].is_animation_finished:
    objects.scenes.scene_variables['game']['gameplay_mask'] = 0

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
