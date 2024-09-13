def dijkstra_path(coords: dict, edges: dict, start: list) -> tuple:
    '''
    Returns a path to all nodes with least weight 
    as a list of names from a specific node
    '''

    neighbor, total_weight = 0, 0
    current_node = start
    visited = [start]
    unvisited = [node[2] for node in coords if node[2] != start]

    while unvisited:
        for index, neighbor in enumerate(unvisited):
            if index == 0:
                current_weight = edges[start, neighbor]
                current_node = neighbor
            elif edges[start, neighbor] < current_weight:
                current_weight = edges[start, neighbor]
                current_node = neighbor
        total_weight += current_weight
        visited.append(current_node)
        unvisited.remove(current_node)

    return visited, total_weight