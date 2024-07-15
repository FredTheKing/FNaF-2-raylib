import random

from pyray import *
import config
from classes.Animation import SelectableAnimation
from classes.Text import JustText
from classes.Image import SelectableBoxImage
from classes.Time import Time

class Special:
  class WhiteShhrrt:
    def __init__(self, layer: int = None, white_on_start: bool = False):
      def spec_load_image(filename: str, animation_subtype: bool = False) -> Texture or list[Texture]:
        image = load_texture_from_image(load_image(config.release_path + filename))
        return [image] if animation_subtype else image
      def spec_load_animation(dirname: str, times: int) -> list:
        arr = []
        for item in range(times):
          arr.append(spec_load_image(dirname + f"/{item}.png"))
        return arr

      self.item: SelectableAnimation = SelectableAnimation([
        spec_load_image('assets/graphics/Other/Static/1/white.png', True),
        spec_load_animation('assets/graphics/Other/Static/1', 5),
        spec_load_image('assets/graphics/Other/Static/1/invisible.png', True),
      ], animation_speed=50, is_looped=True, default_animation_index=0 if white_on_start else 2)
      self.time: Time = Time(10)
      self.layer_order = layer or self.item.layer_order

      self.go: bool = False
      self.activation_completed: bool = False
      self.white_progress: int = 0

    def check_go(self):
      if self.go and not self.activation_completed:
        self.activation_completed = True
        self.white_progress = 0
        self.item.animation_index = 0
        self.time.start_time()


    def update(self):
      self.check_go()
      self.item.update()
      self.time.update_time()
      if self.go:
        self.check_coca_cola()
      # if config.debug:
      #   self.draw_debug()

    def draw_debug(self):
      text = f"go: {int(self.go)}\nact: {int(self.activation_completed)}\ntime: {self.time.time_current}"
      draw_text(text, 700, 600, 40, RED)

    def check_coca_cola(self):
      if self.time.time_current >= 1 and self.white_progress == 0:
        self.white_progress = 1
        self.item.animation_index = 1
        self.time.start_time()
      elif self.time.time_current >= 1 and self.white_progress == 1:
        self.white_progress = 2
        self.item.animation_index = 2
        self.go = False
        self.activation_completed = False
        self.time.time_current = 0
        self.time.kill_time()

  class CameraUI:
    class CameraBox:
      def __init__(self, cam_number: int = 99, pos: Vector2 = Vector2(0, 0), layer: int = 3):
        def spec_load_image(filename: str, animation_subtype: bool = False) -> Texture or list[Texture]:
          image = load_texture_from_image(load_image(config.release_path + filename))
          return [image] if animation_subtype else image

        self.number = cam_number
        self.box = SelectableBoxImage([
          spec_load_image('assets/graphics/Monitor_Cameras/CameraUtilities/camera_afk.png'),
          spec_load_image('assets/graphics/Monitor_Cameras/CameraUtilities/camera_pick.png'),
        ], pos, layer=layer, play_set_sound=True)
        self.cam_text = JustText("CAM", 15, Vector2(pos.x + 7, pos.y + 8), layer=layer, spacing=3,
                                 font_filename='assets/fonts/lcd.ttf')
        self.text = JustText(str(self.number).zfill(2), 15, Vector2(pos.x + 7, pos.y + 21), layer=layer, spacing=1,
                             font_filename='assets/fonts/lcd.ttf')
        self.layer_order = layer
        self.time = Time(1.7)
        self.picked = False

      def update_time(self):
        self.time.update_time()
        if self.picked:
          if not self.time.go:
            self.time.start_time()
        else:
          self.time.kill_time()

      def picked_animation(self):
        if self.picked:
          self.box.texture_index = self.time.time_current % 2 == 0
        else:
          self.box.texture_index = 0

      def update(self):
        self.box.update()
        self.cam_text.update()
        self.text.update()
        self.update_time()
        self.picked_animation()

    def __init__(self, cams_pos_list=None, layer: int = 3, default_pick: int = 0):
      if cams_pos_list is None:
        cams_pos_list = []
      self.total_amount = len(cams_pos_list)
      self.camera_box_collection = []
      self.layer_order = layer
      for i in range(self.total_amount):
        self.camera_box_collection.append(self.CameraBox(i+1, cams_pos_list[i], self.layer_order))
      self.picked = default_pick
      self.pick_changed: bool = False

    def check_changed(self):
      if self.pick_changed:
        self.pick_changed = False

    def check_active_cam(self):
      for i, item in enumerate(self.camera_box_collection):
        if item.box.clicked_verdict:
          self.picked = i
          self.pick_changed = True

    def update_picked_state(self):
      for i, item in enumerate(self.camera_box_collection):
        if i == self.picked:
          item.picked = True
        else:
          item.picked = False

    def update(self):
      self.check_changed()
      for item in self.camera_box_collection:
        item.update()
      self.check_active_cam()
      self.update_picked_state()

  class InvisibleAnchor:
    def __init__(self, pos: Vector2 = Vector2(0, 0), size: Vector2 = Vector2(0, 0), layer: int = 5):
      self.pos: Vector2 = pos
      self.size: Vector2 = size
      self.layer_order: int = layer

    def draw(self):
      transparent_white = Color(255, 255, 255, 153)
      draw_rectangle_v(self.pos, self.size, transparent_white)

    def update(self):
      if config.debug:
        self.draw()

  class Animatronic:
    def __init__(self, name: str, debug_picture_filename: Texture, animatronic_type: str, behavior: list[str], exceptions: list[str], activation: str):
      def spec_load_image(filename: str, animation_subtype: bool = False) -> Texture or list[Texture]:
        image = load_texture_from_image(load_image(config.release_path + filename))
        return [image] if animation_subtype else image

      self.name = name
      self.debug_pic = spec_load_image(debug_picture_filename)
      self.animatronic_type = animatronic_type
      self.difficulty = 10

      self.behavior = behavior
      self.exceptions = exceptions
      self.activation = activation

      self.step = False
      self.default_position = self.behavior[0].split('>')[0]
      self.trying_position = None
      self.current_position = self.default_position
      self.last_visited: list = [0, 0]

      self.timer = Time(random.uniform(0.7, 1.3))

    def restore_position(self):
      self.current_position = self.default_position

    def execute_step_on_timer(self):
      self.timer.update_time()
      if self.timer.time_current >= 5:
        self.timer.start_time()
        if random.randint(0, 20) < self.difficulty:
          self.step = True

    def behavior_update(self):
      if self.step:
        self.step = False

        for item in self.behavior:
          splitted_behavior = item.split('>')
          if splitted_behavior[0] == self.current_position:
            splitted_addresses = splitted_behavior[1].split('|')

            destination_address = {}
            for item in splitted_addresses:
              splitted_percent = item.split('-')
              destination_address[splitted_percent[0]] = int(splitted_percent[1])

            random_percent = random.randint(0, 100)

            for destination, percent in destination_address.items():
              if random_percent in range(percent):
                self.trying_position = destination
                self.last_visited = [random_percent, percent]
                return
              else:
                random_percent -= percent

    def exceptions_update(self):
      if self.trying_position is not None:
        for item in self.exceptions:
          splitted_exception = item.split('<')
          if splitted_exception[0] == self.trying_position:
            splitted_animatronics = splitted_exception[1].split('|')

            useful_animatronics_locations = {}
            for animatronic in config.animatronics_arr:
              temp_name = animatronic.name
              if temp_name in splitted_animatronics and animatronic.name != self.name:
                useful_animatronics_locations[temp_name] = animatronic.current_position

            for animatronic, position in useful_animatronics_locations.items():
              if position != self.trying_position:
                self.current_position = self.trying_position
                self.trying_position = None
                return
            else:
              self.trying_position = None

    def update(self):
      self.execute_step_on_timer()
      self.behavior_update()
      self.exceptions_update()

    def draw_debug(self, x, y):
      draw_text(f'{self.name}: {self.current_position} | {self.timer.time_current} - {self.last_visited}', x, y, 18, WHITE)
      try:
        pos: Vector2 = config.debug_animatronics_positions[self.current_position]
      except KeyError:
        pass
      else:
        draw_texture(self.debug_pic, int(pos.x), int(pos.y), WHITE)
