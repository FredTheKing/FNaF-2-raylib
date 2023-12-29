from raylib.colors import *
from config import *
from etc import *
from assets.animations import *

def main():
  while not window_should_close():
# ----------------------------------------------- #

    if scenes.scene_dict[scenes.scene_index] == "menu":
      # activation
      if scenes.scene_changed:
        config.scenes.start_time()

      # step
      textures_update()

      # draw
      textures_draw()

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

    # always do:
    # step
    config.key_pressed = get_key_pressed()
    config.scenes.update_time()
    config.scenes.update_new_key(KeyboardKey.KEY_F2)
    set_fullscreen(KeyboardKey.KEY_F11)
    if debug: scenes.check_input()

    # draw
    debug_draw_everywhere_text()

# ----------------------------------------------- #
    end_drawing()
    clear_background(BLACK)
  close_window()


if __name__ == "__main__":
  main()
