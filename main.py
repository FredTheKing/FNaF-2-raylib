from classes.Time import Time
from raylib.colors import *
from config import *
from etc import *
from objects import *

def main():
  global actual_night, upcoming_night
  check_textures_time = Time(1)
  check_textures_time.start_time()
  while not window_should_close():
    textures_update()
# ----------------------------------------------- #

    if scenes.scene_list[scenes.scene_index] == "menu":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 0.25

      # step
      if scenes.time_current % 2 == 0:
        bottom_text_draw("Original game by: Scott Cawthon\t\t\t\t\tGame built by: FredTheKing\t\t\t\t\tMade in Python 3.12 with raylib (pyray)")
      else:
        bottom_text_draw("Project's, Author's links and much more are in Extras menu\t\t\t\t\tManipulate game settings in Settings menu")

      if scenes.scene_objects['menu']['to_test_tp'].clicked_verdict and config.debug:
        scenes.set_scene('test_scene')

      menu_temp_selection_arr = [scenes.scene_objects['menu']['new_game'], scenes.scene_objects['menu']['continue'], scenes.scene_objects['menu']['settings'], scenes.scene_objects['menu']['extras']]
      for item in menu_temp_selection_arr:
        if item.hover_verdict:
          scenes.scene_objects['menu']['set'].pos.y = item.pos.y + 1
      if scenes.scene_objects['menu']['new_game'].clicked_verdict:
        upcoming_night = actual_night = 0
        scenes.set_scene('newspaper')
      elif scenes.scene_objects['menu']['continue'].clicked_verdict:
        upcoming_night = actual_night
        scenes.set_scene('night')
      elif scenes.scene_objects['menu']['settings'].clicked_verdict:
        scenes.set_scene('settings')
      elif scenes.scene_objects['menu']['extras'].clicked_verdict:
        scenes.set_scene('extras')
      del menu_temp_selection_arr

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "settings":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

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

    elif scenes.scene_list[scenes.scene_index] == "extras":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
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

    elif scenes.scene_list[scenes.scene_index] == "custom_night":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1


      # step
      if scenes.scene_objects['custom_night']['back_button'].clicked_verdict:
        scenes.set_scene('extras')
      if scenes.scene_objects['custom_night']['start'].clicked_verdict:
        global difficulty_withered_freddy, difficulty_withered_bonnie, difficulty_withered_chica, difficulty_withered_foxy, difficulty_golden_freddy, difficulty_toy_freddy, difficulty_toy_bonnie, difficulty_toy_chica, difficulty_mangle, difficulty_balloon_boy
        difficulty_withered_freddy = objects.custom_night_with_freddy_slider.current_state
        difficulty_withered_bonnie = objects.custom_night_with_bonnie_slider.current_state
        difficulty_withered_chica = objects.custom_night_with_chica_slider.current_state
        difficulty_withered_foxy = objects.custom_night_with_foxy_slider.current_state
        difficulty_golden_freddy = objects.custom_night_golden_freddy_slider.current_state
        difficulty_toy_freddy = objects.custom_night_toy_freddy_slider.current_state
        difficulty_toy_bonnie = objects.custom_night_toy_bonnie_slider.current_state
        difficulty_toy_chica = objects.custom_night_toy_chica_slider.current_state
        difficulty_mangle = objects.custom_night_mangle_slider.current_state
        difficulty_balloon_boy = objects.custom_night_balloon_boy_slider.current_state
        scenes.set_scene('night')

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "jumpscares":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      if scenes.scene_objects['jumpscares']['back_button'].clicked_verdict:
        scenes.set_scene('extras')
      scenes.scene_objects['jumpscares']['stack'].animation_index = scenes.scene_objects['jumpscares']['selector'].current_index

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "development_moments":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      if scenes.scene_objects['development_moments']['back_button'].clicked_verdict:
        scenes.set_scene('extras')

      # draw
      pass


# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "newspaper":
      # activation
      if scenes.scene_changed:
        scenes.time_multiply = 1
        scenes.scene_changed -= 1

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "night":

      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "game":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      if gui_button(Rectangle(300, 400, 100, 80), "go"):
        scenes.set_scene('menu')

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "paycheck":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "pixel_minigame":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "creepy_minigame":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "loading":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      check_all_textures()
      check_textures_time.update_time()
      if objects.all_textures_ready:
        print('No issues found! Enjoy the game.')
        check_textures_time.kill_time()
        if show_preview:
          scenes.set_scene('preview')
        else:
          scenes.set_scene('menu')
        do_valid_filetype()
      if not all_textures_ready and check_textures_time.time_current >= 5 and not config.wait_textures:
        scenes.set_scene('error')

      # draw
      loading_text = "Loading..."
      measure = measure_text(loading_text, 28)
      draw_text(loading_text, resolution[0]//2-measure//2, resolution[1]//2-16, 28, WHITE)
      del loading_text, measure

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "error":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1
        print("ASSETS LOADING ERROR!\n\nOh no! Looks your python console doesn't want to load anything whatsoever. Try choosing different python version to boot this game. Then, reboot the game")

      # step
      space_between = 300

      rec_dont = Rectangle(0, 0, 250, 50)
      rec_dont.x = resolution[0] // 2 - rec_dont.width // 2 - space_between // 2
      rec_dont.y = resolution[1] // 2 + 80

      rec_do = Rectangle(0, 0, 250, 50)
      rec_do.x = resolution[0] // 2 - rec_do.width // 2 + space_between // 2
      rec_do.y = resolution[1] // 2 + 80

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
      draw_text(error_title_text, resolution[0]//2 - error_title_measure//2, resolution[1]//2-60, 40, ORANGE)
      space = 0
      for item in error_description_text.split('\n'):
        error_description_measure = measure_text(item, 20)
        draw_text(item, resolution[0] // 2 - error_description_measure // 2, resolution[1]//2-10+space, 20, WHITE)
        space += 20
      del error_title_text, error_description_text, error_title_measure, space

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "preview":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      if scenes.time_current >= 3:
        scenes.set_scene('menu')

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_list[scenes.scene_index] == "test_scene":
      # activation
      if scenes.scene_changed:
        scenes.scene_changed -= 1
        scenes.time_multiply = 1

      # step
      if scenes.scene_objects['test_scene']['back_button'].clicked_verdict:
        scenes.set_scene('menu')

      # draw
      pass

# ----------------------------------------------- #

    # always do:
    # step
    config.key_pressed = get_key_pressed()
    scenes.update_time()
    set_fullscreen()
    xor_debug()
    scenes.check_changed()
    if config.debug:
      scenes.check_input()
    if config.funny:
      funny_mode(1)

    # draw
    if config.debug:
      debug_draw_everywhere_text()
      animations_draw_debug()


# ----------------------------------------------- #
    end_drawing()
    clear_background(BLACK)
  close_window()


if __name__ == "__main__":
  main()
