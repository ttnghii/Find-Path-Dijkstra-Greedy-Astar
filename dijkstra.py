from collections import list

def dijkstra(nodes: list, edges: list, start: list) -> tuple:
    
    '''
    Returns a path to all nodes with least weight 
    as a list of names from a specific node
    '''

    neighbor, total_weight = 0, 0
    current_node = start
    visited = [start]
    unvisited = [node[2] for node in nodes if node[2] != start]

    while unvisited:
        for index, neighbor in enumerate(unvisited):
            if index == 0:
                current_weight = edges[start, neighbor]
                current_node = neighbor
            elif edges[start, neighbor] < current_weight:
                current_weight = edges[start, neighbor]
                current_node = neighbor
            total_weight += current_weight
            unvisited.remove(current_node)
            visited.append(current_node)

    return visited, total_weight