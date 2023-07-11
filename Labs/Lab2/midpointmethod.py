# Author: Rahul Gupta
# Date: 2/15/2022
# Purpose: Midpoint method of solar system

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

    def update(self, timestep):
        n_steps = 100  # divide the timestep into 100 smaller timesteps
        dt = timestep / n_steps  # calculate the duration of each smaller timestep

        for i in range(n_steps):
            for j in range(len(self.body_list)):

                # Compute acceleration at the beginning of the timestep
                ax1, ay1 = self.compute_acceleration(j)

                # Update velocity using current acceleration
                self.body_list[j].update_velocity(ax1, ay1, dt / 2)

                # Update position using current velocity
                self.body_list[j].update_position(dt / 2)

                # Compute acceleration again at the midpoint of the timestep
                ax2, ay2 = self.compute_acceleration(j)

                # Take the average of the accelerations to get the updated acceleration
                ax_avg = (ax1 + ax2) / 2
                ay_avg = (ay1 + ay2) / 2

                # Update velocity using updated acceleration
                self.body_list[j].update_velocity(ax_avg, ay_avg, dt / 2)

                # Update position using updated velocity
                self.body_list[j].update_position(dt / 2)
        return self.body_list


# Constants for the solar system
G = 6.67384e-11              # gravitational constant
TIME_SCALE = 3.0e6           # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FRAMERATE = 30               # frames per second
TIMESTEP = 1.0 / FRAMERATE   # time between drawing each frame

# Initializing the solar system
sun = Body(1.98892e30, 0, 0, 0, 0, 21, 1, 1, 0)
mercury = Body(3.3011e23, 5.791e10, 0, 0, 47400, 0.73191*5, 0.5, 0.5, 0.5)
venus = Body(4.8675e24, 1.0821e11, 0, 0, 35020, 1.815*5, 0.5, 0.4, 0.2)
earth = Body(5.97219e24, 1.496e11, 0, 0, 29783, 1.92*5, 0, 0, 1)
mars = Body(6.4171e23, 2.2794e11, 0, 0, 24140, 1.01685*5, 1, 0, 0)
body_list = [sun, mercury, venus, earth, mars]
solar_system = System(body_list)


# Main function
def solar():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)


start_graphics(solar, 2400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
