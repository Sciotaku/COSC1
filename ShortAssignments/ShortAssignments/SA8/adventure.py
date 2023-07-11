# Filename: adventure.py
# Author Name: Rahul Gupta
# Date: 03/02/2023
# Purpose: SA8: To create an adventure game.

from vertex import Vertex


def parse_line(line):
    # Split the line into three sections based on the "|" delimiter.
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    # Extract the adjacent vertices from the second section of the line.
    adjacent_vertices = section_split[1].strip().split(",")

    # Add all adjacent vertices to a list, except empty strings.
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    # Extract the text from the third section of the line.
    text = section_split[2].strip()

    # Return the name of the vertex, its adjacent vertices, and its text.
    return vertex_name, adjacent, text


def load_story(filename):
    # Create an empty dictionary to store the vertices.
    vertex_dict = {}

    # Open the specified file and read each line.
    file = open(filename, "r")
    for l in file:

        # Check if the line is in the correct format.
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # Create a new Vertex object and add it to the dictionary.
            vertex_dict[vertex_name] = Vertex(adjacent_vertices, text)

    file.close()
    return vertex_dict


def play_game(vertex_dict):
    # Start the game at the "START" vertex
    current_vertex = vertex_dict["START"]

    # While there are still adjacent vertices, continue the game.
    while current_vertex.adjacent:
        # Print the text for the current vertex.
        print(current_vertex.text)

        # Prompt the player to choose a next move.
        choice = input("Choose your next move: ")

        # Check if the input is not a single letter.
        if len(choice) != 1:
            print("Please enter a valid input!")
        else:
            # Convert the letter to an index.
            choice_index = ord(choice.lower()) - ord('a')

            # Move to the next vertex.
            current_vertex = vertex_dict[current_vertex.adjacent[choice_index]]

    # Print the text for the final vertex.
    print(current_vertex.text)


# Load the story from the specified file.
story_dict = load_story("mystory.txt")

# Play the game with the loaded story.
play_game(story_dict)


