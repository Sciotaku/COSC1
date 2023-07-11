# Author: Rahul Gupta
# Date: 01/30/2023
# Purpose: Create a Pong Game

from cs1lib import *
from random import randint

# Create variables and constants
WINDOW_SIZE = 400

# Dimensions of the paddle
PADDLE_LENGTH = 100
PADDLE_WIDTH = 20

# Positions of the paddles
x_left_paddle = 0
x_right_paddle = 380
y_left_paddle = 150
y_right_paddle = 150

# Check the orientation of the paddles
left_up_paddle = False
left_down_paddle = False
right_up_paddle = False
right_down_paddle = False

# Check the status of the game
start_game = False
quit_game = False
restart_game = False
hit_left_wall = False
hit_right_wall = False

# Dimensions of the ball
c_x = 200
c_y = 200
c_r = 20

# Velocity of the ball
c_vx = randint(1, 5)
c_vy = randint(1, 5)

# Color of the ball
r = 1
g = 1
b = 1


# Check what key is pressed and perform the required operations
def keyword(key):
    global y_left_paddle, y_right_paddle, left_up_paddle, left_down_paddle, right_up_paddle, right_down_paddle
    global restart_game, quit_game, start_game

    if key == "s":
        start_game = True

    if key == "z":  # Check if the pressed key is z
        left_down_paddle = True

    if key == "a":  # Check if the pressed key is a
        left_up_paddle = True

    if key == "m":  # Check if the pressed key is m
        right_down_paddle = True

    if key == "k":  # Check if the pressed key is k
        right_up_paddle = True

    if key == "q":
        quit_game = True

    if key == " ":
        restart_game = True


# Check if key is released and stop the operation
def release(key):
    global start_game, right_up_paddle, right_down_paddle, left_down_paddle, left_up_paddle, restart_game, c_y, c_x
    if key == "z":
        left_down_paddle = False
    if key == "a":
        left_up_paddle = False
    if key == "m":
        right_down_paddle = False
    if key == "k":
        right_up_paddle = False


# Create ball and move it on the canvas
def ball():
    global y_left_paddle, y_right_paddle, left_up_paddle, left_down_paddle, right_up_paddle, right_down_paddle
    global c_x, c_vx, c_y, c_vy, hit_left_wall, hit_right_wall, restart_game, r, g, b

    set_fill_color(r, g, b)
    draw_circle(c_x, c_y, c_r)

    # If the ball hits the left paddle
    if y_left_paddle <= c_y <= y_left_paddle + PADDLE_LENGTH and c_x <= c_r + PADDLE_WIDTH:
        c_vx = - c_vx
        r = randint(0, 300) / 255
        g = randint(0, 300) / 255
        b = randint(0, 300) / 255

    # If the ball hits the right paddle
    if y_right_paddle <= c_y <= y_right_paddle + PADDLE_LENGTH and c_x >= WINDOW_SIZE - c_r - PADDLE_WIDTH:
        c_vx = - c_vx
        r = randint(0, 300) / 255
        g = randint(0, 300) / 255
        b = randint(0, 300) / 255

    # If the ball hits the left wall
    if c_x == c_r:
        hit_left_wall = True

    # If the ball hits the right wall
    if c_x == WINDOW_SIZE - c_r:
        hit_right_wall = True

    # If the ball hits the top wall
    if c_y <= c_r:
        c_vy = - c_vy

    # If the ball hits the bottom wall
    if c_y == WINDOW_SIZE - c_r:
        c_vy = - c_vy


# Draw the Pong table
def draw_pong():
    global x_left_paddle, x_right_paddle, y_left_paddle, y_right_paddle, left_up_paddle, left_down_paddle
    global c_x, c_y, c_vy, c_vx, hit_left_wall, hit_right_wall, restart_game, quit_game

    set_clear_color(1, 1, 0)  # Set yellow background
    clear()
    set_fill_color(0, 0, 0)  # Set black color for paddles

    if not start_game:
        set_stroke_color(1, 0, 0)
        draw_text("Welcome to Ping-Pong!!", 140, 180)
        draw_text("Press s to start the game.", 140, 200)

    if start_game:

        set_stroke_color(0, 0, 0)

        # Draw Paddles
        draw_rectangle(x_left_paddle, y_left_paddle, PADDLE_WIDTH, PADDLE_LENGTH)  # Left paddle
        draw_rectangle(x_right_paddle, y_right_paddle, PADDLE_WIDTH, PADDLE_LENGTH)  # Right paddle

        if left_down_paddle:
            if y_left_paddle >= (WINDOW_SIZE - PADDLE_LENGTH):  # Check if the left paddle hits the bottom wall
                y_left_paddle = 300
            y_left_paddle = y_left_paddle + 10  # Move the paddle

        if left_up_paddle:
            if y_left_paddle <= 0:  # Check if the left paddle hits the top wall
                y_left_paddle = 0
            y_left_paddle = y_left_paddle - 10  # Move the paddle

        if right_down_paddle:
            if y_right_paddle >= (WINDOW_SIZE - PADDLE_LENGTH):  # Check if the right paddle hits the bottom wall
                y_right_paddle = 300
            y_right_paddle = y_right_paddle + 10  # Move the paddle

        if right_up_paddle:
            if y_right_paddle <= 0:  # Check if the right paddle hits the top wall
                y_right_paddle = 0
            y_right_paddle = y_right_paddle - 10  # Move the paddle

        # Draw ball
        ball()
        c_x = c_x + c_vx
        c_y = c_y + c_vy

        # Check if the ball hits the left or right wall
        if hit_left_wall or hit_right_wall:
            c_vx = 0
            c_vy = 0
            draw_text("You lost the game", 150, 180)
            draw_text("Please press q to quit the game", 110, 200)
            draw_text("Please press space bar to restart the game", 80, 220)

        # Quit Game
        if quit_game:
            cs1_quit()

        # Restart Game
        if is_key_pressed(" "):
            hit_left_wall = False
            hit_right_wall = False

            # Draw ball at initial position
            c_x = 200
            c_y = 200
            c_vx = randint(1, 5)
            c_vy = randint(1, 5)

            # Draw Paddle at initial position
            x_left_paddle = 0
            x_right_paddle = 380
            y_left_paddle = 150
            y_right_paddle = 150


start_graphics(draw_pong, width=WINDOW_SIZE, height=WINDOW_SIZE, key_press=keyword, key_release=release)
