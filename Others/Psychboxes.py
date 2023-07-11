# Psychboxes.py
# Gives the illusion of rectangles infinitely moving out from the center.

from cs1lib import *

WINDOW_SIZE = 400       # size of the window, in pixels
BOX_THICKNESS = 4       # thickness of each box, in pixels

iteration = 0  # which iteration we're on; used to change colors
box_number = 1  # just so we can determine the box color
corner = 0          # (x, y) coordinates of upper left of current box
size = WINDOW_SIZE  # width & height of the current box


def draw_boxes():
    global iteration, box_number, corner, size

    disable_stroke()    # it's better without the outlines
    clear()

    box_number = 1  # just so we can determine the box color
    corner = 0          # (x, y) coordinates of upper left of current box
    size = WINDOW_SIZE  # width & height of the current box

    # Draw all the boxes, from largest to smallest.  Each box covers the
    # interior of all the boxes larger than it.
    while size > 0:
        # Determine the color of the box.  For a given box, the color will
        # change from iteration to iteration.
        if (box_number + iteration) % 4 == 0:
            set_fill_color(1, 0, 0)     # red
        elif (box_number + iteration) % 4 == 1:
            set_fill_color(0, 0, 1)     # blue
        elif (box_number + iteration) % 4 == 2:
            set_fill_color(0, 0.8, 0)   # green
        else:
            set_fill_color(1, 1, 0)     # yellow

        draw_rectangle(corner, corner, size, size)

        # Go on to the next box.  It's a little smaller than this one.
        box_number = box_number + 1
        corner = corner + BOX_THICKNESS
        size = size - (2 * BOX_THICKNESS)

    iteration = (iteration - 1) % 4 # so that colors change in the next frame


start_graphics(draw_boxes, 2400)