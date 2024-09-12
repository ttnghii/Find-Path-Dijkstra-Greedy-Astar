from collections import list, defaultdict
from math import sqrt


def distance_between_coords(
        x1: float, y1: float, 
        x2: float, y2: float
        ) -> float:
    '''
    Return the distance between 2 input coords A(x1, y1) and B(x2, y2)
    by using Euclid distance.
    '''
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


def graph(coords: list) -> tuple:
    '''
    Create weighted and undirected graph
    Returns named coordinates and their connected edges as a dictionary
    '''
    coords = name_coords(coords=coords)
    # Because there is small graphs, so we use adjacency matrix
    adjacency_edge = defaultdict(list)

    for current in coords:
        for comparer in coords:
            if comparer == current:
                continue
            weight = distance_between_coords(current[0], current[1], comparer[0], comparer[1])
            adjacency_edge[current[2]].append((comparer[2], weight))

    return coords, adjacency_edge