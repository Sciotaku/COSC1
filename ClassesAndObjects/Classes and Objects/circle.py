from random import *


class circle:
    def __init__(self, gx, gy, gsize):
        self.x = gx
        self.y = gy
        self.radius = gsize
        # For colors
        self.r = uniform(0.4, 0.9)
        self.g = uniform(0.4, 0.9)
        self.b = uniform(0.4, 0.9)

    def update(self, vx, vy):
        self.x = self.x + vx
        self.y = self.y + vy


class flower:
    def __init__(self, x, y, size):
        self.c1 = circle(x - size, y - size, size)
        self.c2 = circle(x + size, y - size, size)
        self.c3 = circle(x + size, y + size, size)
        self.c4 = circle(x - size, y - size, size)

    def update(self, vx, vy):
        self.c1.update(vx, vy)


f1 = flower(200, 200, 50)
print(f1.c1.update(2, 4))
