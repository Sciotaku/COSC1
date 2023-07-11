from cs1lib import *


class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        set_fill_color(.5, .4, 0)
        draw_rectangle(self.x, self.y - 20, 5, 20)
        set_fill_color(0, .7, 0)
        draw_circle(self.x + 2, self.y - 30, 12)


def scene():
    set_clear_color(.5, .8, 1.0)  # light blue sky
    clear()

    disable_stroke()
    set_fill_color(.7, 1.0, .7)   # light green grass
    draw_rectangle(0, 200, 300, 100)

    tree.draw()


tree = Tree(100, 250)

start_graphics(scene, 2400)