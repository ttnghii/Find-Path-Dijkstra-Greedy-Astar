import itertools
from utils import listToString
from dijkstra import dijkstra_path
from greedy import greedy_path
from astar import a_star_path


def shortest_path(
        algorithm: str, 
        coords: dict,
        edges: dict,
        graph: dict = None, 
    ) -> tuple:
    '''
    Find the shortest (optimizal) path for this route by using Dijkstra or Greedy algorithm
    Return:
        - final_path (list): the list contain the final path for this route
        - final_path_weight (float): the weight corresponding for the final_path
    '''
    final_path_weight = float('inf')

    if algorithm != 'astar':
        final_path = list
        for _, node in enumerate(coords):
            if algorithm == 'dijkstra':
                path, weight = dijkstra_path(coords, edges, node[2])
            elif algorithm == 'greedy':
                path, weight = greedy_path(coords, edges, node[2])
    
            if weight < final_path_weight:
                final_path_weight = weight
                final_path = path

    else:
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


def make_directory(link: list, final_path: list, GPS: list) -> list:
    final_link = link
    GPS = [GPS[i][:2] for i in range(len(GPS))]

    for i in final_path:
        i -= 1
        link.append(str(GPS[i]) + "/")

    final_link = listToString(final_link)
    remove = ["[", " ", "]"]
    
    for i in remove:
        final_link = final_link.replace(i, "")

    return final_link


def display(path: list, weight: float, link: list, algorithm: str):
    print('-' * 10, algorithm, '-' * 10)
    print(f'Optimize path by using {algorithm}: {path}')
    print(f'Weight: {weight:.4f}')
    print(f'Link: {link}')
    print('\n')