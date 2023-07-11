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
SHIP_SIZE = 10
SHIP_COLOR = [1, 1, 0]  # yellow

start = False


def keyword(key):
    global start, time_scale, ship_velocity, ship_position, score
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


# Check if the ship has hit any of the planets or the sun
def check_collision(ship_position, solar_system):
    for body in solar_system.get_bodies():
        distance = ((ship_position[0] - body.get_x())**2 + (ship_position[1] - body.get_y())**2)**0.5
        if distance < (body.get_radius() + SHIP_SIZE):
            return True
    return False


# Reset the game after a successful run
def reset_game():
    global score, ship_position
    score += 1
    ship_position = [WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50]


# Main function
def solar():
    global ship_position, ship_velocity, score

    set_clear_color(0, 0, 0)  # black background
    clear()

    if start:
        # Move the ship
        ship_position[1] += ship_velocity

        # Check for collisions
        if ship_position[1] < SHIP_SIZE or check_collision(ship_position, solar_system):
            print("Game over! Score:", score)
            score = 0
            ship_position = [WINDOW_WIDTH / 2, WINDOW_HEIGHT - 50]
            return

        # Check if the ship has reached the top wall
        if ship_position[1] > WINDOW_HEIGHT - SHIP_SIZE:
            reset_game()

        # Draw the background stars
        for i in range(100):
            x = uniform(0, WINDOW_WIDTH)
            y = uniform(0, WINDOW_HEIGHT)
            set_fill_color(1, 1, 1)
            draw_circle(x, y, 2)

        # Draw the system in its current state.
        solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

        # Draw the ship
        set_fill_color(SHIP_COLOR[0], SHIP_COLOR[1], SHIP_COLOR[2])
        draw_circle(ship_position[0], ship_position[1], SHIP_SIZE)

        # Update the system for its next state.
        solar_system.update(TIMESTEP * time_scale)

        # Draw the score
        set_stroke_color(1, 1, 1)
        draw_text("Score: " + str(score), 20, 20)


# Initializing the solar system
sun = Body(1.98892e30, 0, 0, 0, 0, 21, 1, 1, 0)
mercury = Body(3.3011e23, 5.791e10, 0, 0, 47400, 0.73191*5, 0.5, 0.5, 0.5)
venus = Body(4.8675e24, 1.0821e11, 0, 0, 35020, 1.815*5, 0.5, 0.4, 0.2)
earth = Body(5.97219e24, 1.496e11, 0, 0, 29783, 1.92*5, 0, 0, 1)
mars = Body(6.4171e23, 2.2794e11, 0, 0, 24140, 1.01685*5, 1, 0, 0)
body_list = [sun, mercury, venus, earth, mars]
solar_system = System(body_list)


start_graphics(solar, 2400, framerate=FRAMERATE, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
