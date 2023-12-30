import assets.animations
from classes.Time import Time
from raylib.colors import *
from config import *
from etc import *
from assets.animations import *

def main():
  check_textures_time = Time(1)
  check_textures_time.start_time()
  while not window_should_close():
# ----------------------------------------------- #

    if scenes.scene_dict[scenes.scene_index] == "menu":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      textures_update()
      #for item in scenes_list[scenes.scene_index][3:5]:
      #  if item.check_collision_mouse():
      #    menu_set.pos.y = item.pos.y

      # draw
      if config.debug:
        animations_draw_debug()

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "settings":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "custom night":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "newspaper":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "night":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "game":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "paycheck":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "pixel minigame":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "creepy minigame":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      pass

      # draw
      pass

# ----------------------------------------------- #

    elif scenes.scene_dict[scenes.scene_index] == "loading":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      check_all_textures()
      check_textures_time.update_time()
      if assets.animations.all_textures_ready:
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
        print("TEXTURE LOADING ERROR!\n\nOh no! Looks your python console doesn't want to load any images whatsoever. Try choosing different python version to boot this game. Then, reboot the game")

      # step
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
      error_title_text = "TEXTURE LOADING ERROR!"
      error_description_text = "Oh no! Looks your python console doesn't want to load any images whatsoever.\nTry choosing different python version to boot this game. If you think your\ncomputer needs more time to load all textures, please push 'WAIT' button"
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
    config.key_pressed = get_key_pressed()
    config.scenes.update_time()
    config.scenes.update_new_key(KeyboardKey.KEY_F2)
    set_fullscreen(KeyboardKey.KEY_F11)
    xor_debug()
    if config.debug:
      scenes.check_input()

    # draw
    # if config.debug:
    debug_draw_everywhere_text()


# ----------------------------------------------- #
    end_drawing()
    clear_background(BLACK)
  close_window()


if __name__ == "__main__":
  main()
