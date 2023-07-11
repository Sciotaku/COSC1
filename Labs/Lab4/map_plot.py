# Author: Rahul Gupta
# Date: 03/08/2023
# Purpose: map_plot function

from cs1lib import *
from load_graph import *
from bfs import breadth_first_search

# Load the image
img = load_image("dartmouth_map.png")

# Calculate image width and height to adjust the canvas size
img_width = img.width()
img_height = img.height()

# Call the load_graph function
vertices = load_graph("dartmouth_graph.txt")

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



