#Author:Vasanta
#Date: 02/10/2023
#Purpose: Circle class file

from random import uniform

class Circle:
    def __init__(self, gx, gy, gsize):
        self.x = gx
        self.y = gy
        self.radius = gsize
        #For colors
        self.r = uniform(0.4, 0.9)
        self.g = uniform(0.4, 0.9)
        self.b = uniform(0.1, 0.9)

    def update(self, vx, vy):
        self.x = self.x + vx
        self.y = self.y + vy
