import time

class Time:
  def __init__(self, time_mod: int):
    self.time_multiply = time_mod
    self.time_start: float
    self.time_current: int = 0
    self.go = False

  def start_time(self):
    self.time_start = time.time()
    self.go = True

  def update_time(self):
    if self.go:
      self.time_current = int((time.time() - self.time_start) * self.time_multiply)

  def kill_time(self):
    self.go = False
    self.time_current = 0
