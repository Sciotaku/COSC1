# Author: Rahul Gupta
# Date: 03/08/2023
# Purpose: Lab 4 EC: Ask user to choose to type and input the start and goal vertex or use mouse.

from bfs import *
from cs1lib import *
from load_graph import *

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

# Prompt the user
prompt_user = True
wanna_type = False
wanna_mouse = False
if prompt_user:
    question = input("Do you want to type or use mouse pointer? Y or N: ")
    if question == "Y":
        wanna_type = True
        start_vertex_name = input("Enter the correct start location: ")
        goal_vertex_name = input("Enter the correct goal location: ")
    elif question == "N":
        wanna_mouse = True
    prompt_user = False


def draw_map():
    global start_vertex, goal_vertex, mouse_is_pressed, m_x, m_y, start_vertex_name, goal_vertex_name

    if not prompt_user:
        clear()
        # Draw the background image
        draw_image(img, 0, 0)

        # Iterate over all vertices and draw them and their edges
        for vertex in vertices.values():
            vertex.draw_vertex(0, 0, 1)  # draw the vertex with blue color
            vertex.draw_edges(0, 0, 1)  # draw the edges of the vertex with blue color

            # # Check if the mouse is on this vertex and update start or goal vertex if necessary

            if wanna_type:
                if start_vertex_name == vertex.name:
                    start_vertex = vertex
                if goal_vertex_name == vertex.name:
                    goal_vertex = vertex

            if wanna_mouse:
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


