# Growing and Shrinking Circle
from cs1lib import *

WINDOW_SIZE = 200
r = 1
growing = True

def pulse_circle():
  global r, growing

  clear()
  set_fill_color(1,0,0)
  draw_circle(WINDOW_SIZE, WINDOW_SIZE, r)

  set_fill_color(0,0,1)
  draw_circle(WINDOW_SIZE, WINDOW_SIZE, r/2)

  set_fill_color(1,1,0)
  draw_circle(WINDOW_SIZE, WINDOW_SIZE, r/4)

  if growing:
    r = r + 2
  else:
    r = r - 2

  if r >= WINDOW_SIZE or r <= 1:
    growing = not growing



start_graphics(pulse_circle, 1000)