import random

from classes.Time import Time
from config import set_night
from etc import *
from objects import *

def main():
  check_textures_time = Time(1)
  check_textures_time.start_time()
  while not window_should_close():
    current_scene = scenes.scene_list[scenes.scene_index]
    process_update()

# ----------------------------------------------- #

    if current_scene == "config":
      # activation
      if scenes.scene_changed:
        audio_activation_update()
        scenes.scene_changed -= 1

      # step
      set_night(scenes.scene_objects['config']['actual_night_slider'].current_state, False)

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "menu":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)
        scenes.scene_variables['menu']['selection_arr'] = [
          scenes.scene_objects['menu']['new_game'],
          scenes.scene_objects['menu']['continue'],
          scenes.scene_objects['menu']['settings'],
          scenes.scene_objects['menu']['extras'],
        ]
        if config.blinko_after_preview:
          scenes.scene_objects['menu']['boot_up_white_blinko'].go = True
          config.blinko_after_preview = False

      # step
      if scenes.scene_timers['menu']['bottom_text_change'].time_current % 2 == 0:
        bottom_text_draw("Original game by: Scott Cawthon\t\t\t\t\tGame built by: FredTheKing\t\t\t\t\tMade in Python 3.12 with raylib (pyray)")
      else:
        bottom_text_draw("Project's, Author's links and much more are in Extras menu\t\t\t\t\tManipulate game settings in Settings menu")

      if scenes.scene_objects['menu']['to_test_tp'].clicked_verdict and config.debug:
        scenes.set_scene('test_scene')

      for item in scenes.scene_variables['menu']['selection_arr']:
        if item.hover_verdict:
          scenes.scene_objects['menu']['set'].pos.y = item.pos.y + 1
          scenes.scene_variables['menu']['selected_hover_item'] = item

      if scenes.scene_objects['menu']['new_game'].clicked_verdict:
        set_night(1, False)
        set_night(config.actual_night)
        scenes.set_scene('newspaper')
      elif scenes.scene_objects['menu']['continue'].clicked_verdict:
        set_night(config.actual_night)
        if config.upcoming_night == 1:
          scenes.set_scene('newspaper')
        else:
          scenes.set_scene('night')
      elif scenes.scene_objects['menu']['settings'].clicked_verdict:
        scenes.set_scene('settings')
      elif scenes.scene_objects['menu']['extras'].clicked_verdict:
        scenes.set_scene('extras')

      if scenes.scene_timers['menu']['random_twitch'].time_current:
        scenes.scene_timers['menu']['random_twitch'].start_time()
        rand = random.randint(0, 100)
        if rand <= 85:
          scenes.scene_objects['menu']['twitch'].texture_index = 0
        if 85 < rand <= 90:
          scenes.scene_objects['menu']['twitch'].texture_index = 1
        if 90 < rand <= 95:
          scenes.scene_objects['menu']['twitch'].texture_index = 2
        if 95 < rand <= 100:
          scenes.scene_objects['menu']['twitch'].texture_index = 3

      # draw
      if scenes.scene_variables['menu']['selected_hover_item'] is not None and scenes.scene_variables['menu']['selected_hover_item'].text == 'Continue':
        draw_text_ex(config.def_font, f'Night {config.actual_night}', Vector2(230, 470), 15, 0, GRAY)

# ----------------------------------------------- #

    elif current_scene == "settings":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      if scenes.scene_objects['settings']['back_button'].clicked_verdict:
        scenes.set_scene('menu')

      if config.fullscreen:
        scenes.scene_objects['settings']['fullscreen_checkbox'].state = True
      else:
        scenes.scene_objects['settings']['fullscreen_checkbox'].state = False
      if config.wait_textures:
        scenes.scene_objects['settings']['wait_textures_checkbox'].state = True
      else:
        scenes.scene_objects['settings']['wait_textures_checkbox'].state = False
      if config.funny:
        scenes.scene_objects['settings']['funny_checkbox'].state = True
      else:
        scenes.scene_objects['settings']['funny_checkbox'].state = False
      if config.debug:
        scenes.scene_objects['settings']['debug_checkbox'].state = True
      else:
        scenes.scene_objects['settings']['debug_checkbox'].state = False

      if scenes.scene_objects['settings']['fullscreen_checkbox'].clicked_verdict:
        config.fullscreen ^= 1
        config.funny = False
      if scenes.scene_objects['settings']['wait_textures_checkbox'].clicked_verdict:
        config.wait_textures ^= 1
      if scenes.scene_objects['settings']['funny_checkbox'].clicked_verdict:
        config.funny ^= 1
        config.fullscreen = False
      if scenes.scene_objects['settings']['debug_checkbox'].clicked_verdict:
        config.debug ^= 1

      if scenes.scene_objects['settings']['wait_textures_checkbox'].hover_verdict:
        scenes.scene_objects['settings']['wait_textures_notice'].color[3] = 153
      else:
        scenes.scene_objects['settings']['wait_textures_notice'].color[3] = 0
      if scenes.scene_objects['settings']['funny_checkbox'].hover_verdict:
        scenes.scene_objects['settings']['funny_notice'].color[3] = 153
      else:
        scenes.scene_objects['settings']['funny_notice'].color[3] = 0

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "extras":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      scenes.scene_variables['extras']['selection_arr'] = [
        scenes.scene_objects['extras']['proj_github'],
        scenes.scene_objects['extras']['auth_github'],
        scenes.scene_objects['extras']['custom_night'],
        scenes.scene_objects['extras']['jumpscares'],
        scenes.scene_objects['extras']['development_moments'],
      ]
      for item in scenes.scene_variables['extras']['selection_arr']:
        if item.hover_verdict:
          scenes.scene_objects['extras']['set'].pos.y = item.pos.y + 1

      if scenes.scene_objects['extras']['back_button'].clicked_verdict:
        scenes.set_scene('menu')
      if scenes.scene_objects['extras']['custom_night'].clicked_verdict:
        scenes.set_scene('custom_night')
      if scenes.scene_objects['extras']['jumpscares'].clicked_verdict:
        scenes.set_scene('jumpscares')
      if scenes.scene_objects['extras']['development_moments'].clicked_verdict:
        scenes.set_scene('development_moments')
      if scenes.scene_objects['extras']['credits_text'].clicked_verdict and config.debug:
        unload_all_textures(100)


      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "custom_night":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)


      # step
      scene_animatronics_arr = [
        scenes.scene_objects['custom_night']['with_freddy_slider'],
        scenes.scene_objects['custom_night']['with_bonnie_slider'],
        scenes.scene_objects['custom_night']['with_chica_slider'],
        scenes.scene_objects['custom_night']['with_foxy_slider'],
        scenes.scene_objects['custom_night']['balloon_boy_slider'],
        scenes.scene_objects['custom_night']['toy_freddy_slider'],
        scenes.scene_objects['custom_night']['toy_bonnie_slider'],
        scenes.scene_objects['custom_night']['toy_chica_slider'],
        scenes.scene_objects['custom_night']['mangle_slider'],
        scenes.scene_objects['custom_night']['golden_freddy_slider'],
      ]

      if scenes.scene_objects['custom_night']['back_button'].clicked_verdict:
        scenes.set_scene('extras')

      if scenes.scene_objects['custom_night']['start'].clicked_verdict:
        temp_animatronics_arr = []
        for i in range(10):
          temp_animatronics_arr.append(scene_animatronics_arr[i].current_state)
        for i in range(len(config.animatronics_arr)):
          config.animatronics_arr[i].difficulty = temp_animatronics_arr[i]
        del temp_animatronics_arr

        set_night(7)
        scenes.set_scene('night')

      if scenes.scene_objects['custom_night']['confirm_button'].clicked_verdict:
        what_to_set = []
        current_index = scenes.scene_objects['custom_night']['slider'].current_index
        if current_index == 0:  # 20/20/20/20
          what_to_set = [20, 20, 20, 20, 0, 0, 0, 0, 0, 0]
        elif current_index == 1:  # New & Shiny
          what_to_set = [0,	0, 0, 0, 10, 10, 10, 10, 10, 0]
        elif current_index == 2:  # Double Trouble
          what_to_set = [0, 20, 0, 5, 0, 0, 20,	0, 0, 0]
        elif current_index == 3:  # Night of Misfits
          what_to_set = [0, 0, 0, 0, 20, 0, 0, 0, 20, 10]
        elif current_index == 4:  # Foxy Foxy
          what_to_set = [0, 0, 0, 20, 0, 0, 0, 0, 20, 0]
        elif current_index == 5:  # Ladies' Night
          what_to_set = [0, 0, 20, 0, 0, 0, 0, 20, 20, 0]
        elif current_index == 6:  # Freddy's Circus
          what_to_set = [20, 0, 0, 5, 10, 20, 0, 0, 0, 10]
        elif current_index == 7:  # Cupcake Challenge
          what_to_set = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
        elif current_index == 8:  # Fazbear Fever
          what_to_set = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        elif current_index == 9:  # Golden Freddy
          what_to_set = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20]

        if config.debug:
          print(f'apply DING! picked up a "{scenes.scene_objects['custom_night']['slider'].current_state}" difficulty!\t{what_to_set}')

        for i in range(10):
          scene_animatronics_arr[i].current_state = what_to_set[i]
      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "jumpscares":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      if scenes.scene_objects['jumpscares']['back_button'].clicked_verdict:
        scenes.set_scene('extras')
      scenes.scene_objects['jumpscares']['stack'].animation_index = scenes.scene_objects['jumpscares']['selector'].current_index

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "development_moments":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      if scenes.scene_objects['development_moments']['back_button'].clicked_verdict:
        scenes.set_scene('extras')
      scenes.scene_objects['development_moments']['stack'].texture_index = scenes.scene_objects['development_moments']['selector'].current_index

      # draw
      pass


# ----------------------------------------------- #

    elif current_scene == "newspaper":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      if scenes.scene_objects['newspaper']['news'].clicked_verdict or scenes.time_current > 5:
        scenes.set_scene('night')

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "night":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)
        scenes.scene_variables['night']['upcoming_end'] = define_ending(config.upcoming_night)
        scenes.scene_objects['night']['night_count'].text = f'{config.upcoming_night}{scenes.scene_variables['night']['upcoming_end']} Night'
        scenes.scene_objects['night']['white_blinko'].go = True
        if config.debug:
          long = len(config.animatronics_arr)
          print('starting DING! the difficulty is [', end='')
          for i in range(long):
            if i == long-1:
              print(config.animatronics_arr[i].difficulty, end='')
            else:
              print(config.animatronics_arr[i].difficulty, end=', ')
          print(f'], upcoming night is "{config.upcoming_night}"')

      # step
      if config.debug:
        if scenes.time_current >= 0:
          scenes.set_scene("game")
      else:
        if scenes.time_current > 4:
          scenes.set_scene("game")

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "game":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)
        scenes.scene_timers['game']['camera_scroll'].kill_time()
        scenes.scene_objects['game']['ui_battery'].texture_index = 4
        scenes.scene_objects['game']['office_scroll_anchor'].pos.x = -293

      # step
      if config.debug:
        debug_draw_game_text()
      tests_do_testing(scenes)
      border_office_anchor_point()
      camera_anchor_point_walking()
      glue_subjects_to_object.office(glue_subjects_to_object)
      glue_subjects_to_object.camera(glue_subjects_to_object)

      point = int(get_mouse_position().x)
      scenes.scene_variables['game']['scroll_left'] = round((point - int(scenes.scene_objects['game']['office_scroll_line'].pos.x) + scenes.scene_variables['game']['scroll_space']) / scenes.scene_variables['game']['scroll_sensitivity'])
      scenes.scene_variables['game']['scroll_right'] = round((point - int(scenes.scene_objects['game']['office_scroll_line'].pos.x) - scenes.scene_variables['game']['scroll_space']) / scenes.scene_variables['game']['scroll_sensitivity'])
      del point

      if not scenes.scene_variables['game']['gameplay_laptop'] or scenes.scene_variables['game']['gameplay_laptop'] == 2:
        if scenes.scene_variables['game']['scroll_left'] < 0:
          scenes.scene_objects['game']['office_scroll_anchor'].pos.x -= scenes.scene_variables['game']['scroll_left'] / 10 * config.delta
        if scenes.scene_variables['game']['scroll_right'] > 0:
          scenes.scene_objects['game']['office_scroll_anchor'].pos.x -= scenes.scene_variables['game']['scroll_right'] / 10 * config.delta

      pullup_mask()
      pullup_camera()
      #music_box()

      if scenes.scene_timers['game']['red_timer'].time_current % 2 == 0:
        scenes.scene_objects['game']['ui_camera_red'].color[3] = 0
      else:
        scenes.scene_objects['game']['ui_camera_red'].color[3] = 255

      scenes.scene_objects['game']['laptop'].animation_index = scenes.scene_variables['game']['gameplay_laptop']
      scenes.scene_objects['game']['mask'].animation_index = scenes.scene_variables['game']['gameplay_mask']



      if not config.ctrl_hold or objects.scenes.scene_variables['game']['gameplay_mask'] or objects.scenes.scene_variables['game']['gameplay_laptop']:
        scenes.scene_objects['game']['office_selectable'].texture_index = 0
      elif config.ctrl_hold and (not objects.scenes.scene_variables['game']['gameplay_mask'] or not objects.scenes.scene_variables['game']['gameplay_laptop']):
        if scenes.scene_variables['game']['light_not_working']:
          scenes.scene_objects['game']['office_selectable'].texture_index = 4
        else:
          scenes.scene_objects['game']['office_selectable'].texture_index = 1
          scenes.scene_variables['game']['light_left_status'] = False
          scenes.scene_variables['game']['light_right_status'] = False

      if not objects.scenes.scene_variables['game']['gameplay_mask'] or not objects.scenes.scene_variables['game']['gameplay_laptop']:
        scenes.scene_variables['game']['light_left_status'] = scenes.scene_objects['game']['office_left_light'].hold_verdict
        scenes.scene_variables['game']['light_right_status'] = scenes.scene_objects['game']['office_right_light'].hold_verdict
      else:
        scenes.scene_variables['game']['light_left_status'] = 0
        scenes.scene_variables['game']['light_right_status'] = 0


      left_vent_light()
      right_vent_light()

      layers_camera_changing()


      if (scenes.scene_variables['game']['light_left_status'] or scenes.scene_variables['game']['light_right_status']) or (not scenes.scene_variables['game']['light_not_working'] and config.ctrl_hold):
        scenes.scene_sounds['game']['storage']['light_sound'].play()
        scenes.scene_sounds['game']['storage']['broken_light'].stop()
      elif config.ctrl_hold and scenes.scene_variables['game']['light_not_working'] and not (scenes.scene_variables['game']['light_left_status'] or scenes.scene_variables['game']['light_right_status']):
        scenes.scene_sounds['game']['storage']['broken_light'].play()
        scenes.scene_sounds['game']['storage']['light_sound'].stop()
      else:
        scenes.scene_sounds['game']['storage']['light_sound'].stop()
        scenes.scene_sounds['game']['storage']['broken_light'].stop()

      if scenes.scene_variables['game']['gameplay_mask'] == 1:
        scenes.scene_sounds['game']['storage']['mask_on'].play()
        scenes.scene_sounds['game']['storage']['mask_off'].stop()
      elif scenes.scene_variables['game']['gameplay_mask'] == 2:
        scenes.scene_sounds['game']['storage']['mask_on'].stop()
        scenes.scene_sounds['game']['storage']['mask_off'].play()

      if scenes.scene_variables['game']['gameplay_laptop'] == 1:
        scenes.scene_sounds['game']['storage']['laptop_on'].play()
        scenes.scene_sounds['game']['storage']['laptop_off'].stop()
      elif scenes.scene_variables['game']['gameplay_laptop'] == 2:
        scenes.scene_sounds['game']['storage']['laptop_on'].stop()
        scenes.scene_sounds['game']['storage']['laptop_off'].play()

      if scenes.scene_variables['game']['gameplay_mask'] == 3:
        scenes.scene_sounds['game']['storage']['mask_breathing'].play()
      else:
        scenes.scene_sounds['game']['storage']['mask_breathing'].stop()

      if scenes.scene_variables['game']['gameplay_laptop'] == 3:
        scenes.scene_sounds['game']['storage']['bg_fan'].stop()
      else:
        scenes.scene_sounds['game']['storage']['bg_fan'].play()


      sync_camera_selectable_with_map()


      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "win_or_lose":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "paycheck":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "pixel_minigame":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "creepy_minigame":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "loading":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      check_all_textures()
      check_textures_time.update_time()
      if objects.all_textures_ready:
        print('No issues found! Enjoy the game.')
        check_textures_time.kill_time()
        if config.show_preview:
          scenes.set_scene('preview')
        else:
          scenes.set_scene('menu')
        do_valid_filetype()
      if not all_textures_ready and check_textures_time.time_current >= 5 and not config.wait_textures:
        scenes.set_scene('error')

      # draw
      loading_text = "Loading..."
      measure = measure_text(loading_text, 28)
      draw_text(loading_text, config.resolution[0]//2-measure//2, config.resolution[1]//2-16, 28, WHITE)
      del loading_text, measure

# ----------------------------------------------- #

    elif current_scene == "error":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)
        print("ASSETS LOADING ERROR!\n\nOh no! Looks your python console doesn't want to load anything whatsoever. Try choosing different python version to boot this game. Then, reboot the game")

      # step
      space_between = 300

      rec_dont = Rectangle(0, 0, 250, 50)
      rec_dont.x = config.resolution[0] // 2 - rec_dont.width // 2 - space_between // 2
      rec_dont.y = config.resolution[1] // 2 + 80

      rec_do = Rectangle(0, 0, 250, 50)
      rec_do.x = config.resolution[0] // 2 - rec_do.width // 2 + space_between // 2
      rec_do.y = config.resolution[1] // 2 + 80

      if gui_button(rec_dont, "WAIT (DONT REMEMBER PICK)"):
        check_textures_time.start_time()
        config.wait_textures = True
        scenes.set_scene('loading')
      if gui_button(rec_do, "WAIT (DO REMEMBER PICK)"):
        check_textures_time.start_time()
        # set wait_textures to true in save files here
        config.wait_textures = True
        scenes.set_scene('loading')
      del rec_do, rec_dont, space_between

      # draw
      error_title_text = "ASSETS LOADING ERROR!"
      error_description_text = "Oh no! Looks your python console doesn't want to load anything whatsoever.\nTry choosing different python version to boot this game. If you think your\ncomputer needs more time to load all textures, please push 'WAIT' button"
      error_title_measure = measure_text(error_title_text, 40)
      draw_text(error_title_text, config.resolution[0]//2 - error_title_measure//2, config.resolution[1]//2-60, 40, ORANGE)
      space = 0
      for item in error_description_text.split('\n'):
        error_description_measure = measure_text(item, 20)
        draw_text(item, config.resolution[0] // 2 - error_description_measure // 2, config.resolution[1]//2-10+space, 20, WHITE)
        space += 20
      del error_title_text, error_description_text, error_title_measure, space

# ----------------------------------------------- #

    elif current_scene == "preview":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      if scenes.time_current >= 3:
        scenes.set_scene('menu')
        config.blinko_after_preview = True

      # draw
      pass

# ----------------------------------------------- #

    elif current_scene == "test_scene":
      # activation
      if scenes.scene_changed:
        call_activation(audio_activation_update)

      # step
      if scenes.scene_objects['test_scene']['back_button'].clicked_verdict:
        scenes.set_scene('menu')

      scenes.scene_objects['test_scene']['circle_bar'].start_circle = scenes.scene_objects['test_scene']['circle_button'].hold_verdict
      if scenes.scene_objects['test_scene']['circle_button'].hold_verdict:
        scenes.scene_sounds['test_scene']['storage']['wind_sound'].play()

      # draw
      pass

# ----------------------------------------------- #

    # always do:
    # step
    config.delta = get_frame_time() * 1000
    global_keys_update()
    scenes.update_time()
    set_fullscreen()
    xor_debug()
    volume_makes_sense(scenes.scene_objects['settings']['volume_slider'])
    scenes.check_changed()
    if config.debug:
      scenes.check_input()
    if config.funny:
      funny_mode(1)

    # draw
    if config.debug:
      debug_draw_everywhere_text()
      animations_draw_debug()
      sounds_draw_debug()


# ----------------------------------------------- #
    end_drawing()
    if config.debug: clear_background(DARKPURPLE)
    else: clear_background(BLACK)
  close_window()


if __name__ == "__main__":
  main()
