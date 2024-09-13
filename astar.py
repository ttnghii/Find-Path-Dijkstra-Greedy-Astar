from utils import heuristic

def a_star_path(
        coords: dict, 
        graph: dict, edges: dict, 
        start: list, goal: list
    ):
    open, close = set([start]), set()
    came_from = {}

    # g(x) is the shortest distance from start to node x
    g = {node[2]: float('inf') for node in coords}
    g[start] = 0

    # f = g + heuristic
    f = {node[2]: float('inf') for node in coords}
    f[start] = heuristic(coords[start - 1], coords[goal - 1])
    
    while open:
        current = min(open, key=lambda node: f[node])
        
        if current == goal:
            total_path = []
            while current in came_from:
                total_path.append(current)
                current = came_from[current]
            total_path.append(start)
            total_path.reverse()
            return total_path, f[current]

        open.remove(current)
        close.add(current)

        for neighbor in graph[current]:
            tentative_g = g[current] + edges[current, neighbor]

            if tentative_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = tentative_g
                f[neighbor] = g[neighbor] + heuristic(coords[neighbor - 1],
                                                      coords[goal - 1])
                if neighbor not in open:
                    open.add(neighbor)
                
    return None, float('inf')