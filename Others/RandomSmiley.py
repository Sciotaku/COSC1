# Lots of Smiley
from cs1lib import *
from random import randint, uniform


def draw_smiley_face(x, y, r):
    a = uniform(0, 1)
    b = uniform(0, 1)
    c = uniform(0, 1)

    # draw the outline of the face
    set_fill_color(a, b, c)
    draw_circle(x, y, r)

    # draw the mouth

    draw_circle(x, y, 3 * r / 4)
    set_stroke_color(a, b, c)
    draw_rectangle(x - 3 / 4 * r, y - 3 / 4 * r, 4 / 2 * 3 / 4 * r, 3 / 2 * 3 / 4 * r)

    # draw the eyes
    set_fill_color(0, 0, 0)  # black
    draw_circle(x - 20, y - 10, r / 10)
    draw_circle(x + 20, y - 10, r / 10)
    set_stroke_color(0, 0, 0)  # black


def my_draw():
    num = 0
    while num <= 1000:
        r = randint(0, 50)
        x = randint(0, 400)
        y = randint(0, 400)
        draw_smiley_face(x, y, r)
        num = num + 1


start_graphics(my_draw)