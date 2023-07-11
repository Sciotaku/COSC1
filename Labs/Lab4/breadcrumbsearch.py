# Author: Rahul Gupta
# Date: 03/08/2023
# Purpose: Lab 4 Breadcrumb search algorithm


from collections import deque


def breadcrumb_search(start_vertex, goal_vertex):
    frontier_start = deque([start_vertex])  # frontier queue for the search from the start vertex
    frontier_goal = deque([goal_vertex])  # frontier queue for the search from the goal vertex
    visited_start = {start_vertex}  # vertices visited by the search from the start vertex
    visited_goal = {goal_vertex}  # vertices visited by the search from the goal vertex

    # map visited vertices to their breadcrumb vertices in the start search
    breadcrumbs_start = {start_vertex: None}

    # map visited vertices to their breadcrumb vertices in the goal search
    breadcrumbs_goal = {goal_vertex: None}

    # Explore vertices in the frontier queues from start.
    while goal_vertex not in breadcrumbs_start and len(frontier_start) != 0:
        # Take the next vertex from the frontier queue for the search from the start vertex
        curr_vertex_start = frontier_start.popleft()
        if curr_vertex_start is None:  # skip None vertices
            continue
        for adj_vertex_start in curr_vertex_start.adjacency_list:
            # Explore the neighbors of curr_vertex_start
            if adj_vertex_start not in visited_start:
                frontier_start.append(adj_vertex_start)
                visited_start.add(adj_vertex_start)
                breadcrumbs_start[adj_vertex_start] = curr_vertex_start

    # If goal was not reached, there is no path
    if goal_vertex not in breadcrumbs_start:
        return None

    path1 = []
    curr_vertex = goal_vertex
    while curr_vertex is not None:
        path1.append(curr_vertex)
        curr_vertex = breadcrumbs_start[curr_vertex]

    # Explore vertices in the frontier queues from goal.
    while goal_vertex not in breadcrumbs_goal and len(frontier_goal) != 0:
        # Take the next vertex from the frontier queue for the search from the goal vertex
        curr_vertex_goal = frontier_goal.popleft()
        if curr_vertex_goal is None:  # skip None vertices
            continue
        for adj_vertex_goal in curr_vertex_goal.adjacency_list:
            # Explore the neighbors of curr_vertex_goal
            if adj_vertex_goal not in visited_goal:
                frontier_goal.append(adj_vertex_goal)
                visited_goal.add(adj_vertex_goal)
                breadcrumbs_goal[adj_vertex_goal] = curr_vertex_goal

    # If goal was not reached, there is no path
    if goal_vertex not in breadcrumbs_goal:
        return None

    path2 = []
    curr_vertex = goal_vertex
    while curr_vertex is not None:
        path2.append(curr_vertex)
        curr_vertex = breadcrumbs_goal[curr_vertex]

    return path1 + path2



