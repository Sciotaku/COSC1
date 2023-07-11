from cs1lib import *


def draw_smiley(x, y):

    # draw a white background
    clear()

    # draw the outline of the face
    set_fill_color(1, 1, 0)   # set fill color to yellow
    draw_circle(x, y, 25)

    # draw the mouth
    set_fill_color(1, 1, 0)  # yellow
    draw_circle(x, y, 15)
    set_stroke_color(1, 1, 0)
    draw_rectangle(x - 16, y - 16, 31, 20)

    # draw the eyes
    set_stroke_color(0, 0, 0)
    set_fill_color(0, 0, 0)  # set fill color to black
    draw_circle(x - 10, y - 5, 2)
    draw_circle(x + 10, y - 5, 2)


# set the velocity of the smile if a key is pressed
def keydown(key):
    global pressed_D, pressed_A, pressed_W, pressed_S

    if key == "d":
        pressed_D = True
    elif key == "a":
        pressed_A = True


# if a key is released, set corresp. velocity to 0
def keyup(key):
    global pressed_D, pressed_A, pressed_W, pressed_S
    if key == "d":
        pressed_D = False
    elif key == "a":
        pressed_A = False


# draw the smiley face, and move the location based on
#  velocities
def draw_frame():
    global x, y

    draw_smiley(x, y)

    if pressed_A:
        x -= SPEED
    if pressed_D:
        x += SPEED


SPEED = 2

x = 100
y = 100
pressed_W = False
pressed_A = False
pressed_S = False
pressed_D = False


# start the animation
start_graphics(draw_frame, 2400, key_press=keydown)
