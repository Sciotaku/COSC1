# Ping Pong
from cs1lib import *

WINDOW_SIZE = 400
x = 40
y = 200
r = 20
vx = 1

def draw_ball():
    global x, vx
    clear()

    set_fill_color(1, 1, 0) # yellow ball
    draw_circle(x, y, r)

    if x <= 0 or x >= WINDOW_SIZE:
        vx = -vx
    x = x + vx


start_graphics(draw_ball, 5000, width=WINDOW_SIZE, height=WINDOW_SIZE)  # number of frames to draw = 1000
