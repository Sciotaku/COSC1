from cs1lib import *


PIXEL_PER_METER = 20
WW = 400
WH = 400
RADIUS = 1  # meter
bx = 0
by = 10
vx = 2  # meter/sec
vy = 0

FRAMERATE = 40
TIMESTEP = 1/FRAMERATE
TIMESCALE = 2

G = -9.8  # meters/sec^2


def draw_ball():
    pixel_x = bx * PIXEL_PER_METER
    pixel_y = WH - by * PIXEL_PER_METER
    pixel_r = RADIUS * PIXEL_PER_METER
    set_fill_color(1, 0, 1)
    draw_circle(pixel_x, pixel_y, pixel_r)


def update():
    global bx, by, vx, vy
    bx = bx + vx * TIMESTEP * TIMESCALE
    by = by + vy * TIMESTEP * TIMESCALE

    if by - RADIUS <= 0:
        vy = -vy

    # if 0 >= bx - RADIUS >= WW:
    #     vx = -vx

    vy = vy + G * TIMESTEP * TIMESCALE


def my_draw():
    set_clear_color(1, 1, 1)
    clear()

    draw_ball()
    update()


start_graphics(my_draw, framerate=FRAMERATE, width=WW, height=WH)
