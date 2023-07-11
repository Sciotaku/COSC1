# Author: Rahul Gupta
# Date: 03/08/2023
# Purpose: Lab 4 Vertex Class

from cs1lib import *

# Constants
RADIUS = 8
LINE_WIDTH = 2


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adjacency_list = []

    # Method to add adjacent vertices in the adjacency list
    def add_adjacent_vertices(self, neighbour):
        self.adjacency_list.append(neighbour)

    # Method to draw the vertices
    def draw_vertex(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, RADIUS)

    # Method to connect the start and goal vertices
    def draw_edge(self, neighbour, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(LINE_WIDTH)
        draw_line(self.x, self.y, neighbour.x, neighbour.y)

    # Method to draw the edges connecting each and every vertices on the campus map
    def draw_edges(self, r, g, b):
        for neighbour in self.adjacency_list:
            self.draw_edge(neighbour, r, g, b)

    # Method that returns a boolean indicating whether this location is within the smallest surrounding square
    # for this vertex.
    def is_on_vertex(self, x, y):
        return self.x + RADIUS >= x >= self.x - RADIUS and self.y + RADIUS >= y >= self.y - RADIUS
