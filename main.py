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

link = ["www.google.com.br/maps/dir/"]





    print('-' * 10, 'astar', '-' * 10)
    print(f'Optimize path by using astar: {shortest_path_taken}')
    print(f'Weight: {shortest_path_weight:.4f}')


if __name__ == '__main__':
    coords = GPS
    edges = graph(coords=coords)

    label = ['HCMUS 1', 'RMIT', 'USSH', 'VLU', 'FTU2',
             'HCMUTE', 'HCMUT', 'UEH', 'UFM', 'HCMUS 2']
    
    [print(f'Label {i + 1}: {label[i]}') for i in range(len(coords))]

    # Dijkstra
    shortest_path('dijkstra', coords, edges)

    # # Greedy
    # shortest_path('greedy', coords, edges)

    # # Astar
    # graphs, edges = graph(coords=coords,
    #                       algorithm='astar')
    # shortest_path_astar(coords, graphs, edges)