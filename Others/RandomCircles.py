# Draw circles with random colors when the user clicks the mouse button.
from cs1lib import start_graphics, set_fill_color, draw_circle
from random import uniform


def press(mx, my):
    global draw
    draw = True


def release(mx, my):
    global draw
    draw = False


def move(mx, my):
    global r, g, b, x, y

    # Pick a circle color at random
    r = uniform(.5, 1)
    g = uniform(.5, 1)
    b = uniform(.5, 1)
    x = mx
    y = my


def graphics():
    if draw:
        set_fill_color(r, g, b)
        draw_circle(x, y, 50)


r = 0
g = 0
b = 0
x = 0
y = 0
draw = False

start_graphics(graphics, 500, mouse_move=move, mouse_press=press, mouse_release=release)