from cs1lib import *
from math import sqrt


# Compute the distance between points x1, y1 and x2, y2
def point_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(dx * dx + dy * dy)


def press(mx, my):
    print("press")
    global center_x, center_y, radius, drawing
    center_x = mx
    center_y = my
    radius = 0
    drawing = True


def release(mx, my):
    global drawing
    drawing = False


def move(mx, my):
    global radius
    radius = point_distance(center_x, center_y, mx, my)


def circle_drag():
    set_stroke_color(1, 1, 1)   # white
    set_fill_color(1, 0.5, 0)   # orange

    if drawing:
        draw_circle(center_x, center_y, radius)


center_x = 0
center_y = 0
radius = 0
drawing = False

start_graphics(circle_drag, 2400, mouse_press=press, mouse_release=release, mouse_move=move)