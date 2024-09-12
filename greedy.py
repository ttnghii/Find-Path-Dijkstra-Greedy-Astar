def greedy(nodes: list, edges: dict, start: list) -> tuple:
    '''
    Build the function using Greedy algorithm to find the
    shortest path over all nodes from start node.
    '''
    current_node = start
    visited = [start]
    unvisited = [node[2] for node in nodes if node[2] != start]
    total_weight = 0

    while unvisited:
        nearest_neighbor = min(
            unvisited,
            key=lambda x: edges[current_node, x]
        )
        total_weight += edges[current_node, nearest_neighbor]

        current_node = nearest_neighbor
        unvisited.remove(nearest_neighbor)
        visited.append(nearest_neighbor)