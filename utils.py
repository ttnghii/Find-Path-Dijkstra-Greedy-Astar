from collections import defaultdict
from math import sqrt
from dijkstra import dijkstra_path
from greedy import greedy_path
from astar import a_star_path
import itertools


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


def make_directory(link: list, final_path: list, GPS: list) -> list:
    for i in final_path:
        i -= 1
        link.append(str(GPS[i]) + '/')

    final_link = listToString(link)
    remove = ['[', ' ', ']']
    
    [final_link.replace(i, '') for i in remove]

    return final_link


def shortest_path(
        algorithm: str, 
        coords: dict, 
        edges: dict
    ) -> tuple:
    '''
    Find the shortest (optimizal) path for this route by using Dijkstra or Greedy algorithm
    Return:
        - final_path (list): the list contain the final path for this route
        - final_path_weight (float): the weight corresponding for the final_path
    '''
    final_path = list
    final_path_weight = float('inf')

    for _, node in enumerate(coords):
        if algorithm == 'dijkstra':
            path, weight = dijkstra_path(coords, edges, node[2])
        elif algorithm == 'greedy':
            path, weight = greedy_path(coords, edges, node[2])
   
        if weight < final_path_weight:
            final_path_weight = weight
            final_path = path

    return final_path, final_path_weight


def shortest_path_astar(
        coords: dict, 
        graph: dict, 
        edges: dict
    ) -> tuple:
    '''
    Find the shortest (optimizal) path for this route by using Astar algorithm
    Return:
        - final_path (list): the list contain the final path for this route
        - final_path_weight (float): the weight corresponding for the final_path
    '''
    final_path, final_path_weight = None, float('inf')
    nodes = [node[2] for node in coords]

    for perm in itertools.permutations(nodes):
        current_path, current_weight = [], 0
        valid_path = True

        for i in range(len(perm) - 1):
            path, weight = a_star_path(
                coords=coords,
                graph=graph,
                edges=edges,
                start=perm[i],
                goal=perm[i + 1]
            )
            if path is None:
                valid_path = False
                break
            current_path.extend(path[:-1])
            current_weight += weight

        if valid_path:
            current_path.append(perm[-1])

        if valid_path and current_weight < final_path_weight:
            final_path_weight = current_weight
            final_path = current_path
    
    return final_path, final_path_weight