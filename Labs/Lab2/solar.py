# Author: Rahul Gupta
# Date: 2/19/2022
# Purpose: solar system driver for lab 2


from cs1lib import *
from system import System
from body import Body

# Constants for the solar system
G = 6.67384e-11              # gravitational constant
TIME_SCALE = 3.0e6           # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FRAMERATE = 30               # frames per second
TIMESTEP = 1.0 / FRAMERATE   # time between drawing each frame


# Main function
def solar():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)


# Initializing the solar system
sun = Body(1.98892e30, 0, 0, 0, 0, 20, 1, 1, 0)  # yellow sun
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 0.73191*5, 0.5, 0.5, 0.5)  # gray mercury
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 1.815*5, 0.5, 0.4, 0.2)  # brown venus
earth = Body(5.97e24, -149.6e9, 0, 0, 29790, 1.92*5, 0, 0, 1)  # blue earth
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 1.01685*5, 1, 0, 0)  # red mars
body_list = [sun, mercury, venus, earth, mars]
solar_system = System(body_list)

start_graphics(solar, 2400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
