from collections import defaultdict
from math import sqrt


def listToString(s: list) -> str:
    return ' '.join(s)


def distance_between_coords(node1: list, node2: list) -> float:
    '''
    Return the distance between 2 input coords A(x1, y1) and B(x2, y2)
    by using Euclid distance.
    '''
    x1, y1 = node1[:2]
    x2, y2 = node2[:2]
    return sqrt( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) )


def name_coords(coords: list) -> list:
    '''
    Adds 'name' for coordinates to use as keys for edge detection
    '''
    n_coord = 0
    for coord in coords:
        n_coord += 1
        coord.append(n_coord)
    return coords


def graph(coords: dict, algorithm: str = None):
    '''
    Create weighted and undirected graph
    Returns:
        - Named coordinates and their connected edges as a dictionary for
        Dijkstra and Greedy algorithm.
        - All of them and the graph for Astar algorithm.
    '''
    coords = name_coords(coords)
    graphs = defaultdict(list)
    edges = {}

    for current in coords:
        for comparer in coords:
            if comparer == current:
                continue
            else:
                weight = distance_between_coords(current, comparer)
                graphs[current[2]].append(comparer[2]) 
                edges[current[2], comparer[2]] = weight 
    
    if algorithm == 'astar':
        return graphs, edges
    else:
        return edges
    

def heuristic(node1: list, node2: list) -> float:
    return distance_between_coords(node1, node2)