import time

class Time:
  def __init__(self, time_multiply):
    self.time_multiply = time_multiply
    self.time_start: float
    self.time_current: int
    self.go = True

  def start_time(self):
    self.time_start = time.time()

  def update_time(self):
    if self.go:
      self.time_current = int((time.time() - self.time_start) * self.time_multiply)

  def kill_time(self):
    self.go = False
