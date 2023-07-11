# Author: Rahul Gupta
# Date: 01/30/2023
# Purpose: Create a Pong Game

from cs1lib import *

# Variables and constants
WINDOW_SIZE = 400
PADDLE_LENGTH = 100
PADDLE_WIDTH = 20
x_left_paddle = 0
x_right_paddle = 380
y_left_paddle = 150
y_right_paddle = 150
left_up_paddle = False
left_down_paddle = False
right_up_paddle = False
right_down_paddle = False


# Check and run based on the pressed key
def keyword(key):
    global y_left_paddle, y_right_paddle, left_up_paddle, left_down_paddle, right_up_paddle, right_down_paddle

    if is_key_pressed("z"):  # Check if the pressed key is z
        left_down_paddle = True

    if is_key_pressed("a"):  # Check if the pressed key is a
        left_up_paddle = True

    if is_key_pressed("m"):  # Check if the pressed key is m
        right_down_paddle = True

    if is_key_pressed("k"):  # Check if the pressed key is k
        right_up_paddle = True


# Check if key is released
def release(key):
    global right_up_paddle, right_down_paddle, left_down_paddle, left_up_paddle
    if key == "z":
        left_down_paddle = False
    if key == "a":
        left_up_paddle = False
    if key == "m":
        right_down_paddle = False
    if key == "k":
        right_up_paddle = False


# Draw the Pong table
def draw_pong():
    global x_left_paddle, x_right_paddle, y_left_paddle, y_right_paddle, left_up_paddle, left_down_paddle

    set_clear_color(1, 1, 0)  # Set yellow background
    clear()
    set_fill_color(0, 0, 0)  # Set black color for paddles

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


start_graphics(draw_pong, width=WINDOW_SIZE, height=WINDOW_SIZE, key_press=keyword, key_release=release)