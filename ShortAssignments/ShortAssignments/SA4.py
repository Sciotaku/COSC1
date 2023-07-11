# Author: Rahul Gupta
# Date: 01/18/2023
# Purpose: Write a drawing program

from cs1lib import *
# Colors
r = 1
g = 1
b = 1

# Position of the mouse pointer
old_x = 0
old_y = 0
new_x = 0
new_y = 0
draw = False
background = True


# Create a chalkboard
def black_background():
    global background
    set_clear_color(0, 0, 0)
    clear()
    background = False


# Draw when mouse is pressed
def mouse_press(mx, my):
    global draw, old_x, old_y, new_x, new_y
    draw = True


# Stop Drawing when mouse released
def mouse_release(mx, my):
    global draw
    draw = False


# Draw when the pointer moves
def mouse_move(mx, my):
    global r, g, b, old_x, old_y, new_x, new_y
    new_x = mouse_x()
    new_y = mouse_y()


# Change colors based on the pressed key
def keyword(key):
    global r, g, b

    # Draw red
    if key == "r":
        r = 1
        g = 0
        b = 0

    # Draw green
    if key == "g":
        r = 0
        g = 1
        b = 0

    # Draw blue
    if key == "b":
        r = 0
        g = 0
        b = 1

    # Draw yellow
    if key == "y":
        r = 1
        g = 1
        b = 0

    # Draw white
    if key == "w":
        r = 1
        g = 1
        b = 1


# let user draw on the canvas
def drawing():
    global background, old_y, old_x, new_x, new_y

    # Black Background
    if background:
        black_background()

    if draw:
        set_stroke_width(5)
        set_stroke_color(r, g, b)
        draw_line(old_x, old_y, new_x, new_y)

    old_x = new_x
    old_y = new_y


start_graphics(drawing, mouse_move=mouse_move, mouse_press=mouse_press, mouse_release=mouse_release, key_press=keyword)