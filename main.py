from utils import graph
from dijkstra import dijkstra_path
from greedy import greedy_path
from astar import a_star_path
import itertools


GPS = [
    [10.762861, 106.682472], # 1: HCMUS 1
    [10.729189, 106.695783], # 2: RMIT
    [10.785861, 106.702722], # 3: USSH
    [10.827829, 106.700567], # 4: VLU
    [10.806762, 106.712719], # 5: FTU2
    [10.850631, 106.771937], # 6: HCMUTE
    [10.773267, 106.659466], # 7: HCMUT
    [10.783258, 106.694751], # 8: UEH
    [10.811472, 106.680583], # 9: UFM
    [10.875658, 106.799184], # 10: HCMUS 2
]


def shortest_path(algorithm: str, coords: dict, edges: dict) -> None:

    shortest_path_taken = list
    shortest_path_weight = float('inf')

    for _, node in enumerate(coords):
        if algorithm == 'dijkstra':
            path, weight = dijkstra_path(coords, edges, node[2])
        elif algorithm == 'greedy':
            path, weight = greedy_path(coords, edges, node[2])
   
        if weight < shortest_path_weight:
            shortest_path_weight = weight
            shortest_path_taken = path

    print('-' * 10, algorithm, '-' * 10)
    print(f'Optimize path by using {algorithm}: {shortest_path_taken}')
    print(f'Weight: {shortest_path_weight:.4f}')


def shortest_path_astar(
        coords: dict, 
        graph: dict, 
        edges: dict
    ) -> None:

    shortest_path_taken, shortest_path_weight = None, float('inf')
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

        if valid_path and current_weight < shortest_path_weight:
            shortest_path_weight = current_weight
            shortest_path_taken = current_path

    print('-' * 10, 'astar', '-' * 10)
    print(f'Optimize path by using astar: {shortest_path_taken}')
    print(f'Weight: {shortest_path_weight:.4f}')


if __name__ == '__main__':
    coords = GPS
    edges = graph(coords=coords)

    # Dijkstra
    shortest_path('dijkstra', coords, edges)

    # Greedy
    shortest_path('greedy', coords, edges)

    # Astar
    graphs, edges = graph(coords=coords,
                          algorithm='astar')
    shortest_path_astar(coords=coords,
                        graph=graphs,
                        edges=edges)