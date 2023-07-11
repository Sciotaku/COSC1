#Author:Vasanta
#Date: 02/10/2023
#Purpose: Flower class file

from Lectures.Lec16.Lec16_2.circle import Circle

class Flower:
    def __init__(self, x, y, size):
        self.c1 = Circle(x - size, y - size, size)
        self.c2 = Circle(x - size, y + size, size)
        self.c3 = Circle(x + size, y - size, size)
        self.c4 = Circle(x + size, y + size, size)

    def update(self, vx, vy):
        self.c1.update(vx, vy)
        self.c2.update(vx, vy)
        self.c3.update(vx, vy)
        self.c4.update(vx, vy)
