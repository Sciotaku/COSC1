from random import uniform
from face import Face


class Crowd:
    def __init__(self, n):
        self.face_list = []
        for i in range(0, n):
            self.face_list.append(Face(int(uniform(20, 380)), int(uniform(20, 380)), 30))

    def lookat(self, lx, ly):
        for i in range(0, len(self.face_list)):
            self.face_list[i].lookat(lx, ly)

    def draw(self):
        for i in range(0, len(self.face_list)):
            self.face_list[i].draw()








