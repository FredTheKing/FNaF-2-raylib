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
  t_office_scroll_pos_x = int(objects.scenes.scene_objects['game']['office_scroll_anchor'].pos.x)
  t_camera_scroll_pos_x = int(objects.scenes.scene_objects['game']['camera_scroll_anchor'].pos.x)

  t_camera_state = objects.scenes.scene_variables['game']['camera_scroll_state']
  t_camera_timer = objects.scenes.scene_timers['game']['camera_scroll']

  t_left_light = objects.scenes.scene_variables['game']['light_left_status']
  t_right_light = objects.scenes.scene_variables['game']['light_right_status']

  t_laptop = objects.scenes.scene_variables['game']['gameplay_laptop']
  t_mask = objects.scenes.scene_variables['game']['gameplay_mask']

  text = f"Scroll coords: ({t_scroll_left}, {t_scroll_right})\nOffice scroll anchor x: {t_office_scroll_pos_x}\nCamera scroll anchor x: {t_camera_scroll_pos_x}\n\nCamera scroll state: {t_camera_state}\nCamera scroll timer: {t_camera_timer.time_current}\n\nBroken light [L]: {int(t_broken_light)}\n\nLeft light: {int(t_left_light)}\nRight light: {int(t_right_light)}\n\nLaptop state: {t_laptop}\nMask state: {t_mask}"

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

def border_office_anchor_point():
  object = objects.scenes.scene_objects['game']['office_scroll_anchor']
  right_border = 576

  if object.pos.x > 0: object.pos.x = 0
  elif object.pos.x < right_border*-1: object.pos.x = right_border*-1

def camera_anchor_point_walking():
  object = objects.scenes.scene_objects['game']['camera_scroll_anchor']
  state = objects.scenes.scene_variables['game']['camera_scroll_state']
  timer = objects.scenes.scene_timers['game']['camera_scroll']
  right_border = 576

  if object.pos.x >= 0:
    if state == 0:
      objects.scenes.scene_variables['game']['camera_scroll_state'] = 1
      timer.start_time()
      objects.scenes.scene_objects['game']['camera_scroll_anchor'].pos.x = 0

  elif object.pos.x <= right_border * -1:
    if state == 2:
      objects.scenes.scene_variables['game']['camera_scroll_state'] = 3
      timer.start_time()
      objects.scenes.scene_objects['game']['camera_scroll_anchor'].pos.x = right_border * -1

  if timer.time_current >= 4:
      timer.kill_time()
      if state == 1:
        objects.scenes.scene_variables['game']['camera_scroll_state'] = 2
      elif state == 3:
        objects.scenes.scene_variables['game']['camera_scroll_state'] = 0

  if state == 0:
    object.pos.x += 0.081 * config.delta
  elif state == 2:
    object.pos.x -= 0.081 * config.delta

  if objects.scenes.scene_objects['game']['camera_selectable'].pack_index not in range(0, 6):
    objects.scenes.scene_objects['game']['camera_selectable'].pos.x = object.pos.x
  else:
    objects.scenes.scene_objects['game']['camera_selectable'].pos.x = 0

def left_vent_light():
  if objects.scenes.scene_variables['game']['light_left_status']:
    objects.scenes.scene_objects['game']['office_left_light'].texture_index = 1
    objects.scenes.scene_objects['game']['office_selectable'].texture_index = 2
  else:
    objects.scenes.scene_objects['game']['office_left_light'].texture_index = 0

def right_vent_light():
  if objects.scenes.scene_variables['game']['light_right_status']:
    objects.scenes.scene_objects['game']['office_right_light'].texture_index = 1
    objects.scenes.scene_objects['game']['office_selectable'].texture_index = 3
  else:
    objects.scenes.scene_objects['game']['office_right_light'].texture_index = 0

def sync_camera_selectable_with_map():
  objects.scenes.scene_objects['game']['camera_selectable'].pack_index = objects.scenes.scene_objects['game']['map_cams'].picked
  objects.scenes.scene_objects['game']['ui_camera_name'].word_index = objects.scenes.scene_objects['game']['map_cams'].picked
  if objects.scenes.scene_objects['game']['map_cams'].pick_changed:
    objects.scenes.scene_objects['game']['camera_white_shhrrt'].go = True

def animatronics_restored():
  for item in config.animatronics_arr:
    item.restore_position()
    item.timer.start_time()

def jumpscare_finished():
  jump = objects.scenes.scene_objects['game']['ui_jumpscares']
  if jump.animation_index and jump.is_animation_ended:
    objects.scenes.set_scene('win_or_lose')
    objects.scenes.scene_variables['win_or_lose']['won'] = False

def six_am_event():
  if objects.scenes.time_current >= 408:  # 408 is right
    objects.scenes.set_scene('win_or_lose')
    objects.scenes.scene_variables['win_or_lose']['won'] = True

def layers_camera_changing():
  if objects.scenes.scene_variables['game']['gameplay_laptop'] == 3:
    objects.scenes.hide_layer([1, 4])
    objects.scenes.show_layer([2, 5, 9, 6])
  else:
    objects.scenes.show_layer([1, 4])
    objects.scenes.hide_layer([2, 5, 9, 6])

class glue_subjects_to_object:
  class SetGlueOffset:
    def __init__(self, subject, offset: Vector2 = Vector2(0, 0)):
      self.subject = subject
      self.offset = offset

  def office(self):
    object = objects.scenes.scene_objects['game']['office_scroll_anchor']
    subjects = [
      self.SetGlueOffset(objects.scenes.scene_objects['game']['office_selectable']),
      self.SetGlueOffset(objects.scenes.scene_objects['game']['office_fun_fan'], Vector2(560, 333)),
      self.SetGlueOffset(objects.scenes.scene_objects['game']['office_left_light'], Vector2(90, 356)),
      self.SetGlueOffset(objects.scenes.scene_objects['game']['office_right_light'], Vector2(1420, 356)),
    ]
    for item in subjects:
      x = object.pos.x + item.offset.x
      y = object.pos.y + item.offset.y
      item.subject.pos = Vector2(x, y)

  def camera(self):
    object = objects.scenes.scene_objects['game']['camera_scroll_anchor']
    subjects = [

    ]
    for item in subjects:
      x = object.pos.x + item.offset.x
      y = object.pos.y + item.offset.y
      item.subject.pos = Vector2(x, y)

def call_activation(audio_check):
  objects.scenes.scene_changed -= 1
  audio_check()
  for scene in objects.scenes.scene_list:
    for item in objects.scenes.scene_timers[scene].items():
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
