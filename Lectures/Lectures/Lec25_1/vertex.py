#Author: Vasanta
#Date: 02/28/2023
#Purpose: Vertex class

class Vertex:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.adj_list = []
