from Recitations.R5.point import Point


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return str(self.p1) + " and " + str(self.p2) + " are two end points of the line."
