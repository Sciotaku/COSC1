# Move the smiley with the pointer
from cs1lib import *

# define as global variables
x = 200
y = 200
r = 50

# def my_mouse_press(mx, my):
#     global x, y
#     # print(mx, my)
#     x = mx
#     y = my

def my_mouse_move(mx, my):
    global x, y
    # print(mx, my)
    x = mx
    y = my

def draw_smiley_face():

    # clear background
    clear()

    # draw the outline of the face
    set_fill_color(1, 1, 0) # yellow
    draw_circle(x, y, r)

    # draw the mouth
    set_stroke_color(0, 0, 0)
    draw_circle(x, y, 30)
    set_stroke_color(1, 1, 0) # yellow
    draw_rectangle(x - 30, y - 30, 60, 40)

    # draw the eyes
    set_fill_color(0, 0, 0) # black
    draw_circle(x - 20, y - 10, 5)
    draw_circle(x + 20, y - 10, 5)

start_graphics(draw_smiley_face, 1000, mouse_move=my_mouse_move)