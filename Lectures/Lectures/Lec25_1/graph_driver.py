from Lectures.Lec25_1.vertex import Vertex

vertex_dict = {}

v1 = Vertex("Hanover", 6000)
vertex_dict["Hanover"] = v1

v2 = Vertex("WestLebanon", 7000)
vertex_dict["WestLebanon"] = v2

v3 = Vertex("Lebanon", 15000)
vertex_dict["Lebanon"] = v3


v1.adj_list.append("WestLebanon")
v2.adj_list.append("Hanover")

v1.adj_list.append("Lebanon")
v3.adj_list.append("Hanover")

