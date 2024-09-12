from utils import graph
from dijkstra import dijkstra_path
from greedy import greedy_path
from astar import a_star_path
import itertools

GPS = [
    [10.762861, 106.682472], # HCMUS 1
    [10.729189, 106.695783], # RMIT
    [10.785861, 106.702722], # USSH
    [10.827829, 106.700567], # VLU
    [10.806762, 106.712719], # FTU2
    [10.850631, 106.771937], # HCMUTE
    [10.773267, 106.659466], # HCMUT
    [10.783258, 106.694751], # UEH
    [10.811472, 106.680583], # UFM
    [10.875658, 106.799184], # HCMUS 2
]

def shortest_path(
        algorithm: str, 
        coords: dict, 
        graph: dict, 
        edges: dict
    ) -> None:
    
    if algorithm == 'dijkstra':
        model = dijkstra_path()
    elif algorithm == 'greedy':
        model = greedy_path()
    elif algorithm == 'astar':
        model == a_star_path()

    shortest_path_taken, shortest_path_weight = None, float('inf')
    nodes = [node[2] for node in coords]

    for perm in itertools.permutations(nodes):
        
        current_path, current_weight = [], 0
        valid_path = True

        for i in range(len(perm) - 1):
            path, weight = model(
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

        if shortest_path_taken is None:
            print('No valid path found.')
        else:
            print('-' * 10, algorithm, '-' * 10)
            print(f'Optimizal path for this route by using {algorithm}: {shortest_path_taken}')
            print(f'Weight: {shortest_path_weight}')
    

# def apply(algorithm: str, coords: dict, edges: dict) -> None:

#     if algorithm == 'dijkstra':
#         model = dijkstra()
#     elif algorithm == 'greedy':
#         model = greedy()
#     elif algorithm == 'astar':
#         model == astar()

#     shortest_path_taken = list
#     shortest_path_weight = float('inf')

#     for index, node in enumerate(coords):
#         path, weight = model(coords, edges, node[2])
#         print('-'*20)
#         print(f'Path starting from node {node[2]}: {path}')
#         print(f'Weight: {weight}')
#         if weight < shortest_path_weight:
#             shortest_path_weight = weight
#             shortest_path_taken = path

#     print('-' * 20)
#     print(f'Optimizal path for this route by using {algorithm}: {shortest_path_taken}')
#     print(f'Weight: {shortest_path_weight}')


if __name__ == '__main__':
    coords = GPS
    coords, edges = graph(coords=coords)

    # # Dijkstra
    # shortest_path('dijkstra', coords, edges)

    # # Greedy
    # shortest_path('greedy', coords, edges)

    # Astar
    coords, graph_, edges = graph(coords=coords,
                                  algorithm='astar')
    shortest_path(algorithm='astar', 
                  coords=coords,
                  graph=graph_,
                  edges=edges)