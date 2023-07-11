# Rahul Gupta
# Date: 02/08/2023
# Purpose: Flower class driver

from random import uniform, randint
from cs1lib import *


class Circle:
    def __init__(self, gx, gy, gsize, r, g, b):
        self.x = gx
        self.y = gy
        self.radius = gsize
        self.r = r
        self.g = g
        self.b = b

    def update(self, vx, vy):
        self.x = self.x + vx
        self.y = self.y + vy

    def draw(self):
        set_fill_color(self.r, self.g, self.b)
        draw_circle(self.x, self.y, self.radius)

    def __str__(self):
        return str(self.x) + " , " + str(self.y)


class Flower:
    def __init__(self, x, y, size, r, g, b):
        self.clist = []

        c1 = Circle(x - size, y - size, size, r, g, b)
        self.clist.append(c1)
        c2 = Circle(x + size, y - size, size, r, g, b)
        self.clist.append(c2)
        c3 = Circle(x + size, y + size, size, r, g, b)
        self.clist.append(c3)
        c4 = Circle(x - size, y + size, size, r, g, b)
        self.clist.append(c4)

    def update(self, vx, vy):
        for i in range(len(self.clist)):
            c = self.clist[i]
            c.update(vx, vy)

    def draw(self):
        for i in range(len(self.clist)):
            c = self.clist[i]
            c.draw()


# Circle Driver
# c = Circle(100, 200, 50, 1, 0, 1)


# def my_draw():
#     set_clear_color(1, 1, 1)
#     clear()
#
#     c.draw()
#     c.update(1, 1)
#
#
# start_graphics(my_draw)


# Flower Driver
N = 100
flist = []
i = 0
while i < N:
    f1 = Flower(randint(0, 500), 0, 10, uniform(0, 1), 0, uniform(0, 1))
    flist.append(f1)
    i = i + 1


def my_draw():
    set_clear_color(1, 1, 1)
    clear()

    f1.draw()
    f1.update(1, 1)

    for f in flist:
        f.draw()
        f.update(0, randint(1, 10))


start_graphics(my_draw, 1000)

