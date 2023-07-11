# Author: Rahul Gupta
# Date: 2/19/2022
# Purpose: SiriusAB system


from cs1lib import *
from system import System
from body import Body


# Constants for the Sirius AB binary star system
G = 6.67384e-11              # gravitational constant
TIME_SCALE = 3.0e5           # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FRAMERATE = 30               # frames per second
TIMESTEP = 1.0 / FRAMERATE   # time between drawing each frame

# Initializing the Sirius AB binary star system
siriusA = Body(2.02 * 1.9885e30, 4.52e10, 0, 0, 0, 7, 1, 1, 1)
siriusB = Body(1.00 * 1.9885e30, -4.52e10, 0, 0, 16640, 5, 1, 1, 1)

body_list = [siriusA, siriusB]
sirius_system = System(body_list)


def sirius():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    sirius_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    sirius_system.update(TIMESTEP * TIME_SCALE)


start_graphics(sirius, 2400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
