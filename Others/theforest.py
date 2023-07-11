from cs1lib import *
from random import randint


class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        set_fill_color(.5, .4, 0)
        set_stroke_color(.5, .4, 0)

        draw_rectangle(self.x, self.y - 20, 5, 20)
        set_fill_color(0, .7, 0)

        set_stroke_color(0, .5, 0)
        draw_circle(self.x + 2, self.y - 30, 12)


def key_y(tree):
    return tree.y


def create_forest(num_trees):
    trees = []
    for i in range(num_trees):
        x = randint(0, 300)
        y = randint(200, 300)
        tree = Tree(x, y)
        trees.append(tree)

    trees.sort(key=key_y)
    return trees


def scene():
    set_clear_color(.5, .8, 1.0)  # light blue sky
    clear()

    set_fill_color(.7, 1.0, .7)   # light green grass
    draw_rectangle(0, 200, 300, 100)

    for tree in forest:
        tree.draw()


forest = create_forest(30)

start_graphics(scene, 1)
