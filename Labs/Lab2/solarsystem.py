# Author: Rahul Gupta
# Date: 2/19/2022
# Purpose: Built a solar system with stars


from cs1lib import *
from system import System
from body import Body
from random import uniform


# Constants for the solar system
G = 6.67428e-11  # gravitational constant
time_scale = 1000000  # real seconds per simulation second
PIXELS_PER_METER = 1 / 1e9  # distance scale for the simulation
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
FRAMERATE = 30             # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame


def keyword(key):
    global start, time_scale
    if key == "s":
        start = True
    if key == "p":
        start = False
    if key == "e":
        cs1_quit()
    if key == ".":
        time_scale = time_scale * 2
    if key == ",":
        time_scale = time_scale / 2


# Main function
def solar():

    set_clear_color(0, 0, 0)  # black background
    clear()

    set_stroke_color(1, 1, 1)
    draw_text("Welcome to my solar system!!", 400, 100)
    draw_text("Please press s to start!!", 400, 120)
    draw_text("Please press p to pause!!", 400, 140)
    draw_text("Please press e to exit!!", 400, 160)
    draw_text("Please press > to increase timescale!!", 400, 180)
    draw_text("Please press < to decrease timescale!!", 400, 200)

    if start:
        # Draw the stars in the background
        for i in range(100):
            x = uniform(0, WINDOW_WIDTH)
            y = uniform(0, WINDOW_HEIGHT)
            set_fill_color(1, 1, 1)
            draw_circle(x, y, 2)

        # Draw the system in its current state.
        solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

        # Update the system for its next state.
        solar_system.update(TIMESTEP * time_scale)


# Initializing the solar system
sun = Body(1.98892e30, 0, 0, 0, 0, 21, 1, 1, 0)
mercury = Body(3.3011e23, 5.791e10, 0, 0, 47400, 0.73191*5, 0.5, 0.5, 0.5)
venus = Body(4.8675e24, 1.0821e11, 0, 0, 35020, 1.815*5, 0.5, 0.4, 0.2)
earth = Body(5.97219e24, 1.496e11, 0, 0, 29783, 1.92*5, 0, 0, 1)
mars = Body(6.4171e23, 2.2794e11, 0, 0, 24140, 1.01685*5, 1, 0, 0)
jupiter = Body(1.8982e27, 3.785e11, 0, 0, 13070, 6.9911, 0.6, 0.7, 0.2)
body_list = [sun, mercury, venus, earth, mars, jupiter]
solar_system = System(body_list)
start = False

start_graphics(solar, 2400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, key_press=keyword)
