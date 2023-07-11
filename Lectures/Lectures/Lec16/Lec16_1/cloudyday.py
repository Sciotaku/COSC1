from cs1lib import *
from random import randint


class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        set_fill_color(1, 1, 1)
        set_stroke_color(1, 1, 1)

        draw_ellipse(self.x, self.y, 30, 10)


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


def create_clouds(run_time):
    cloud_list = []
    for i in range(run_time):
        if randint(0, 50) < 4:
            x = randint(0, 100)
            y = randint(0, 100)
            cloud = Cloud(x, y)
            cloud_list.append(cloud)

    return cloud_list


def remove_offscreen(cloud_list):
    i = len(cloud_list) - 1
    while i >= 0:
        if cloud_list[i].x > 300:
            del cloud_list[i]
        i -= 1


def scene():
    set_clear_color(.5, .8, 1.0)  # light blue sky
    clear()

    set_fill_color(.7, 1.0, .7)   # light green grass
    draw_rectangle(0, 200, 300, 100)

    newclouds = create_clouds(1)

    for cloud in newclouds:
        clouds.append(cloud)

    for cloud in clouds:
        cloud.x += 1
        cloud.draw()

    for tree in forest:
        tree.draw()

    remove_offscreen(clouds)


forest = create_forest(30)
clouds = []

start_graphics(scene, 1000, height=300, width=300)
