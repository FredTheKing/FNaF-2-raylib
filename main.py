import assets.objects
from classes.Time import Time
from raylib.colors import *
from config import *
from etc import *
from assets.objects import *

def main():
  global actual_night, upcoming_night

  check_textures_time = Time(1)
  check_textures_time.start_time()
  while not window_should_close():
    textures_update()
# ----------------------------------------------- #

    if scenes.scene_dict[scenes.scene_index] == "menu":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 0.25
      if config.scenes.time_current % 2 == 0:
        bottom_text_draw("Original game by: Scott Cawthon\t\t\t\t\tGame built by: FredTheKing\t\t\t\t\tMade in Python 3.12 with raylib (pyray)")
      else:
        bottom_text_draw("thingo, funny thingo")

      menu_temp_selection_arr = [menu_new_game, menu_continue, menu_settings, menu_extras]
      for item in menu_temp_selection_arr:
        if item.hover_verdict:
          menu_set.pos.y = item.pos.y + 1
      if menu_new_game.clicked_verdict:
        menu_new_game.reset()
        upcoming_night = actual_night = 0
        scenes.set_scene(3)
      elif menu_continue.clicked_verdict:
        menu_continue.reset()
        upcoming_night = actual_night
        scenes.set_scene(4)
      elif menu_settings.clicked_verdict:
        menu_settings.reset()
        scenes.set_scene(1)
      elif menu_extras.clicked_verdict:
        menu_extras.reset()
        scenes.set_scene(2)

      # draw
      if config.debug:
        animations_draw_debug()

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "settings":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1
      if multi_back_button.clicked_verdict:
        scenes.set_scene(0)

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "extras":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1
      if multi_back_button.clicked_verdict:
        scenes.set_scene(0)

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "newspaper":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "night":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "game":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "paycheck":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "pixel minigame":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "creepy minigame":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "loading":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      config.scenes.time_multiply = 1
      check_all_textures()
      check_textures_time.update_time()
      if assets.objects.all_textures_ready:
        print('No issues found! Enjoy the game.')
        check_textures_time.kill_time()
        scenes.set_scene(0)
      if not all_textures_ready and check_textures_time.time_current >= 5 and not config.wait_textures:
        scenes.set_scene(10)

      # draw
      loading_text = "Loading..."
      measure = measure_text(loading_text, 28)
      draw_text(loading_text, int(resolution.x)//2-measure//2, int(resolution.y)//2-16, 28, WHITE)

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "error boot":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()
        print("ASSETS LOADING ERROR!\n\nOh no! Looks your python console doesn't want to load anything whatsoever. Try choosing different python version to boot this game. Then, reboot the game")

      # step
      config.scenes.time_multiply = 1
      space_between = 300

      rec_dont = Rectangle(0, 0, 250, 50)
      rec_dont.x = int(resolution.x) // 2 - rec_dont.width // 2 - space_between // 2
      rec_dont.y = int(resolution.y) // 2 + 80

      rec_do = Rectangle(0, 0, 250, 50)
      rec_do.x = int(resolution.x) // 2 - rec_do.width // 2 + space_between // 2
      rec_do.y = int(resolution.y) // 2 + 80

      if gui_button(rec_dont, "WAIT (DONT REMEMBER PICK)"):
        check_textures_time.start_time()
        config.wait_textures = True
        config.scenes.set_scene(9)
      if gui_button(rec_do, "WAIT (DO REMEMBER PICK)"):
        check_textures_time.start_time()
        # set wait_textures to true in save files here
        config.wait_textures = True
        config.scenes.set_scene(9)

      # draw
      error_title_text = "ASSETS LOADING ERROR!"
      error_description_text = "Oh no! Looks your python console doesn't want to load anything whatsoever.\nTry choosing different python version to boot this game. If you think your\ncomputer needs more time to load all textures, please push 'WAIT' button"
      error_title_measure = measure_text(error_title_text, 40)
      draw_text(error_title_text, int(resolution.x)//2 - error_title_measure//2, int(resolution.y)//2-60, 40, ORANGE)
      space = 0
      for item in error_description_text.split('\n'):
        error_description_measure = measure_text(item, 20)
        draw_text(item, int(resolution.x) // 2 - error_description_measure // 2, int(resolution.y) // 2 - 10 + space, 20, WHITE)
        space += 20

# ----------------------------------------------- #

    # always do:
    # step
    settings_top_text.center_text()
    extras_top_text.center_text()
    config.key_pressed = get_key_pressed()
    config.scenes.update_time()
    config.scenes.update_new_key(KeyboardKey.KEY_F2)
    set_fullscreen(KeyboardKey.KEY_F11)
    xor_debug()
    if config.debug:
      scenes.check_input()

    # draw
    if config.debug:
      debug_draw_everywhere_text()


# ----------------------------------------------- #
    end_drawing()
    clear_background(BLACK)
  close_window()


if __name__ == "__main__":
  main()
