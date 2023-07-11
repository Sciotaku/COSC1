# Author: Rahul Gupta
# Date: 03/08/2023
# Purpose: Lab 4 Breadth-first search algorithm

from collections import deque


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

