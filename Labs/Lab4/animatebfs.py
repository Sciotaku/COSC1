# Author: Rahul Gupta
# Date: 03/08/2023
# Purpose: Lab 4 EC: Animate breath-first search

from cs1lib import *
from collections import deque
from random import *

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


def load_graph(file_name):
    vertices = {}

    # First pass: create Vertex objects and add them to dictionary
    file = open(file_name, "r")
    for line in file:
        # Split the line into name, adjacent vertices, and coordinates
        line_list = line.strip().split(";")
        name = line_list[0]
        coordinates = line_list[2]

        # Split the coordinates into x and y
        coord_list = coordinates.strip().split(",")
        x = coord_list[0]
        y = coord_list[1]

        # Create new Vertex object and add to dictionary
        vertex = Vertex(name, int(x), int(y))
        vertices[name] = vertex

    file.close()

    # Second pass: add adjacent vertices to the adjacency list in the dictionary
    file = open(file_name, "r")
    for line in file:
        # Split the line into name and adjacent vertices.
        name, adjacent_vertices, coordinates = line.strip().split(";")  # Shorter way than in the first pass

        # Find the Vertex object for the current vertex
        current_vertex = vertices[name]

        # Add references to adjacent vertices to the adjacency list
        for adjacent_name in adjacent_vertices.strip().split(","):
            adjacent_vertex = vertices[adjacent_name.strip()]
            current_vertex.add_adjacent_vertices(adjacent_vertex)

    file.close()
    return vertices


def breadth_first_search(start_vertex, goal_vertex):
    frontier = deque([start_vertex])  # frontier queue contains the vertices to be explored
    backpointer = {start_vertex: None}  # Store the parent of each vertex in the path

    # Maintain a queue for the frontier of the breadth-first search: the vertices that have been reached from the
    # start vertex but have not yet been explored from.
    while goal_vertex not in backpointer and len(frontier) != 0:
        # Take the next vertex from the frontier and explore its neighbors
        curr_vertex = frontier.popleft()
        if curr_vertex is None:  # skip None vertices
            continue
        for adj_vertex in curr_vertex.adjacency_list:  # explore the neighbors of curr_vertex
            if adj_vertex not in backpointer:  # if adj_vertex hasn't been explored before
                frontier.append(adj_vertex)  # add it to the frontier
                backpointer[adj_vertex] = curr_vertex  # set its parent to curr_vertex

    # If goal was not reached, there is no path
    if goal_vertex not in backpointer:
        return None

    # Reconstruct the path from start to goal using backpointers
    path = []
    curr_vertex = goal_vertex
    while curr_vertex is not None:  # follow the backpointers from goal to start
        path.append(curr_vertex)  # add each vertex to the path
        curr_vertex = backpointer[curr_vertex]  # move to the parent of curr_vertex

    return path


# Load the image
img = load_image("dartmouth_map.png")

# Calculate image width and height to adjust the canvas size
img_width = img.width()
img_height = img.height()

# Call the load_graph function
vertices = load_graph("new_dartmouth_graph.txt")

# Defining variables
start_vertex = None
goal_vertex = None
mouse_is_pressed = False
m_x = 0  # x position of mouse
m_y = 0  # y position of mouse


def draw_map():
    global start_vertex, goal_vertex, mouse_is_pressed, m_x, m_y

    clear()
    # Draw the background image
    draw_image(img, 0, 0)

    # Iterate over all vertices and draw them and their edges
    for vertex in vertices.values():
        vertex.draw_vertex(0, 0, 1)  # draw the vertex with blue color
        vertex.draw_edges(0, 0, 1)  # draw the edges of the vertex with blue color

        # Check if the mouse is on this vertex and update start or goal vertex if necessary
        if vertex.is_on_vertex(m_x, m_y):
            if mouse_is_pressed:
                start_vertex = vertex
                mouse_is_pressed = False
            else:
                goal_vertex = vertex

    # Draw start and goal vertices in red
    if start_vertex is not None:
        # Draw the start vertex with red color
        start_vertex.draw_vertex(1, 0, 0)
    if goal_vertex is not None:
        # Draw the goal vertex with red color
        goal_vertex.draw_vertex(1, 0, 0)

    # Draw path between start and goal vertices
    path = breadth_first_search(start_vertex, goal_vertex)
    if path is not None:
        # Draw the path edges in red
        for i in range(len(path) - 1):
            vertex1 = path[i]
            vertex2 = path[i + 1]
            vertex1.draw_edge(vertex2, 1, 0, 0)  # Draw the edge between the two vertices with red color

        # Draw the vertices in the path in red
        for vertex in path:
            vertex.draw_vertex(1, 0, 0)
            set_stroke_width(10)
            set_stroke_color(1, 0, 0)
            enable_stroke()
            draw_text(vertex.name, vertex.x - 20, vertex.y - 20)
            if vertex is not goal_vertex and start_vertex:
                vertex.draw_vertex(uniform(0, 1), uniform(0, 1), uniform(0, 1))


def check_mouse_move(x, y):
    global m_x, m_y
    m_x = x
    m_y = y


def check_mouse_press(x, y):
    global mouse_is_pressed

    # Check if the mouse is on a vertex
    for name, vertex in vertices.items():
        if vertex.is_on_vertex(x, y):
            mouse_is_pressed = True


start_graphics(draw_map, width=img_width, height=img_height, mouse_press=check_mouse_press, mouse_move=check_mouse_move)


