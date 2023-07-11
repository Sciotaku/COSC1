# Author: Rahul Gupta
# Date: 2/15/2022
# Purpose: SiriusAB Improved look

from cs1lib import *


class Body:
    def __init__(self, mass, x, y, vx, vy, image_file):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = load_image(image_file).scaled(50, 50)
        self.width = self.image.width()
        self.height = self.image.height()

    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep
        self.y = self.y + self.vy * timestep

    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep
        self.vy = self.vy + ay * timestep

    def draw(self, cx, cy, pixels_per_meter):
        draw_image(self.image, cx + self.x * pixels_per_meter - self.width / 2, cy + self.y * pixels_per_meter -
                   self.height / 2)


class System:
    def __init__(self, body_list):
        self.body_list = body_list  # Defining instance variable

    # Method to call the draw method in body class
    def draw(self, cx, cy, pixels_per_meter):
        for planet in self.body_list:
            planet.draw(cx, cy, pixels_per_meter)

    # Method to compute acceleration of the body
    def compute_acceleration(self, n):
        ax = 0
        ay = 0
        for i in range(len(self.body_list)):
            if i != n:
                # calculate the x distance between the Earth and the moon
                dx = self.body_list[i].x - self.body_list[n].x

                # calculate the y distance between the Earth and the moon
                dy = self.body_list[i].y - self.body_list[n].y

                # calculate the total distance between the Earth and the moon
                total_dist = (dx ** 2 + dy ** 2) ** (1 / 2)

                # Calculate the acceleration due to gravity
                a = 6.67 * 10 ** (-11) * self.body_list[i].mass / total_dist ** 2

                # Calculate the x-component of acceleration
                ax = ax + a * dx / total_dist

                # Calculate the x-component of acceleration
                ay = ay + a * dy / total_dist

        return ax, ay

    # Method to call the update_position and update_velocity in body class.
    def update(self, timestep):
        for i in range(len(self.body_list)):
            (ax, ay) = self.compute_acceleration(i)
            self.body_list[i].update_position(timestep)
            self.body_list[i].update_velocity(ax, ay, timestep)


# Constants for the Sirius AB binary star system
G = 6.67384e-11              # gravitational constant
TIME_SCALE = 3.0e5           # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FRAMERATE = 30               # frames per second
TIMESTEP = 1.0 / FRAMERATE   # time between drawing each frame

# Initializing the solar system
siriusA = Body(2.02 * 1.9885e30, 4.52e10, 0, 0, 0, "siriusA.jpg")
siriusB = Body(1.00 * 1.9885e30, -4.52e10, 0, 0, 0, "siriusB.jpg")

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