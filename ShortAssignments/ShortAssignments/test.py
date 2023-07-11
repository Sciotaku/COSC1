class Vertex:
    def __init__(self, data):
        self.adjacency_list = []
        self.data = data


def load_story(file_name):
    with open(file_name, 'r') as file:
        vertices = {}
        for line in file:
            name, connections, data = line.strip().split("|")
            vertex = Vertex(data)
            vertex.adjacency_list = connections.split(",")
            vertices[name] = vertex
        return vertices

def play_game(vertices):
    current_vertex = vertices["START"]
    while current_vertex.adjacency_list:
        print(current_vertex.data)
        for i, choice in enumerate(current_vertex.adjacency_list):
            print(chr(i + 97) + ")", vertices[choice].data)
        selection = input("Enter a choice: ")
        next_vertex = vertices[current_vertex.adjacency_list[ord(selection) - 97]]
        current_vertex = next_vertex
    print(current_vertex.data)

if __name__ == "__main__":
    vertices = load_story("story.txt")
    play_game(vertices)
