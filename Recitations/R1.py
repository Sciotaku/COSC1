# Filename: R1.py
# Author Name: Rahul Gupta
# Date: 01/16/2023
# Course: COSC 1
# Purpose: Draw a bullseye


from cs1lib import *

def draw_bullseye():
    set_fill_color(0, 0, 1)
    draw_circle(200, 200, 100)

    set_fill_color(0, 1, 0)
    draw_circle(200, 200, 60)

    set_fill_color(1, 0, 0)
    draw_circle(200, 200, 20)

start_graphics(draw_bullseye)



