# Author: Rahul Gupta
# Date: 2/15/2022
# Purpose: Solar System Game

from cs1lib import *


class Body:
    def __init__(self, mass, x, y, vx, vy, image_file):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = load_image(image_file).scaled(10, 10)
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


# Constants for the solar system
G = 6.67384e-11              # gravitational constant
TIME_SCALE = 3.0e6           # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
FRAMERATE = 30               # frames per second
TIMESTEP = 1.0 / FRAMERATE   # time between drawing each frame

# Initialize the solar system
sun = Body(1.98892e30, 0, 0, 0, 0, "sun.jpg")
mercury = Body(3.3011e23, 5.791e10, 0, 0, 47400, "mercury.jpg")
venus = Body(4.8675e24, 1.0821e11, 0, 0, 35020, "venus.jpg")
earth = Body(5.97219e24, 1.496e11, 0, 0, 29783, "earth.jpg")
mars = Body(6.4171e23, 2.2794e11, 0, 0, 24140, "mars.jpg")

body_list = [sun, mercury, venus, earth, mars]
solar_system = System(body_list)


# Main function
mass = 0    # mass of new planet being created
ship = Body(1000, 0, 0, 0, 0, "ship.jpg")    # create a new ship object
start = False


def game():

    global mass    # use the global mass variable

    # Check for mouse clicks to add new planets
    if is_mouse_pressed():
        # Create a new planet at the mouse location with mass determined by how long the button is held down
        if mass > 0:
            x, y = mouse_x() - WINDOW_WIDTH / 2, mouse_y() - WINDOW_HEIGHT / 2
            planet = Body(mass, x / PIXELS_PER_METER, y / PIXELS_PER_METER, 0, 0, "jupiter.jpg")
            solar_system.body_list.append(planet)
            mass = 0

    # Check for arrow key presses to control the ship's thrusters
    if is_key_pressed("left"):
        ship.vx -= 100
    elif is_key_pressed("right"):
        ship.vx += 100
    if is_key_pressed("up"):
        ship.vy -= 100
    elif is_key_pressed("down"):
        ship.vy += 100

    # Update the ship's position and velocity
    ship.update_position(TIMESTEP * TIME_SCALE)
    ship.update_velocity(0, 0, TIMESTEP * TIME_SCALE)

    # Draw the system in its current state.
    solar_system.draw(WINDOW_WIDTH / 2 - ship.x * PIXELS_PER_METER, WINDOW_HEIGHT / 2 - ship.y * PIXELS_PER_METER, PIXELS_PER_METER)
    ship.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    solar_system.update(TIMESTEP * TIME_SCALE)

    # Display the mass of the new planet being created
    set_font_size(20)
    set_fill_color(1, 1, 1)
    draw_text("Mass", 10, 30)

    # Increase the mass of the new planet the longer the mouse button is held down
    if is_mouse_pressed():
        mass += 100 * TIMESTEP * TIME_SCALE


start_graphics(game, 2400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
