from collections import list, dict 
from utils import heuristic
import itertools

def a_star(
        nodes: list, 
        graph: dict, edges: dict, 
        start: list, goal: list
    ):
    open, close = set([start]), set()
    came_from = dict()

    # g(x) is the shortest distance from start to node x
    g = {node[2]: float('inf') for node in nodes}
    g[start] = 0

    # f = g + heuristic
    f = {node[2]: float('inf') for node in nodes}
    f[start] = heuristic(nodes[start - 1], nodes[goal - 1])
    
    while open:
        
        current = min(open, key=lambda node: f[node])
        
        if current == goal:
            total_path = list
            while current in came_from:
                total_path.append(current)
                current = came_from[current]
            total_path.append(start)
            total_path.reverse()
            return total_path, f[current]

        open.remove(current)
        close.add(current)

        for neighbor in graph[current]:

            if neighbor in close:
                continue
            tentative_g = g[current] + edges[current, neighbor]

            if neighbor not in open:
                open.add(neighbor)
            elif tentative_g >= g[neighbor]:
                continue
            
            came_from[neighbor] = current
            g[neighbor] = tentative_g
            f[neighbor] = g[neighbor] + heuristic(nodes[neighbor - 1],
                                                  nodes[goal - 1])
            
        return None, float('inf')
    

def shortest_path(coords: list, graph: dict, edges: dict):
    
    shortest_path_taken, shortest_path_weight = None, float('inf')
    nodes = [node[2] for node in coords]

    for perm in itertools.permutations(nodes):
        
        current_path, current_weight = [], 0
        valid_path = True

        for i in range(len(perm) - 1):
            path, weight = a_star(
                coords=coords,
                graph=graph,
                edges=edges,
                start=perm[i],
                goal=perm[i + 1]
            )
            if not path:
                valid_path = False
                break
            current_path.extend(path[:-1])
            current_path += weight

        if valid_path:
            current_path.append(perm[-1])

        if valid_path and current_weight < shortest_path_weight:
            shortest_path_weight = current_weight
            shortest_path_taken = current_path

        return shortest_path_taken, shortest_path_weight