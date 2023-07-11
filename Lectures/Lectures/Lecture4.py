from cs1lib import *

# def mydraw(): #cannot take any parameters
    # set_clear_color(1,1,1)
    # clear()

    # draw_circle(100,100,50)

# start_graphics(mydraw) # do not call the mydraw fuction, use only the name

# Input: x and y coordinates of the eya and the size of the eye
# Output: Draws the eye on the canvas set by start_graphics

SX = 200
SY = 200
SSIZE = 100

def draw_eyes(x, y, size):
    set_stroke_color(1,1,1)
    set_stroke_width(1)
    #Draw outer circle of the smiley
    set_fill_color(1,1,1)
    draw_circle(x, y, size)

    #Draw inner circle
    in_size = size//2
    set_fill_color(0,0,0)
    draw_circle(x, y - in_size, in_size)


def draw_smiley():
    set_clear_color(1,1,1)
    clear()

    #draw face
    set_fill_color(1,1,0)
    draw_circle(SX,SY,SSIZE)

    #draw mouth
    x1 = int(SX-SSIZE*0.3)
    y1 = int(SY+SSIZE*0.3)
    x2 = int(SX+SSIZE*0.3)
    y2 = int(SY+SSIZE*0.3)
    set_stroke_color(1,0,0)
    enable_stroke()
    set_stroke_width(2)
    draw_line(x1, y1, x2, y2)

    #draw eyes
    #left eye
    ex1 = int(SX-SSIZE*0.3)
    ey1 = int(SY-SSIZE*0.3)
    eye_size = int(0.2*100)
    draw_eyes(ex1, ey1, eye_size )

    #right eye
    ex2 = int(SX + SSIZE * 0.3)
    ey2 = int(SY - SSIZE * 0.3)
    eye_size = int(0.2 * 100)
    draw_eyes(ex2, ey2, eye_size)

start_graphics(draw_smiley)




