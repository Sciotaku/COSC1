# Filename: adventure.py
# Author Name: Rahul Gupta
# Date: 03/02/2023
# Purpose: SA8: To create a vertex class for the adventure game.


class Vertex:
    def __init__(self, adjacent, text):
        # Instance variables to initialize the Vertex object with its adjacent vertices and text.
        self.adjacent = adjacent
        self.text = text

