# Filename: SA2.py
# Author Name: Rahul Gupta
# Date: 01/14/2023
# Course: COSC 1
# Purpose: SA2: To draw the cover of your favorite picture book.
# Idea: Draw mickey mouse.

from cs1lib import *


def circle(x, y, r):
    draw_circle(x,y,r)


def fill_yellow():
    set_fill_color(1, 1, 0)


def fill_black():
    set_fill_color(0, 0, 0)


def fill_grey():
    set_fill_color(232/255, 190/255, 172/255)


def fill_white():
    set_fill_color(1, 1, 1)


def fill_red():
    set_fill_color(1, 0, 0)


def stroke_black():
    set_stroke_color(0, 0, 0)


def draw_mickey():
    clear()
    disable_stroke()

    # change background
    fill_yellow()
    draw_rectangle(0, 0, 400, 400)

    # draw a head
    fill_black()
    # draw_circle(200, 200, 150)
    circle(200,200,150)

    # draw ears
    draw_circle(100, 50, 75)
    draw_circle(300, 50, 75)

    # draw face
    fill_grey()
    draw_circle(170, 240, 100)
    draw_circle(220, 150, 80)
    draw_circle(270, 160, 70)
    draw_circle(250, 200, 100)
    draw_ellipse(250, 270, 100, 90)

    # draw nose
    fill_black()
    draw_ellipse(340, 230, 45, 30)

    # draw eyes
    fill_white()
    draw_ellipse(240, 170, 20, 40)
    draw_ellipse(300, 170, 20, 40)
    fill_black()
    draw_ellipse(230, 170, 10, 20)
    draw_ellipse(290, 170, 10, 20)

    # draw mouth
    draw_ellipse(220, 310, 70, 50)

    # draw tongue
    fill_red()
    draw_ellipse(200, 320, 40, 30)
    draw_ellipse(230, 320, 40, 30)

    # draw name
    enable_stroke()
    set_font_italic()
    set_font_size(20)
    stroke_black()
    draw_line(0, 370, 400, 370)
    draw_line(20, 0, 20, 400)
    draw_line(380, 0, 380, 400)
    draw_text("Mickey Mouse, ", 40, 390)
    draw_text("Art by Rahul Gupta", 180, 390)


start_graphics(draw_mickey)