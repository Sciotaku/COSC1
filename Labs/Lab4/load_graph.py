# Author: Rahul Gupta
# Date: 03/08/2023
# Purpose: Load_graph function

from vertex import Vertex


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



