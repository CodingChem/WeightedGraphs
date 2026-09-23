import heapq
from helpers import reconstruct_path

def a_star(graph, start, goal, h):
    # start prioritet blir avstanden
    frontier = [(h(start), start)]
    cost_so_far = {start: 0}
    came_from = {}
    visited = []
    seen = set()

    while frontier:
        f_cost, node = heapq.heappop(frontier)
        if node not in seen:
            seen.add(node)
            visited.append(node)

        if node == goal:
            break

        for neighbour, weight in graph[node]:
            # new_cost = g(n)
            new_cost = cost_so_far[node] + weight

            if neighbour not in cost_so_far or new_cost < cost_so_far[neighbour]:
                cost_so_far[neighbour] = new_cost
                came_from[neighbour] = node
                # Vi bruker f score i køen
                # f(n) = g(n) + h(n)
                f_score = new_cost + h(neighbour)
                heapq.heappush(frontier, (f_score, neighbour))

    path = reconstruct_path(came_from, start, goal)
    return path, visited
