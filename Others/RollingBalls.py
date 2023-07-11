# Rolling Balls
from cs1lib import *

WINDOW_SIZE = 400
x = 20
y = 20
r = 20
vy = 1


def draw_ball():
    global x, y, vy
    z = 400
    clear()

    set_fill_color(0, 1, 0) # yellow ball
    i = 1
    while i <= 20:
        draw_circle(x, y, r)
        draw_circle(z, y, r)

        if y <= 0 or y >= WINDOW_SIZE:
            vy = -vy
            x = x + 20
        z = z - 20

        y = (y + vy)

        i = i + 1


start_graphics(draw_ball, 1000, width=WINDOW_SIZE, height=WINDOW_SIZE)  # number of frames to draw = 1000