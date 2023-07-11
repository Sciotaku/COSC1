# Author: Rahul Gupta
# Date: 2/19/2022
# Purpose: Body class for lab 2

from cs1lib import *


class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, r, g, b):

        # Defining instance variables
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.pixel_radius = pixel_radius
        self.r = r
        self.g = g
        self.b = b

    # Method to update position of the body

    def update_position(self, timestep):
        self.x = self.x + self.vx * timestep  # equation to calculate the x-position of body moving with velocity vx.
        self.y = self.y + self.vy * timestep  # equation to calculate the y-position of body moving with velocity vy.

    # Method to update velocity of the body
    def update_velocity(self, ax, ay, timestep):
        self.vx = self.vx + ax * timestep  # equation to calculate the x-velocity of body moving with acceleration ax.
        self.vy = self.vy + ay * timestep  # equation to calculate the y-velocity of body moving with acceleration ay.

    def draw(self, cx, cy, pixels_per_meter):
        set_fill_color(self.r, self.g, self.b)
        c_x = cx + self.x * pixels_per_meter  # calculate the instantaneous x-position of the body
        c_y = cy + self.y * pixels_per_meter  # calculate the instantaneous y-position of the body
        draw_circle(c_x, c_y, self.pixel_radius)
